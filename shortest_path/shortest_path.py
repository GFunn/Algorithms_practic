graph = {}
costs = {}
parents = {}

# 此处有插图，示意graph结构

graph['S'] = {'A': 5, 'B': 0}
graph['A'] = {'C': 15, 'D': 20}
graph['B'] = {'C': 30, 'D': 35}
graph['C'] = {'F': 20}
graph['D'] = {'F': 10}
graph['F'] = {}

infinity = float('inf')
costs = {
        'A': 5,
        'B': 0,
        'C': infinity,
        'D': infinity,
        'F': infinity
}

parents = {
        'A': 'S',
        'B': 'S',
        'C': None,
        'D': None,
        'F': None
}


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if node not in processed and cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 正题开始，迪克斯特拉算法求最短路径

processed = []
node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)
