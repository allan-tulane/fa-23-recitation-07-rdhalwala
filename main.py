from collections import defaultdict


def make_undirected_graph(edge_list):
  """ Makes an undirected graph from a list of edge tuples. """
  graph = defaultdict(set)
  for e in edge_list:
    graph[e[0]].add(e[1])
    graph[e[1]].add(e[0])
  return graph


def reachable(graph, start_node):
  """
    Returns:
      the set of nodes reachable from start_node
    """
  #start at beginning node
  result = set([start_node])
  frontier = set([start_node])
  #check frontier len not 0
  while len(frontier) != 0:
    #visit a node
    visited = frontier.pop()
    #check if in result or not
    if visited not in result:
      result.add(visited)
    #go to next node
    #repeat until no more nodes in frontier
    nextN = graph[visited]
    nextN = nextN.difference(result)
    frontier = frontier.union(nextN)
    #return all reachable nodes
  return result


def connected(graph):
  #see if connected
  Nodes = len(graph)
  #set of reachable nodes stored
  connect = reachable(graph, list(graph.keys())[0])
  return len(connect) == Nodes


def n_components(graph):
  """
    Returns:
      the number of connected components in an undirected graph
    """
  ### TODO
  #result to store
  result = []
  #frontier
  frontier = set(list(graph.keys()))

  #check length isnt 0
  while len(frontier) != 0:
    #pop
    node = frontier.pop()
    connected = reachable(graph, node)
    #subtract connected
    frontier = frontier - connected
    result.append(connected)


#components in undirected graph
  return len(result)
