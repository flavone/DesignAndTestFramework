"""
全局参数类型设置
"""


class ContentType:
    JSON = 'JSON'
    XML = 'XML'
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
