# data serialization and deserialization testing

## Start

```bash
$ MULTICAST_GROUP=groupIP docker-compose up --build
```

## Testing

Example of running all tests

```bash
$ nc -u 0.0.0.0 2000
> get_result all
```

You can test separately in this way

```bash
> get_result format_name
```
