import numpy as np
from create_edges import pairwise_dists
import matplotlib.pyplot as plt
def find_cutoff(db, pic):
    """

        Displays a plot

        :parameter
            db: .npy file that contains the database to be used
            pic: .npy file containing the picture to be used.


    """
    db=np.load(db) #your database
    dq=np.load(pic) #your picture
    nodes=pairwise_dists(db,dq)
    fig, ax = plt.subplots()
    ax.hist(nodes,bin=len(nodes)//2,density=True)
    plt.show()

