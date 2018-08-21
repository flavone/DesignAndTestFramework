import json

from framework.route_traversal.nodes import NodeModel

node_A = NodeModel('node_A','["data": [{"type": "JSON", "values": "1"}, {"type": "FORM_DATA", "values": "2"}]]', [])
node_B = NodeModel('node_B','{"data": [{"type": "JSON", "values": "2"}, {"type": "FORM_DATA", "values": null}]}', [node_A])
node_C = NodeModel('node_C','{"data": [{"type": "JSON", "values": "5"}, {"type": "FORM_DATA", "values": "7"}]}', [node_A,node_B])

node_A.add_next_node(node_C)
node_A.add_next_node(node_A)
node_A.add_next_node(node_C)
node_A.add_next_node(node_B)

for n in node_A.next_nodes:
    print(n.name)

node_D = node_A.__deepcopy__()
print("------------------")
node_A.remove_next_node('node_B')
for n in node_A.next_nodes:
    print(n.name)
print("------------------")
node_D.remove_next_node(node_C)
for n in node_D.next_nodes:
    print(n.name)


print(node_B.get_node_data())

print(node_B.get_node_data('$.data[1].value'))

