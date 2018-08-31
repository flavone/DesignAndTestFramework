from G import ContentType
from framework.utils import Parser


class OldCoreUtils:
    """
    核算工具类，只有静态方法
    """

    @staticmethod
    def get_post_data_from_json(json_data, encoding):
        """
        将json数据转换为旧核算使用的格式

        :param json_data: json数据字符串

        :param encoding: xml encoding码值

        :return:
        """
        serviceId = Parser.json_path_parse(json_data, '$.msgbody.serviceId')
        xml_header = '<?xml version="1.0" encoding="%s" standalone="yes"?>' % encoding
        xml_format = '''XXXXX;%s;\n%s\n%s''' % (
            serviceId, xml_header, Parser.p_parse(ContentType.XML_S, json_data, encoding))
        return xml_format
