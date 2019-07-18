# run this cell to setup matplotlib, and also import the very important take_picture function from camera!
% matplotlib notebook
import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np

# run this cell to download the models from dlib
from dlib_models import download_model, download_predictor, load_dlib_models

download_model()
download_predictor()
from dlib_models import models



# take the picture
pic = take_picture()

# first, we load the models that dlib has to detect faces.
load_dlib_models()
face_detect = models["face detect"]
face_rec_model = models["face rec"]
shape_predictor = models["shape predict"]

# detects the face through corners
detections = list(face_detect(pic))
print(detections)  # list of shape n for n faces

from matplotlib.patches import Rectangle

fig, ax = plt.subplots()
ax.imshow(pic)

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
    rect = patches.Rectangle((faces.left(), faces.bottom()), faces.width(), -faces.height(), linewidth=1, edgecolor='g',
                             facecolor='none')
    # Add the patch to the Axes
    ax.add_patch(rect)
    plt.show()

for face in detections:
    # let's take a look as to what the descriptor is!!
    shape = shape_predictor(pic, face)
    descriptor = np.array(face_rec_model.compute_face_descriptor(pic, shape))
    print(descriptor)  # descriptor vector
    print(descriptor.shape)

    # compares descriptor to database through img_in_databse

    #