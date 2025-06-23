import numpy as np
from app.utils.preprocessing import preprocess
from app.services.model_manager import model_manager

DISEASES = [
    "BacterialLeafBlight", "Blast", "BrownSpot", "Healthy",
    "LeafBlast", "NeckBlast", "NarrowBrownSpot", "Tungro",
    "FalseSmut", "SheathRot"
]

VARIETIES = [
    "OM5451", "OM18", "OM4900", "OM576", "OM7347",
    "OM4495", "OM6976", "OM380", "OMCS2000", "OM2517"
]

IMG_SIZES = {
    "task1": (224, 224),
    "task2": (128, 128),
    "task3": (224, 224)
}

def run_all_models(image_bytes):
    x1 = preprocess(image_bytes, IMG_SIZES["task1"])
    x2 = preprocess(image_bytes, IMG_SIZES["task2"])
    x3 = preprocess(image_bytes, IMG_SIZES["task3"])

    x1 = np.expand_dims(x1, axis=0)
    x2 = np.expand_dims(x2, axis=0)
    x3 = np.expand_dims(x3, axis=0)

    disease_pred = DISEASES[np.argmax(model_manager.disease_model.predict(x1))]
    variety_pred = VARIETIES[np.argmax(model_manager.variety_model.predict(x2))]
    age_pred = float(model_manager.age_model.predict(x3)[0][0])

    return {
        "disease": disease_pred,
        "variety": variety_pred,
        "age": round(age_pred, 2)
    }
