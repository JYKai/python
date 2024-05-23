import struct

with open('output', 'rb') as f:
    chunk = f.read(16)
    result = struct.unpack('dicccc', chunk)
    print(result)

struct.pack('dicccc', 7.5, 15, b'A', b'\x00', b'\x00', b'\x00')
