import base64

from G import EncodeType


class Encoder:
    """
    编码类，只有静态方法
    """

    @staticmethod
    def encode(original_str: str, encode_type, **kwargs):
        """
        将字符串进行编码处理

        :param original_str: 初始字符串

        :param encode_type: 编码方式,包括Base64、UTF8、GBK

        :param kwargs: 附带参数

        :return: 编码后的字符串
        """
        if encode_type == EncodeType.BASE64:
            return base64.b64encode(original_str.encode('UTF8'))

            # TODO

    @staticmethod
    def decode(original_str: str, decode_type, **kwargs):
        """
        将字符串进行解码处理

        :param original_str: 初始字符串

        :param decode_type: 解码方式,包括Base64、UTF8、GBK

        :param kwargs: 附带参数

        :return: 解码后的字符串
        """
        if decode_type == EncodeType.BASE64:
            return base64.b64decode(original_str)

        # TODO

