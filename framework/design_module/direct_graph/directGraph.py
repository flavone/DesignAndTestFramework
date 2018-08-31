# coding = utf-8
import networkx as nx
from pylab import *


# 获取权重，用于filter
def get_weight(elem):
    return elem['weight']


class DirectGraph:
    """
    根据有向联接实现流程图
    """

    def __init__(self, edges=None, flow_list=None):
        """
        初始化有向图，如果定义了edges，则按edges生成流程图，否则按flow_list生成

        :param flow_list: 潜在流向列表，一对多，如：

        {
            '登录': {
                '登出': 1,
                '申请贷款': 10,
                '查询贷款': 2.5
            },
            '登出': {
                '登录': 1
            },
            '申请贷款': {
                '提交审核': 10,
                '提交审批': 2,
                '登出': 1
            }
        }

        :param edges: 流向，一对一，如：

        [
            ('登录', '登出', 1),
            ('登录', '申请贷款', 8),
            ('登录', '查询贷款', 1.5),
            ('申请贷款', '提交审核', 8),
            ('申请贷款', '提交审批', 3),
            ('申请贷款', '登出', 2),
            ('登出', '登录', 1)
        ]
        """
        if flow_list is None and edges is None:
            raise ValueError('flow_list and edges can not both be empty or null!')
        elif edges is not None:
            self._edges = edges
        else:
            self._tmp_data = flow_list
            self._edges = self._get_edges()
        self._graph = self._get_di_graph()

    def _get_edges(self):
        edges = []
        for key in self._tmp_data:
            for t_key in self._tmp_data[key]:
                edges.append((key, t_key, self._tmp_data[key][t_key]))
        return edges

    def _get_di_graph(self):
        g = nx.DiGraph()
        g.add_weighted_edges_from(self._edges)
        return g

    def remove_nodes(self, nodes):
        """
        移除节点

        :param nodes:

        :return:
        """
        if len(nodes) == 0:
            return
        for node in nodes:
            if self._graph.has_node(node):
                self._graph.remove_node(node)

    def remove_edges(self, edges):
        """
        移除路由

        :param edges:

        :return:
        """
        if len(edges) == 0:
            return
        for edge in edges:
            if len(edge) < 2:
                continue
            if self._graph.has_edge(*edge[:2]):
                self._graph.remove_edge(*edge[:2])

    def get_all_path(self, start=None, stop=None, weight_limit=-1, percent=100):
        """
        获取有向图对应节点的全部可执行路径

        :param start: 起始节点，如果为空，则自动选取没有前节点的节点，可以是多个

        :param stop: 结束节点，如果为空，则自动选取没有后节点的节点，可以是多个

        :param weight_limit: 权重，默认-1

        :param percent: 占总路径数量比例，默认100

        :return: json格式的路径集合
        """
        tmp_dict = []
        if start is None or str(start) == '':
            start_nodes = [node for node in list(self._graph.nodes) if len(list(self._graph.predecessors(node))) == 0]
        else:
            start_nodes = [start]
        if stop is None or str(stop) == '':
            stop_nodes = [node for node in list(self._graph.nodes) if len(list(self._graph.successors(node))) == 0]
        else:
            stop_nodes = [stop]

        if len(start_nodes) == 0 or len(stop_nodes) == 0:
            return []
        # 遍历起始节点到结束节点的所有路径
        for start_node in start_nodes:
            for stop_node in stop_nodes:
                tmp_dict.extend([path for path in self._get_paths(start_node, stop_node) if path is not None])
        tmp_dict.sort(key=get_weight, reverse=True)
        if len(tmp_dict) == 0:
            return []
        # 权重设定
        if weight_limit < 0:
            weight_dict = tmp_dict
        else:
            weight_dict = [v for v in tmp_dict if v['weight'] >= weight_limit]
        # 比例设定
        if percent >= 100:
            return weight_dict
        else:
            return weight_dict[0:round(len(weight_dict) * percent / 100.00)]

    def _get_paths(self, start, stop):
        tmp_dict = []
        if not self._graph.has_node(start) or not self._graph.has_node(stop):
            return tmp_dict
        for i in nx.all_simple_paths(self._graph, source=start, target=stop):
            weight = 0.0
            for j in range(len(i) - 1):
                k = (i[j], i[j + 1])
                weight += [float('%.2f' % d['weight']) for (u, v, d) in self._graph.edges(data=True) if (u, v) == k][0]
                tmp_dict.append({'weight': weight, 'path': i})
        return tmp_dict
