import json
import uuid
from json import JSONDecodeError

import jsonpath


def _data_to_json(node_data):
    if type(node_data) != str:
        return {}, True
    else:
        try:
            return json.loads(node_data, encoding='UTF-8'), True
        except JSONDecodeError:
            # TODO 添加log
            return {}, False


class NodeModel:
    """
    节点模型
    """

    def __init__(self, name, node_data, next_nodes: list):
        """
        节点包括唯一序列号、名称、节点数据及格式、潜在后向节点列表

        :param name: 节点名称，命名最好唯一

        :param node_data: 节点数据，存储为json格式

        :param next_nodes: 潜在后向节点列表
        """
        self.serializedID = uuid.uuid4()
        self.name = name
        self.node_data, flag = _data_to_json(node_data)
        self.next_nodes = next_nodes

    def add_next_node(self, node):
        """
        添加单个后向节点
        :param node: 节点
        :return:
        """
        if node not in self.next_nodes:
            self.next_nodes.append(node)

    def remove_next_node(self, node):
        """
        移除一个后向节点，是否应该考虑传入节点名称来进行移除？

        :param node: 节点

        :return:
        """
        for t_node in self.next_nodes:
            if type(node) == str and t_node.name == node:
                self.next_nodes.remove(t_node)
                return
        if node in self.next_nodes:
            self.next_nodes.remove(node)

    def get_node_data(self, xpath=None):
        """
        获取节点数据

        :param xpath: 数据路径，如果为空则返回全部数据

        :return: 对应路径的数据，注意：一般来说xpath获取的数据是个list，如果没有匹配到path，则返回False
        """
        if xpath is None:
            return json.dumps(self.node_data, ensure_ascii=False)
        else:
            return jsonpath.jsonpath(self.node_data, xpath)

    def __deepcopy__(self, memodict={}):
        return NodeModel(self.name + '_copy', self.node_data, self.next_nodes)
