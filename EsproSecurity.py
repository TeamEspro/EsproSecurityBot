from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
import logging

import pyrogram
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.INFO)

# -------------------------------------------------------------------------------------

BOT_USERNAME = os.environ.get("BOT_USERNAME","EsproSecurityBot")

OWNER_ID = "7186439442"
# -------------------------------------------------------------------------------------

API_ID = "20563951" # 
API_HASH = "91a46c36f5bc745fc45ce4de8b51292d"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------


start_txt = """<b>нєу</b> 🥀\n\n๏ ᴛʜɪs ɪs \n\n➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ᴄᴏᴘʏʀɪɢʜᴛ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n<b><u>Sᴜᴘᴘᴏʀᴛᴇᴅ Pʟᴀᴛғᴏʀᴍs :</b></u> .\n──────────────────\n<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.</b> """

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("Aᴅᴅ Mᴇ Bᴀʙʏ", url=f"https://t.me/EsproSecurityBot?startgroup=true")
        ],
        [
            InlineKeyboardButton("🍁Support🥀", url="https://t.me/EsproSupport"),
            InlineKeyboardButton("🍁Update🥀", url="https://t.me/EsproUpdate"),    
        ],
        [
          InlineKeyboardButton("❄️Owner❄️", user_id=OWNER_ID)
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/9bc30e079df53c38aae6d.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("❄️Owner❄️", user_id=OWNER_ID),
            InlineKeyboardButton("🍁Update🥀", url="https://t.me/EsproUpdate"),    
        ]
        ]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("dil_back"))
async def dil_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"



@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)


    
# -------------------------------------------------------------------------------------



FORBIDDEN_KEYWORDS = ["porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
      #  user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
        
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
def delete_long_messages(_, m):
    return len(m.text.split()) > 10

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"Hey {user_mention}, please keep your messages short!")
    

# -----------------------------------------------------------------------------------


    
@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message(client, message: Message):
    pass 
# -------------------------------

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"@{message.from_user.username} ᴍᴀᴀ ᴍᴀᴛ ᴄʜᴜᴅᴀ ᴘᴅғ ʙʜᴇᴊ ᴋᴇ,\n ʙʜᴏsᴀᴅɪᴋᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀɢʏᴇɢᴀ \n\n ᴅᴇʟᴇᴛᴇ ᴋᴀʀ ᴅɪʏᴀ ᴍᴀᴅᴀʀᴄʜᴏᴅ.\n\n ᴀʙ @WereWolfDemon ʙʜᴀɪ ᴋᴇ ᴅᴍ ᴍᴇ ᴀᴘɴɪ ᴍᴜᴍᴍʏ ᴋᴏ ʙʜᴇᴊ ᴅᴇ 🍌🍌🍌."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

# -----------------------------------------------------------------------------------

print(f"""╔═════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪║┏━━━━━━➣║┣⪼ ᴏᴡɴᴇʀ :- 𝐈 𝐀𝐦 𝐘𝐨𝐮𝐫 𝐃𝐚𝐝 ║┣⪼ ᴘᴀʀᴛ ᴏғ :- https://t.me/EsproSupport║┗━━━━━━➣║╔═════ஜ۩۞۩ஜ════╗║अनंत अखंड अमर अविनाशी║कष्ट हरण है║शंभु कैलाशी║╚═════ஜ۩۞۩ஜ════╝╚═════════════════❍⊱❁ """)
app.run()
