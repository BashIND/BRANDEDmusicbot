from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from ZexxOp import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bc732461b0a5f8481a0c1.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐃𝐌 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦋⃝🇮🇳⃝𓆩 ❛⚔️🇸𝐇𝐈𝐕⚔️𐀔𖣔ꠋꠋ ‌ٖٖ𝐗𝐃?", url=f"https://t.me/xx_Zexx_xx")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bc732461b0a5f8481a0c1.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐃𝐌 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦋⃝🇮🇳⃝𓆩 ❛⚔️🇸𝐇𝐈𝐕⚔️𐀔𖣔ꠋꠋ ‌ٖٖ𝐗𝐃?", url=f"https://t.me/xx_Zexx_xx")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bc732461b0a5f8481a0c1.jpg",
        caption=f"""🎧𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐌𝐘 𝐑𝐄𝐏𝐎🎧""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👉𝐆𝐎 𝐇𝐄𝐑𝐄👈", url=f"https://t.me/xx_Zexx_xx")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bc732461b0a5f8481a0c1.jpg",
        caption=f"""🎧𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐌𝐘 𝐑𝐄𝐏𝐎🎧""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👉𝐆𝐎 𝐇𝐄𝐑𝐄👈", url=f"https://t.me/xx_Zexx_xx")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bc732461b0a5f8481a0c1.jpg",
        caption=f"""🎧𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐌𝐘 𝐑𝐄𝐏𝐎🎧""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👉𝐆𝐎 𝐇𝐄𝐑𝐄👈", url=f"https://t.me/xx_Zexx_xx")
                ]
            ]
        ),
    )
