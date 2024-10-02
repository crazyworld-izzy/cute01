import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from BrandrdXMusic import app

LOGGER = getLogger(__name__)

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        self.data[chat_id] = {}

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(500, 500)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname):
    background = Image.open("BrandrdXMusic/assets/wel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp, brightness_factor=brightness_factor)
    pfp = pfp.resize((892, 800))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('BrandrdXMusic/assets/font.ttf', size=98)
    welcome_font = ImageFont.truetype('BrandrdXMusic/assets/font.ttf', size=45)
    
    # Draw user's name with shining red fill and dark saffron border
    draw.text((1820, 1080), f': {user}', fill=(255, 0, 0), font=font)
    draw.text((1820, 1080), f': {user}', fill=None, font=font, stroke_fill=(255, 153, 51), stroke_width=6)
    
    # Draw user's id with shining blue fill and white border
    draw.text((1620, 1280), f': {id}', fill=(0, 0, 139))
    draw.text((1620, 1280), f': {id}', fill=None, font=font, stroke_fill=(0, 225, 255), stroke_width=6)
    
    # Draw user's username with white fill and green border
    draw.text((2000, 1510), f': {uname}', fill=(255, 255, 255), font=font)
    draw.text((2000, 1510), f': {uname}', fill=None, font=font, stroke_fill=(0, 128, 0), stroke_width=6)
    
    pfp_position = (265, 360)
    background.paste(pfp, pfp_position, pfp)

    # Calculate circular outline coordinates
    center_x = pfp_position[0] + pfp.width / 2
    center_y = pfp_position[1] + pfp.height / 2
    radius = min(pfp.width, pfp.height) / 2

    # Draw circular outlines
    draw.ellipse([(center_x - radius - 10, center_y - radius - 10),
                  (center_x + radius + 10, center_y + radius + 10)],
                 outline=(255, 153, 51), width=25)  # Saffron border

    draw.ellipse([(center_x - radius - 20, center_y - radius - 20),
                  (center_x + radius + 20, center_y + radius + 20)],
                 outline=(255, 255, 255), width=25)  # White border

    draw.ellipse([(center_x - radius - 30, center_y - radius - 30),
                  (center_x + radius + 30, center_y + radius + 30)],
                 outline=(0, 128, 0), width=25)  # Green border
    
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one(chat_id)
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "BrandrdXMusic/assets/wel2.png"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        try:
            welcomeimg = welcomepic(
                pic, user.first_name, member.chat.title, user.id, user.username
            )
            button_text = "🍷 𝐍𖽞𖽮 𝐌𖽞𖽧𖽜𖽞𖽷 😻"
            add_button_text = "🍷 𝐊𖽹𖾓𖽡𖽖𖽳 𝐌𖽞 😻"
            deep_link = f"tg://openmessage?user_id={user.id}"
            add_link = f"https://t.me/{app.username}?startgroup=true"
            temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
                member.chat.id,
                photo=welcomeimg,
                caption=f"""
**☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★**
 
**🦋‌𝆺𝅥𓆩〭〬𝐂𖽪֟፝‌𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 ‌𝆺𝅥😻⤍🖤**

**⊰●⊱┈─★ 𝑊𝑒𝑙𝑐𝑜𝑚𝑒 ★─┈⊰●⊱**

**➽───────────────────❥**   

**🍷 𝐍𖽖𖽧𖽞 😻** {user.mention}

**🍷 𝐈𖽴 😻** {user.id}

**🍷 𝐔𖾗𖽞𖽷𖽡𖽖𖽧𖽞 😻** @{user.username}

**🍷 𝐌𖽞𖽧𖽜𖽞𖽷𖾗 😻** {count}

**➽───────────────────❥**   

**☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★**
""",
 reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(button_text, url=deep_link)],
                    [InlineKeyboardButton(text=add_button_text, url=add_link)],
                ])
            )
    except Exception as e:
        LOGGER.error(e)

\
