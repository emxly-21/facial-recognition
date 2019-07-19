from os.path import dirname, abspath
from pathlib import Path
import skimage.io as io
import numpy as np
import pickle
from dlib_models import download_model, download_predictor, load_dlib_models, models
download_model()
download_predictor()


def saveImages():
    """
    Takes the saved images from the /Images folder, finds the faces, creates vectors to represent the faces, and then saves them to the database.pkl file
    """

    dict = {}
    try:
        with open("database.pkl", mode="rb") as opened_file:
            dict = pickle.load(opened_file)
    except:
        dict = {}
    d = Path(dirname(abspath("saveImg.py")))
    d = Path(d / r"Images")
    images = sorted(d.glob('*.jpg'))
    for item in images:
        img = io.imread(item)
        print(item.stem)
        load_dlib_models()
        face_detect = models["face detect"]
        face_rec_model = models["face rec"]
        shape_predictor = models["shape predict"]
        detections = list(face_detect(img))
        if detections != []:
            shape = shape_predictor(img, detections[0])
            descriptor = np.array(face_rec_model.compute_face_descriptor(img, shape))
            print(descriptor)
            key = str(item.stem)
            value = (str(item.stem), descriptor.reshape(-1,128), descriptor)
            dict[key] = value
    dict["Unknown Counter"] = 0
    with open("database.pkl", mode="wb") as opened_file:
        pickle.dump(dict, opened_file)
