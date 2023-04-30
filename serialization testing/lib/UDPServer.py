import select
import socket
import struct

import lib.constants as constants

def send_answer(format_name, answer):
    socket_unicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_multicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    socket_unicast.bind((format_name, constants.UNICAST_PORT))
    socket_multicast.bind((constants.MULTICAST_GROUP, constants.MULTICAST_PORT))

    mreq = struct.pack("=4sl", socket.inet_aton(constants.MULTICAST_GROUP), socket.INADDR_ANY)
    socket_multicast.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    sockets = [socket_unicast, socket_multicast]
    while True:
        cur_sockets, _, _ = select.select(sockets, [], [])
        for socket_ in cur_sockets:
            socket_.recvfrom(constants.BUFSIZE)
            socket_.sendto(answer.encode(), ("proxy", constants.PROXY_PORT))
