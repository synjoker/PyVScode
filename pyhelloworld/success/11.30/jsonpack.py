import json
import struct

header_dic = {
    'filename': 'a.txt',
    'total_size':
    111111111111111111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223131232,
    'hash': 'asdf123123x123213x'
}

header_json = json.dumps(header_dic)

header_bytes = header_json.encode('utf-8')
print(len(header_bytes))

# 'i'是格式
obj = struct.pack('i', len(header_bytes))
print(obj, len(obj))

res = struct.unpack('i', obj)
print(res[0])
