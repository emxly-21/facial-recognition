import numpy as np
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
        if(key != "Unknown Counter"):
            #print("db[key]")
            #print(db[key])
            diff = des - db[key][2]
            sqrd = diff ** 2
            sum_sqrd = np.sum(sqrd)
            mag = np.sqrt(sum_sqrd)
            if mag < cutoff:
                return db[key][0]
    return "not found"
