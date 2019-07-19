import numpy as np
from os.path import dirname, abspath
from pathlib import Path
import skimage.io as io
import numpy as np
import pickle
from dlib_models import download_model, download_predictor, load_dlib_models
download_model()
download_predictor()
from dlib_models import models

def saveImages():
    """
    TODO: This docstring
    :return:
    """
    dict = {}
    try:
        with open("database.pkl", mode="rb") as opened_file:
            my_loaded_grades = pickle.load(opened_file)
    except:
        dict = {}
    d = Path(dirname(abspath("saveImg.py")))
    d = Path(d / r"Images")
    images = sorted(d.glob('*.jpg'))
    for item in images:
        img = io.imread(item)
        load_dlib_models()
        face_detect = models["face detect"]
        face_rec_model = models["face rec"]
        shape_predictor = models["shape predict"]
        detections = list(face_detect(img))
        if detections != []:
            shape = shape_predictor(img, detections[0])
            descriptor = np.array(face_rec_model.compute_face_descriptor(img, shape))
            print(descriptor)
            print(descriptor.shape)