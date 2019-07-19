def find_cutoff():
    """
        Defines a local neighborhood and finds the local peaks
        in the spectrogram, which must be larger than the
        specified `amp_min`.


        Returns
        -------
        List[Tuple[int, int]]
            Time and frequency index-values of the local peaks in spectrogram.
            Sorted by ascending frequency and then time.
    """
    db=np.load(stuff.npy) #your database
    dq=np.load(david.npy) #your picture
    nodes=pairwise_dists(db,dq)
    fig, ax = plt.subplots()
    ax.hist(nodes,bin=len(nodes)//2,density=True)
    plt.show()

