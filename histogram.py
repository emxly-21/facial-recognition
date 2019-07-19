def find_cutoff(db, pic):
    """
        Defines a local neighborhood and finds the local peaks
        in the spectrogram, which must be larger than the
        specified `amp_min`.

        Displays a plot
    """
    db=np.load() #your database
    dq=np.load() #your picture
    nodes=pairwise_dists(db,dq)
    fig, ax = plt.subplots()
    ax.hist(nodes,bin=len(nodes)//2,density=True)
    plt.show()

