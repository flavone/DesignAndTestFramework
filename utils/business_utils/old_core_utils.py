from G import ContentType
from utils.parseUtils import Parser


class OldCoreUtils:
    """
    核算工具类，只有静态方法
    """

    @staticmethod
    def get_post_data_from_json(json_data, encoding):
        serviceId = Parser.json_path_parse(json_data, '$.msgbody.serviceId')
        xml_header = '<?xml version="1.0" encoding="%d" standalone="yes"?>' % encoding
        xml_format = '''
        XXXXX;%s;
        %s
        %s
        ''' % serviceId, xml_header, Parser.p_parse(ContentType.XML, json_data)
        return xml_format
