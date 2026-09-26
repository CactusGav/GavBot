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
        f"nahhh {user} ur whole vibe is a 404 error"
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
