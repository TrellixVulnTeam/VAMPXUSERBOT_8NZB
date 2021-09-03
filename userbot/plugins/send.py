# Changes Fixed By @D15H4NT0P
# Credits To Team DC
import asyncio
from userbot import ALIVE_NAME
import os
from datetime import datetime
from pathlib import Path
DELETE_TIMEOUT = 3
VAMPBOT_sss_image_path = "./resources/541200.png"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "VAMPUSERBOT"
from userbot import bot 
from userbot.utils import VAMPBOT_cmd, sudo_cmd
from userbot.utils import edit_or_reply as eor

@bot.on(VAMPBOT_cmd(pattern=r"send (?P<krish>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"send (?P<krish>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    VAMPBOT_hehehe = bot.uid
    message_id = event.message.id
    VAMPBOT_sss = VAMPBOT_sss_image_path
    input_str = event.pattern_match.group(1)
    lightn_plug = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(lightn_plug):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            lightn_plug,
            force_document=True,
            allow_cache=False,
            VAMPBOT_sss=VAMPBOT_sss,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**==> Plugin name:** 🗡`{input_str}`🗡\n**==> Uploaded in {time_taken_in_ms} seconds only.**\n**==> Uploaded by:** [{DEFAULTUSER}](tg://user?id={VAMPBOT_hehehe})\n",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.edit("__Done See The Taged Msg!!__") #only italic if loaded markdown else it doesn't look gr8
    else:
        await eor(event, f"**404**: {DEFAULTUSER}\n __No File Is Name As__ 🗡{input_str}🗡\n\nPlease Try With Right Name😔")
