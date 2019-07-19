import random
from collections import Counter

def near_labels(db):
    '''
    Performs label propagation through the network of nodes and clusters
    similar nodes by giving them the same label.

    Parameters
    ----------
    db : List[Node]
        Network of Nodes, connected based on similarity.

    Returns
    -------
    Dictionary[int, List[Node]]
        Dictionary of Nodes based on which label they belong to, with the key
        being the label and the value being the list of Nodes that belong to that
        label.
    '''
    counts = [len(db)] # keeps track of how many unique labels there are
    counter = 1
    while not all(elem == counts[counter-1] for elem in counts[counter-5:]):
        rand = random.randint(0, len(db))
        rand_node = db[rand]
        neighbors = rand_node.neighbors
        highest_count = Counter(neighbors).most_common()[0][0]
        if rand_node.ID != highest_count:
            rand_node.ID = highest_count
            counts.append(counts[counter-1]-1)
        else:
            counts.append(counts[counter-1])