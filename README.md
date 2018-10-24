Appriximation for graphs:
***What is Approximation for node Connection?***

***FUNCTIONS***
node_connectivity(G, s=None, t=None)[source]:

"Node connectivity is equal to the minimum number of nodes that must be removed to disconnect G or render it trivial. By Menger’s theorem, this is equal to the number of node independent paths (paths that share no nodes other than source and target)."

"If source and target nodes are provided, this function returns the local node connectivity: the minimum number of nodes that must be removed to break all paths from source to target in G."

"This algorithm is based on a fast approximation that gives an strict lower bound on the actual number of node independent paths between two nodes [1]. It works for both directed and undirected graphs."

local_node_connectivity(G, source, target, cutoff=None)

"Compute node connectivity between source and target.

Pairwise or local node connectivity between two distinct and nonadjacent nodes is the minimum number of nodes that must be removed (minimum separating cutset) to disconnect them. By Menger’s theorem, this is equal to the number of node independent paths (paths that share no nodes other than source and target). Which is what we compute in this function.

This algorithm is a fast approximation that gives an strict lower bound on the actual number of node independent paths between two nodes [1]. It works for both directed and undirected graphs."

all_pairs_node_connectivity(G, nbunch=None, cutoff=None)

"Compute node connectivity between all pairs of nodes.

Pairwise or local node connectivity between two distinct and nonadjacent nodes is the minimum number of nodes that must be removed (minimum separating cutset) to disconnect them. By Menger’s theorem, this is equal to the number of node independent paths (paths that share no nodes other than source and target). Which is what we compute in this function.

This algorithm is a fast approximation that gives an strict lower bound on the actual number of node independent paths between two nodes [1]. It works for both directed and undirected graphs."

https://networkx.github.io/documentation/stable/reference/algorithms/approximation.html#

