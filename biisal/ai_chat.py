# ©️biisal jai shree krishna 😎
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import random
import time
from info import *
from .db import *
import asyncio
from telegraph import upload_file
import os
from .fsub import get_fsub

user_cooldowns = {}


@Client.on_message(filters.command("start") & filters.incoming)
async def startcmd(client, message):
    userMention = message.from_user.mention()
    if not userList.find_one({"userId": message.from_user.id}):
        addUser(message.from_user.id, message.from_user.first_name)
        await client.send_message(
            LOG_CHANNEL,
            text=f"#New_user_started\n\nUser: {message.from_user.mention()}\nid :{message.from_user.id}",
        )
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    btn = [[
        InlineKeyboardButton('Information ✨', callback_data='information')
    ],[
        InlineKeyboardButton('Help ☘️', callback_data='help'),
        InlineKeyboardButton('Updates 〽️', url='https://t.me/FilmZone_official')
    ],[
        InlineKeyboardButton('Owner ⭕', url='https://t.me/Itzmecp')
    ]]
    await message.reply_photo(
        photo="https://telegra.ph/file/e9082bc50bdab83da0eee.jpg",
        caption=f"<b>✨ Hᴇʏ {userMention},\nWᴇʟᴄᴏᴍᴇ Tᴏ Aɴɢᴇʟ'ꜱ Wᴏʀʟᴅ ! ⭕\n\n<blockquote>Yᴏᴜ ᴄᴀɴ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ.I ᴄᴀɴ ʀᴇᴄᴀʟʟ ᴘʀᴇᴠɪᴏᴜs ᴄʜᴀᴛs ᴛᴏ ᴘᴇʀsᴏɴᴀʟɪᴢᴇ ʏᴏᴜʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ, ᴍᴀᴋɪɴɢ ɪᴛ ᴍᴏʀᴇ\nʜᴜᴍᴀɴ-ʟɪᴋᴇ.\nʜᴏᴡ ᴄᴀɴ ɪ ᴀssɪsᴛ ʏᴏᴜ ?</blockquote>\n\nᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href=https://t.me/itzmecp>Itzmecp</a></b>",
        reply_markup=InlineKeyboardMarkup(btn)
    )
    return


@Client.on_callback_query(filters.regex(r'^help'))
async def help(client, query):
    btn = [[
        InlineKeyboardButton('Back', callback_data='back_start')
    ]]
    text = """
<b>✨ Usᴇs ᴏғ ᴄᴏᴍᴍᴀɴᴅs ✨

• /bard - ɪғ ʏᴏᴜ ᴀʀᴇ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀsᴋ ᴀɴʏᴛʜɪɴɢ
Ex: <code>/bard who is Best In the World</code>
ɴᴏᴛᴇ : ɪɴ ᴘʀɪᴠᴀᴛᴇ ʏᴏᴜ ᴅᴏɴ'ᴛ ɴᴇᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs

• /scan_ph - Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴄᴀɴ ᴀɴ ɪᴍᴀɢᴇ ᴀɴᴅ ʀᴇᴛʀɪᴇᴠᴇ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ɪᴛ ғʀᴏᴍ ᴍᴇ. Tᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, sɪᴍᴘʟʏ ᴜᴘʟᴏᴀᴅ ᴛʜᴇ ɪᴍᴀɢᴇ ғɪʀsᴛ. Aғᴛᴇʀ ᴛʜᴀᴛ, ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴇ ᴘʜᴏᴛᴏ ᴜsɪɴɢ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇʀʏ
Ex: <code>/scan_ph tell me about this img !</code></b>
"""
    await query.message.edit(text, reply_markup=InlineKeyboardMarkup(btn))

        
@Client.on_callback_query(filters.regex(r'^information'))
async def information(client, query):
    btn = [[
        InlineKeyboardButton('Back', callback_data='back_start')
    ]]
    text = """
<b>Angel Ai Information ✨

☘️ Welcome to Angel Ai Bot,

 ⭕ A powerful AI chat bot created by @Itzmecp This bot is designed to engage with users in conversation, providing intelligent responses and assistance across various topics. 〽️</b>
 """
    await query.message.edit(text, reply_markup=InlineKeyboardMarkup(btn))


@Client.on_callback_query(filters.regex(r'^back_start'))
async def back_start(client, query):
    btn = [[
        InlineKeyboardButton('Information ✨', callback_data='information')
    ],[
        InlineKeyboardButton('Help ☘️', callback_data='help'),
        InlineKeyboardButton('Updates 〽️', url='https://t.me/FilmZone_Official')
    ],[
        InlineKeyboardButton('Owner ⭕', url='https://t.me/Itzmecp')
    ]]
    await query.message.edit(
        text=f"<b>✨ Hᴇʏ {query.from_user.mention()},\nWᴇʟᴄᴏᴍᴇ Tᴏ Aɴɢᴇʟ'ꜱ Wᴏʀʟᴅ ! ⭕\n\n<blockquote>Yᴏᴜ ᴄᴀɴ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ.I ᴄᴀɴ ʀᴇᴄᴀʟʟ ᴘʀᴇᴠɪᴏᴜs ᴄʜᴀᴛs ᴛᴏ ᴘᴇʀsᴏɴᴀʟɪᴢᴇ ʏᴏᴜʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ, ᴍᴀᴋɪɴɢ ɪᴛ ᴍᴏʀᴇ\nʜᴜᴍᴀɴ-ʟɪᴋᴇ.\nʜᴏᴡ ᴄᴀɴ ɪ ᴀssɪsᴛ ʏᴏᴜ ?</blockquote>\n\nᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href=https://t.me/itzmecp>Itzmecp</a></b>",
        reply_markup=InlineKeyboardMarkup(btn)
    )



async def ai_res(message, query):
    try:
        userMention = message.from_user.mention()
        obj = {'query' : query ,'bot_name' : BOT_NAME , 'bot_admin'  :ADMIN_NAME }
        url = f"https://bisal-ai-api.vercel.app/biisal"  # dont try to change anything here ⚠️
        res = requests.post(url , data=obj)
        if res.status_code == 200:
            response_json = res.json()
            api_response = response_json.get("response")
            if len(query) <= 280:
                await message.reply_text(
                    text=f"<b><blockquote>{BOT_NAME}</blockquote> :\n{api_response}</b>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "start me 🌙",
                                    url=f"https://t.me/AngelAi_cpbot?start=z",
                                )
                            ]
                        ]
                    ),
                    disable_web_page_preview=True,
                )
            else:
                cut_query_str = query[:77]
                await message.reply_text(
                    text=f"<b><blockquote>{BOT_NAME}</blockquote> :\n{api_response}</b>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "start me 🌙",
                                    url=f"https://t.me/AngelAi_cpbot?start=z",
                                )
                            ]
                        ]
                    ),
                    disable_web_page_preview=True,
                )
                await client.send_message(
                    LOG_CHANNEL,
                    text=f"user: {userMention}\n\nAsked to Ai : {query}\n\nAi Res: {api_response}",
                )

    except Exception as e:
        print(f"i got this err : {e}")
        await message.reply_text(f"sry i got this err : {e}")
    return


@Client.on_message(filters.command("bol") & filters.chat(CHAT_GROUP))
async def grp_res(client, message):
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    grp_query = (
        message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    )
    print(grp_query)
    if not grp_query:
        return await message.reply_text(
            "<b>Example Use:\n<code>/bol Who is best in the world ??</code>\n\nHope you got it.Try it now..</b>"
        )
    current_time = time.time()
    coolDownUser = message.from_user.id
    if (
        coolDownUser in user_cooldowns
        and current_time - user_cooldowns[coolDownUser] < COOL_TIMER
    ):
        remaining_time = int(COOL_TIMER - (current_time - user_cooldowns[coolDownUser]))
        try:
            await message.react(emoji="😢")
        except Exception:
            pass
        remTimeMsg = await message.reply_text(
            f"<b>Nope..!! Spaming not allowed bro...\nPlease wait {remaining_time} seconds before sending new message...</b>"
        )
        await asyncio.sleep(remaining_time)
        await remTimeMsg.delete()
        return
    try:
        await message.react(emoji=random.choice(REACTIONS))
    except Exception:
        pass
    thinkStc = await message.reply_sticker(sticker=random.choice(STICKERS_IDS))
    await ai_res(message, grp_query)
    user_cooldowns[coolDownUser] = current_time
    await thinkStc.delete()
    return


@Client.on_message(
    filters.command("broadcast") & (filters.private) & filters.user(ADMIN)
)
async def broadcasting_func(client, message):
    if message.from_user.id != ADMIN:
        return
    count = 0
    failed = 0
    bAdminText = (
        message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    )
    if not bAdminText:
        return await message.reply_text("caption to likh gadhe !!")
    bmsg = await message.reply_text(text=f"Broadcast Started for :\n\n{bAdminText}")
    if message.reply_to_message and message.reply_to_message.audio:
        audio_message = message.reply_to_message.audio
        audio_file_id = audio_message.file_id
        bmsg = await bmsg.edit(
            f"Broadcast started for...\n\nMsg Text : {bAdminText}",
        )
        for userDoc in userList.find():
            try:
                userId = userDoc["userId"]
                await client.send_audio(
                    userId,
                    audio_file_id,
                    caption=f"<b>{bAdminText}</b>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Admin Support ☘",
                                    url=f"https://t.me/Itzmecp",
                                )
                            ]
                        ]
                    ),
                )
                count += 1  # counting successful broadcasts
                if count % 20 == 0:
                    await bmsg.edit(
                        f"broadcasted to {count} users...done..!!\nFailed : {failed}"
                    )
            except Exception as loopErr:
                failed += 1
                print(f"got this err in for loop for broadcasting aud : {loopErr}")
    else:
        try:
            for userDoc in userList.find():
                try:
                    userId = userDoc["userId"]
                    await client.send_message(
                        userId,
                        text=f"<b>{bAdminText}</b>",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        "Admin Support 🌙",
                                        url=f"https://t.me/Itzmecp",
                                    )
                                ]
                            ]
                        ),
                    ),
                    count += 1  # counting succesfull broadcasts
                    if count % 20 == 0:
                        await bmsg.edit(
                            f"broadcasted to {count} users...done..!!\nFailed : {failed}"
                        )
                except Exception as loopErr:
                    failed += 1
                    print(f"got this err in for loop for broadcasting : {loopErr}")
        except Exception as loopErr:
            failed += 1
            print(f"got this err in for loop for broadcasting : {loopErr}")
    await bmsg.edit(
        f"succesfully broadcasted to {count} users...\n\n Failed : {failed}"
    )
    return


@Client.on_message(filters.command("scan_ph"))
async def telegraph_upload(client, message):
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    if ONLY_SCAN_IN_GRP and message.chat.id != CHAT_GROUP:
        return await message.reply(
            text=f"<b>You can use this feature only in our channel</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Updates 〽️",
                            url=f"https://t.me/FilmZone_talk",
                        )
                    ]
                ]
            ),
        )
    try:
        current_time = time.time()
        coolDownUser = message.from_user.id
        question = (
            message.text.split(" ", 1)[1]
            if len(message.text.split(" ", 1)) > 1
            else None
        )
        replied = message.reply_to_message
        if (
            coolDownUser in user_cooldowns
            and current_time - user_cooldowns[coolDownUser] < COOL_TIMER
        ):
            remaining_time = int(
                COOL_TIMER - (current_time - user_cooldowns[coolDownUser])
            )
            try:
                await message.react(emoji=random.choice(REACTIONS))
            except Exception:
                pass    
            remTimeMsg = await message.reply_text(
                f"<b>Please wait for {remaining_time} seconds before using /scan_ph again to prevent flooding. Thanks for your patience! 😊</b>"
            )
            await asyncio.sleep(remaining_time)
            await remTimeMsg.delete()
            return
        elif not replied:
            return await message.reply_text("<b>Replay a photo with this command !</b>")
        elif not (replied.photo):
            return await message.reply_text("<b>Please reply with valid image file</b>")
        elif replied.video:
            return await message.reply_text("Please reply with valid image file")
        question = message.text.split(" ", 1)[1] if " " in message.text else ""
        if not question:
            return await message.reply_text(
                "<b>Please provide a qustion after the /scan_ph command.\n\nExample Use:\n<code>/scan_ph tell me about this image ! </code>\n\nHope you got it.Try it now..</b>"
            )
        try:
            await message.react(emoji=random.choice(REACTIONS))
        except Exception:
            pass
        text = await message.reply_text(
            f"<b>✨ Hello {message.from_user.mention()},\nWᴀɪᴛ...😎</b>",
            disable_web_page_preview=True,
        )
        media = await replied.download()
        await text.edit_text(
            f"<b>✨ Hello {message.from_user.mention()},\nNᴏᴡ Iᴍ ᴄʜᴇᴄᴋɪɴɢ ʏᴏᴜʀ ɪᴍᴀɢᴇ...🤔</b>",
            disable_web_page_preview=True,
        )
        try:
            response = upload_file(media)
        except Exception as error:
            print(error)
            return await text.edit_text(
                text=f"Error :- {error}", disable_web_page_preview=True
            )
        try:
            os.remove(media)
        except Exception as error:
            print(error)
            return
        imgUrl = f"https://graph.org{response[0]}"
        try:
            url = f"https://bisal-ai-api.vercel.app/biisal/img?link={imgUrl}&question={question}"
            res = requests.get(url)
            if res.status_code == 200:
                response_json = res.json()
                airesponse = response_json.get("response")
            await text.edit_text(
                text=f"<b>Jai Shree Krishna {message.from_user.mention()},\n\n•{airesponse}</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "start me 🌙", url=f"https://t.me/AngelAi_cpbot?start=z"
                            )
                        ]
                    ]
                ),
            )
            user_cooldowns[coolDownUser] = current_time
            return
        except Exception as e:
            await text.edit_text(f"<b>Sorry i Got Some error !!</b>")
            await asyncio.sleep(5)
            await text.delete()
            await replied.delete()
            await message.delete()
            return
    except Exception as e:
        print(f"I got this err to scan this img : {e}")
        await message.reply(f"I got this err to scan this img : {e}")


@Client.on_message(filters.text & filters.private)
async def AiMsgHanDl(client, message):
    if not userList.find_one({"userId": message.from_user.id}):
        addUser(message.from_user.id, message.from_user.first_name)
        await client.send_message(
            LOG_CHANNEL,
            text=f"#New_user_started\n\nUser: {message.from_user.mention()}\nid :{message.from_user.id}",
        )
    if message.text.startswith("/"):
        return
    if FSUB:
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    current_time = time.time()
    coolDownUser = message.from_user.id
    if (
        coolDownUser in user_cooldowns
        and current_time - user_cooldowns[coolDownUser] < COOL_TIMER
    ):
        remaining_time = int(COOL_TIMER - (current_time - user_cooldowns[coolDownUser]))
        try:
            await message.react(emoji="😢")
        except Exception:
            pass
        remTimeMsg = await message.reply_text(
            f"<b>Nope..!! Spaming not allowed bro...\nPlease wait {remaining_time} seconds before sending new message...</b>"
        )
        await asyncio.sleep(remaining_time)
        await remTimeMsg.delete()
        return
    try:
        await message.react(emoji=random.choice(REACTIONS))
    except Exception:
        pass
    thinkStc = await message.reply_sticker(sticker=random.choice(STICKERS_IDS))
    private_query = message.text
    await ai_res(message, private_query)
    user_cooldowns[coolDownUser] = current_time
    await thinkStc.delete()
    return
