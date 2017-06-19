import time
from collections import deque

class NodeList:
    def __init__(self, nodeList):
        self.iterationIndex = 0
        self.nodeList = nodeList

    # for maintaining the node index on the interface to start from 1 and not from 1
    def __getitem__(self, item):
        return self.nodeList[item - 1]

    def __len__(self):
        return len(self.nodeList)

    # make the class iteratable (via: https://stackoverflow.com/questions/19151/build-a-basic-python-iterator)
    def __iter__(self):
        return self

    def __next__(self):
        if self.iterationIndex >= len(self.nodeList):
            self.iterationIndex = 0
            raise StopIteration
        else:
            self.iterationIndex += 1
            return self.nodeList[self.iterationIndex - 1]

    # nodeList is expected to contain the nodes in ascending order
    def __contains__(self, index):
        return index <= len(self.nodeList) and index > 0

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.finishing_time = -1

    @property
    def is_visited(self):
        return self.visited

    def __str__(self):
        return str(self.name)

class Graph:
    def __init__(self, length):
        self.nodes = [Node(i) for i in range(1, length + 1)]
        self.connections = {node:[] for node in self.nodes}

    def add_connection(self, from_node_index, to_node_index):
        from_node = self.nodes[from_node_index-1]
        to_node = self.nodes[to_node_index-1]
        self.connections[from_node].append(to_node)

    def get_node(self, index):
        return self.nodes[index - 1]


# 1) calculate finishing times
    # start at a node, the node 'finishes' if no more nodes can be reached from it

# 2) search for sscs
    # loop on all nodes, start with the nodes with the highest finishing times
        # check if the node is visited. If it is, go to the next highest
        # do bfs until the starting node is reached
            # if reached add the path to the ssc, mark the path as visited
        # if a node is reached that is visited, check if it is a part of the current ssc
            # if it is add the path to the ssc, mark the path as visited
        # if the starting node cannot be reached, this is an ssc with a single node

def calculate_finishing_time(graph):

    finishing_time = 0
    for i in range(len(graph.nodes)-1, -1, -1):
        node = graph.nodes[i]
        to_visit = deque([node])

        def visited():
            nonlocal finishing_time, to_visit
            current.finishing_time = finishing_time
            finishing_time += 1
            if(finishing_time% 1000 == 0): print(finishing_time, time.time())
            to_visit.popleft()

        while len(to_visit) > 0:
            # print(to_visit)
            # for j in to_visit:
                # print(j.name, end=', ')
            # print('')
            current = to_visit[0]
            # print(current)
            # already finished
            if current.finishing_time > -1:
                to_visit.popleft()

                continue

            if current.visited:
                visited()
                continue

            current.visited = True


            try:
                connections = graph.connections[current]
                connections_to_be_visited = []
                for connection in connections:
                    if not connection.visited:
                        connections_to_be_visited.append(connection)

                # all sub nodes are finished, this one is finished too
                if len(connections_to_be_visited) == 0:
                    visited()
                else:
                    # print('remaining sub-nodes')
                    # print(connections_to_be_visited)
                    # print(to_visit)
                    to_visit.extendleft(connections_to_be_visited)
            except KeyError:
                # print('key error')
                # no sub node to visit
                visited()

def find_sscs(file_name, node_count):
    start_time = time.time()

    graph = Graph(node_count)
    graph_reversed = Graph(node_count)

    with open(file_name) as f:
        content = f.readlines()

    for line in content:
        line = line.split(' ')
        tail = int(line[0])
        head = int(line[1])
        graph.add_connection(tail, head)
        graph_reversed.add_connection(head, tail)

    prev_time = time.time()
    print('graphs loaded ({} seconds)'.format(prev_time - start_time))

    calculate_finishing_time(graph_reversed)

    print('finished finishing time calculation (+{} seconds)'.format(time.time() - prev_time))
    prev_time = time.time()


    # get node indexes ordered by descending finishing times
    finishing_time_dict = {}
    for node in graph_reversed.nodes:
        finishing_time_dict[node.name] = node.finishing_time

    node_indexes_by_finishing_time = sorted(finishing_time_dict, key=lambda k: finishing_time_dict[k], reverse=True)

    print('nodes by finishing times (desc:) (+{} seconds)'.format(time.time() - prev_time))
    prev_time = time.time()

    # print(finishing_time_dict)
    print(node_indexes_by_finishing_time)
    print('total {} seconds'.format(time.time() - start_time))

find_sscs('test.txt', 9)
#
find_sscs('SCC.txt', 875714)