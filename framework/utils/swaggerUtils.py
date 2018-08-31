from framework.utils import HttpUtil
from framework.utils import Parser


class SwaggerUtil:
    def __init__(self, url):
        self._url = url
        self._resp = HttpUtil(url).get_json('')
        if self._resp is None:
            raise TypeError('Swagger UI没有返回正确的api数据！')
        self._host, self._base_path = self._get_host_and_path()

    def _get_host_and_path(self):
        host = Parser.json_path_parse(self._resp, '$.host')[0]
        base_path = Parser.json_path_parse(self._resp, '$.basePath')[0]
        return host, base_path

    def get_all_api(self):
        None  # TODO
