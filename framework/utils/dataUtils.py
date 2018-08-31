import random


def get_random_name():
    """
    生成随机姓名

    :return:
    """
    a1 = ['张', '金', '李', '王', '赵', '黄', '卫', '胡', '毛']
    a2 = ['玉', '明', '龙', '芳', '军', '玲', '周', '胡', '来', '符', '建']
    a3 = ['', '立', '玲', '', '国', '', '文', '炜', '加', '可', '级', '龙']
    return random.choice(a1) + random.choice(a2) + random.choice(a3)


def get_random_phone():
    """
    生成随机手机号

    :return:
    """
    a1 = ['131', '133', '134', '135', '136', '137', '138', '139', '157', '159']
    pn = random.choice(a1)
    for i in range(8):
        pn += str(random.randint(0, 9))
    return pn


def get_random_email(spec_domain=None):
    """
    生成随机邮箱

    :param spec_domain: 指定域名，如 qq.com, 不检查该值的合法性

    :return:
    """
    a1 = ['com', 'cn', 'org', 'net', 'tv', 'us']
    seed = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sa = []
    sb = []
    for i in range(random.randint(5, 10)):
        sa.append(random.choice(seed))
    for j in range(random.randint(3, 8)):
        sb.append(random.choice(seed))
    if spec_domain is None or not isinstance(spec_domain, str):
        email = ''.join(sa) + '@' + ''.join(sb) + '.' + random.choice(a1)
    else:
        email = ''.join(sa) + '@' + spec_domain
    return email


def get_random_str(min_len: int = 8, max_len: int = 16):
    """
    生成随机字符串

    :return:
    """
    seed = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sa = []
    for i in range(random.randint(min_len, max_len)):
        sa.append(random.choice(seed))
    return ''.join(sa)


def get_random_occupation_code(occupation_list):
    """
    获取随机职业编号

    :param occupation_list: 职业映射列表

    :return: 职业编码
    """
    new_list = []
    if occupation_list is None or len(occupation_list) == 0:
        return ''
    for index in range(len(occupation_list)):
        tmp_o = occupation_list[index]
        if 'parent' not in tmp_o:
            continue
        flag = True
        for i in range(len(occupation_list)):
            if 'parent' not in occupation_list[i]:
                continue
            if tmp_o['value'] == occupation_list[i]['parent']:
                flag = False
                break
        if flag:
            new_list.append(tmp_o)
    return new_list[random.randint(0, len(new_list) - 1)]['value']


def get_random_region_code(region_list):
    """
    获取随机区域编码

    :param region_list: 区域编码映射列表

    :return: 区域编码
    """
    new_list = []
    if region_list is None or len(region_list) == 0:
        return ''
    for index in range(len(region_list)):
        tmp_o = region_list[index]
        if 'parent' not in tmp_o:
            continue
        flag = True
        for i in range(len(region_list)):
            if 'parent' not in region_list[i]:
                continue
            if tmp_o['value'] == region_list[i]['parent']:
                flag = False
                break
        if flag:
            new_list.append(tmp_o)
    region = new_list[random.randint(0, len(new_list) - 1)]
    return region['parent'], region['value']


def get_occupation_code(occupation_list):
    """
    获取随机职业编码

    :param occupation_list: 职业编码列表

    :return: 随机职业编码
    """
    new_list = []
    if occupation_list is None or len(occupation_list) == 0:
        return ''
    for index in range(len(occupation_list)):
        tmp_o = occupation_list[index]
        if 'parent' not in tmp_o:
            continue
        flag = True
        for i in range(len(occupation_list)):
            if 'parent' not in occupation_list[i]:
                continue
            if tmp_o['value'] == occupation_list[i]['parent']:
                flag = False
                break
        if flag:
            new_list.append(tmp_o)
    return new_list[random.randint(0, len(new_list) - 1)]['value']
