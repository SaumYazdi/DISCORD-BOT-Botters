import discord
from discord.ext import commands

class User:
    def __init__(self, name, age, location, country, hobby):
        self.name = name
        self.age = age
        self.location = location
        self.country = country
        self.hobby = hobby

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

users = []  # Store user profiles

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")

@bot.command()
async def createprofile(ctx):
    await ctx.send("Welcome to Profile Creator! Please answer the following questions.")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send("What's your name?")
    name = await bot.wait_for("message", check=check)

    await ctx.send("How old are you?")
    age = await bot.wait_for("message", check=check)

    await ctx.send("Where are you from?")
    location = await bot.wait_for("message", check=check)

    await ctx.send("What country are you from?")
    country = await bot.wait_for("message", check=check)

    await ctx.send("What's your favorite hobby?")
    hobby = await bot.wait_for("message", check=check)

    user_profile = User(name.content, age.content, location.content, country.content, hobby.content)
    users.append(user_profile)

    await ctx.send(f"Profile Created:\nName: {user_profile.name}\nAge: {user_profile.age}\nLocation: {user_profile.location}\nCountry: {user_profile.country}\nHobby: {user_profile.hobby}")

@bot.command()
async def findsimilar(ctx):
    await ctx.send("Finding users with similar interests...")

    user_profile = users[-1]  # Get the last created user profile

    similar_users = []
    for user in users:
        if (
            user.hobby == user_profile.hobby
            and user.age == user_profile.age
            and user.location == user_profile.location
            and user.country == user_profile.country
            and user.name != user_profile.name
        ):
            similar_users.append(user)

    if similar_users:
        similar_names = ", ".join(user.name for user in similar_users)
        await ctx.send(f"Users with similar interests: {similar_names}")
    else:
        await ctx.send("No users with similar interests found.")

bot.run("BOT TOKEN")
