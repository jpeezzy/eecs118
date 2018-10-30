Appriximation for graphs:  
***What is Approximation for node Connection?***  

<button class="button-save large">About Me</button>

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

k_components(G[, min_density]) - Returns the approximate k-component structure of a graph G  

Max-Clique(G): Returns the max clique  
Clique-Remove(G): Removes the max clique.   
Highlights the graph in the GUI and deletes them  

average_clustering(G, no. of trials):  
Gets average clustering.  
Will highlight all clusters during simulation.  

min_weighted_dominating_set(G[,weight])   
returns a dominating set that approximates the minimum weight node dominating set.  

Maximum_independent_set(G)  
Returns an approximate maximum independent set  
WIll highlight all nodes in that set  

min_maximal_matching(G)  
Returns the minimum maximal matching of G  
Will display in the GUI screen  

ramsey_R2(G)  
Approximately computes the Ramsey number R(2;s,t)  
Will display Ramsey number in the GUI  

httpghted_vertex_cover(G[, weight])  
Returns an approximate minimum weighted vertex cover  
After getting the minimum vertex cover, will display it inside the GUI screen  

**GOALS**  
Implementing graphs in python -- IN PROGRESS  
Implementing GUI -- NOT COMPLETED   
Documentation -- NOT COMPLETED  


