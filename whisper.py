import numpy as np
from create_edges import create_edges
from near_label import near_labels
from node import Node
from node import plot_graph

def whispers():
    database=np.load("stuff.npy")
    nodes=create_edges(database)
    nodes=near_labels(nodes)
    plot_graph(nodes)






