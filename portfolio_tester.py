import numpy as np

def update_profile(des, name, db):
    '''
    Updates the profile of the recognized person by adding the descriptor
    for the current picture into the database.

    Parameters
    ----------
    des : numpy.ndarray[numpy.float32]
        (128,)-dimensional descriptor taken from the image of the recognized
        person's face

    name : string
        Name of the recognized person

    db : Dictionary[string, Tuple[string, numpy.ndarray[numpy.ndarray[numpy.float32]], numpy.ndarray[numpy.float32]]]
        Database containing current profiles, with the keys as the people's
        names and the values as tuples with their (names, descriptors,
        mean descriptors). Each descriptors list is (N, 128), where N is
        the number of descriptors currently in each person's list.

    Returns
    -------
    Dictionary[string, Tuple[string, numpy.ndarray[numpy.ndarray[numpy.float32]], numpy.ndarray[numpy.float32]]]
        Updated database with descriptor from current picture added into the
        recognized person's portfolio. Each descriptors list is (N, 128), where N is
        the number of descriptors currently in each person's list.

    '''
    cur_name, des_list, mean_des = db[name]
    des_list = np.vstack((des_list, des))
    mean_des = np.mean(des_list, axis=0)
    value = (name, des_list, mean_des)
    db[name] = value
    return db


def create_portfolio(des, name, db):
    '''
    Creates the profile of the recognized person by adding the name of the
    person and descriptor for the current picture into the database.

    Parameters
    ----------
    des : numpy.ndarray[numpy.float32]
        (128,)-dimensional descriptor taken from the image of the recognized
        person's face.

    name : string
        Name of the recognized person.

    db : Dictionary[string, Tuple[string, numpy.ndarray[numpy.ndarray[numpy.float32]], numpy.ndarray[numpy.float32]]]
        Database containing current profiles, with the keys as the people's
        names and the values as tuples with their (names, descriptors,
        mean descriptors). Each descriptors list is (N, 128), where N is
        the number of descriptors currently in each person's list.

    Returns
    -------
    Dictionary[string, Tuple[string, numpy.ndarray[numpy.ndarray[numpy.float32]], numpy.ndarray[numpy.float32]]]
        Updated database with descriptor from current picture added into the
        recognized person's portfolio. Each descriptors list is (N, 128), where N is
        the number of descriptors currently in each person's list.

    '''
    value = (name, np.array([des]), des)
    db[name] = value
    return db

db = create_portfolio(np.array([0, 1, 2, 3, 4]), "David", {})
db = update_profile(np.array([1, 2, 3, 4, 5]), "David", db)
print(db)
