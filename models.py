from dotenv import load_dotenv
import os

load_dotenv()

models = os.getenv("MODELS")

MODELS = [
    "WarriorMama777/OrangeMixs",
    "hakurei/waifu-diffusion",
    "gsdf/Counterfeit-V2.5",
    "Yntec/AbsoluteReality",
    "digiplay/AbsoluteReality_v1.8.1",
    "Yntec/AbsoluteRemix",
    "segmind/SSD-1B",
]

if models:
    models_list = models.split(",")
    MODELS.extend(models_list)
