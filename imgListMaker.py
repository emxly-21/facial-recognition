from camera import take_picture
# run this cell to setup matplotlib, and also import the very important take_picture function from camera!
import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np
import portfolio_methods as portfolio
import match
import pickle

# run this cell to download the models from dlib
from dlib_models import download_model, download_predictor, load_dlib_models

download_model()
download_predictor()
from dlib_models import models


def doStuff():
# take the picture
    pic = take_picture()
    b = np.load("stuff.npy")



    # first, we load the models that dlib has to detect faces.
    load_dlib_models()
    face_detect = models["face detect"]
    face_rec_model = models["face rec"]
    shape_predictor = models["shape predict"]

    # detects the face through corners
    detections = list(face_detect(pic))
    print(detections)  # list of shape n for n faces

    fig, ax = plt.subplots()
    ax.imshow(pic)

    with open("database.pkl", mode="rb") as opened_file:
        database = pickle.load(opened_file)


    print("Number of faces detected: {}".format(len(detections)))
    for k, d in enumerate(detections):
        # Get the landmarks/parts for the face in box d.
        shape = shape_predictor(pic, d)
        # Draw the face landmarks on the screen.
        for i in range(68):
            ax.plot(shape.part(i).x, shape.part(i).y, '+', color="blue")

    import matplotlib.patches as patches

    for faces in detections:
        # Create a Rectangle patch
        rect = patches.Rectangle((faces.left(), faces.bottom()), faces.width(), -faces.height(), linewidth=1,
                                 edgecolor='g', facecolor='none')
        # Add the patch to the Axes
        ax.add_patch(rect)
        shape = shape_predictor(pic, faces)
        descriptor = np.array(face_rec_model.compute_face_descriptor(pic, shape))
        print(descriptor)
        print("b shape", b.shape)
        descriptor= descriptor.reshape(1, 128)
        print("descriptor shape", descriptor.shape)

        b = np.append(b, descriptor, axis=0)
        np.save("stuff.npy", b)
        print("b", b)
        if b[0][1] == 0.0 and b[0][11] == 0.0:
            b = np.array(b[1]).reshape(1, 128)
        print("b",b)
    np.save("stuff.npy",b)
    plt.show()
doStuff()