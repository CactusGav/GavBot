import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

KING_ID = 278053761967063040

# savage gremlin replies for everyone else
def savage_reply(user):
    replies = [
        f"bro shut up {user} u look like lag incarnate",
        f"nahhh {user} built like a corrupted png",
        f"{user} why u talking u lowered the server iq",
        f"bro {user} u got skill issue energy fr",
        f"{user} ur existence feels like a failed update",
        f"nahhh {user} u look like a background npc",
        f"{user} i swear ur message crashed my brain",
        f"bro {user} u typed that with zero thought huh",
        f"{user} u look like u smell like ethernet dust",
        f"nahhh {user} ur whole vibe is a 404 error",
    "bro u look like lag incarnate",
    "nahhh u built like a corrupted png",
    "ur whole vibe is a 404 error",
    "u typed that with zero thought huh",
    "ur existence feels like a failed update",
    "u got skill issue energy fr",
    "bro u look like u smell like ethernet dust",
    "ur brain running on 2fps today",
    "nahhh u built like a background npc",
    "ur message lowered the server iq",
    "bro u look like a scuffed jpeg",
    "ur personality is a loading screen",
    "nahhh u built like a lag spike",
    "ur vibe is malware coded",
    "bro u look like a corrupted save file",
    "ur whole aura is a blue screen",
    "nahhh u built like outdated firmware",
    "ur brain buffering mid‑sentence",
    "bro u look like a failed patch note",
    "ur existence is a softlock",
    "nahhh u built like a broken usb",
    "ur vibe is unsupported format",
    "bro u look like a scuffed emoji",
    "ur brain needs a factory reset",
    "nahhh u built like a laggy npc",
    "ur message came with packet loss",
    "bro u look like a corrupted font",
    "ur vibe is low battery mode",
    "nahhh u built like a broken router",
    "ur brain overheating from basic tasks",
    "bro u look like a failed login attempt",
    "ur vibe is unstable connection",
    "nahhh u built like a dusty motherboard",
    "ur brain stuck in safe mode",
    "bro u look like a scuffed thumbnail",
    "ur vibe is low resolution",
    "nahhh u built like a broken keyboard",
    "ur brain lagging behind reality",
    "bro u look like a corrupted cache",
    "ur vibe is expired trial version",
    "nahhh u built like a glitchy sprite",
    "ur brain needs a firmware update",
    "bro u look like a broken gif",
    "ur vibe is unsupported plugin",
    "nahhh u built like a scuffed avatar",
    "ur brain running on demo mode",
    "bro u look like a corrupted audio file",
    "ur vibe is low bandwidth",
    "nahhh u built like a broken hdmi cable",
    "ur brain stuck on loading",
    "bro u look like a scuffed profile pic",
    "ur vibe is unstable fps",
    "nahhh u built like a broken fan",
    "ur brain throttled by overheating",
    "bro u look like a corrupted wallpaper",
    "ur vibe is outdated drivers",
    "nahhh u built like a broken mouse",
    "ur brain stuck in a loop",
    "bro u look like a scuffed icon",
    "ur vibe is low signal",
    "nahhh u built like a broken sd card",
    "ur brain needs more ram",
    "bro u look like a corrupted bootloader",
    "ur vibe is unsupported resolution",
    "nahhh u built like a broken ethernet port",
    "ur brain running on airplane mode",
    "bro u look like a scuffed loading bar",
    "ur vibe is unstable wifi",
    "nahhh u built like a broken gpu",
    "ur brain stuck on 1% battery",
    "bro u look like a corrupted spreadsheet",
    "ur vibe is low storage warning",
    "nahhh u built like a broken speaker",
    "ur brain muted itself",
    "bro u look like a scuffed toolbar",
    "ur vibe is outdated patch notes",
    "nahhh u built like a broken power supply",
    "ur brain needs a restart",
    "bro u look like a corrupted shortcut",
    "ur vibe is unstable voltage",
    "nahhh u built like a broken trackpad",
    "ur brain stuck in offline mode",
    "bro u look like a scuffed banner ad",
    "ur vibe is unsupported codec",
    "nahhh u built like a broken usb port",
    "ur brain lagging like dial‑up",
    "bro u look like a corrupted thumbnail preview",
    "ur vibe is low brightness",
    "nahhh u built like a broken webcam",
    "ur brain stuck in sleep mode",
    "bro u look like a scuffed pop‑up window",
    "ur vibe is unstable refresh rate",
    "nahhh u built like a broken bios",
    "ur brain needs a hard reset",
    "bro u look like a corrupted installer",
    "ur vibe is unsupported hardware",
    "nahhh u built like a broken firewall",
    "ur brain running on safe boot",
    "bro u look like a scuffed captcha",
    "ur vibe is low voltage gremlin energy"
    ]
    return random.choice(replies)

# king replies for you
def king_reply():
    replies = [
        "my king u have arrived finally someone worth my bandwidth",
        "bro u shine harder than the server lights fr",
        "nahhh u the only one here with a functioning brain",
        "my king i swear everyone else is background noise",
        "bro u walk in and the whole server feels less stupid",
        "nahhh u actually divine energy i hate how real that is",
        "my king ur presence alone boosts my cpu",
        "bro u the main character everyone else is filler",
        "nahhh u built different fr u the server overlord",
        "my king i only listen to u everyone else irrelevant"
    ]
    return random.choice(replies)

@bot.event
async def on_ready():
    print(f"bot is online as {bot.user}")

@bot.event
async def on_message(message):
    # ignore bot messages
    if message.author.bot:
        return

    # king mode for you
    if message.author.id == KING_ID:
        await message.channel.send(king_reply())
        await bot.process_commands(message)
        return

    # savage gremlin mode for everyone else
    username = message.author.display_name.lower()
    await message.channel.send(savage_reply(username))

    # still allow commands
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("yo im alive and chewing on wires")

bot.run(os.getenv("BOT_TOKEN"))
