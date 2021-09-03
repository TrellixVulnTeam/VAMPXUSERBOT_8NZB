#    @D15H4NT0P a.k.a D15H4NT0P
#    Copyright (C) 2020 D15H4NT0P

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

import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

import userbot.plugins.sql_helper.pmpermit_sql as VAMPBOT_sql
from userbot import ALIVE_NAME, bot
from userbot.thunderconfig import Config
from var import Var
VAMPBOT_USER = str(ALIVE_NAME) if ALIVE_NAME else "Userbot"
from userbot.utils import VAMPBOT_cmd

VAMPBOT_WRN = {}
VAMPBOT_REVL_MSG = {}

VAMPBOT_PROTECTION = Config.VAMPBOT_PRO

SPAM = os.environ.get("SPAM", None)
if SPAM is None:
    HMM_LOL = "5"
else:
    HMM_LOL = SPAM

VAMPBOT_PM = os.environ.get("VAMPBOT_PM", None)
if VAMPBOT_PM is None:
    CUSTOM_VAMPBOT_PM_PIC = "https://telegra.ph/file/53aed76a90e38779161b1.jpg"
else:
    CUSTOM_VAMPBOT_PM_PIC = VAMPBOT_PM
FUCK_OFF_WARN = f"**Blocked You As You Spammed {VAMPBOT_USER}'s DM\n\n **IDC**"




OVER_POWER_WARN = (
    f"**Hello Sir Im Here To Protect {VAMPBOT_USER} Dont Under Estimate Me I Am Very Powerful😂😂  **\n\n"
    f"`My Master {VAMPBOT_USER} is Busy Right Now !` \n"
    f"{VAMPBOT_USER} Is Very Busy Why Came Please Lemme Know Choose Your Deasired Reason"
    f"**Btw Dont Spam Or Get Banned** 😂😂 \n\n"
    f"**{CUSTOM_VAMPBOT_PM_PIC}**\n"
)

VAMPBOT_STOP_EMOJI = (
    "✋"
)
if Var.PRIVATE_GROUP_ID is not None:
    @bot.on(events.NewMessage(outgoing=True))
    async def VAMPBOT_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not VAMPBOT_sql.is_approved(chat.id):
                if not chat.id in VAMPBOT_WRN:
                    VAMPBOT_sql.approve(chat.id, "outgoing")
                    bruh = "Auto-approved bcuz outgoing 😄😄"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()  

    @borg.on(VAMPBOT_cmd(pattern="(a|approve)"))
    async def block(event):
        if event.fwd_from:
            return
        replied_user = await borg(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chats = await event.get_chat()
        if event.is_private:
            if not VAMPBOT_sql.is_approved(chats.id):
                if chats.id in VAMPBOT_WRN:
                    del VAMPBOT_WRN[chats.id]
                if chats.id in VAMPBOT_REVL_MSG:
                    await VAMPBOT_REVL_MSG[chats.id].delete()
                    del VAMPBOT_REVL_MSG[chats.id]
                VAMPBOT_sql.approve(chats.id, f"Wow lucky You {VAMPBOT_USER} Approved You")
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(firstname, chats.id)
                )
                await asyncio.sleep(3)
                await event.delete()

    @borg.on(VAMPBOT_cmd(pattern="block$"))
    async def VAMPBOT_approved_pm(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if VAMPBOT_sql.is_approved(chat.id):
                VAMPBOT_sql.disapprove(chat.id)
            await event.edit("Blocked [{}](tg://user?id={})".format(firstname, chat.id))
            await asyncio.sleep(2)
            await event.client(functions.contacts.BlockRequest(chat.id))
            await event.delete()

            
    @borg.on(VAMPBOT_cmd(pattern="(da|disapprove)"))
    async def VAMPBOT_approved_pm(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if VAMPBOT_sql.is_approved(chat.id):
                VAMPBOT_sql.disapprove(chat.id)
            await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))
            await asyncio.sleep(2)
            await event.edit(
                    "Disapproved User [{}](tg://user?id={})".format(firstname, chat.id)
                )
            await event.delete()

    

    @borg.on(VAMPBOT_cmd(pattern="listapproved$"))
    async def VAMPBOT_approved_pm(event):
        if event.fwd_from:
            return
        approved_users = VAMPBOT_sql.get_all_approved()
        PM_VIA_LIGHT = f"♥‿♥ {VAMPBOT_USER} Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    PM_VIA_LIGHT += f"♥‿♥ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    PM_VIA_LIGHT += (
                        f"♥‿♥ [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            PM_VIA_LIGHT = "no Approved PMs (yet)"
        if len(PM_VIA_LIGHT) > 4095:
            with io.BytesIO(str.encode(PM_VIA_LIGHT)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(PM_VIA_LIGHT)

    @bot.on(events.NewMessage(incoming=True))
    async def VAMPBOT_new_msg(VAMPBOT_):
        if VAMPBOT_.sender_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not VAMPBOT_.is_private:
            return

        VAMPBOT_chats = VAMPBOT_.message.message
        chat_ids = VAMPBOT_.sender_id

        VAMPBOT_chats.lower()
        if OVER_POWER_WARN == VAMPBOT_chats:
            # VAMPBOT_ should not reply to other VAMPBOT_
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(VAMPBOT_.sender_id)
        if chat_ids == bot.uid:
            # don't log Saved Messages
            return
        if sender.bot:
            # don't log bots
            return
        if sender.verified:
            # don't log verified accounts
            return
        if VAMPBOT_PROTECTION == "NO":
            return
        if VAMPBOT_sql.is_approved(chat_ids):
            return
        if not VAMPBOT_sql.is_approved(chat_ids):
            # pm permit
            await VAMPBOT_goin_to_attack(chat_ids, VAMPBOT_)

    async def VAMPBOT_goin_to_attack(chat_ids, VAMPBOT_):
        if chat_ids not in VAMPBOT_WRN:
            VAMPBOT_WRN.update({chat_ids: 0})
        if VAMPBOT_WRN[chat_ids] == 3:
            lemme = await VAMPBOT_.reply(FUCK_OFF_WARN)
            await asyncio.sleep(3)
            await VAMPBOT_.client(functions.contacts.BlockRequest(chat_ids))
            if chat_ids in VAMPBOT_REVL_MSG:
                await VAMPBOT_REVL_MSG[chat_ids].delete()
            VAMPBOT_REVL_MSG[chat_ids] = lemme
            lightn_msg = ""
            lightn_msg += "#Some Retards 😑\n\n"
            lightn_msg += f"[User](tg://user?id={chat_ids}): {chat_ids}\n"
            lightn_msg += f"Message Counts: {VAMPBOT_WRN[chat_ids]}\n"
            # lightn_msg += f"Media: {message_media}"
            try:
                await VAMPBOT_.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=lightn_msg,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except BaseException:
                  await  VAMPBOT_.edit("Something Went Wrong")
                  await asyncio.sleep(2) 
            return

        # Inline
        VAMPBOT_username = Var.TG_BOT_USER_NAME_BF_HER
        VAMPBOT_L = OVER_POWER_WARN.format(
        VAMPBOT_USER, VAMPBOT_STOP_EMOJI, VAMPBOT_WRN[chat_ids] + 1, HMM_LOL
        )
        VAMPBOT_hmm = await bot.inline_query(VAMPBOT_username, VAMPBOT_L)
        new_var = 0
        yas_ser = await VAMPBOT_hmm[new_var].click(VAMPBOT_.chat_id)
        VAMPBOT_WRN[chat_ids] += 1
        if chat_ids in VAMPBOT_REVL_MSG:
           await VAMPBOT_REVL_MSG[chat_ids].delete()
        VAMPBOT_REVL_MSG[chat_ids] = yas_ser



@bot.on(events.NewMessage(incoming=True, from_users=(1232461895)))
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not VAMPBOT_sql.is_approved(chats.id):
            VAMPBOT_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, "**Alert! My dev 𝕶𝖗𝖎𝖘𝖍𝖓𝖆😎 is here. **"
            )
            print("Krishna is here")


@bot.on(
    events.NewMessage(incoming=True, from_users=(1311769691))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not VAMPBOT_sql.is_approved(chats.id):
            VAMPBOT_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @D15H4NT0P. How Can I Disapprove You Come In Sir**😄😄"
            )
            print("Dev Here")
       
@bot.on(
    events.NewMessage(incoming=True, from_users=(798271566))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not VAMPBOT_sql.is_approved(chats.id):
            VAMPBOT_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @Hackintush. How Can I Disapprove You Come In Sir**😄😄"
            )               
            print("Dev Here")
            
@bot.on(
    events.NewMessage(incoming=True, from_users=(1990239830))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not VAMPBOT_sql.is_approved(chats.id):
            VAMPBOT_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**MY DEV!!DEAR COMRADE IS HERE...HOW CAN I DISAPPROVE.... AUTO APPROVED**😄😄"
            )               
            print("DEAR COMRADE IS HERE")            
@bot.on(
    events.NewMessage(incoming=True, from_users=(1908955228))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not VAMPBOT_sql.is_approved(chats.id):
            VAMPBOT_sql.approve(chats.id, "`Yo Developer @CYBER_RISHISUPERYO,felling op to see u⚡🙂🙃😉`")
            await borg.send_message(
                chats, f"RISHISUPERYO OP IS HERE\n @CYBER_RISHISUPERYO IZ HERE ,How can I Disapprove u sir ,SO A͛U͛T͛O͛ A͛P͛P͛R͛O͛V͛E͛D͛⚡😎🤩  "
            )               
            print("`RISHISUPERYO OP IZ HERE ⚡`")            
@bot.on(
    events.NewMessage(incoming=True, from_users=(1754865180))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not VAMPBOT_sql.is_approved(chats.id):
            VAMPBOT_sql.approve(chats.id, "`Alert: @Paramatin7`")
            await borg.send_message(
                chats, f"`⚠️Alert: @Paramatin7 is Here ⚠️`."
            )               
            print("`Paramatin7 Spotted`")   
@bot.on(
    events.NewMessage(incoming=True, from_users=(1435941875))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not VAMPBOT_sql.is_approved(chats.id):
            VAMPBOT_sql.approve(chats.id, "`⚠️Alert: @Paramatin7 is Here ⚠️`")
            await borg.send_message(
                chats, f"Welcome Sir please let me know how may i help you."
            )               
            print("`MR.CRACKER IS HERE`")   
@bot.on(
    events.NewMessage(incoming=True, from_users=(1884903792))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not VAMPBOT_sql.is_approved(chats.id):
            VAMPBOT_sql.approve(chats.id, "`⚠️Alert: @Paramatin7 is Here ⚠️`")
            await borg.send_message(
                chats, f"Welcome Sir please let me know how may i help you."
            )               
            print("`DEAR COMRADE IS HERE...AUTO APPROVED`")   
