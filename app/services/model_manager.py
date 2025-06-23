from tensorflow.keras.models import load_model

class ModelManager:
    def __init__(self):
        self.disease_model = load_model("models/inception_v3_final_model.keras", compile=False)
        self.variety_model = load_model("models/resnet50_variety_final.keras", compile=False)
        self.age_model     = load_model("models/mobilenetv2_age_final.keras", compile=False)

model_manager = ModelManager()
