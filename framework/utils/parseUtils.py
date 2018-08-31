import json

import jsonpath
import xmltodict
from datetime import date, timedelta

from G import ContentType, EncodeType, AGE_RNG_CODE, MAX_AGE


class Parser:
    """
    解析工具类，只有静态方法
    """

    @staticmethod
    def p_parse(p_type, p_contents, encoding=EncodeType.UTF8):
        """
        根据p_type类型将p_contents解析成对应格式的字符串

        :param p_type:  在ContentType中定义，包括 JSON, XML,XML_S(不带<?xml?>头), FORM_DATA, MULTI_DATA

        :param p_contents: json数据

        :param encoding: 编码格式

        :return: 对应格式的字符串
        """
        if p_type == ContentType.XML_S:
            return xmltodict.unparse(json.loads(p_contents, encoding=encoding), full_document=False, pretty=True)
        elif p_type == ContentType.XML:
            return xmltodict.unparse(json.loads(p_contents, encoding=encoding), full_document=True, pretty=True)
        elif p_type == ContentType.JSON:
            return json.dumps(p_contents, ensure_ascii=False)

        # TODO
        else:
            return None

    @staticmethod
    def domain_split_parse(ds_str: str):
        """
        解析包含 && 或 || 的语句，成多个子串

        :param ds_str:

        :return:
        """
        if ds_str is None or ds_str == '':
            return ds_str
            # TODO

    @staticmethod
    def domain_compare_parse(dc_str: str):
        """
        解析包含 > 、= 、< 的语句，成对应的数据域

        :param dc_str:

        :return:
        """
        if dc_str is None or dc_str == '':
            return dc_str
            # TODO

    @staticmethod
    def global_string_parse(gb_str: str):
        """
        解析全局变量或内置函数

        全局变量格式: ${para_name}

        内置函数格式: ${function_name(para1, para2, ...)}

        :param gb_str: 变量或函数字符串

        :return: 解析结果
        """
        # TODO 借鉴jmeter

    @staticmethod
    def json_path_parse(json_str, xpath):
        """
        根据xpath获取json字符串对应的路径值

        :param json_str: json字符串

        :param xpath: xpath路径字符串

        :return: 路径对应的值，如果找不到，则返回空值
        """
        if type(json_str) == dict:
            result = jsonpath.jsonpath(json_str, xpath)
        else:
            result = jsonpath.jsonpath(json.loads(json_str, encoding='UTF8'), xpath)
        if result:
            return result[0]
        else:
            return None

    @staticmethod
    def day_parse(period: str):
        if period is None or period == '':
            return 'D', 0
        period_list = period.split('-')
        if len(period_list) == 1:
            return _replace_age_code(period_list[0])
        else:
            return _replace_age_code(period_list[len(period_list) - 1])  # 按上限算

    @staticmethod
    def date_range_parse(age_str: str):
        """
            根据字符串(如20D-15Y、>30Y、<20M)判断时间区间

            :param age_str: 时间区间字符串，支持>、<、-、=，年月日的定义参见config的AGE_RNG_CODE

            :return:(开始时间,结束时间)
            """
        today = date.today()
        start_date = today
        end_date = today
        if age_str.find('-') != -1:
            a_list = age_str.split('-')
            if len(a_list) == 1:
                return Parser.date_range_parse(a_list[0])
            start = a_list[0]
            end = a_list[1]
            s_sign, s_code, s_i = _phase_age(start)
            e_sign, e_code, e_i = _phase_age(end)
            for index in range(len(AGE_RNG_CODE)):
                if AGE_RNG_CODE[index]['code'] == e_code:
                    if AGE_RNG_CODE[index]['name'] == '年':
                        start_date = today.replace(year=today.year - e_i, day=today.day + 1)
                    elif AGE_RNG_CODE[index]['name'] == '月':
                        start_date = today.replace(month=today.month - e_i, day=today.day + 1)
                    else:
                        start_date = today - timedelta(days=e_i - 1)
                    break
            for index in range(len(AGE_RNG_CODE)):
                if AGE_RNG_CODE[index]['code'] == s_code:
                    if AGE_RNG_CODE[index]['name'] == '年':
                        end_date = today.replace(year=today.year - s_i)
                    elif AGE_RNG_CODE[index]['name'] == '月':
                        end_date = today.replace(month=today.month - s_i)
                    else:
                        end_date = today - timedelta(days=s_i)
                    break
        else:
            sign, code, i = _phase_age(age_str)
            for index in range(len(AGE_RNG_CODE)):
                if AGE_RNG_CODE[index]['code'] == code:
                    start_date = today.replace(year=today.year - MAX_AGE)
                    if AGE_RNG_CODE[index]['name'] == '年':
                        if sign == '>':
                            end_date = today.replace(year=today.year - i, day=today.day)
                        elif sign == '<':
                            start_date = today.replace(year=today.year - i, day=today.day + 1)
                        elif sign == '=':
                            start_date = today.replace(year=today.year - i, day=today.day)
                            end_date = start_date
                    elif AGE_RNG_CODE[index]['name'] == '月':
                        if sign == '>':
                            end_date = today.replace(month=today.month - i)
                        elif sign == '<':
                            start_date = today.replace(month=today.month - i, day=today.day + 1)
                        elif sign == '=':
                            start_date = today.replace(month=today.month - i, day=today.day)
                            end_date = start_date
                    else:
                        if sign == '>':
                            end_date = today - timedelta(days=i)
                        elif sign == '<':
                            start_date = today - timedelta(days=i + 1)
                        elif sign == '=':
                            start_date = today - timedelta(days=i)
                            end_date = start_date
                    break
        return start_date, end_date


def _phase_age(age: str):
    if age is None:
        return '18Y-65Y'
    elif _find(age, '-'):
        return age
    if _find(age, '>'):
        age = age.replace('>', '')
        code, i = _replace_age_code(age)
        if code is None or i is None:
            return None
        else:
            return '>', code, i
    elif _find(age, '<'):
        age = age.replace('<', '')
        code, i = _replace_age_code(age)
        if code is None or i is None:
            return None
        else:
            return '<', code, i
    else:
        age = age.replace('=', '')
        code, i = _replace_age_code(age)
        if code is None or i is None:
            return None
        else:
            return '=', code, i


def _find(origin: str, sub: str):
    if origin.find(sub) == -1:
        return False
    return True


def _replace_age_code(origin: str):
    for index in range(len(AGE_RNG_CODE)):
        age_rng = AGE_RNG_CODE[index]
        code = age_rng['code']
        if _find(origin, code):
            return code, int(origin.replace(code, ''))
        else:
            continue
    return None, None
