from flask import request, jsonify
from flask_restplus import abort

from ._api import api
from framework.design_module.direct_graph.directGraph import DirectGraph
from framework.design_module.orthogonal_experiment.OAT import OAT


@api.route('/getcase/di', methods=['POST'])
def design_di_graph():
    if not request.json:
        abort(400)
    digraph = DirectGraph(flow_list=request.json.get('nodes'))
    start = request.json.get('start')
    end = request.json.get('end')
    weight = request.json.get('weight')
    percent = request.json.get('percent')
    return jsonify({'result': digraph.get_all_path(start=start, stop=end, weight_limit=weight, percent=percent)})


@api.route('/getcase/oat', methods=['POST'])
def design_oat():
    if not request.json:
        abort(400)
    oat = OAT()
    result = oat.genSets(request.json)
    total = len(result)
    return jsonify({"total": total, "result": result})


@api.route('/', methods=['GET'])
def root():
    return jsonify('Hello World!')
