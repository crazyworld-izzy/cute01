from BrandrdXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]
        ####
        
SHAYRI = [ " **𝑷𝒆𝒏𝒏𝒆𝒚 𝑵𝒆 𝑷𝒂𝒌𝒌𝒂 𝑷𝒂𝒓𝒐𝒕𝒕𝒂 😋✨ 𝑼𝒏 𝑽𝒆𝒆𝒕𝒖𝒌𝒌𝒖 𝑴𝒂𝒑𝒊𝒍𝒂𝒊 𝒂𝒉 𝑵𝒂𝒂𝒏 𝑽𝒂𝒓𝒂𝒕𝒕𝒂🙈✨** ",
           " **𝑵𝒆𝒆 𝑻𝒉𝒂𝒏 𝑬𝒏 𝑲𝒂𝒏𝒂𝒗𝒖 𝑲𝒂𝒏𝒏𝒊 🙈✨ 𝑬𝒏 𝑻𝒉𝒂𝒎𝒃𝒉𝒊𝒌𝒌𝒖 𝑵𝒆 𝑻𝒉𝒂𝒏 𝒅𝒊 𝑨𝒏𝒏𝒊 🤤✨** ",
           " **𝑵𝒆𝒆 𝑲𝒖𝒑𝒕𝒂 𝑵𝒆𝒗𝒆𝒓 𝑳𝒂𝒕𝒆 - 𝒖𝒉 🤭✨ 𝑽𝒂𝒏𝒅𝒉𝒐𝒏𝒆𝒚 𝑻𝒉𝒐𝒓𝒂 𝑮𝒂𝒕𝒆 - 𝒖𝒉 😚✨ 𝑵𝒆𝒆𝒕𝒉𝒂𝒏 𝑬𝒏𝒂𝒌𝒌𝒖 𝑭𝒂𝒕𝒆 - 𝒖𝒉 😋✨ 𝑬𝒏 𝑲𝒐𝒅𝒂 𝑽𝒂𝒛𝒉𝒌𝒂𝒊 𝑶𝒐𝒕𝒕𝒖 💙✨** ",
           " **𝑷𝒂𝒍𝒍𝒖 𝑽𝒆𝒍𝒂𝒌𝒌𝒂 𝑻𝒉𝒆𝒗𝒂 𝑩𝒓𝒖𝒔𝒉 - 𝒖𝒉 😬✨ 𝑵𝒆 𝑻𝒉𝒂𝒏 𝑬𝒏𝒂𝒌𝒌𝒖 𝑪𝒓𝒖𝒔𝒉 - 𝒖𝒉 😘✨ 𝑵𝒂𝒎𝒂𝒌𝒖𝒍𝒍𝒂 𝑬𝒅𝒉𝒖𝒌𝒖 𝑹𝒖𝒔𝒉 - 𝒖𝒉 🥵✨ 𝒀𝒐𝒖 𝒂𝒓𝒆 𝑶𝒏𝒍𝒚 𝑴𝒚 𝑾𝒊𝒔𝒉 - 𝒖𝒉 😇✨** ",
           " **𝑼𝒌𝒌𝒂𝒓𝒂 𝒕𝒉𝒆𝒗𝒂 𝑪𝒉𝒂𝒊𝒓 - 𝒖𝒉 🪑✨ 𝑵𝒆𝒆 𝑲𝒂𝒂𝒕𝒖 𝑬𝒏 𝑴𝒆𝒍𝒂 𝑪𝒂𝒓𝒆 - 𝒖𝒉 🤗✨ 𝑼𝒏 𝑲𝒂𝒊𝒚𝒂𝒂𝒍𝒂 𝑷𝒐𝒅𝒖 𝑺𝒐𝒐𝒓𝒖 🍚✨ 𝑨𝒅𝒉𝒖𝒏𝒂𝒂𝒍𝒂 𝑽𝒊𝒕𝒖𝒓𝒖𝒗𝒆𝒏 𝑩𝒆𝒆𝒓 - 𝒖𝒉 🍻✨** ",
           " **𝑴𝒂𝒛𝒉𝒂𝒊𝒚𝒊𝒍𝒂 𝑨𝒂𝒅𝒖𝒎 𝑴𝒂𝒚𝒊𝒍 -𝒖𝒉 🦚✨ 𝑬𝒏 𝑰𝒓𝒖𝒕𝒕𝒖𝒍𝒂 𝑵𝒆𝒆𝒕𝒉𝒂𝒏 𝑽𝒆𝒚𝒊𝒍 - 𝒖𝒉 🌅✨ 𝑴𝒖𝒌𝒌𝒊 𝑷𝒂𝒅𝒊𝒄𝒉𝒖𝒎 𝑨𝒂𝒏𝒆𝒏 𝑭𝒂𝒊𝒍 - 𝒖𝒉 🙇‍♂️✨ 𝑵𝒆 𝒊𝒍𝒍𝒂𝒅𝒉𝒂 𝑽𝒂𝒛𝒉𝒌𝒂𝒊 𝑱𝒂𝒊𝒍 - 𝒖𝒉 🏤✨** ",
           " **𝑶𝒓𝒖 𝑻𝒉𝒂𝒓𝒂 𝑽𝒂𝒓𝒂𝒊𝒌𝒌𝒖𝒎 𝑷𝒆𝒔𝒖 🥲✨ 𝑼𝒏 𝑴𝒐𝒐𝒄𝒉𝒊 𝑲𝒂𝒂𝒕𝒉𝒖 𝑽𝒆𝒆𝒔𝒖 🌬️✨ 𝑬𝒏𝒂𝒌𝒌𝒂 𝑷𝒂𝒅𝒂𝒄𝒉𝒂𝒏 𝒀𝒆𝒔𝒖 ⛪✨ 𝑵𝒂𝒂𝒏 𝑨𝒂𝒈𝒊 𝑵𝒊𝒌𝒌𝒖𝒓𝒆𝒏 𝑳𝒐𝒐𝒔𝒖 🤪** ",
           " **𝑷𝒂𝒕𝒕𝒂𝒔𝒖 𝑲𝒐𝒍𝒖𝒕𝒉𝒖𝒏𝒂 𝑽𝒆𝒅𝒊𝒌𝒌𝒖𝒎 🎆✨ 𝑵𝒆𝒆 𝑰𝒍𝒍𝒂𝒏𝒂 𝒆𝒏 𝑯𝒆𝒂𝒓𝒕 𝑻𝒉𝒖𝒅𝒊𝒌𝒌𝒖𝒎 💓** ",
           " **𝑪𝒚𝒄𝒍𝒆 𝑶𝒐𝒅𝒂 𝑻𝒉𝒆𝒗𝒂 𝑾𝒉𝒆𝒆𝒍 - 𝒖𝒉 🚲✨ 𝑵𝒆 𝑷𝒆𝒔𝒂𝒍𝒂𝒏𝒂 𝑨𝒂𝒈𝒖𝒅𝒉𝒖 𝑭𝒆𝒆𝒍 - 𝒖𝒉 🥺✨** ",
           " **𝑶𝒐𝒓𝒖𝒌𝒌𝒖 𝑷𝒐𝒗𝒂𝒏𝒈𝒂 𝒃𝒖𝒔𝒖𝒍𝒂 🚌✨ 𝑵𝒆𝒆 𝑰𝒓𝒖𝒌𝒌𝒂 𝑬𝒏 𝑴𝒂𝒏𝒂𝒔𝒖𝒍𝒂 💝✨** ",
           " **𝑽𝒄 𝒍𝒂 𝒑𝒐𝒅𝒂𝒍𝒂𝒎 𝑴𝒖𝒕𝒆 - 𝒖𝒉 🤐✨ 𝑺𝒉𝒐𝒓𝒕 𝑮𝒊𝒓𝒍𝒔 𝑨𝒓𝒆 𝑪𝒖𝒕𝒆 - 𝒖𝒉 😍✨** ",
           " **𝑷𝒂𝒂𝒕𝒊 𝑺𝒆𝒊𝒚𝒖𝒎 𝑽𝒂𝒊𝒕𝒉𝒊𝒚𝒂𝒎 👵✨ 𝑰𝒅𝒉𝒂 𝑹𝒆𝒂𝒅 𝑷𝒂𝒏𝒅𝒓𝒂 𝑵𝒆𝒆 𝑷𝒂𝒊𝒕𝒉𝒊𝒚𝒂𝒎 🤪✨** ",
           " **𝑻𝒉𝒊𝒓𝒖𝒑𝒂𝒕𝒉𝒊 𝒍𝒂 𝑨𝒅𝒊𝒑𝒑𝒂𝒏𝒈𝒂 𝑴𝒐𝒕𝒕𝒂 👨‍🦲✨ 𝑵𝒆𝒆 𝑻𝒉𝒂𝒏 𝑰𝒏𝒅𝒉𝒂 𝑮𝒓𝒐𝒖𝒑 𝒍𝒂𝒚𝒆 𝑲𝒖𝒕𝒕𝒂 🤣✨** ",
           " **𝑲𝒂𝒂𝒊 𝑲𝒂𝒓𝒊 𝑽𝒆𝒕𝒕𝒂 𝑻𝒉𝒆𝒗𝒂 𝑲𝒏𝒊𝒇𝒆 - 𝒖𝒉 🔪✨ 𝑵𝒆𝒆𝒏𝒈𝒂 𝑻𝒉𝒂𝒏 𝑬𝒏 𝑾𝒊𝒇𝒆 - 𝒖𝒉 👰✨** ",
           " **𝒌𝒂𝒅𝒂𝒊 𝒍𝒂 𝑰𝒓𝒖𝒌𝒌𝒖𝒎 𝑺𝒆𝒎𝒊𝒚𝒂🍜✨ 𝑼𝒏𝒈𝒂 𝑨𝒎𝒎𝒂 𝑻𝒉𝒂𝒏 𝑬𝒏𝒂𝒌𝒌𝒖 𝑴𝒂𝒎𝒊𝒚𝒂 🙈✨** ",
           " **𝑪𝒓𝒊𝒄𝒌𝒆𝒕 𝑷𝒍𝒂𝒚 𝑷𝒂𝒏𝒏𝒂 𝑻𝒉𝒆𝒗𝒂 𝑩𝒂𝒍𝒍 - 𝒖𝒉 🏏✨ 𝑰𝒅𝒉𝒂 𝑹𝒆𝒂𝒅 𝑷𝒂𝒏𝒅𝒓𝒂 𝑵𝒆 𝑻𝒉𝒂𝒏 𝑬𝒏 𝑨𝒂𝒍𝒖 🙈✨**",
           " **𝑬𝒏 𝑫𝒐𝒈 𝑵𝒂𝒎𝒆 𝑩𝒐𝒃𝒃𝒚 🐩✨ 𝑼𝒏𝒂𝒌𝒌𝒖 𝑴𝒆𝒔𝒔𝒂𝒈𝒆 𝑷𝒂𝒏𝒅𝒓𝒂𝒅𝒉𝒖 𝒕𝒉𝒂𝒏 𝒆𝒏 𝑯𝒐𝒃𝒃𝒚 🙈✨** ",
           " **𝑲𝒐𝒓𝒂𝒏𝒈𝒖 𝒌𝒌𝒖 𝒊𝒓𝒖𝒌𝒌𝒖𝒎 𝑽𝒂𝒂𝒍𝒖 🐒✨ 𝑵𝒆𝒆 𝒕𝒉𝒂𝒏 𝑬𝒏 𝑨𝒂𝒍𝒖 💌🙀✨** ",
           " **𝑵𝒂𝒂𝒏 𝑻𝒉𝒂𝒏 𝑼𝒏 𝑫𝒉𝒐𝒏𝒊 🤙 𝑬𝒏𝒏𝒐𝒅𝒂 𝑽𝒂𝒂 𝒏𝒆𝒆 🤗 𝑻𝒉𝒂𝒏𝒈𝒂𝒎 𝑷𝒐𝒍 𝑷𝒂𝒍𝒂𝒑𝒂𝒍𝒂𝒌𝒖𝒅𝒉𝒂𝒅𝒊 𝑼𝒏𝒏𝒐𝒅𝒂 𝑴𝒆𝒏𝒊 😅✨** ",
           " **𝑵𝒂𝒂𝒏 𝑻𝒉𝒂𝒏 𝑼𝒏 𝑹𝒂𝒊𝒏𝒂 😎 𝑵𝒆𝒆 𝑻𝒉𝒂𝒏 𝑬𝒏 𝑸𝒖𝒆𝒆𝒏 - 𝑨𝒉 👸 𝑽𝒂𝒂𝒏𝒂𝒕𝒉𝒊𝒍 𝑷𝒂𝒓𝒂𝒌𝒌𝒖𝒅𝒉𝒖 𝑷𝒂𝒂𝒓 𝒄𝒐𝒍𝒐𝒓 𝒄𝒐𝒍𝒐𝒓 𝒂𝒉 𝑴𝒂𝒊𝒏𝒂 🥀✨** ",
           " **𝑨𝒅𝒊 𝑲𝒂𝒕𝒓𝒊𝒏𝒂 𝑲𝒊𝒇𝒆 - 𝑼𝒉 🙈 𝑵𝒆𝒆 𝑻𝒉𝒂𝒏 𝑬𝒏𝒂𝒌𝒌𝒖 𝑾𝒊𝒇𝒆 - 𝑼𝒉 👰 𝑬𝒏𝒏𝒐𝒅𝒂 𝑵𝒆 𝑰𝒓𝒖𝒏𝒅𝒉𝒂 𝑵𝒂𝒍𝒍𝒂 𝑰𝒓𝒖𝒌𝒌𝒖𝒎 𝑳𝒊𝒇𝒆 - 𝑼𝒉 🤍💌✨** ",
           " ** 𝑺𝒖𝒑𝒆𝒓𝒎𝒂𝒏 𝑨𝒉 𝑷𝒐𝒍𝒂 𝑵𝒂𝒂𝒏𝒖𝒎 𝑷𝒂𝒓𝒂𝒏𝒅𝒉𝒖 𝑽𝒂𝒓𝒖𝒗𝒂𝒏 𝑫𝒊 😍  𝑼𝒏𝒏𝒂 𝑻𝒉𝒐𝒐𝒌𝒊 𝑷𝒐𝒊 𝒖𝒉 𝑻𝒉𝒂𝒂𝒍𝒊 𝑲𝒂𝒕𝒕𝒊 𝑽𝒂𝒛𝒉𝒌𝒂𝒊 𝑻𝒉𝒂𝒓𝒖𝒗𝒆𝒏 𝑫𝒊 🤭✨** ",
           " **𝑷𝒂𝒂𝒚𝒂𝒔𝒂𝒕𝒉𝒖𝒍𝒂 𝒊𝒓𝒖𝒌𝒌𝒖𝒎 𝑴𝒖𝒏𝒅𝒉𝒊𝒓𝒊 😋✨ 𝑵𝒆𝒆 𝑻𝒉𝒂𝒏 𝑬𝒏 𝑺𝒐𝒑𝒑𝒂𝒏𝒂 𝑺𝒖𝒏𝒅𝒉𝒂𝒓𝒊 😅✨** ",
           " **𝑻𝒉𝒐𝒐𝒌𝒌𝒂𝒕𝒉𝒖𝒍𝒂 𝑽𝒂𝒓𝒖𝒎 𝑲𝒂𝒏𝒂𝒗𝒖 😴 𝑬𝒑𝒑𝒐𝒅𝒉𝒖𝒎 𝑼𝒏𝒏𝒐𝒅𝒂 𝑵𝒊𝒏𝒂𝒊𝒗𝒖 🤗✨** ",
           " **𝑺𝒖𝒏𝒅𝒂𝒚 𝑷𝒐𝒗𝒂𝒏𝒈𝒂 𝑩𝒂𝒓 - 𝑼𝒉 🍾🍻 𝑼𝒏𝒏𝒂 𝑷𝒂𝒂𝒕𝒉𝒂𝒅𝒉𝒖 𝑨𝒂𝒈𝒊𝒕𝒆𝒏 𝑮𝒂𝒓 - 𝑼𝒉 🥴✨** ",
           " **𝑾𝒊𝒏𝒆𝒔𝒉𝒐𝒑 𝒍𝒂 𝑰𝒓𝒖𝒌𝒌𝒖𝒎 𝑩𝒆𝒆𝒓 - 𝑼𝒉 🍾✨ 𝑵𝒆𝒆 𝑰𝒍𝒍𝒂𝒅𝒉𝒂 𝑳𝒊𝒇𝒆  𝒖𝒉 𝑩𝒐𝒓𝒆 - 𝑼𝒉 🥱✨** ",
           " **𝑴𝒂𝒕𝒉𝒔 𝑲𝒖 𝑻𝒂𝒎𝒊𝒍 𝒍𝒂 𝑲𝒂𝒏𝒂𝒌𝒌𝒖 🧮 𝑬𝒑𝒑𝒐 𝑶𝒌 𝑺𝒐𝒍𝒍𝒖𝒗𝒂 𝑬𝒏𝒂𝒌𝒌𝒖 🙈✨** ",
           " **𝑸𝒖𝒆𝒆𝒏 𝒌𝒌𝒖 𝑷𝒂𝒊𝒓 𝑲𝒊𝒏𝒈 - 𝑼𝒉 🤴 𝑼𝒏𝒂𝒌𝒌𝒖 𝑷𝒐𝒕𝒕𝒖 𝑽𝒊𝒅𝒂𝒗𝒂 𝑹𝒊𝒏𝒈 - 𝑼𝒉 💍✨** ",
           " **𝑼𝒏 𝑩𝒅𝒂𝒚 𝑲𝒌𝒖 𝑻𝒉𝒂𝒓𝒆𝒏 𝑮𝒊𝒇𝒕 - 𝑼𝒉🛍 𝑬𝒏𝒂𝒌𝒌𝒖 𝑳𝒊𝒇𝒆 𝑳𝒐𝒏𝒈 𝑻𝒉𝒂𝒓𝒖𝒗𝒊𝒚𝒂 𝑳𝒊𝒇𝒕 - 𝑼𝒉 🤭✨** ",
           " **𝑻𝒉𝒂𝒍𝒂𝒊𝒍𝒂 𝑻𝒉𝒆𝒊𝒑𝒑𝒂𝒏𝒈𝒂 𝑬𝒏𝒏𝒂 🤪 𝑰𝒅𝒉𝒖𝒗𝒂𝒓𝒂𝒊𝒌𝒖𝒎 𝑷𝒂𝒂𝒕𝒉𝒂𝒅𝒉𝒖 𝑰𝒍𝒍𝒂 𝑼𝒏𝒏𝒂 𝑴𝒂𝒂𝒓𝒊 𝑶𝒓𝒖 𝑨𝒍𝒂𝒈𝒂𝒏𝒂 𝑷𝒐𝒏𝒏𝒂 🤩✨** ",
           " **𝑺𝒂𝒎𝒂𝒚𝒂𝒍 𝑺𝒆𝒊𝒚𝒚𝒂 𝑻𝒉𝒆𝒗𝒂 𝑺𝒕𝒐𝒗𝒆 - 𝑼𝒉 𝑵𝒂𝒎𝒎𝒂 𝑹𝒆𝒏𝒅𝒖 𝑷𝒆𝒓𝒖𝒎 𝑷𝒂𝒏𝒏𝒂𝒍𝒂𝒎 𝑨𝒉 𝑳𝒐𝒗𝒆 - 𝑼𝒉 💙**" ]

# Command
@app.on_message(filters.command(["pickup", "uruttu", "love" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/uruttu  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/uruttu  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/uruttu  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(SHAYRI)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


#

@app.on_message(filters.command(["cancelshayari", "shayarioff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("👣  𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐒𝐓𝐎𝐏𝐏𝐄𝐃 💗")
