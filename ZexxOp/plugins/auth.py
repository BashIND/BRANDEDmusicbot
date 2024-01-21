from pyrogram import filters
from pyrogram.types import Message
##from pyrogram.enums import ParseMode

from config import BANNED_USERS, adminlist
from strings import get_command
from ZexxOp import app
from ZexxOp.utils.database import (delete_authuser, get_authuser,
                                       get_authuser_names,
                                       save_authuser)
from ZexxOp.utils.decorators import AdminActual
from ZexxOp.utils.formatters import int_to_alpha

# Command
AUTH_COMMAND = get_command("AUTH_COMMAND")
UNAUTH_COMMAND = get_command("UNAUTH_COMMAND")
AUTHUSERS_COMMAND = get_command("AUTHUSERS_COMMAND")


@app.on_message(
    filters.command(AUTH_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def auth(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ.**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        user_id = message.from_user.id
        token = await int_to_alpha(user.id)
        from_user_name = message.from_user.first_name
        from_user_id = message.from_user.id
        _check = await get_authuser_names(message.chat.id)
        count = len(_check)
        if int(count) == 20:
            return await message.reply_text("**» ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ʜᴀᴠᴇ 20 ᴜsᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ's ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ (ᴀᴜʟ).**")
        if token not in _check:
            assis = {
                "auth_user_id": user.id,
                "auth_name": user.first_name,
                "admin_id": from_user_id,
                "admin_name": from_user_name,
            }
            get = adminlist.get(message.chat.id)
            if get:
                if user.id not in get:
                    get.append(user.id)
            await save_authuser(message.chat.id, token, assis)
            await message.reply_sticker("CAACAgUAAxkBAAIjRmKPXjN-4bwPCXyRDgQJi4EGns7mAALxBwACXqhRVO2OaCyX0hkNJAQ")
            return await message.reply_text("**» ᴀᴅᴅᴇᴅ ᴛᴏ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏꜰ ʏᴏᴜʀ ɢʀᴏᴜᴘ.**")
        else:
            await message.reply_text("**» ᴀʟʀᴇᴀᴅʏ ɪɴ ᴛʜᴇ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ.**")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    token = await int_to_alpha(user_id)
    from_user_name = message.from_user.first_name
    _check = await get_authuser_names(message.chat.id)
    count = 0
    for smex in _check:
        count += 1
    if int(count) == 20:
        return await message.reply_text("**» ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ʜᴀᴠᴇ 20 ᴜsᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ's ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ (ᴀᴜʟ).**")
    if token not in _check:
        assis = {
            "auth_user_id": user_id,
            "auth_name": user_name,
            "admin_id": from_user_id,
            "admin_name": from_user_name,
        }
        get = adminlist.get(message.chat.id)
        if get:
            if user_id not in get:
                get.append(user_id)
        await save_authuser(message.chat.id, token, assis)
        await message.reply_sticker("CAACAgUAAxkBAAIjRmKPXjN-4bwPCXyRDgQJi4EGns7mAALxBwACXqhRVO2OaCyX0hkNJAQ")
        return await message.reply_text("**» ᴀᴅᴅᴇᴅ ᴛᴏ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏꜰ ʏᴏᴜʀ ɢʀᴏᴜᴘ.**")
    else:
        await message.reply_text("**» ᴀʟʀᴇᴀᴅʏ ɪɴ ᴛʜᴇ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ.**")


@app.on_message(
    filters.command(UNAUTH_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def unauthusers(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ.**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        token = await int_to_alpha(user.id)
        deleted = await delete_authuser(message.chat.id, token)
        get = adminlist.get(message.chat.id)
        if get:
            if user.id in get:
                get.remove(user.id)
        if deleted:
            await message.reply_sticker("CAACAgUAAxkBAAIjQWKPXN20bTyku-xHuWi1piQjwfnqAALVBAACkG4oV_eRTF-VyhGfJAQ")
            return await message.reply_text("**» ʀᴇᴍᴏᴠᴇᴅ ꜰʀᴏᴍ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏꜰ ᴛʜɪs ɢʀᴏᴜᴘ.**")
        else:
            return await message.reply_text("**» ᴛᴀʀɢᴇᴛᴇᴅ ᴜsᴇʀ ɪs ɴᴏᴛ ᴀɴ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀ.**")
    user_id = message.reply_to_message.from_user.id
    token = await int_to_alpha(user_id)
    deleted = await delete_authuser(message.chat.id, token)
    get = adminlist.get(message.chat.id)
    if get:
        if user_id in get:
            get.remove(user_id)
    if deleted:
        await message.reply_sticker("CAACAgUAAxkBAAIjQWKPXN20bTyku-xHuWi1piQjwfnqAALVBAACkG4oV_eRTF-VyhGfJAQ")
        return await message.reply_text("**» ʀᴇᴍᴏᴠᴇᴅ ꜰʀᴏᴍ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏꜰ ᴛʜɪs ɢʀᴏᴜᴘ.**")
    else:
        return await message.reply_text("**» ᴛᴀʀɢᴇᴛᴇᴅ ᴜsᴇʀ ɪs ɴᴏᴛ ᴀɴ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀ.**")


@app.on_message(
    filters.command(AUTHUSERS_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
async def authusers(_, message: Message):
    _playlist = await get_authuser_names(message.chat.id)
    if not _playlist:
        return await message.reply_text("ɴᴏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.")
    else:
        j = 0
        mystic = await message.reply_text("» ғᴇᴛᴄʜɪɴɢ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ...")
        text = f"» ʟɪsᴛ ᴏғ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ɪɴ {message.chat.title} :\n\n"
        for note in _playlist:
            _note = await get_authuser(message.chat.id, note)
            user_id = _note["auth_user_id"]
            admin_id = _note["admin_id"]
            admin_name = _note["admin_name"]
            try:
                user = (await app.get_users(user_id)).first_name
                j += 1
            except:
                continue
            text += f"{j}➤ {user}[<code>{user_id}</code>]\n"
            text += f"   <b>↬ ᴀᴅᴅᴇᴅ ʙʏ :</b> {admin_name}[<code>{admin_id}</code>]\n\n"
        await mystic.delete()
        await message.reply_text(text)