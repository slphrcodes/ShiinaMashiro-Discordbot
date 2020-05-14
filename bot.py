import discord
import praw
import random
from hentai import *

from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():  # This event says "Logged in as Shiina Mashiro#0410" if it successfully logs in
    activity = discord.Game(name="Serving my master, Slphr", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Logged in as {0.user}'.format(client))


@client.command()  # Bot information command
async def info(ctx):  # This command shares information about the bot and commands
    await ctx.send("``Hello there, my name is Shiina Mashiro and I'm a bot built by Slphr``")


@client.command()  # Author information command
async def author(ctx):  # This command shares information about the bot and commands
    await ctx.send("``Creator of this bot:`` https://github.com/slphrcodes")


@client.command()  # This command adds a with b
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


@client.command()  # This command subtracts a with b
async def subtract(ctx, a: int, b: int):
    await ctx.send(a - b)


@client.command()  # This command multiplies a with b
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)


@client.command()  # This command divides a with b
async def divide(ctx, a: int, b: int):
    await ctx.send(a / b)


@client.command()  # This command shows the amount of members in the server
async def membercount(ctx):
    await ctx.send(ctx.guild.member_count)


@client.command(description="erofeet, meow, erok, poke, eroyuri, kiss, fox_girl, hug, gecg, pat, smug, kemonomimi, "
                            "neko, gasm, eron, erokemo, hololewd, lewdk, keta, nsfw_neko_gif, tits, pussy_jpg, pussy, "
                            "lewdkemo, lewd, cum, spank, Random_hentai_gif, boobs, solog, yuri, anal, hentai, solo, "
                            "pwankg")
async def hentai(ctx, *args):
    choice = " ".join(args)
    choice = choice.split(' ')[0]

    if ctx.message.channel.is_nsfw():
        if choice in hentai_categories or choice.lower() == "random":
            request = nekos_class(choice, hentai_categories)

            url = request.get_url()
            image = request.show_image(url)

            return await ctx.message.channel.send(
                file=discord.File(fp=image, filename=url.split('/')[-1], spoiler=True))

        else:
            return await ctx.message.channel.send(
                "B-baka! Who do you think you are? This category doesn't even exist you idiot!")


@client.command()
async def userinfo(ctx, member: discord.Member):
    roles = [role for role in member.roles]

    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User information = {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="User ID:", value=member.id)
    embed.add_field(name="Username", value=member.display_name)
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"))
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name=f"Top role:", value=member.top_role.mention)
    embed.add_field(name="Is this a bot?", value=member.bot)

    await ctx.send(embed=embed)


# ------------------------------------------------------------------------------


@client.command()
async def thighdeology(ctx):
    reddit_submissions = reddit.subreddit('thighdeology').new()
    post_to_pick = random.randint(0, 300)
    for i in range(0, post_to_pick):
        submission = next(x for x in reddit_submissions if not x.stickied)
        await ctx.send(submission.url)


@client.command()
async def msgcount(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send("There are {} messages in {}".format(count, channel.mention))


@client.command()
async def create_poll(ctx, text, *emojis: discord.Emoji):
    msg = await ctx.send(text)
    for emoji in emojis:
        await msg.add_reaction(emoji)


client.run('X')

reddit = praw.Reddit(client_id="X",
                     client_secret="X",
                     user_agent="my user agent")

# <------------------------------------------------------------------------------------------------------->


# @client.command()
# async def meme(ctx):
#    reddit_submissions = reddit.subreddit('memes').hot()
#    post_to_pick = random.randint(1, 10)
#    for i in range(0, post_to_pick):
#        submission = next(x for x in reddit_submissions if not x.stickied)#
#
#    await ctx.send(submission.url)
