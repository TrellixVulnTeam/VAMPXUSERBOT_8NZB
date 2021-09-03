#    Copyright (C) 2021 D15H4NT0P

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.



"""Thanks To 
@Midhun_xD
@D15H4NT0P
@Shivam_Patel
@NOOBIzBack
"""









import os

import re
import json
from math import ceil
from userbot.thunderconfig import Config

from telethon import Button, custom, events, functions

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST, DETAIL_CMD_HELP, bot

from var import Var


LIGHT_LOGS = Config.PM_LOGGR_BOT_API_ID 
VAMPBOT_bot = Var.TG_BOT_USER_NAME_BF_HER
import asyncio

from datetime import datetime
from pathlib import Path


from userbot.utils import VAMPBOT_cmd, load_module, remove_plugin

DELETE_TIMEOUT = 5


thumb_image_path = "./resources/541200.png"

VAMPBOT_USER = str(ALIVE_NAME) if ALIVE_NAME else "ℓιgнтηιηg мαѕтєя"
VAMPBOT_BOT = Var.TG_BOT_TOKEN_BF_HER






@borg.on(VAMPBOT_cmd(pattern=r"unload (?P<krish_blac>\w+)$"))
async def unload(VAMPBOT_):
    if VAMPBOT_.fwd_from:
        return
    krish_blac = VAMPBOT_.pattern_match["krish_blac"]
    try:
        remove_plugin(krish_blac)
        await VAMPBOT_.edit(f"Successfully unloaded {krish_blac}")
    except Exception as e:
        await VAMPBOT_.edit(
            "Successfully unloaded {krish_blac}\n{}".format(krish_blac, str(e))
        )


@borg.on(VAMPBOT_cmd(pattern=r"load (?P<krish_blac>\w+)$"))
async def load(VAMPBOT_):
    if VAMPBOT_.fwd_from:
        return
    krish_blac = VAMPBOT_.pattern_match["krish_blac"]
    try:
        try:
            remove_plugin(krish_blac)
        except BaseException:
            pass
        load_module(krish_blac)
        await VAMPBOT_.edit(f"Successfully loaded {krish_blac}")
    except Exception as e:
        await VAMPBOT_.edit(
            f"Sorry,{krish_blac} can not be loaded\nbecause of the following error.\n{str(e)}"
        )

 # created by @cyper666
"""xoxbot: Avaible commands: .xnxx picx les<link>
"""


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError




@borg.on(VAMPBOT_cmd(pattern="xnxx?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "💋2016 Videolar🔞{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(VAMPBOT_cmd(pattern="picx?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "♨️Old photo👙{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(VAMPBOT_cmd(pattern="les?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "🔞Uz_sex♨️{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


BOT_MSG = os.environ.get("BOT_MSG", None)
if BOT_MSG is None:
    BOT_LIT = f"Hey! This is adavanced PM Protection by [𝐁𝐥𝐚𝐜𝐤 𝐋𝐢𝐠𝐡𝐭𝐧𝐢𝐧𝐠](https://t.me/VAMPBOT_support). "
else:
    BOT_LIT = BOT_MSG   


VAMPBOT_WARN = os.environ.get("VAMPBOT_WARN", None)
VAMPBOT_BOT_PIC = os.environ.get("VAMPBOT_BOT_PIC", None)

if VAMPBOT_WARN is None:
    WARNING = (
    f"**{BOT_LIT}"
    f"** I'm here to protect {VAMPBOT_USER}'s PM from spamming.**\n\n"
    f"**My master {VAMPBOT_USER} is busy right now !** \n"
    f"Please let me know why you came here. "
    f"**Choose your desired reason from below.**  \n\n"
    f"**But don't spam otherwise you will be blocked**\n\n"
    f"**Also choose your Original reason Else you will be blocked [Don't Underestimate]**"
   )
else:
    WARNING = VAMPBOT_WARN

VAMPBOT_BOT_PIC = (
    VAMPBOT_BOT_PIC
    if VAMPBOT_BOT_PIC
    else "https://telegra.ph/file/ff90ed0b44221a7b438b7.jpg"
)









@tgbot.on(events.InlineQuery)
async def inline_handler(VAMPBOT_):
    builder = VAMPBOT_.builder
    result = None
    query = VAMPBOT_.text
    if VAMPBOT_.query.user_id == bot.uid and query.startswith("**sed") or query.startswith("soosed"):
        rev_text = query[::-1]
        buttons = VAMPBOT_s_menu_for_help(0, CMD_LIST, "helpme")
        result = builder.article(
            f"Help Menu",
            text="\n{}\n`Plugins`: {}".format(query, len(CMD_LIST)),
            buttons=buttons,
            link_preview=False,
        )
        await VAMPBOT_.answer([result] if result else None)
    elif VAMPBOT_.query.user_id == bot.uid and query.startswith("**Black") or query.startswith("Black"):
        result = builder.article(
            title="Cool",
            text=f"**How If Face Problem \n{VAMPBOT_USER}** \nChoose Your Problem For Help ",
            buttons=[
                [custom.Button.inline("Help Menu😎", data="what?"),
                custom.Button.inline("Ping🙃", data="bitch")],
                [Button.url("Support Group🥺", "https://t.me/VAMPBOT_support")],
                [Button.url("Help Article🤓", "https://app.gitbook.com/@poxsisofficial/s/help/")],
                [Button.url("Get Updates😅",
                    "https://t.me/VAMPBOT_official"
                    )
                ], 
            ],
        )
        await VAMPBOT_.answer([result])

    elif VAMPBOT_.query.user_id == bot.uid and query.startswith("**Hello Sir"):
        result = builder.photo(
            file=VAMPBOT_BOT_PIC,
            text=WARNING,
            buttons=[
                [custom.Button.inline("Wanna Spam Something?😉", data="VAMPBOT_is_here_cant_spam")],
                [
                    custom.Button.inline(
                        "My Friend❤️❤️",
                        data="he_sucks",
                    )
                ],
                [custom.Button.inline("Requesting🙏", data="fck_ask")],
                [
                    custom.Button.inline(
                        "Lemme In :)", 
                        data="lol_u_think_so",
                        
                    )
                        
                ],

            ],
            )
        await VAMPBOT_.answer([result] if result else None)
    else:
        return
    


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    )
)
async def VAMPBOT_pugins_query_hndlr(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:  # pylint:disable=E0602
        VAMPBOT_page = int(VAMPBOT_.data_match.group(1).decode("UTF-8"))
        buttons = VAMPBOT_s_menu_for_help(
            VAMPBOT_page + 1, CMD_LIST, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await VAMPBOT_.edit(buttons=buttons)
    else:
        VAMPBOT_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"
        await VAMPBOT_.answer(VAMPBOT_is_best, cache_time=0, alert=True)


@tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"_VAMPBOT_plugins_(.*)")
   )
) # Thanks To Friday Userbot
async def VAMPBOT_pugins_query_hndlr(VAMPBOT_):
    if not VAMPBOT_.query.user_id == bot.uid:
        how = "Do you Really Think This is for you? \nThen Make your own VAMPBOT_ Bot and don't poke your nose in mine"
        await VAMPBOT_.answer(how, cache_time=0, alert=True)
        return
    light_pulu_name = VAMPBOT_.data_match.group(1).decode("UTF-8")
   
    if light_pulu_name in CMD_HELP.keys():
       
       VAMPBOT_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n{CMD_HELP[light_pulu_name]}"
       VAMPBOT_is_best = VAMPBOT_help_strin 
       VAMPBOT_is_best += "\n\n**In Case Any Problem**[𝐁𝐥𝐚𝐜𝐤 𝐋𝐢𝐠𝐡𝐭𝐧𝐢𝐧𝐠](https://t.me/VAMPBOT_support) ".format(light_pulu_name)
    
    else:
       VAMPBOT_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n`{CMD_LIST[light_pulu_name]}`\n\n**Ask at @VAMPBOT_support"
       VAMPBOT_is_best = VAMPBOT_help_strin 
       VAMPBOT_is_best += "\n\n**In Case Any Problem @VAMPBOT_support** ".format(light_pulu_name)
    if len(VAMPBOT_is_best) >= 4096:
          D15H4NT0P = "`Wait.( ͡🔥 ͜ʖ ͡🔥)`"
          await VAMPBOT_.answer(D15H4NT0P, cache_time=0, alert=True)
          out_file = VAMPBOT_is_best
          lig_url = "https://del.dog/documents"
          r = requests.post(lig_url, data=out_file.encode("UTF-8")).json()
          lig_url = f"https://del.dog/{r['key']}"
          await VAMPBOT_.edit(
               f"Pasted {light_pulu_name} to {lig_url}",
               link_preview=False,
               buttons=[
                [custom.Button.inline("🇸‌🇵‌🇪‌🇨‌🇮‌🇦‌🇱‌", data="krish")],
                [custom.Button.inline("Ⴆαƈƙ 💢", data="lghtback")]],
         )
    else:
           await VAMPBOT_.edit(
            message=VAMPBOT_is_best,
            buttons=[
                [custom.Button.inline("🇸‌🇵‌🇪‌🇨‌🇮‌🇦‌🇱‌", data="krish")],
                [custom.Button.inline("Ⴆαƈƙ 💢", data="lghtback")],
            ],
        )


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"helpme_prev\((.+?)\)")
    )
)
async def VAMPBOT_pugins_query_hndlr(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:  # pylint:disable=E0602
        VAMPBOT_page = int(VAMPBOT_.data_match.group(1).decode("UTF-8"))
        buttons = VAMPBOT_s_menu_for_help(
            VAMPBOT_page - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await VAMPBOT_.edit(buttons=buttons)
    else:
        VAMPBOT_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"
        await VAMPBOT_.answer(VAMPBOT_is_best, cache_time=0, alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"what?")))
async def what(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
        fck_bit = "**VAMPUSERBOT Heres With The Detailed Help For CMDs** 😉😉 ! "
        buttons = VAMPBOT_s_menu_for_help(0, CMD_LIST, "helpme")
        await VAMPBOT_.edit(fck_bit, buttons=buttons)
    else:
        txt = f"Ohh C'mon You Think That This Is For You?\n Ok I Will Complain To {VAMPBOT_USER}👀👀"
        await VAMPBOT_.answer(txt, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"VAMPBOT_is_here_cant_spam")))
async def VAMPBOT_is_better(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {VAMPBOT_USER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await VAMPBOT_.answer(fck_bit, cache_time=0, alert=True)
        return
    await VAMPBOT_.get_chat()
    VAMPBOT_id = VAMPBOT_.query.user_id
    text1 = f"LOL **You Think So You Can**😂😂\n\n**[Idiot](tg://user?id={VAMPBOT_id}) Bye I'm going to block you.**😂😂"
    await VAMPBOT_.edit("Off Course Go To Hell Dude")
    await bot.send_message(VAMPBOT_.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(VAMPBOT_.query.user_id))
    await VAMPBOT_.edit("😛")
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={VAMPBOT_id}) Trying To Spam 😂\n\n**So Blocked**.",
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_u_think_so")))
async def VAMPBOT_is_better(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {VAMPBOT_USER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await VAMPBOT_.answer(fck_bit, cache_time=0, alert=True)
        return
    await VAMPBOT_.get_chat()
    VAMPBOT_id = VAMPBOT_.query.user_id
    text1 = f"LOL You Think So You Can😂😂\nGo and wait😂😂"
    await VAMPBOT_.edit("Off Course Go To Hell Dude😛")
    await bot.send_message(VAMPBOT_.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(VAMPBOT_.query.user_id))
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={VAMPBOT_id}) Tryin To Enter With Out approval😂 \n.",
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"coming_soon")))
async def VAMPBOT_is_better(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
        await VAMPBOT_.edit(
        "Which Alive You Wanna See?", buttons= [
        (Button.inline("Friday Alive", data="falive"),
        Button.inline("Dark Cobra Alive", data="dalive"))
        , [Button.inline("VAMPBOT_ Alive", data="alive"),
            Button.inline("Hell Alive", data="halive")],[
            Button.inline("Venom Alive", data="valive"
            )
            ]
    ])


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"bitch")))

async def VAMPBOT_is_better(VAMPBOT_):
        start = datetime.now()

        end = datetime.now()

        ping = (end - start).microseconds / 1000
        wews = bot.me.first_name
        weds = bot.me.username
        if VAMPBOT_.query.user_id == bot.uid:
          fck_bit = f"꧁ Pong! ꧂\n\n⚘ Ping Time:- {ping}\n\n⚘ My VAMPBOT_ Master [{wews}](t.me/{weds})"
          await VAMPBOT_.edit(fck_bit, link_preview=False, buttons=[Button.inline("Back", data="wtshit")])
        else: 
           await VAMPBOT_.answer(f"I am {VAMPBOT_USER}'s Assistant not your", alert=True)
    

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"he_sucks")))
async def VAMPBOT_is_better(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {VAMPBOT_USER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await VAMPBOT_.answer(fck_bit, cache_time=0, alert=True)
        return
    await VAMPBOT_.get_chat()
    VAMPBOT_id = VAMPBOT_.query.user_id
    await VAMPBOT_.edit("Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** **You Can Wait For My Master**")
    await asyncio.sleep(2)
    await VAMPBOT_.edit(
        "Name Which Type Of Friend?", buttons= [
        [Button.inline("School", data="school")],
        [Button.inline("Tg Causal Friend", data="tg_okay")],
        ], 
    )
    light_text = "`Warning`- ❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"
    await bot.send_message(VAMPBOT_.query.user_id, light_text)
    
    
    
    
    
    
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))
async def yeahbaba(VAMPBOT_):
        if VAMPBOT_.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {VAMPBOT_USER} "
            await VAMPBOT_.answer(fck_bit, cache_time=0, alert=True)
            return
        light_text = "**So You  Are TG Friend** Okay wait"
        VAMPBOT_id = VAMPBOT_.query.user_id
        await asyncio.sleep(2)
        await VAMPBOT_.edit(f"`Informing To Master {VAMPBOT_USER}`")
        await asyncio.sleep(2)
        await VAMPBOT_.edit("`Done Informed`")
        await bot.send_message(VAMPBOT_.query.user_id, light_text)
        await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Friend](tg://user?id={VAMPBOT_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={VAMPBOT_id}) Is Waiting.",
    
    )
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"School")))
async def yeahbaba(VAMPBOT_):
        if VAMPBOT_.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {VAMPBOT_USER} "
            await VAMPBOT_.answer(fck_bit, cache_time=0, alert=True)
            return
        light_text = "**So You  Are  Friend** Okay wait"
        VAMPBOT_id = VAMPBOT_.query.user_id
        await asyncio.sleep(2)
        await VAMPBOT_.edit(f"`Informing To Master {VAMPBOT_USER}`")
        await asyncio.sleep(2)
        await VAMPBOT_.edit("`Done Informed`")
        await bot.send_message(VAMPBOT_.query.user_id, light_text)
        await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Friend](tg://user?id={VAMPBOT_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={VAMPBOT_id}) Is Waiting.",
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_ask")))
async def VAMPBOT_is_better(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {VAMPBOT_USER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await VAMPBOT_.answer(fck_bit, cache_time=0, alert=True)
        return
    await VAMPBOT_.get_chat()
    VAMPBOT_id = VAMPBOT_.query.user_id
    await VAMPBOT_.edit("Okay let Me Think🤫")
    await asyncio.sleep(2)
    await VAMPBOT_.edit("Okay Giving You A Chance🤨")
    await asyncio.sleep(2)
    await VAMPBOT_.edit(
        "You Will Spam?", buttons= [
        [Button.inline("Yes", data="lemme_ban")],
        [Button.inline("No", data="hmm")],
        ],
    )

    
    reqws = "`Warning`- ❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"


    await bot.send_message(VAMPBOT_.query.user_id, reqws)
    await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Nibba](tg://user?id={VAMPBOT_id}). Wants To Request Something.",
        buttons=[Button.url("Contact Him", f"tg://user?id={VAMPBOT_id}")],
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))
async def yes_ucan(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
           lmaoo = "You Are Not Requesting , Lol."
           await VAMPBOT_.answer(lmaoo, cache_time=0, alert=True)
           return          
    await VAMPBOT_.get_chat()
    await asyncio.sleep(2)
    await VAMPBOT_.edit("Okay You Can Wait Till Wait")
    hmmmmm = "Okay Kindly wait  i will inform you"
    await bot.send_message(
              VAMPBOT_.query.user_id, hmmmmm)
          
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
async def yes_ucan(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
           lmaoo = "You Are Not Requesting , Lol."
           await VAMPBOT_.answer(lmaoo, cache_time=0, alert=True)
           return    
    await VAMPBOT_.get_chat()
    await asyncio.sleep(2)
    await VAMPBOT_.edit("Get Lost Retard")
    ban = "Get Lost Goin To Block You" 
    await bot.send_message(
         VAMPBOT_.query.user_id, ban)
    await bot(functions.contacts.BlockRequest(VAMPBOT_.query.user_id))

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stta")))
async def hmm(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
        text = "🇲‌🇾‌ 🇭‌🇪‌🇱‌🇵‌ 🇸‌🇹‌🇦‌🇹‌🇸‌\n\nᴘʟᴜɢɪɴ-- All Good ✔\nʜᴇʀᴏᴋᴜ - Connected ✔\nʟᴏɢs -- Looks Good :/\nTottal Plugs: {}".format(len(CMD_LIST))
        await VAMPBOT_.answer(text, alert=True)
    else:
        txt = f"Stats For {VAMPBOT_USER} Not For You :)"
        await VAMPBOT_.answer(txt, alert=True)



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"krish")))
async def hmm(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
        text = "Bot Alright Master if in case of any Problems reach out to support group;)"
        await VAMPBOT_.answer(text, alert=True)
    else:
        txt = f"For {VAMPBOT_USER} Not For You :)"
        await VAMPBOT_.answer(txt, alert=True)   

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"wtshit"))) 
async def lmaao(VAMPBOT_):
    if VAMPBOT_.query.user_id == bot.uid:
        await VAMPBOT_.edit(
            "Hi Master,\nPlss lemme know in which section you need my help🤨",
            buttons=[
                [custom.Button.inline("Help Menu😎", data="what?"),
                custom.Button.inline("Ping🙃", data="bitch")],
                [Button.url("Support Group🥺", "https://t.me/VAMPBOT_support")],
                [Button.url("Help Article🤓", "https://app.gitbook.com/@poxsisofficial/s/help/")],
                [Button.url("Get Updates😅",
                    "https://t.me/VAMPBOT_support" ,
                    )
                ], 
            ]
        )
    else:
        fukoff = "You Don't belong to my master's category. So, why should i follow your orders\nHence, Fuck off" 
        await VAMPBOT_.answer(fukoff, alert=True)

"""
Thanks To Friday Userbot and @Midhun_xD For This idea
"""
import requests




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lghtback")))
async def ho(event):
    if event.query.user_id != bot.uid:
        how = "Not For You Idiot 🖕( ͡❛ ͜ʖ ͡❛)."
        await event.answer(how, cache_time=0, alert=True)
        return
    await event.answer("( ͡🔥 ͜ʖ ͡🔥)", cache_time=0, alert=False)
    # This Is Copy of Above Code. (C) @SpEcHiDe
    buttons = VAMPBOT_s_menu_for_help(0, CMD_LIST, "helpme")
    ho = f"""VAMPUSERBOT Is Here With Stunning Help !\n
In Case Any Problem [𝐁𝐥𝐚𝐜𝐤 𝐋𝐢𝐠𝐡𝐭𝐧𝐢𝐧𝐠](https://t.me/VAMPBOT_support) \nTottal Plugs( ͡🔥 ͜ʖ ͡🔥): {len(CMD_LIST)}"""
    await event.edit(message=ho, buttons=buttons)



        


    
def VAMPBOT_s_menu_for_help(b_lac_krish, VAMPBOT_plugs, VAMPBOT_lol):
    VAMPBOT_no_rows = 10
    VAMPBOT_no_coulmns = 3
    VAMPBOT_plugins = []
    for p in VAMPBOT_plugs:
        if not p.startswith("_"):
            VAMPBOT_plugins.append(p)
    VAMPBOT_plugins = sorted(VAMPBOT_plugins)
    plugins = [
        custom.Button.inline(
            "{} {} {}".format("⨵", x, "⨵"), data="_VAMPBOT_plugins_{}".format(x)
        )
        for x in VAMPBOT_plugins
    ]
    pairs = list(zip(plugins[::VAMPBOT_no_coulmns], plugins[1::VAMPBOT_no_coulmns]))
    if len(plugins) % VAMPBOT_no_coulmns == 1:
        pairs.append((plugins[-1],))
    max_fix = ceil(len(pairs) / VAMPBOT_no_rows)
    VAMPBOT_plugins_pages = b_lac_krish % max_fix
    if len(pairs) > VAMPBOT_no_rows:
        pairs = pairs[
            VAMPBOT_plugins_pages * VAMPBOT_no_rows : VAMPBOT_no_rows * (VAMPBOT_plugins_pages + 1)
        ] + [
            (
                custom.Button.inline(
                    "🗡яιgнт ρℓυgιи", data="{}_prev({})".format(VAMPBOT_lol, VAMPBOT_plugins_pages)
                ),
               # Thanks To Friday For This Idea
               custom.Button.inline("Back", data="wtshit"
               ),
               custom.Button.inline(
                    "ℓєfт ρℓυgιи ", data="{}_next({})".format(VAMPBOT_lol, VAMPBOT_plugins_pages)
                ),
                
            )
        ]
    return pairs
