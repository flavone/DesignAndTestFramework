from G import EncodeType
from utils.encodeUtils import Encoder

print(Encoder.encode('6530000010120100452902', EncodeType.BASE64))

print(Encoder.decode('NjUzMDAwMDAxMDEyMDEwMDQ1MjkwMg==', EncodeType.BASE64))