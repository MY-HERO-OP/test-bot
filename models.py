from dotenv import load_dotenv
import os

load_dotenv()

models = os.getenv("MODELS")

MODELS = [
   "prompthero/openjourney",
   "Yntec/DreamWorksRemix", 
    "digiplay/MengX_Mix_Fantasy_v4", #689
    "Yntec/Paramount",
    "digiplay/Yuzu_v1.1", #688
    "Yntec/Playground", #690
    "digiplay/AM-mix1",
    "Yntec/Analog",
    "digiplay/MeinaPastel_v1",
    "Yntec/Tea", #687
    "digiplay/AingDiffusion7.5",
    "Yntec/StableDiffusion768", #686
    "digiplay/perfectlevel10", #685
    "Yntec/IdleFancy",
    "digiplay/Shadir_Diffusion_AR_v2.1_fp16_test1",
    "Yntec/NyankoMotsiX",
    "digiplay/GhostMixV1.2VAE",
    "Yntec/CuteFurry",
    "digiplay/LuckyStrikeMix1.05_Lovelylady",
    "Yntec/Looking-Glass",
    "digiplay/AbsoluteReality_v1.0_diffusers",
    "Yntec/epiCCartoon",
    "digiplay/quincemix_v1",
    "Yntec/DaintyMix",
    "digiplay/fantasticmix_v7",
    "Yntec/DucHaiten-AnyUnreal",
    "digiplay/fantexi_v0.9",
    "Yntec/Genuine",
    "digiplay/OrangeChillMix_v7fix",
    "Yntec/GoFish",
    "digiplay/bluePencilRealistic_v05",
    "Yntec/nuipenimix",
    "digiplay/A80S_v1.0",
    "Yntec/iffyMix",
    "digiplay/lutDiffusion_v09Beta",
    "Yntec/EmeraldCity",
    "digiplay/CleanLinearMix",
    "Yntec/animeSIXTYNINE",
    "digiplay/PolyMorphMix",
    "Yntec/AsianMix",
    "digiplay/polla_mix_2.3D",
    "Yntec/ResidentCNZCartoon3D",
    "digiplay/AbsoluteReality_v1.8.1",
    "Yntec/Memento",
    "digiplay/RealCartoon3D_v6",
    "Yntec/RealLife",
    "digiplay/majicMIX_realistic_v6",
    "Yntec/Vintedois",
    "digiplay/SXZ_Luma_v0.98VAE",
    "Yntec/Based64",
    "digiplay/NextGenMix_R2.8VAE",
    "Yntec/SQUEE",
    "digiplay/HIJKLMix_v2",
    "Yntec/Aurora",
    "digiplay/BeenReal_diffusers",
    "Yntec/Paragon",
    "digiplay/OnlyReal-Black-Mix",
    "Yntec/Infinite80s",
    "digiplay/AI-infinity-V1-fp16",
    "Yntec/InfiniteLiberty",
    "digiplay/XXMix_9realistic_v1",
    "Yntec/aBagOfChips",
    "digiplay/Dolka_Rusalka_v0.5.1",
    "Yntec/IsThisArt",
    "digiplay/YutaMix_realistic_v11",
    "Yntec/Jackpot",
    "digiplay/XRYCJ_RealisticModel",
    "Yntec/C-.-_-.-Aravaggio",
    "digiplay/RunDiffusionFX2.5D_v1_diffusers",
    "Yntec/Stuff",
    "digiplay/NightmareShaper_v2DarkageLobotomy",
    "Yntec/LiberteRedmond",
    "digiplay/nk15_diffusers", #230
    "Yntec/Emoticons",
    "digiplay/2K", #216
    "Yntec/BabeBae",
    "digiplay/2-KWI", #213
    "Yntec/SinkOrSwim",
    "digiplay/majicMIXfantasy_v1",
    "Yntec/Nostalgic",
    "digiplay/yiSMix2.8D_v1",
    "Yntec/mixRealisticFantasy",
    "digiplay/hellopure_v2.23",
    "Yntec/Astro_-_-Gemu",
    "digiplay/m3u", #263
    "Yntec/StorybookRedmond",
    "digiplay/ZHMix-Dramatic-v2.0",
    "digiplay/fishmix_other_v1",
    "Yntec/Cheesecake",
    "digiplay/Gap_2.6",
    "digiplay/ZemiHR_v2_diffusers",
    "Yntec/GimmeDatDing",
    "digiplay/ya3p_VAE", #258
    "digiplay/counterfeitV2525d_tweak",
    "Yntec/Gacha",
    "digiplay/ShadowGost_v1",
    "digiplay/LemonTea2.5D",
    "Yntec/GenerateMe",
    "digiplay/xxgSl526_v1",
    "digiplay/incursiosMemeDiffusion_v1.6",
    "Yntec/incha_re_zoro",
    "digiplay/YabaLMixTrue25D_V1.0",
    "digiplay/Perfect_Gap_Blend_v1",
    "Yntec/GodMode",
    "digiplay/LEAU",
    "digiplay/EdisonNilMix_v1", # Added 7.10 Updated 12.5
    "Yntec/FantassifiedIcons",
    "digiplay/asyncsMIX_v5",
    "digiplay/insaneRealistic_v1",
    "Yntec/IncredibleWorld2",
    "digiplay/CoharuMix_real",
    "digiplay/Photon_v1",
    "Yntec/IncredibleWorld",
    "digiplay/WolfSystems_v1",
    "digiplay/MGM",
    "Yntec/TheDarkNight",
    "digiplay/Koji_v2.1_diffusers",
    "Yntec/Cryptids",
    "digiplay/ARRealVX1.1",
    "Yntec/Tantrum",
    "digiplay/MengX_Mix_Real_v3",
    "Yntec/CutesyAnime",
    "Yntec/HellSKitchen",
    "Yntec/Kitsch-In-Sync",
    "Yntec/La-dee-dah-.-_",
    "Yntec/HELLmix",
    "Yntec/AnalogMadness4",
    "Yntec/Wonderland",
    "Yntec/Atlas",
    "Yntec/KomowataHaruka",
    "Yntec/FotoPhoto",
    "Yntec/Ambrosia",
    "Yntec/Reliberate",
    "Yntec/BaronMix",
    "Yntec/ChilloutMix",
    "Yntec/Shirayuki",
    "Yntec/foto-assisted-diffusion",
    "Yntec/elldrethSDreamMix",
    "Yntec/mistoonEmerald2",
    "Yntec/AnythingRemix",
    "Yntec/AnalogMadness",
    "Yntec/IronCatFateToons",
    "Yntec/CultClassic",       #1K
    "Yntec/samaritan3dCartoon2MVAE", #1K
    "Yntec/Crystalwave", #1k
    "Yntec/Synthwave",
    "Yntec/OG",                        #1k
    "Yntec/Crayon",                    #1K
    "Yntec/LuckyStrike",               #1K
    "Yntec/Deliberate",                #1K
    "Yntec/DeliberateRealisticWoop",   #1K
    "Yntec/EstheticRetroAnime",        #1K
    "Yntec/DucHaiten-GoldenLife", 
    "Yntec/3DCuteWave",
    "Yntec/GoldenEra", #1K
    "Yntec/ClassicEra", #1K
    "Yntec/GoodLife", #1K
    "Yntec/Hassanim", #1K
    "Yntec/DeliberateRemix",   #1K
    "Yntec/HassanBlend12",      #1K
    "Yntec/HassanBlend1512VAE", #1K
    "Yntec/MangledMerge3_768", #1K
    "Yntec/OpenLexica",        #1K
    "Yntec/MapleSyrup",        #1K
    "Yntec/iComixRemix",       #1K
    "Yntec/SamaritanDoesArt",  #1K
    "Yntec/CinemaEros", #1K
    "Yntec/CartoonStyleClassic", #1K
    "Yntec/GalenaVAE",         #1K
    "Yntec/a-ZovyaRemix",      #1K
    "Yntec/a-ZoviaRPGArtistV2VAE", #2K
    "Yntec/MemeDiffusion", #2K
    "Yntec/Abased", #2k
    "Yntec/SCMix", #2k
    "Yntec/Hassaku", #2k
    "Yntec/m0nst3rfy3",    #2k
    "Yntec/PotaytoPotahto",    #2K
    "Yntec/3DCute",               #2K
    "Yntec/SuperCuteRemix",       #2K
    "Yntec/Trending", #2K
    "Yntec/a-ZovyaRPGV3VAE",   #3K
    "Yntec/StolenDreams", #3k
    "Yntec/LeyLines", #3k
    "Yntec/SillySymphonies", #3K
    "Yntec/MeinaAlter",                #3K
    "Yntec/WoopWoopAnime",             #3K
    "Yntec/DreamWorld",                #3K
    "Yntec/MGM",                       #3K
    "Yntec/3DKX/",                 #3K
    "Yntec/3DKXv11",              #3K
    "Yntec/Cute",                 #3K
    "Yntec/DreamFulV2",           #3K
    "Yntec/DucHaitenDarkside4",   #3K
    "Yntec/Citrus",               #3K
    "Yntec/Classic",              #3K
    "Yntec/BasilRemix", #3K
    "Yntec/Yuzu",                      #4K
    "Yntec/Protogen",                  #4K
    "Yntec/BeautyFool",                #4K
    "Yntec/CyberRealistic",            #4K
    "Yntec/Lyriel",               #4K
    "Yntec/3DRendering",          #4K
    "Yntec/aMovieTrend", #2K
    "Yntec/Dreamscape", #2K
    "Yntec/elldrethSVividMix",    #2K
    "Yntec/elldrethSLucidMix",    #2K
    "Yntec/CitrineDreamMix",   #2K
    "Yntec/elldrethsImagination",            #2K
    "Yntec/ReVAnimated768", #2K
    "Yntec/OpenNijiRemix",        #2K
    "Yntec/DreamShaperRemix",  #2K
    "Yntec/RadiantCinemagic",  #2K
    "Yntec/RadiantVibes",      #1K
    "Yntec/NeverEndingDream768", #2K
    "Yntec/vividicAnime", #2K
    "Yntec/WoopWoopRemix",     #2K
    "Yntec/ArcticFowl",        #2K
    "Yntec/CrystalClearRemix", #5k
    "Yntec/CrystalClear",   #3k
    "Yntec/Reanimate", #5k
    "Yntec/Deliberate2",     #5k
    "Yntec/526",     #5k
    "Yntec/526Mix",     #5k
    "Yntec/Dreamful3",            #5K
    "Yntec/theAllysMixIIIRevolutions", #6k
    "Yntec/UberRealisticLegacy",     #6k
    "Yntec/BrandiMilne",          #6K
    "Yntec/dosmixVAE",            #3K
    "Yntec/aPhotographicTrend", #3K
    "Yntec/BeenYou",                         #3K
    "Yntec/level4",            #3K
    "Yntec/dreamlike-photoreal-remix", #3K
    "Yntec/lamettaRemix", #3K
    "Yntec/lametta",      #2K
    "Yntec/AgarthaChadstyle",       #7k
    "Yntec/DucHaitenLofi", #7k
    "Yntec/DreamWorks",                #7K
    "Yntec/AbsoluteRemix",        #7K
    "Yntec/mistoonAnime2",        #7K
    "Yntec/DucHaiten-FANCYxFANCY",#7K
    "Yntec/LAMEanime",            #8K
    "Yntec/3Danimation",          #4K
    "Yntec/DucHaitenNiji",        #4K
    "Yntec/Darkside",             #4K
    "Yntec/animeTEN",          #4K
    "Yntec/Dreamscapes_n_Dragonfire_v2", #4K
    "Yntec/Cetus",             #4K
    "Yntec/DeliShaper",        #4K
    "Yntec/epiCVision",        #4K
    "Yntec/Dreamlike",         #3K
    "Yntec/AnythingV4-768", #9k
    "Yntec/makeitdoubleplz",   #10k
    "Yntec/ChiliConCarne",     #11k
    "Yntec/Dreamshaper8",         #12K
    "Yntec/pineappleAnimeMix", #13k
    "Yntec/Oiran",                #6K
    "Yntec/RealCartoon3D",        #6K
    "Yntec/animeTWO",                        #6K
    "Yntec/lamettaNightly", #6K   
    "Yntec/REV",               #6K
    "Yntec/NaughtyChildren",   #6K
    "Yntec/humu",              #6K
    "Yntec/Thriller",             #13K
    "Yntec/Splash",            #7K
    "Yntec/OpenGenDiffusers",  #7K
    "Yntec/DreamLikeRemix",    #7K
    "Yntec/epiCRealismVAE",       #8K
    "Yntec/LehinaModel",                     #8K
    "Yntec/realistic-vision-v12", #14K
    "Yntec/animeSEXTILLION/",  #15K
    "Yntec/AbsoluteReality",      #15K
    "Yntec/CetusRemix",        #16K
    "Yntec/AnythingV3-768",            #18K
    "Yntec/edgeOfRealism",     #25K
    "Yntec/fennPhoto", #27k
    "Yntec/aMovieX/", #28K
    "Yntec/photoMovieXFinal", #31K
    "Yntec/nuipenimix2",          #34K
    "Yntec/epiCPhotoGasm",        #40K
    "Yntec/YiffyMix", #44K
    "Yntec/HitenDiffusion",    #2K
    "Yntec/GameAssetsDigitalUnitsCreationKit",
    "Yntec/QToriReloaded",
    "Yntec/Toonify2",
    "Yntec/LunarLuma",
    "Yntec/Lunar",
    "Yntec/Chik2",
    "Yntec/photoMovieRealistic",
    "Yntec/DucHaiten-StyleLikeMeVAE",
    "Yntec/InsaneRealisticCVAE",
    "Yntec/Noosphere_v3_CVAE",
    "Yntec/RealRainbows",
    "Yntec/InsaneM3U",
    "Yntec/ChildrenStoriesAnime",
    "Yntec/theallysMixIV-verisimilar",
    "Yntec/DucHaitenAnime768",
    "Yntec/RainbowClassicAnime",
    "Yntec/DucHaitenClassicAnime768",
    "Yntec/Luma",
    "Yntec/WesternAnimation",
    "Yntec/NeverExisted",
    "Yntec/Rainbowsphere",
    "Yntec/Ninja-Diffusers",
    "Yntec/GOLDFish",
    "Yntec/DreamAnything",
    "Yntec/Dreamsphere",
    "Yntec/Photosphere",
    "Yntec/yabalMixTrue25D_v2_VAE",
    "dreamlike-art/dreamlike-anime-1.0",
    "Yntec/RainbowDreams",
    "Yntec/rainbowpatch",
    "Yntec/DucHaiten-Retro-Diffusers",
    "Yntec/ElldrethsRetroMix_Diffusers",
    "Yntec/sexyToons",
    "Yntec/photoMovieX/",
    "dreamlike-art/dreamlike-photoreal-2.0",
    "dreamlike-art/dreamlike-diffusion-1.0",
    "Yntec/CuteYuki2",
    "Yntec/KIDSILLUSTRATIONS",
    "Yntec/COOLKIDSV2",
    "Yntec/Pavo-Mix-Diffusers",
    "Yntec/RPG_Remix",
    "Yntec/OrangeRemix",
    "Yntec/PeachMix3",
    "Yntec/DucHaitenAIart-beta",
    "Yntec/samdoesartsUlt",
    "Yntec/NovelAI",
    "Yntec/NovelAIRemix",
    "Yntec/Hiten",
    "digiplay/fantasticmix2.5D_v4.0",
    "digiplay/majicMIX_realistic_v1",
    "digiplay/RunDiffusionFXPhotorealistic_v1",
    "digiplay/2K-VAE",
    "digiplay/DucHaiten-Real3D-NSFW-V1",
    "digiplay/kencanmix_v1.5",
    "digiplay/ZHMix-Dramatic-v3.0",
    "digiplay/Gap",
    "digiplay/ya3_VAE",
    "digiplay/asyncsMIX_v2",
    "digiplay/fantasticmix_v65_test",
    "digiplay/AingDiffusion8",
    "digiplay/AingDiffusion9",
    "digiplay/AingDiffusion8.5",
    "digiplay/AingDiffusion6",
    "digiplay/AingDiffusion8.17",
    "digiplay/AingDiffusion9.2",
    "digiplay/MeinaMix_v11",
    "AIARTCHAN/AbyssHellHero",
    "digiplay/MeinaMix_v7",
    "digiplay/futaall_v8_VAE_diffusers",
    "digiplay/Sudachi_diffusers",
    "digiplay/CleanLinearMix_nsfw",
    "digiplay/majicMIX_realistic_v4",
    "digiplay/VersaMix_base_diffusers",
    "digiplay/OldFish_fix1.1.997_diffusers",
    "digiplay/VoidnoiseCore_R0829",
    "digiplay/OldFish_v1.1",
    "digiplay/wantan25D_prototype",
    "digiplay/PotoPhotoRealism_v1",
    "digiplay/LunarDiffusion_v1.27",
    "digiplay/OLDFish_2348_diffusers",
    "digiplay/OldFish_v1.1_diffusers_recover",
    "digiplay/OldFish_v1.1mix_hello",
    "digiplay/OldFish_v1.1_personal_HDmix",
    "digiplay/FishMix_v1",
    "DucHaiten/DucHaitenDreamWorld",
    "digiplay/LemonteaMixPainterly2_v1",
    "Hius/DreamFul-V2",
    "lambdalabs/sd-naruto-diffusers", #201
    "digiplay/SweetMuse_diffusers",
    "stablediffusionapi/icomix-2",
    "digiplay/Realisian_v1",
    "digiplay/RMHF_2.5D_v2",
    "digiplay/FishMix_v1.1",
    "digiplay/Remedy",
    "Hemlok/QuinceMix",
    "digiplay/K-main",
    "digiplay/LusterMix_v1.5_safetensors", #256
    "digiplay/perfectLewdFantasy_v1.01",
    "digiplay/Opiate_v2",
    "digiplay/PhotoSomnia_vFinal",
    "stablediffusionapi/all-526-animated",
    "digiplay/polla_mix_2.5D",
    "AstraliteHeart/pony-diffusion",
    "stablediffusionapi/chilloutmixsf",
    "Masagin/Deliberate", #235
    "DucHaiten/DucHaitenSuperCute",
    "stablediffusionapi/all-526",
    "theintuitiveye/HARDblend",
    "stablediffusionapi/cyberrealistic",
    "stablediffusionapi/cusp-of-serenity",
    "SG161222/Realistic_Vision_V1.4",
    "digiplay/paulEberSRealismMix_v1",
    "Ojimi/anime-kawai-diffusion",
    "hassanblend/hassanblend1.4",
    "digiplay/zodiac_eclipse_DAY1",
    "claudfuen/photorealistic-fuen-v1",
    "stablediffusionapi/chillout-app-factory",
    "DucHaiten/DucHaitenJourney",
    "robotjung/SemiRealMix",
    "Joeythemonster/anything-midjourney-v-4-1",
    "prompthero/midjourney-v4-diffusion",
    "prompthero/openjourney-v4",
    "x67/shortjourney",
    "FredZhang7/paint-journey-v2",
    "digiplay/PersonaStyleCheckpoint",
    "darkstorm2150/Protogen_Infinity_Official_Release",
    "PeggyWang/openjourney-v2",
    "darkstorm2150/Protogen_x3.4_Official_Release",
    "stablediffusionapi/deliberateappfactory", #236
    "digiplay/CrossoverMix_v2",
    "stablediffusionapi/spybg",
    "stablediffusionapi/dreamshaper-v6", #239
    "stablediffusionapi/the-ally",
    "darkstorm2150/Protogen_x5.8_Official_Release",
    "coreco/seek.art_MEGA",
    "digiplay/BlankCanvas_v1", #07.11
    "digiplay/OnlyAnime_v2.3",
    "Korakoe/OpenNiji",
    "digiplay/Pika_v2",
    "digiplay/RealCartoon3D_F16full_v3.1", #254
    "digiplay/realidefmix_3.5VAE",
    "digiplay/realmixUnrealjourney_v1",
    "digiplay/SyncMix_v1.5",
    "stablediffusionapi/chilledremixsazyou-r", #195
    "digiplay/TWingshadow_v1.2",
    "digiplay/V3_by_Hans_Asian",
    "digiplay/whatamix_v1",
   "stabilityai/stable-diffusion-xl-base-1.0",
]

if models:
    models_list = models.split(",")
    MODELS.extend(models_list)
