# TODO 将http工具迁移过来
import requests

from G import RequestMethod, HEADERS


def _get_real_url(url: str, para):
    if isinstance(para, str) or isinstance(para, int):
        url = url.replace('%s', str(para), 1)
    elif isinstance(para, tuple) or isinstance(para, list):
        for param in para:
            url = url.replace('%s', param, 1)  # TODO 如果param包含%s，则不安全
    return url


# TODO 添加其他返回格式的解析
class HttpUtil:
    """
    HTTP请求工具，包括get，post
    """

    def __init__(self, url):
        """
        初始化请求session

        :param url: http请求主机地址
        """
        self.session = requests.session()
        self.url = url

    def get_json(self, relative_url: str, para=None):
        """
        GET类型的请求，返回json结果

        :param relative_url: 请求相对路径字符串，当包含%s时，自动用para内参数替换%s，有多个时按顺序替换

        :param para:  请求参数，可以是list或str

        :return: 响应结果的json
        """
        if self.session is None:
            return None
        if relative_url.find('%s') >= 0:
            relative_url = _get_real_url(relative_url, para)
            resp = self.session.request(method='GET', url=self.url + relative_url, params=None, headers=HEADERS)
        else:
            resp = self.session.request(method='GET', url=self.url + relative_url, params=para, headers=HEADERS)
        if resp.status_code != 200:
            return None
        return resp.json()

    def post_json(self, relative_url, para=None):
        """
        POST类型的请求，返回json结果

        :param relative_url: 请求相对路径字符串，不允许出现%s

        :param para: 请求参数，只可以是json

        :return: 响应结果的json
        """
        if self.session is None:
            return None
        resp = self.session.request(method='POST', url=self.url + relative_url, json=para, headers=HEADERS)
        if resp.status_code != 200:
            return None
        return resp.json()

    def do_request(self, relative_url, method, para=None):
        if method == RequestMethod.GET:
            return self.get_json(relative_url, para)
        elif method == RequestMethod.POST:
            return self.post_json(relative_url, para)
