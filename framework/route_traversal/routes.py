from datetime import datetime

from utils.parseUtils import Parser


class RouteModel:
    """
    路由模型，根据路由模型可以生成全节点遍历流程序列，并自动执行，完整遍历执行在其他方法中

    [TODO] 其他方法调用节点类和路由类进行自动遍历生成用例和执行用例
    """
    def __init__(self, name, from_node, to_node, action: Action, check_rules=None):
        """
        初始化路由模型，每个路由模型是从一个节点到另一个节点的直接联接

        # [TODO]
        1. 节点是取节点类实例，还是节点名称/序列号？
        2. 操作需要包括哪些必要因素？
        3. 检查规则应该放到路由还是后节点？应该包括哪些内容？

        :param name: 路由名称

        :param from_node: 前节点

        :param to_node: 后节点

        :param action: 操作

        :param check_rules: 检查规则
        """
        self.name = name
        self.from_node = from_node
        self.to_node = to_node
        self.action = action
        self.check_rules = check_rules

    def _check(self, result):
        if self.check_rules is None:
            return True
        # TODO
        return False

    def run_route(self):
        """
        执行该路由，因为前后节点、操作、检查点都已定义，直接调用action进行执行即可，需要输出的内容待定

        :return: (运行时间， 执行结果， 检查结果True/False)
        """
        start_at = datetime.now()
        result = self.action.do()
        stop_at = datetime.now()
        runtime = stop_at - start_at  # TODO 是否需要转换为对应格式？
        return runtime, result, self._check(result)


class Action:
    def __init__(self, action_obj, action_contents: ActionContent):
        self.action_obj = action_obj
        self.action_contents = action_contents

    def do(self):
        # TODO 根据action_obj类型调用对应执行方法
        return None

    def modify(self, action_obj, action_contents: ActionContent):
        if action_obj is not None:
            self.action_obj = action_obj
        if action_contents is not None:
            self.action_contents = action_contents


class ActionContent:
    def __init__(self, para_in: Parameters, para_out: Parameters = None):
        self.para_in = para_in
        self.para_out = para_out

    def modify(self, para_in: Parameters, para_out: Parameters = None):
        if para_in is not None:
            self.para_in = para_in
        if para_out is not None:
            self.para_out = para_out


class Parameters:
    def __init__(self, p_type, p_contents):
        self.p_type = p_type
        self.p_contents = p_contents

    def modify_type(self, p_type):
        if p_type is not None:
            self.p_type = p_type

    def modify_contents(self, p_contents):
        if p_contents is not None:
            self.p_contents = p_contents

    def try_parse_contents(self):
        return Parser.p_parse(self.p_type, self.p_contents)
