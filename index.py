import tkinter as tk
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

from networkx.algorithms import approximation as approx
#build a window using tkInter
window = tk.Tk()
window.title('Menu of Graph problems')
window.geometry('500x800')


#The followings are based on one graph problem, which is traversal problem: DFS

#when clickc(hit) on traversal_dfs_edges  to calculate input graph's using dfs
def hit_traversal_dfs_edges():
    def show_result():
        m = path.get()
        n = depth.get()

        #input user graph
        with open(m) as csvfile: #read the csv file, row by row
            reader = csv.reader(csvfile)
            next(reader)
            source = []
            target = []
            value = []
            for row in reader:
                source.append(int(row[0]))
                target.append(int(row[1]))
                value.append(int(row[2]))

        #create one empty graph
        G = nx.DiGraph()

        #add nodes to the graph
        for i in range(0, np.size(target) + 1):
            G.add_node(i)

        #add weighted edges to the graph
        for i in range(np.size(source)):
            G.add_weighted_edges_from([(source[i], target[i], value[i])])

        #assign layout with spacing
        pos = nx.spring_layout(G)
        #graph is loaded completely

        messagebox.showinfo(title='Result', message=('the edges of G in dfs are:', list(nx.dfs_edges(G, source=0, depth_limit=int(n))))) #this is the function that you need to solve the problem: nx.dfs_edges()

        #draw the graph
        nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
        pylab.title('Self_Define Net', fontsize=15)
        pylab.show()

    #create window for dfs_edges
    a = messagebox.askyesno(title='are you sure', message='you have chosen dfs_edges problem, continue?')
    if (a == True):
        window3 = tk.Toplevel(window)
        window3.geometry('400x300')
        window3.title('Iterate over edges in a depth-ﬁrst-search')
        tk.Label(window3, text='input the necessary components: ', bg='yellow').place(x=10, y=10)

    def select_path():
        path_ = askopenfilename() #path function
        path.set(path_)

    #use path function to get path
    #pass the value of path

    path = tk.StringVar()
    path.set('path')
    tk.Label(window3, text='input the path to import your own graph : ', bg = 'green').place(x=10, y=10)
    entry_path = tk.Entry(window3, textvariable = path, width = 35)
    entry_path.place(x=10, y=35)
    tk.Button(window3, text = 'choose path', command = select_path).place(x = 250, y = 35)

    #this dfs problem can be implemented with constraint of depth:
    depth = tk.StringVar()
    depth.set('number')
    tk.Label(window3, text='input the depth limit you want to see: ', bg = 'green').place(x=10, y=60)
    entry_depth = tk.Entry(window3, textvariable=depth,width = 35)
    entry_depth.place(x=10, y=85)

    ''' 
        这是输入的代码写法，按照格式修改变量名和文本内容即可

        new_name = tk.StringVar()  # 将输入的注册名赋值给变量
        new_name.set('number')  # 将最初显示定为'number'
        tk.Label(window_sign_up, text='input the number of path of the Graph you want to create : ').place(x=10, y=10)
        entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_new_name.place(x=10, y=35)  # `entry`放置在坐标（10,35）.

    '''
    #confirm, and generate the output
    confirm = tk.Button(window3, text = 'confirm', command = show_result, bg = 'yellow').place(x = 150, y = 130)




def hit_traversal_dfs():
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen Depth_first_search problem, continue?')
    if(a == True):
        #create a new window for traversal_dfs problem
        #create a menu of dfs subproblems
        window2 = tk.Toplevel(window)
        window2.geometry('500x300')
        window2.title('Depth_first_search problems')
        tk.Label(window2, text='choose the sort of Depth_first_search problem you want to deal with: ', bg='yellow').place(x = 10, y = 10)
        dfs_edges = tk.Button(window2, text='Iterate over edges in a depth-ﬁrst-search', command = hit_traversal_dfs_edges, width = 40, anchor = 'w')
        dfs_edges.place(x = 10, y = 50)
        dfs_tree = tk.Button(window2, text='Return oriented tree constructed from a depth-ﬁrst-search from source', width = 40, anchor = 'w')
        dfs_tree .place(x=10, y=80)
        dfs_predecessors = tk.Button(window2, text='Return dictionary of predecessors in depth-ﬁrst-search from source', width = 40, anchor = 'w')
        dfs_predecessors.place(x=10, y=110)
        dfs_successors = tk.Button(window2, text='Return dictionary of successors in depth-ﬁrst-search from source', width = 40, anchor = 'w')
        dfs_successors.place(x=10, y=140)
        dfs_preorder_nodes = tk.Button(window2, text='Generate nodes in a depth-ﬁrst-search pre-ordering starting at source', width = 40, anchor = 'w')
        dfs_preorder_nodes.place(x=10, y=170)
        dfs_postorder_nodes = tk.Button(window2, text='Generate nodes in a depth-ﬁrst-search post-ordering starting at source', width = 40, anchor = 'w')
        dfs_postorder_nodes.place(x=10, y=200)
        dfs_labeled_edges = tk.Button(window2, text='Iterate over edges in a depth-ﬁrst-search labeled by type',width=40, anchor='w')
        dfs_labeled_edges.place(x=10, y=230)



#when choosing traversal problem:
def hit_traversal():
    #prompt for confirmation
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen traversal problem, continue?')
    if(a == True):
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x200')
        window1.title('traversal problems')
        tk.Label(window1, text='choose the sort of traversal problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
        dfs = tk.Button(window1, text = 'Depth_first_search', command = hit_traversal_dfs, width = 25, anchor = 'w')
        dfs.place(x = 10, y = 50)
        bfs = tk.Button(window1, text = 'Breadth_first_search', width = 25, anchor = 'w')
        bfs.place(x = 10, y = 80)
        bs = tk.Button(window1, text = 'Beam_search', width = 25, anchor = 'w')
        bs.place(x = 10, y = 110)


#start approximation methods 

########################
#Connectivity start
def node_connectivity_hit():
    def show_result():
        m = path.get()
        #input user graph
        with open(m) as csvfile: #read the csv file, row by row
            reader = csv.reader(csvfile)
            next(reader)
            source = []
            target = []
            value = []
            for row in reader:
                source.append(int(row[0]))
                target.append(int(row[1]))
                value.append(int(row[2]))
        #create one empty graph
        G = nx.Graph()
        #add nodes to the graph
        for i in range(0, np.size(target) + 1):
            G.add_node(i)
        #add weighted edges to the graph
        for i in range(np.size(source)):
            G.add_weighted_edges_from([(source[i], target[i], value[i])])
        #assign layout with spacing
        pos = nx.spring_layout(G)
        #graph is loaded completely
        messagebox.showinfo(title='Result', message=('the node_connectivity is ', approx.node_connectivity(G))) #solves the node connectivity problem
        #draw the graph
        nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
        pylab.title('Self_Define Net', fontsize=15)
        pylab.show()
        return
    #create window for dfs_edges
    a = messagebox.askyesno(title='are you sure', message='you have chosen node_connectivity, continue?')
    if (a == True):
        window3 = tk.Toplevel(window)
        window3.geometry('400x300')
        window3.title('Iterate over edges in a depth-ﬁrst-search')
        tk.Label(window3, text='input the necessary components: ', bg='yellow').place(x=10, y=10)

    #use path function to get path
    def select_path():
        path_ = askopenfilename() #path function
        path.set(path_)

    #pass the value of path
    path = tk.StringVar()
    path.set('path')
    tk.Label(window3, text='input the path to import your own graph : ', bg = 'green').place(x=10, y=10)
    entry_path = tk.Entry(window3, textvariable = path, width = 35)
    entry_path.place(x=10, y=35)
    tk.Button(window3, text = 'choose path', command = select_path).place(x = 250, y = 35)
    #confirm, and generate the output
    confirm = tk.Button(window3, text = 'confirm', command = show_result, bg = 'yellow').place(x = 150, y = 130)


    return

def all_pairs_node_connectivity_hit():
    def show_result():
        m = path.get()
        #input user graph
        with open(m) as csvfile: #read the csv file, row by row
            reader = csv.reader(csvfile)
            next(reader)
            source = []
            target = []
            value = []
            for row in reader:
                source.append(int(row[0]))
                target.append(int(row[1]))
                value.append(int(row[2]))
        #create one empty graph
        G = nx.Graph()
        #add nodes to the graph
        for i in range(0, np.size(target) + 1):
            G.add_node(i)
        #add weighted edges to the graph
        for i in range(np.size(source)):
            G.add_weighted_edges_from([(source[i], target[i], value[i])])
        #assign layout with spacing
        pos = nx.spring_layout(G)
        #graph is loaded completely
        result = approx.all_pairs_node_connectivity(G)
        print(result[0])
        print("HERES THE G")
        G = nx.Graph(result)
        print("conversion complete")
        messagebox.showinfo(title='Result', message=('the all pairs node_connectivity maximum is ', approx.node_connectivity(G))) #solves the node connectivity problem
        #draw the graph
        nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
        pylab.title('Self_Define Net', fontsize=15)
        pylab.show()
        return
    #create window for dfs_edges
    a = messagebox.askyesno(title='are you sure', message='you have chosen all_pairs_node_connectivity, continue?')
    if (a == True):
        window3 = tk.Toplevel(window)
        window3.geometry('400x300')
        window3.title('Iterate over edges in a depth-ﬁrst-search')
        tk.Label(window3, text='input the necessary components: ', bg='yellow').place(x=10, y=10)

    #use path function to get path
    def select_path():
        path_ = askopenfilename() #path function
        path.set(path_)

    #pass the value of path
    path = tk.StringVar()
    path.set('path')
    tk.Label(window3, text='input the path to import your own graph : ', bg = 'green').place(x=10, y=10)
    entry_path = tk.Entry(window3, textvariable = path, width = 35)
    entry_path.place(x=10, y=35)
    tk.Button(window3, text = 'choose path', command = select_path).place(x = 250, y = 35)
    #confirm, and generate the output
    confirm = tk.Button(window3, text = 'confirm', command = show_result, bg = 'yellow').place(x = 150, y = 130)
    return

def local_node_connectivity_hit():
    def show_result():
        m = path.get()
        #input user graph
        with open(m) as csvfile: #read the csv file, row by row
            reader = csv.reader(csvfile)
            next(reader)
            source = []
            target = []
            value = []
            for row in reader:
                source.append(int(row[0]))
                target.append(int(row[1]))
                value.append(int(row[2]))
        #create one empty graph
        G = nx.Graph()
        #add nodes to the graph
        for i in range(0, np.size(target) + 1):
            G.add_node(i)
        #add weighted edges to the graph
        for i in range(np.size(source)):
            G.add_weighted_edges_from([(source[i], target[i], value[i])])
        #assign layout with spacing
        pos = nx.spring_layout(G)
        #graph is loaded completely
        messagebox.showinfo(title='Result', message=('the node_connectivity is ', approx.local_node_connectivity(G,int(node1.get()),int(node2.get())))) #solves the node connectivity problem
        #draw the graph
        nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
        pylab.title('Self_Define Net', fontsize=15)
        pylab.show()
        return
    #create window for dfs_edges
    a = messagebox.askyesno(title='are you sure', message='you have chosen Local_node_node_connectivity, continue?')
    if (a == True):
        window3 = tk.Toplevel(window)
        window3.geometry('400x300')
        window3.title('Iterate over edges in a depth-ﬁrst-search')
        tk.Label(window3, text='input the necessary components: ', bg='yellow').place(x=10, y=10)

    #use path function to get path
    def select_path():
        path_ = askopenfilename() #path function
        path.set(path_)

    #pass the value of path
    path = tk.StringVar()
    node1 = tk.StringVar()
    node2 = tk.StringVar()
    path.set('path')
    tk.Label(window3, text='input the path to import your own graph : ', bg = 'green').place(x=10, y=10)
    tk.Label(window3, text='Place node 1 : ', bg = 'green').place(x=10, y=60)
    tk.Label(window3, text='Place node 2 : ', bg = 'green').place(x=10, y=100)
    node1_entry = tk.Entry(window3, textvariable = node1, width = 5)
    node2_entry = tk.Entry(window3, textvariable = node2, width = 5)
    entry_path = tk.Entry(window3, textvariable = path, width = 35)
    entry_path.place(x=10, y=35)
    node1_entry.place(x=300, y=60)
    node2_entry.place(x=300, y=100)
    tk.Button(window3, text = 'choose path', command = select_path).place(x = 250, y = 35)

    #confirm, and generate the output
    confirm = tk.Button(window3, text = 'confirm', command = show_result, bg = 'yellow').place(x = 150, y = 130)


    return
    return

def connectivity_hit():
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen connectivity, continue?')
    if(a == True):
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x200')
        window1.title('Connectivity')
        tk.Label(window1, text='choose the sort of Connectivity problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
        dfs = tk.Button(window1, text = 'Node_Connectivity', command = node_connectivity_hit, width = 25, anchor = 'w')
        dfs.place(x = 10, y = 50)
        bfs = tk.Button(window1, text = 'all_pairs_node_connectivity', command = all_pairs_node_connectivity_hit, width = 25, anchor = 'w')
        bfs.place(x = 10, y = 80)
        bs = tk.Button(window1, text = 'local_node_connectivity', command = local_node_connectivity_hit, width = 25, anchor = 'w')
        bs.place(x = 10, y = 110)
    return
#connectivity end
######################

#####################
#k_components start

def k_components_hit():
    def show_result():
        m = path.get()
        #input user graph
        with open(m) as csvfile: #read the csv file, row by row
            reader = csv.reader(csvfile)
            next(reader)
            source = []
            target = []
            value = []
            for row in reader:
                source.append(int(row[0]))
                target.append(int(row[1]))
                value.append(int(row[2]))
        #create one empty graph
        G = nx.Graph()
        #add nodes to the graph
        for i in range(0, np.size(target) + 1):
            G.add_node(i)
        #add weighted edges to the graph
        for i in range(np.size(source)):
            G.add_weighted_edges_from([(source[i], target[i], value[i])])
        #assign layout with spacing
        pos = nx.spring_layout(G)
        #graph is loaded completely
        result = approx.k_components(G) #solves the node connectivity problem
        print(dict(result))
        messagebox.showinfo(title='Result', message=('Here are the K components of the graph!', dict(result)))
        #draw the graph
        nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
        pylab.title('Self_Define Net', fontsize=15)
        pylab.show()
        return
    #create window for dfs_edges
    a = messagebox.askyesno(title='are you sure', message='you have chosen K components hit continue?')
    if (a == True):
        window3 = tk.Toplevel(window)
        window3.geometry('400x300')
        window3.title('K components')
        tk.Label(window3, text='input the necessary components: ', bg='yellow').place(x=10, y=10)

    #use path function to get path
    def select_path():
        path_ = askopenfilename() #path function
        path.set(path_)

    #pass the value of path
    path = tk.StringVar()
    path.set('path')
    tk.Label(window3, text='input the path to import your own graph : ', bg = 'green').place(x=10, y=10)
    entry_path = tk.Entry(window3, textvariable = path, width = 35)
    entry_path.place(x=10, y=35)
    tk.Button(window3, text = 'choose path', command = select_path).place(x = 250, y = 35)
    #confirm, and generate the output
    confirm = tk.Button(window3, text = 'confirm', command = show_result, bg = 'yellow').place(x = 150, y = 130)
    return
#K_component end
####################

############
#Clique start
def max_clique_hit(): 
    def show_result():
        m = path.get()
        #input user graph
        with open(m) as csvfile: #read the csv file, row by row
            reader = csv.reader(csvfile)
            next(reader)
            source = []
            target = []
            value = []
            for row in reader:
                source.append(int(row[0]))
                target.append(int(row[1]))
                value.append(int(row[2]))
        #create one empty graph
        G = nx.Graph()
        #add nodes to the graph
        for i in range(0, np.size(target) + 1):
            G.add_node(i)
        #add weighted edges to the graph
        for i in range(np.size(source)):
            G.add_weighted_edges_from([(source[i], target[i], value[i])])
        #assign layout with spacing
        pos = nx.spring_layout(G)
        #graph is loaded completely
        result = approx.max_clique(G)
        G = nx.make_max_clique_graph(G)
        print("conversion complete")
        messagebox.showinfo(title='Result', message=('the max clique is ', approx.max_clique(G))) #solves the node connectivity problem
        #draw the graph
        nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
        pylab.title('Self_Define Net', fontsize=15)
        pylab.show()
        return
    #create window for dfs_edges
    a = messagebox.askyesno(title='are you sure', message='max clique, continue?')
    if (a == True):
        window3 = tk.Toplevel(window)
        window3.geometry('400x300')
        window3.title('clique')
        tk.Label(window3, text='input the necessary components: ', bg='yellow').place(x=10, y=10)

    #use path function to get path
    def select_path():
        path_ = askopenfilename() #path function
        path.set(path_)

    #pass the value of path
    path = tk.StringVar()
    path.set('path')
    tk.Label(window3, text='input the path to import your own graph : ', bg = 'green').place(x=10, y=10)
    entry_path = tk.Entry(window3, textvariable = path, width = 35)
    entry_path.place(x=10, y=35)
    tk.Button(window3, text = 'choose path', command = select_path).place(x = 250, y = 35)
    #confirm, and generate the output
    confirm = tk.Button(window3, text = 'confirm', command = show_result, bg = 'yellow').place(x = 150, y = 130)
    return
    return

def clique_remove_hit():
    def show_result():
        m = path.get()
        #input user graph
        with open(m) as csvfile: #read the csv file, row by row
            reader = csv.reader(csvfile)
            next(reader)
            source = []
            target = []
            value = []
            for row in reader:
                source.append(int(row[0]))
                target.append(int(row[1]))
                value.append(int(row[2]))
        #create one empty graph
        G = nx.Graph()
        #add nodes to the graph
        for i in range(0, np.size(target) + 1):
            G.add_node(i)
        #add weighted edges to the graph
        for i in range(np.size(source)):
            G.add_weighted_edges_from([(source[i], target[i], value[i])])
        #assign layout with spacing
        pos = nx.spring_layout(G)
        #graph is loaded completely
        result = approx.clique_removal(G)
        print("conversion complete")
        messagebox.showinfo(title='Result', message=('the max clique removed is ', result)) #solves the node connectivity problem
        #draw the graph
        nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
        pylab.title('Self_Define Net', fontsize=15)
        pylab.show()
        return
    #create window for dfs_edges
    a = messagebox.askyesno(title='are you sure', message='max clique, continue?')
    if (a == True):
        window3 = tk.Toplevel(window)
        window3.geometry('400x300')
        window3.title('clique')
        tk.Label(window3, text='input the necessary components: ', bg='yellow').place(x=10, y=10)

    #use path function to get path
    def select_path():
        path_ = askopenfilename() #path function
        path.set(path_)

    #pass the value of path
    path = tk.StringVar()
    path.set('path')
    tk.Label(window3, text='input the path to import your own graph : ', bg = 'green').place(x=10, y=10)
    entry_path = tk.Entry(window3, textvariable = path, width = 35)
    entry_path.place(x=10, y=35)
    tk.Button(window3, text = 'choose path', command = select_path).place(x = 250, y = 35)
    #confirm, and generate the output
    confirm = tk.Button(window3, text = 'confirm', command = show_result, bg = 'yellow').place(x = 150, y = 130)
    return

def clique_hit():
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen clique problem, continue?')
    if(a == True):
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x200')
        window1.title('Clique problems')
        tk.Label(window1, text='choose the sort of traversal problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
        dfs = tk.Button(window1, text = 'Max Clique', command = max_clique_hit, width = 25, anchor = 'w')
        dfs.place(x = 10, y = 50)
        bfs = tk.Button(window1, text = 'Clique Remove', command = clique_remove_hit, width = 25, anchor = 'w')
        bfs.place(x = 10, y = 80)
    return

#Clique end
#################3

def clustering_hit():
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen clique problem, continue?')
    if(a == True):
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x200')
        window1.title('traversal problems')
        tk.Label(window1, text='choose the sort of traversal problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
        dfs = tk.Button(window1, text = 'Depth_first_search', command = hit_traversal_dfs, width = 25, anchor = 'w')
        dfs.place(x = 10, y = 50)
        bfs = tk.Button(window1, text = 'Breadth_first_search', width = 25, anchor = 'w')
        bfs.place(x = 10, y = 80)
        bs = tk.Button(window1, text = 'Beam_search', width = 25, anchor = 'w')
        bs.place(x = 10, y = 110)
    return

def dominating_set_hit():
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen dominating set problem, continue?')
    if(a == True):
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x200')
        window1.title('traversal problems')
        tk.Label(window1, text='choose the sort of traversal problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
        dfs = tk.Button(window1, text = 'Depth_first_search', command = hit_traversal_dfs, width = 25, anchor = 'w')
        dfs.place(x = 10, y = 50)
        bfs = tk.Button(window1, text = 'Breadth_first_search', width = 25, anchor = 'w')
        bfs.place(x = 10, y = 80)
        bs = tk.Button(window1, text = 'Beam_search', width = 25, anchor = 'w')
        bs.place(x = 10, y = 110)
    return

def independent_set_hit():
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen independent set problem, continue?')
    if(a == True):
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x200')
        window1.title('traversal problems')
        tk.Label(window1, text='choose the sort of traversal problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
        dfs = tk.Button(window1, text = 'Depth_first_search', command = hit_traversal_dfs, width = 25, anchor = 'w')
        dfs.place(x = 10, y = 50)
        bfs = tk.Button(window1, text = 'Breadth_first_search', width = 25, anchor = 'w')
        bfs.place(x = 10, y = 80)
        bs = tk.Button(window1, text = 'Beam_search', width = 25, anchor = 'w')
        bs.place(x = 10, y = 110)
    return

def matching_hit():
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen matching problem, continue?')
    if(a == True):
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x200')
        window1.title('traversal problems')
        tk.Label(window1, text='choose the sort of traversal problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
        dfs = tk.Button(window1, text = 'Depth_first_search', command = hit_traversal_dfs, width = 25, anchor = 'w')
        dfs.place(x = 10, y = 50)
        bfs = tk.Button(window1, text = 'Breadth_first_search', width = 25, anchor = 'w')
        bfs.place(x = 10, y = 80)
        bs = tk.Button(window1, text = 'Beam_search', width = 25, anchor = 'w')
        bs.place(x = 10, y = 110)
    return

def ramsey_hit():
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen ramsey problem, continue?')
    if(a == True):
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x200')
        window1.title('traversal problems')
        tk.Label(window1, text='choose the sort of traversal problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
        dfs = tk.Button(window1, text = 'Depth_first_search', command = hit_traversal_dfs, width = 25, anchor = 'w')
        dfs.place(x = 10, y = 50)
        bfs = tk.Button(window1, text = 'Breadth_first_search', width = 25, anchor = 'w')
        bfs.place(x = 10, y = 80)
        bs = tk.Button(window1, text = 'Beam_search', width = 25, anchor = 'w')
        bs.place(x = 10, y = 110)
    return

def vertex_cover_hit():
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen vertex cover problem, continue?')
    if(a == True):
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x200')
        window1.title('traversal problems')
        tk.Label(window1, text='choose the sort of traversal problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
        dfs = tk.Button(window1, text = 'Depth_first_search', command = hit_traversal_dfs, width = 25, anchor = 'w')
        dfs.place(x = 10, y = 50)
        bfs = tk.Button(window1, text = 'Breadth_first_search', width = 25, anchor = 'w')
        bfs.place(x = 10, y = 80)
        bs = tk.Button(window1, text = 'Beam_search', width = 25, anchor = 'w')
        bs.place(x = 10, y = 110)
    return

#end approximation methods

def hit_approximation():
    #prompt for confirmation
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen approximation problem, continue?')
    if(a == True):
        algorithm_names = ["Connectivity", "K-components", "Clique", "Clustering", "Dominating Set", "Independent Set", "Matching", "Ramsey", "Vertex Cover"]
        algorithms      = [ connectivity_hit,k_components_hit,clique_hit,clustering_hit,dominating_set_hit,independent_set_hit,matching_hit,ramsey_hit, vertex_cover_hit]
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x400')
        window1.title('traversal problems')
        label = [None] * len(algorithm_names)
        tk.Label(window1, text='choose the sort of Approximation problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)

        for i in range(len(algorithm_names)):
            label[i] = tk.Button(window1, text = algorithm_names[i], command = algorithms[i], width = 25, anchor = 'w')
            label[i].place(x = 10, y = 50 + 40*i)

        return

        #dfs = tk.Button(window1, text = 'Depth_first_search', command = hit_traversal_dfs, width = 25, anchor = 'w')
        #dfs.place(x = 10, y = 50)
        #bfs = tk.Button(window1, text = 'Breadth_first_search', width = 25, anchor = 'w')
        #bfs.place(x = 10, y = 80)
        #bs = tk.Button(window1, text = 'Beam_search', width = 25, anchor = 'w')
        #bs.place(x = 10, y = 110)




#buttons of the big menu (you don't need to create this menu)

traversal = tk.Button(window, text = '46.Traversal problem', command = hit_traversal, width = 25, anchor = 'w')
traversal.place(x= 260, y = 570)
approximation = tk.Button(window, text = '1. Approximation problem', command = hit_approximation, width = 25, anchor = 'w')
approximation.place(x = 10, y = 0)
assortativity = tk.Button(window, text = '2. Assortativity problem', width = 25, anchor = 'w')
assortativity.place(x= 10, y = 30)
bipartite = tk.Button(window, text = '3. Bipartite problem', width = 25, anchor = 'w')
bipartite.place(x = 10, y = 60)
boundary = tk.Button(window, text = '4. Boundary problem', width = 25, anchor = 'w')
boundary.place(x = 10, y = 90)
bridges = tk.Button(window, text = '5. Bridges problem', width = 25, anchor = 'w')
bridges.place(x = 10, y = 120)
centrality = tk.Button(window, text = '6. Centrality problem', width = 25, anchor = 'w')
centrality.place(x = 10, y = 150)
chains = tk.Button(window, text = '7. Chains problem', width = 25, anchor = 'w')
chains.place(x= 10, y = 180)
chordal = tk.Button(window, text = '8. Chordal problem', width = 25, anchor = 'w')
chordal.place(x = 10, y = 210)
clique = tk.Button(window, text = '9. Clique problem', width = 25, anchor = 'w')
clique.place(x= 10, y = 240)
clustering = tk.Button(window, text = '10. Clustering problem', width = 25, anchor = 'w')
clustering.place(x= 10, y = 270)
coloring = tk.Button(window, text = '11. Coloring problem', width = 25, anchor = 'w')
coloring.place(x = 10, y = 300)
communicability = tk.Button(window, text = '12. Communicability', width = 25, anchor = 'w')
communicability.place(x = 10, y = 330)
components = tk.Button(window, text = '13. Components problem', width = 25, anchor = 'w')
components.place(x = 10, y = 360)
connectivity = tk.Button(window, text = '14. Connectivity problem', width = 25, anchor = 'w')
connectivity.place(x = 10, y = 390)
cores = tk.Button(window, text = '15. Cores problem', width = 25, anchor = 'w')
cores.place(x = 10, y = 420)
covering = tk.Button(window, text = '16. Covering problem', width = 25, anchor = 'w')
covering.place(x= 10, y = 450)
cycles = tk.Button(window, text = '17. Cycles problem', width = 25, anchor = 'w')
cycles.place(x= 10, y = 480)
cuts = tk.Button(window, text = '18. Cuts problem', width = 25, anchor = 'w')
cuts.place(x= 10, y = 510)
directed_acyclic = tk.Button(window, text = '19. Directed_acyclic problem', width = 25, anchor = 'w')
directed_acyclic.place(x = 10, y = 540)
dispersion = tk.Button(window, text = '20. Dispersion problem', width = 25, anchor = 'w')
dispersion.place(x = 10, y = 570)
distance_measures = tk.Button(window, text = '21. Distance_measure problem', width = 25, anchor = 'w')
distance_measures.place(x = 10, y = 600)
distance_regular = tk.Button(window, text = '22. Distance_regular',width = 25, anchor = 'w')
distance_regular.place(x = 10, y = 630)
dominance = tk.Button(window, text = '23. Dominance', width = 25, anchor = 'w')
dominance.place(x = 10, y = 660)
dominating_sets = tk.Button(window, text = '24. Dominating_sets problem', width = 25, anchor = 'w')
dominating_sets.place(x = 10, y = 690)
efficiency = tk.Button(window, text = '25. Efficiency problem', width = 25, anchor = 'w')
efficiency.place(x = 10, y = 720)
eulerian = tk.Button(window, text = '26. Eulerian problem', width = 25, anchor = 'w')
eulerian.place(x = 10, y = 750)
flows = tk.Button(window, text = '27. Flows problem', width = 25, anchor = 'w')
flows.place(x = 260, y =0)
graphical_degree = tk.Button(window, text = '28. Graphical_degree problem', width = 25, anchor = 'w')
graphical_degree.place(x = 260, y = 30)
hierarchy = tk.Button(window, text = '29. Hierarchy problem',width = 25, anchor = 'w')
hierarchy.place(x = 260, y = 60)
hybrid = tk.Button(window, text = '30. Hybrid problem', width = 25, anchor = 'w')
hybrid.place(x = 260, y = 90)
isolates = tk.Button(window, text = '31. Isolates problem', width = 25, anchor = 'w')
isolates.place(x = 260, y = 120)
isomorphism = tk.Button(window, text = '32. Isomorphism problem', width = 25, anchor = 'w')
isomorphism.place(x = 260, y = 150)
link_analysis = tk.Button(window, text = '33. Link_analysis problem', width = 25, anchor = 'w')
link_analysis.place(x = 260, y = 180)
link_prediction = tk.Button(window, text = '34. Link_prediction problem', width = 25, anchor = 'w')
link_prediction.place(x = 260, y = 210)
matching = tk.Button(window, text = '35. Matching problem', width = 25, anchor = 'w')
matching.place(x = 260, y = 240)
minors = tk.Button(window, text = '36. Minors problems', width = 25, anchor = 'w')
minors.place(x = 260, y = 270)
max_independent_set = tk.Button(window, text = '37. Max_independent_set problem', width = 30, anchor = 'w')
max_independent_set.place(x = 260, y = 300)
operators = tk.Button(window, text = '38. Operators problems', width = 25, anchor = 'w')
operators.place(x = 260, y = 330)
reciprocity = tk.Button(window, text = '39. Reciprocity problem', width = 25, anchor = 'w')
reciprocity.place(x = 260, y = 360)
rich_club = tk.Button(window, text = '40. Rich_club problem', width = 25, anchor = 'w')
rich_club.place(x = 260, y = 390)
shortest_path = tk.Button(window, text = '41. Shortest_path problem', width = 25, anchor = 'w')
shortest_path.place(x = 260, y = 420)
simple_path = tk.Button(window, text = '42. Simple_path problem', width = 25, anchor = 'w')
simple_path.place(x = 260, y = 450)
structural_holes = tk.Button(window, text = '43. Structural_holes problem', width = 25, anchor = 'w')
structural_holes.place(x = 260, y = 480)
swap = tk.Button(window, text = '44. Swap problems', width = 25, anchor = 'w')
swap.place(x = 260, y = 510)
tournament = tk.Button(window, text = '45. Tournament problem', width = 25, anchor = 'w')
tournament.place(x = 260, y = 540)
tree = tk.Button(window, text = '47. Tree problem', width = 25, anchor = 'w')
tree.place(x = 260, y = 600)
triads = tk.Button(window, text = '48. Triads problem', width = 25, anchor = 'w')
triads.place(x = 260, y = 630)
vitality = tk.Button(window, text = '49. Vitality problem', width = 25, anchor = 'w')
vitality.place(x = 260, y =  660)
voronoi_cells = tk.Button(window, text = '50. Voronoi_cells problem', width = 25, anchor = 'w')
voronoi_cells.place(x = 260, y = 690)
wiener_index = tk.Button(window, text = '51. Wiener_index problem', width = 25, anchor = 'w')
wiener_index.place(x = 260, y = 720)



window.mainloop()
