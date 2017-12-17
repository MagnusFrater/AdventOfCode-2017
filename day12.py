# read in the data
with open("PuzzleInputs/12", "r") as f:
	data = f.read()

class UndirectedGraph():
	'custom undirected-graph data structure'

	def __init__(self):
		self.connections = {}
	
	# connects two nodes together
	def connect(self, i, j):
		# make sure the nodes exist within `connections`
		if i not in self.connections:
			self.connections[i] = []

		# connect the nodes to each other
		self.connections[i].append(j)
	
	# returns the specified node's neighbours
	def get_neighbours(self, node):
		return self.connections[node]

# returns an `Undirected Graph` filled from `data`
def create_undirected_graph(data):
	ug = UndirectedGraph()

	# for every line in the file,
	for line in data.split('\n'):
		if len(line) > 0:
			# split the line (if it contains content) on the spaces (without the unneeded commas)
			parts = line.replace(',', '').split()

			# connect each connection within the undirected graph
			i = 2
			while i < len(parts):
				ug.connect(int(parts[0]), int(parts[i]))
				i += 1
	return ug

# create the undirected graph
ug = create_undirected_graph(data)

#
#	Part 1
#

class DepthFirstSearch():
	'custom depth first search algorithm'

	def __init__(self, undirected_graph, node):
		self.visited = []
		self.ug = undirected_graph
		self.visit(node)
	
	# marks the specified node as 'visited', then 'visits' all of its children nodes
	def visit(self, node):
		# mark current node as 'visited'
		self.visited.append(node)

		# 'visit' all children nodes (if they haven't already been visited)
		for sub_node in self.ug.connections[node]:
			if sub_node not in self.visited:
				self.visit(sub_node)

# returns the number of node connections to the given node key
def get_connection_count(undirected_graph, node):
	dfs = DepthFirstSearch(undirected_graph, 0)
	return len(dfs.visited)

connection_count = get_connection_count(ug, 0)
print(connection_count)

#
#	Part 2
#

# returns the number of distinct, separate groups of nodes within the specified undirected graph
def get_group_count(undirected_graph):
	groups = []

	# cycle through each node within the graph
	for node in undirected_graph.connections:
		# check to see if current node exists within any group
		found = False
		for group in groups:
			if node in group:
				found = True

		# if node not found within any groups, append its own group (from dfs visited list)
		if not found:
			dfs = DepthFirstSearch(undirected_graph, node)
			groups.append(dfs.visited)
	
	return len(groups)

group_count = get_group_count(ug)
print(group_count)
