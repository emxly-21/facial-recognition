def update_profile(des, name, db):
    '''
    Updates the profile of the recognized person by adding the descriptor
    for the current picture into the database.

    Parameters
    ----------
    des : numpy.ndarray[numpy.float32]
        128-dimensional descriptor taken from the image of the recognized
        person's face

    name : string
        Name of the recognized person

    db : Dictionary[string, Tuple[string, List[numpy.ndarray[numpy.float32]], numpy.ndarray[numpy.float32]]]
        Database containing current profiles, with the keys as the people's
        names and the values as tuples with their (names, descriptors,
        mean descriptors).

    Returns
    -------
    Dictionary[string, Tuple[string, List[numpy.ndarray[numpy.float32]], numpy.ndarray[numpy.float32]]]
        Updated database with descriptor from current picture added into the
        recognized person's portfolio.

    '''
    cur_name, des_list, mean_des = db[name]
    des_list.append(des)
    for val in range(len(mean_des)):
        mean_des[val] *= len(des_list - 1)
        mean_des[val] += des[val]
        mean_des[val] /= len(des_list)
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
        128-dimensional descriptor taken from the image of the recognized
        person's face

    name : string
        Name of the recognized person

    db : Dictionary[string, Tuple[string, numpy.ndarray[numpy.ndarray[numpy.float32]], numpy.ndarray[numpy.float32]]]
        Database containing current profiles, with the keys as the people's
        names and the values as tuples with their (names, descriptors,
        mean descriptors).

    Returns
    -------
    Dictionary[string, Tuple[string, List[numpy.ndarray[numpy.float32]], numpy.ndarray[numpy.float32]]]
        Updated database with descriptor from current picture added into the
        recognized person's portfolio.

    '''
    value = (name, [des], des)
    db[name] = value
    return db