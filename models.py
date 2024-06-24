from dotenv import load_dotenv
import os

load_dotenv()

models = os.getenv("MODELS")

MODELS = [
    "prompthero/openjourney",
    "Yntec/Timeless",
    "Yntec/Paramount",
    "Yntec/HyperRealism",
    "digiplay/AbsoluteReality",
    "UnfilteredAI/NSFW-gen-v2",
    "phenixrhyder/NSFW-generator",
    "digiplay/MengX_Mix_Fantasy_v4",
    "Malary/Mala-Anime-Mix-NSFW-PonyXL",
    "Yntec/CyberRealistic",
    "Yntec/NaughtyChildren",
    "gsdf/Counterfeit-V2.5",
    "Yntec/AbsoluteReality",
    "Yntec/AbsoluteRemix",
    "WarriorMama777/OrangeMixs",
    "segmind/SSD-1B",
    "sakura002/NSFW-Img",
    "stablediffusionapi/mklan-xxx-nsfw-pony",
    "Dremmar/nsfw-xl",
    "stablediffusionapi/omnigenxl-nsfw-sfw",
    "GraydientPlatformAPI/yamers-nsfw4-xl",
    "stablediffusionapi/explicit-freedom-nsfw-wai",
    "UnfilteredAI/NSFW-gen-v2",
    "Nymbo/NSFW-generator",
    "stablediffusionapi/hassaku-xl-sfwnsfw",
    "Bambambimbam/stablediffusionapi-mklan-xxx-nsfw-pony",
    "stabilityai/stable-diffusion-xl-base-1.0",
]

if models:
    models_list = models.split(",")
    MODELS.extend(models_list)
