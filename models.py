from dotenv import load_dotenv
import os

load_dotenv()

models = os.getenv("MODELS")

MODELS = [
   "prompthero/openjourney",
   "digiplay/AbsoluteReality",
   "UnfilteredAI/NSFW-gen-v2",
   "phenixrhyder/NSFW-generator",
   "digiplay/MengX_Mix_Fantasy_v4",
   "Nymbo/NSFW-generator",
   "stabilityai/stable-diffusion-xl-base-1.0",
]

if models:
    models_list = models.split(",")
    MODELS.extend(models_list)
