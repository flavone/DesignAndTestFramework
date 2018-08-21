from G import DomainType


class Parser:
    """
    解析工具类，只有静态方法
    """

    @staticmethod
    def p_parse(p_type, p_contents):
        """
        根据p_type类型将p_contents解析成对应格式的字符串

        :param p_type:  在ContentType中定义，包括 JSON, XML, FORM_DATA, MULTI_DATA

        :param p_contents: json数据

        :return: 对应格式的字符串
        """
        # TODO
        return None

    @staticmethod
    def swagger_parse(url):
        """
        通过调用/api-docs获取全部接口信息

        :param url:

        :return:
        """
        # TODO
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
