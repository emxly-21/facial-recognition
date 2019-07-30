# run this cell to setup matplotlib, and also import the very important take_picture function from camera!
import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np
import portfolio_methods as portfolio
import match
import pickle

# run this cell to download the models from dlib
from dlib_models import download_model, download_predictor, load_dlib_models
from dlib_models import models
def main(database):
    namereturn=''
    descreturn=np.array([])
    ##download_model()
    ##download_predictor()


# take the picture
    pic = take_picture()


# first, we load the models that dlib has to detect faces.
    ##load_dlib_models()
    face_detect = models["face detect"]
    face_rec_model = models["face rec"]
    shape_predictor = models["shape predict"]

# detects the face through corners
    detections = list(face_detect(pic))
# print(detections)  # list of shape n for n faces

    ##fig, ax = plt.subplots()
    ##ax.imshow(pic)

    ##database = {}


    ##with open("database.pkl", mode="rb") as opened_file:
        ##database = pickle.load(opened_file)
        #print("DATABASE")
        #print(database)



    print("Number of faces detected: {}".format(len(detections)))
    ##for k, d in enumerate(detections):
        # Get the landmarks/parts for the face in box d.
        ##shape = shape_predictor(pic, d)
        # Draw the face landmarks on the screen.
        ##for i in range(68):
            ##ax.plot(shape.part(i).x, shape.part(i).y, '+', color="blue")

    import matplotlib.patches as patches

    ##for faces in detections:
        # Create a Rectangle patch
        ##rect = patches.Rectangle((faces.left(), faces.bottom()), faces.width(), -faces.height(), linewidth=1, edgecolor='g',
        ##                         facecolor='none')
        # Add the patch to the Axes
        ##ax.add_patch(rect)

    names = {}
    database["Unknown Counter"]=0
    unknown_counter = database["Unknown Counter"]

    for face in detections:
        # let's take a look as to what the descriptor is!!
        shape = shape_predictor(pic, face)
        descriptor = np.array(face_rec_model.compute_face_descriptor(pic, shape))

        # compares descriptor to database through img_in_database
        cutoff = .4
        #print("DATABASE")
        #print(database)
        name = match.img_in_database(descriptor, database, cutoff)

        if name == "not found":
            name = "Unknown" + str(unknown_counter)
            database["Unknown Counter"] += 1

        # plots name underneath square
        ##ax.text(face.left()+(0.25*faces.width()), face.bottom()+(0.2*faces.height()), name, bbox=dict(facecolor='green', alpha=0.5))

        # adds to names dictionary
        names[name] = descriptor
        descreturn = descriptor
    ##plt.show()

    add_profile = "y"#input("Would you like to add this picture to the database? [y/n]  ")
    if add_profile == "y":
        for name in names:
        # updates or creates a profile
            if "Unknown" not in name:
                namereturn+=name
                database = portfolio.update_profile(names[name], name, database)
            else:
                add_name = input(f"Would you like to give a name for {name}? [y/n]  ")
                if add_name == "y":
                    new_name = input(f"What is {name}'s name?   ")
                    namereturn+=new_name
                    if new_name in database:
                        database = portfolio.update_profile(names[name], new_name, database)
                    else:
                        database = portfolio.create_profile(names[name], new_name, database)
                else:
                    print(f"Saving this person as {name}")
                    database = portfolio.create_profile(names[name], name, database)

    with open("database.pkl", mode="wb") as opened_file:
        pickle.dump(database, opened_file)
    return (namereturn,descreturn)
if __name__ == '__main__':
    main()