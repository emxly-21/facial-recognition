def img_in_database(des, db, cutoff):
    """
    Returns the name of recognized face; if not recognized return 'not found'

    Parameters
    ----------
    des : numpy.1darray, shape=(128,)
        The descriptor vector from dlib
    db : dictionary containing [str name : (str name, array of descriptors, mean descriptor method)]
        database of all image data
    cutoff: int
        how similar descriptor vector must be

    Returns
    -------
    string
    """
    for key in db:
        if np.abs(des - d[key][2]) <= cutoff:
            return d[key][0]
    return "not found"