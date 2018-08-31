"""
全局参数类型设置
"""


class ContentType:
    JSON = 'JSON'
    XML = 'XML'
    XML_S = 'XML_SIMPLE'
    FORM_DATA = 'FORM_DATA'
    MULTI_DATA = 'MULTI_DATA'


class DomainType:
    GE = '>='
    GT = '>'
    LE = '<='
    LT = '<'
    EQ = '='
    AND = '&&'
    OR = '||'


class EncodeType:
    BASE64 = 'Base64'
    UTF8 = 'UTF8'
    GBK = 'GBK'


AGE_RNG_CODE = [{'name': '年', 'code': 'Y'}, {'name': '月', 'code': 'M'}, {'name': '日', 'code': 'D'}]

MAX_AGE = 65

# TODO 添加完整区域码
DISTRICT_CODE = ('110108', '120100', '429004', '430010', '130903', '510101', '622901')


class RequestMethod:
    POST = 'POST'
    GET = 'GET'


HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
