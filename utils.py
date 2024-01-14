from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from models import MODELS

HELP = """
● Send a Prompt , Reply /generate to the Prompt to start Image Generation

◆〓◆⬭❖ 𝐖𝐃 𝐙𝐎𝐍𝐄 ❖ ™⬭◆〓◆
"""

START_STRING = """ **Hello {}, I'm Text to Image bot**
Capable of running all Large image Generation Models from huggingface.

`Join My Updates Channel for Getting more familiar with me`

"""

ABOUT = """
● **AUTHOR :** [Opleech](https://t.me/Opleech) 
● **LIBRARY :** `Pyrogram` 
● **LANGUAGE :** `Python 3.10` 
● **SOURCE :** [SudoR2spr](https://github.com/SudoR2spr) 
"""

GITHUB_LINK = "https://github.com/SudoR2spr"

CHANNEL_BUTTON = InlineKeyboardMarkup(
    [[InlineKeyboardButton("✜ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✜", url="https://t.me/Opleech")]]
)

GITHUB_BUTTON = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🦋 𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 🦋", url=GITHUB_LINK)]]
)

START_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("✜ 𝐀𝐛𝐨𝐮𝐭 ✜", callback_data="cbabout"),
            InlineKeyboardButton("✜ 𝐇𝐞𝐥𝐩 ✜", callback_data="cbhelp"),
        ],
        [InlineKeyboardButton("✜ 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 ✜", callback_data="cbsettings")],
        [
            InlineKeyboardButton("✜ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✜", url="https://t.me/Opleech"),
        ],
    ]
)
CLOSE_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("◁◎𝐁𝐚𝐜𝐤", callback_data="cbclose"),
        ]
    ]
)


BACK = [InlineKeyboardButton("◁◎𝐁𝐚𝐜𝐤", callback_data="back")]


SETTINGS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝐂𝐡𝐨𝐨𝐬𝐞 𝐌𝐨𝐝𝐞𝐥", callback_data="choose_model"),
            InlineKeyboardButton("𝐂𝐡𝐚𝐧𝐠𝐞 𝐒𝐭𝐞𝐩𝐬", callback_data="change_steps"),
        ],
        [
            InlineKeyboardButton("𝐂𝐡𝐚𝐧𝐠𝐞 𝐒𝐞𝐞𝐝", callback_data="change_seed"),
            InlineKeyboardButton(
                "𝐂𝐡𝐚𝐧𝐠𝐞 𝐢𝐦𝐚𝐠𝐞 𝐂𝐨𝐮𝐧𝐭", callback_data="change_image_count"
            ),
        ],
        [InlineKeyboardButton("𝐒𝐚𝐯𝐞 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬", callback_data="save_settings")],
    ]
)

MODELS_BUTTON = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(model, callback_data=f"select_model_{index}")]
        for index, model in enumerate(MODELS)
    ]
    + [[InlineKeyboardButton("◁◎𝐁𝐚𝐜𝐤", callback_data="cb_back_settings")]]
)


STEPS_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("-", callback_data="-steps"),
            InlineKeyboardButton("+", callback_data="+steps"),
        ],
        [InlineKeyboardButton("◁◎𝐁𝐚𝐜𝐤", callback_data="cb_back_settings")],
    ]
)
IMAGE_COUNT_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("-", callback_data="-image"),
            InlineKeyboardButton("+", callback_data="+image"),
        ],
        [InlineKeyboardButton("◁◎𝐁𝐚𝐜𝐤", callback_data="cb_back_settings")],
    ]
)
