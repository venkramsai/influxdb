import sys


def calculate_size():
    size = 0.0
    # Size of tags
    size += sys.getsizeof('10000')  # zone id
    size += sys.getsizeof('1000')  # site id
    size += sys.getsizeof('2000')

    # Size of fields
    size += sys.getsizeof(4.0)  # qos id
    size += sys.getsizeof(10.0)  # wan id
    size += sys.getsizeof(50.0)  # rule id
    size += sys.getsizeof(10000.0)  # in pkts
    size += sys.getsizeof(10000.0)  # out pkts
    size += sys.getsizeof(10000.0)  # in bytes
    size += sys.getsizeof(10000.0)  # out bytes
    size += sys.getsizeof(1494055562000000)  # timestamp
    return size

print calculate_size()
