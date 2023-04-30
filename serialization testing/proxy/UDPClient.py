import socket

import lib.constants as constants

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("proxy", constants.PROXY_PORT))

while True:
    request, address = sock.recvfrom(constants.BUFSIZE)
    request = request.decode()

    if len(request.split()) != 2 or request.split()[0] != "get_result":
        sock.sendto(b'Unknown request!\n', address)
        continue

    format_name = request.split()[1]
    if format_name in constants.formats:
        sock.sendto(b'get_result\n', (format_name, constants.UNICAST_PORT))
    elif format_name == "all":
        sock.sendto(b'get_result\n', (constants.MULTICAST_GROUP, constants.MULTICAST_PORT))
    else:
        sock.sendto(b'Unknown format!\n', address)

    if format_name == "all":
        for _ in range(len(constants.formats)):
            answer, _ = sock.recvfrom(constants.BUFSIZE)
            sock.sendto(answer, address)
    else:
        answer, _ = sock.recvfrom(constants.BUFSIZE)
        sock.sendto(answer, address)
