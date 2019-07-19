def pairwise_dists(x, y):
    """ Computing pairwise distances using memory-efficient
        vectorization.

        Parameters
        ----------
        x : numpy.ndarray, shape=(M, D)
        y : numpy.ndarray, shape=(N, D)

        Returns
        -------
        numpy.ndarray, shape=(M, N)
            The Euclidean distance between each pair of
            rows between `x` and `y`."""
    dists = -2 * np.matmul(x, y.T)
    dists +=  np.sum(x**2, axis=1)[:, np.newaxis]
    dists += np.sum(y**2, axis=1)
    return  np.sqrt(dists)


def create_edges(db, threshold):
    '''
    Updates the list of nodes by including the neighbors to it. Neighbors are identified
    as nodes that's euclidian distances are within a certain threshold value.

    :param nodes: a list of the nodes with an empty list of neighbors
    :return: list of the nodes with an updates list of neighbors
    '''
    nodes = []
    distances = pairwise_dist(db,db)
    distances = distances < threshold
    index = np.argwhere(distances)
    for i in range(len(distances)):
        neighbors = index[np.nonzero(index[:, 0] == i), 1].tolist()
        nodes.append(Node(i, neighbors, db[i]))
    return nodes