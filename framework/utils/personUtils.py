import random
from datetime import timedelta

from G import DISTRICT_CODE
from framework.utils import Parser
from framework.utils import get_random_name, get_random_email, get_random_phone


class Person:
    """
    生成独立的人员信息
    """

    def __init__(self, age_range: str, is_male: bool):
        """
        基于参数生成人员信息

        :param age_range: 年龄范围(如：=25Y, 10M-65Y, <30Y,如果为空，默认是 18Y-65Y),生日在年龄范围内随机生成

        :param is_male: 是否为男性
        """
        if age_range == '' or age_range is None:
            self.age_range = '18Y-65Y'
        else:
            self.age_range = age_range
        self.is_male = is_male
        self.birthday = self._get_birthday()
        self.p_name = get_random_name()
        self.email = get_random_email()
        self.phone_num = get_random_phone()
        self.id_card = self._get_id_card()

    def _get_id_card(self):
        district_code = DISTRICT_CODE[random.randint(0, len(DISTRICT_CODE) - 1)]
        birthday = self.birthday.strftime('%Y%m%d')
        order_code = _get_order_code(self.is_male)
        return _get_verify(district_code + birthday + order_code)

    def get_id_card(self):
        return self.id_card

    def get_birthday(self):
        return self.birthday.strftime('%Y-%m-%d')

    def get_name(self):
        return self.p_name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone_num

    @staticmethod
    def verify_id(id_card):
        """
        静态方法，校验身份证是否合法
        :param id_card: 身份证号码
        :return: (身份证号码，是否合法)
        """
        if len(id_card) != 18:
            return id_card, False
        if not id_card[:-1].isdigit():
            return id_card, False
        fact = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        _sum = 0
        for i in range(17):
            _sum += fact[i] * int(id_card[i])
        m = _sum % 11
        chk = '10X98765432'
        if chk[m] == id_card[-1]:
            return id_card, True
        else:
            return id_card, False

    def _get_birthday(self):
        start_date, end_date = Parser.date_range_parse(self.age_range)
        delta = (end_date - start_date).days
        if delta < 1:
            return start_date
        else:
            return start_date + timedelta(days=random.randint(1, delta))


def _get_order_code(is_male):
    code = random.randint(0, 99)
    if code < 10:
        order_code = '0' + str(code)
    else:
        order_code = str(code)
    if is_male:
        order_code += str(random.randint(0, 4) * 2 + 1)
    else:
        order_code += str(random.randint(0, 4) * 2)
    return order_code


def _get_verify(pre_id):
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    chk = '10X98765432'  # 校验码映射
    for i in range(len(pre_id)):
        count = count + int(pre_id[i]) * weight[i]
    return pre_id + chk[count % 11]  # 算出校验码
