import numpy as np
from create_edges import create_edges
from near_label import near_labels
from node import Node
from node import plot_graph
from create_edges import pairwise_dists

def whispers():
    database=np.load("stuff.npy")
    nodes=create_edges(database)
    nodes=near_labels(nodes)
    adj=pairwise_dists(database,database)
    plot_graph(nodes,adj)

'''def find_adj(nodes):
    adj=np.zeros(len(nodes)**2).reshape(len(nodes),len(nodes))
    for node in nodes:
        if node.ID is nodes[i]

'''




