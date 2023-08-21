import discord
from discord.ext import commands
import pickle
import dotenv
import random
from datetime import date
from dotenv import load_dotenv
import requests
import urllib.parse
import os
from discord import Intents, Client, Interaction
from discord import app_commands 
import json

load_dotenv()

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
intents = discord.Intents.default()
intents = discord.Intents.all()
intents.message_content= True
bot = commands.Bot(command_prefix='!', intents=intents,heartbeat_timeout=60,case_insensitive=True)
class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@bot.event
async def on_ready():
    print('{0.user}がログインしました'.format(bot))
    count = len(bot.guilds)
    await bot.change_presence(activity=discord.Game(name="/info|サーバー数" + str(count), type=1))  
    invite_link = discord.utils.oauth_url(
        bot.user.id,
        permissions=discord.Permissions(administrator=True),
        scopes=("bot", "applications.commands")
    )
    print(f"Invite link: {invite_link}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1091715077398343740)
    if channel is None:
        return
    
    embed = discord.Embed(
        title="ようこそサーバーへ!",
        description=f"{member.mention}, さんサーバールールを確認して、楽しんでくださいね。",
        color=discord.Color.blue()
    )

    embed.set_thumbnail(url="https://github.com/rimycka/as/assets/95421757/6af587c5-59ce-435e-b073-9d781bf3c183")  # Replace with your image URL

    await channel.send(embed=embed)

    video_url = "\n[welcome_image](https://github.com/rimycka/as/assets/95421757/6af587c5-59ce-435e-b073-9d781bf3c183)"  # Replace with your video URL
    await channel.send(video_url)

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if message.content == 'こんにちは':
        responses = ['こんにちは', 'おはよう', 'こんばんは', 'お疲れ様です', '元気ですか？']  # Replace with your responses
        response = random.choice(responses)
        await message.channel.send(response)

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  # メッセージがボット自身からのものであれば無視
        return

    if message.channel.id != 1104046457373347932:  # チャンネルIDを指定
        return

    if 'とりあえず' in message.content:
        msg = await message.channel.send('私に返信してみてください')

    # ユーザーがボットのメッセージに対して返信を行った場合のみ反応
    if message.reference is not None and message.reference.message_id == msg.id:
        await message.channel.send('あなたが返信しましたね！')



last_draw = {}

@bot.command()
async def omikuji(ctx):
    user_id = ctx.author.id
    today = date.today()

    if user_id in last_draw and last_draw[user_id] == today:
        await ctx.send(f'{ctx.author.mention} すでに今日のおみくじを引いています。明日また来てください！')
    else:
        last_draw[user_id] = today
        fortune = ['大吉', '中吉', '吉', '小吉', '末吉', '凶', '大凶']
        result = random.choice(fortune)
        await ctx.send(f'{ctx.author.mention} おみくじの結果は... {result} です！')




@bot.listen('on_message')
async def on_message(message):
    if message.channel.id != 1104046457373347932:  # チャンネルIDを指定
        return
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if message.content == '好きな食べ物':
        responses = ['は、春です', 'なんだと思いますか？', '桜の花が咲く時期が好きですよ',]  # Replace with your responses
        response = random.choice(responses)
        await message.channel.send(response)

@bot.listen('on_message')
async def on_message(message):
    if message.channel.id != 1104046457373347932:  # チャンネルIDを指定
        return
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if message.content == '好きな季節':
        responses = ['は、春です', 'なんだと思いますか？', '桜の花が咲く時期が好きですよ',]  # Replace with your responses
        response = random.choice(responses)
        await message.channel.send(response)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1139414780608790559)
    await channel.send(f"{member.mention}がサーバーから脱退しました。\n[withdrawal_image](https://tenor.com/view/bocchi-bocchitherock-hitori-gotou-%E3%81%BC%E3%81%A3%E3%81%A1%E3%81%96%E3%82%8D%E3%81%A3%E3%81%8F-anime-gif-26895033)", )

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if bot.user in message.mentions:  # The bot was mentioned
        await message.channel.send('どうしましたか？')        

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  
        return

    if message.content == 'test':
        await message.channel.send('てすと')

@bot.hybrid_command(name="test", description="test")
async def testcommand(ctx):
    await ctx.send("test is done")

bot.remove_command("help")   
@bot.hybrid_command(name="help", description="bot使いを確認する")
async def help(ctx):
    embed = discord.Embed(title="Bot Commands", color=0x00ff00)
    embed.add_field(name="", value="プレイヤーは、chatterloungeのルールに同意した上で、サーバーに参加することができます。", inline=False)
    embed.add_field(name="", value="本サーバーのサービスにおいて利用されるプレイヤーは、本ルールを遵守する必要があります。", inline=False)
    embed.add_field(name="", value="プレイヤーが本ルールに違反した場合は、本ルールに定める各種の処罰なのでアクセスが禁止になることもあります。", inline=False)   
    embed.add_field(name="禁止行為", value="下記の行為すべてを禁止とします。", inline=False)
    embed.add_field(name="", value ="・不適切な画像(r18その他法に触れるもの等)", inline=False)
    embed.add_field(name="", value ="・不適切な発言(人種差別、暴言、悪口、その他法に触れるもの等)", inline=False)
    embed.add_field(name="", value ="・スパム(同じ内容を不必要に送信する行為等)", inline=False)
    embed.add_field(name="他はこちらのサーバーに聞いてください！", value ="https://discord.gg/tKBPhhZX7u", inline=False)
    
    await ctx.send(embed=embed)

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if message.content == 'ぼっち':
        responses = ['https://tenor.com/view/bocchi-bocchi-the-rock-anime-cringe-freak-out-gif-27026752', 'https://tenor.com/view/bocchitherock-bocchi-hitori-gotou-%E3%81%BC%E3%81%A3%E3%81%A1%E3%81%96%E3%82%8D%E3%81%A3%E3%81%8F-anime-gif-26998598', 'https://tenor.com/view/bocchi-the-rock-ikuyo-kita-bocchi-hitori-gotou-%E3%81%BC%E3%81%A3%E3%81%A1%E3%81%96%E3%82%8D%E3%81%A3%E3%81%8F-gif-26974910', 'https://tenor.com/view/bocchi-the-rock-oomfie-bocchi-the-rock-bocchi-shake-head-hitoribocchi-gif-27010676', 'https://tenor.com/view/bocchi-bocchi-the-rock-anime-hitori-gotou-you-wot-gif-27026760']  # Replace with your responses
        response = random.choice(responses)
        await message.channel.send(response)

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  
        return

    if message.content == 'きたーん':
        await message.channel.send('https://tenor.com/view/%E3%81%BC%E3%81%A3%E3%81%A1%E3%81%96%E3%82%8D%E3%81%A3%E3%81%8F-%E5%96%9C%E5%A4%9A%E9%83%81%E4%BB%A3-bocchi-the-rock-bothero-bozaro-gif-27262605')

@bot.listen('on_raw_reaction_add') #ボカロ
async def handle_reaction_add(payload):
    if payload.message_id != 1140286642846957719:
        return

    if str(payload.emoji) != '👍':
        return

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    role = discord.utils.get(guild.roles, id=1109814980229988413)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        return

    if role in member.roles:
        return

    await member.add_roles(role)

bot.remove_command("bokaro")   
@bot.hybrid_command(name="bokaro", description="うん")
async def help(ctx):
    embed = discord.Embed(title="ガジェット関係のチャンネルを視聴したい方はこちらのリアクションを選択", color=0x90bf) #😀 😱 🎧 
    embed.add_field(name="@ガジェット：😀 ", value=f" ", inline=False)
    embed.set_footer(text="made by nehatsu",
    icon_url="https://cdn.discordapp.com/avatars/1103934176916410428/80c07ac6b7ad0609543c9fa880e9ef1a.png")
    await ctx.send(embed=embed)

@bot.listen('on_raw_reaction_add') #音ゲー
async def handle_reaction_add(payload):
    if payload.message_id != 1140913631408689223:
        return

    if str(payload.emoji) != '🎧':
        return

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    role = discord.utils.get(guild.roles, id=1108732243993698326)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        return

    if role in member.roles:
        return

    await member.add_roles(role)

@bot.listen('on_raw_reaction_add') #技術
async def handle_reaction_add(payload):
    if payload.message_id != 1140945396466716672:
        return

    if str(payload.emoji) != '💻':
        return

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    role = discord.utils.get(guild.roles, id=1110919495897337896)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        return

    if role in member.roles:
        return

    await member.add_roles(role)

@bot.listen('on_raw_reaction_add') #ガジェット
async def handle_reaction_add(payload):
    if payload.message_id != 1140949652657688646:
        return

    if str(payload.emoji) != '😀':
        return

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    role = discord.utils.get(guild.roles, id=1115240705191858296)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        return

    if role in member.roles:
        return

    await member.add_roles(role)

poll_message = None
poll_options = {}
emoji_list = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']  # 10個までの選択肢に対応
emoji_option_mapping = {}

@bot.listen()
async def on_reaction_add(reaction, user):
    global poll_message, poll_options
    if user != bot.user and reaction.message == poll_message:
        if reaction.emoji in poll_options.keys():
            poll_options[reaction.emoji] += 1

@bot.listen()
async def on_reaction_remove(reaction, user):
    global poll_message, poll_options
    if user != bot.user and reaction.message == poll_message:
        if reaction.emoji in poll_options.keys():
            poll_options[reaction.emoji] -= 1

@bot.command()
async def createpoll(ctx, question, *options):
    global poll_message, poll_options, emoji_option_mapping
    if len(options) > 10:
        await ctx.send("回答は10個まで")
        return

    description = '\n'.join([f"{emoji_list[i]} : {option}" for i, option in enumerate(options)])
    embed = discord.Embed(title=question, description=description, color=0xffffff)
    poll_message = await ctx.send(embed=embed)

    poll_options = {emoji_list[i]: 0 for i in range(len(options))}
    emoji_option_mapping = {emoji_list[i]: options[i] for i in range(len(options))}
    for emoji in poll_options.keys():
        await poll_message.add_reaction(emoji)

@bot.command()
async def endpoll(ctx):
    global poll_message, poll_options, emoji_option_mapping
    embed = discord.Embed(title="結果！", description="\n".join([f"{emoji_option_mapping[option]}: {votes}" for option, votes in poll_options.items()]), color=0xffffff)
    await ctx.send(embed=embed)

global_channels = []
filename = 'global_channels.pkl'

@bot.event
async def on_ready():
    print('{0.user}がログインしました'.format(bot))
    count = len(bot.guilds)
    await bot.change_presence(activity=discord.Game(name="/info|サーバー数" + str(count), type=1))  
    invite_link = discord.utils.oauth_url(
        bot.user.id,
        permissions=discord.Permissions(administrator=True),
        scopes=("bot", "applications.commands")
    )
    print(f"Invite link: {invite_link}")

    global global_channels
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            global_channels_ids = pickle.load(f)
        for channel_id in global_channels_ids:
            channel = bot.get_channel(channel_id)
            if channel:
                global_channels.append(channel)
                

@bot.listen()
async def on_message(message):
    if message.author == bot.user or message.content.startswith('!'):
        return 

    if message.channel in global_channels:
        embed = discord.Embed(description=message.content, color=0xffffff)
        embed.set_author(name=f"{message.author.name}@{message.guild.name}", icon_url=message.author.avatar.url)

        # メッセージに添付ファイルがある場合、最初の添付ファイルを画像として埋め込みます
        if message.attachments:
            embed.set_image(url=message.attachments[0].url)

        for channel in global_channels:
            await channel.send(embed=embed)

@bot.listen()
async def on_message_delete(message):
    if message.author == bot.user:
        return
    if message.channel in global_channels:
        for channel in global_channels:
            if channel != message.channel:
                try:
                    msg = await channel.fetch_message(message.id)
                    await msg.delete()
                except discord.NotFound:
                    pass

@bot.command()
@commands.has_permissions(administrator=True)
async def touroku(ctx):
    if ctx.channel not in global_channels:
        global_channels.append(ctx.channel)
        with open(filename, 'wb') as f:
            pickle.dump([channel.id for channel in global_channels], f)
        await ctx.send("登録しました！")
    else:
        await ctx.send("既に登録されてます")

@bot.command()
@commands.has_permissions(administrator=True)
async def kaijyo(ctx):
    if ctx.channel in global_channels:
        global_channels.remove(ctx.channel)
        with open(filename, 'wb') as f:
            pickle.dump([channel.id for channel in global_channels], f)
        await ctx.send("登録を解除しました")
    else:
        await ctx.send("すでに解除されてます")

@bot.command()
async def saba(ctx):
    embed = discord.Embed(title="サーバー一覧", description="\n".join([channel.guild.name for channel in global_channels]), color=0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def syoukyo(ctx, member: discord.Member, limit: int):
    deleted = 0
    async for message in ctx.channel.history():
        if message.author == member:
            await message.delete()
            deleted += 1
            if deleted >= limit:
                break
    embed = discord.Embed(title="たぶんいい感じに削除されました", description=f"大体 {deleted} くらいのメッセージを削除しました。削除したユーザー名 {member.name}.", color=0x00bfff)
    await ctx.send(embed=embed)

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')  # 環境変数からAPIキーを読み込む

@bot.command()
async def kennsaku(ctx, *, query):
    # YouTube Data APIを使用して曲を検索
    response = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={query}&key={YOUTUBE_API_KEY}")
    data = json.loads(response.text)
    video = data['items'][0]
    title = video['snippet']['title']
    video_id = video['id']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    # 再生数と概要欄の取得は別のAPIリクエストが必要です

    embed = discord.Embed(title=title, url=video_url)
    # embed.add_field(name="再生数", value=再生数)
    # embed.add_field(name="概要", value=概要)
    await ctx.send(embed=embed)

@bot.command()
async def kasi(ctx, *, query):
    # Genius APIを使用して歌詞を検索
    response = requests.get(f"http://api.genius.com/search?q={query}&access_token=BP3SS6BFkviLcR0J6aPH2FsAhg9gMCusuBXEo_UINOQipI7HrZk9iLDi8ImS_Y4W")
    data = json.loads(response.text)
    song = data['response']['hits'][0]['result']
    song_title = song['title']
    # YouTube Data APIを使用して曲を検索
    response = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={song_title}&key={YOUTUBE_API_KEY}")
    data = json.loads(response.text)
    video = data['items'][0]
    title = video['snippet']['title']
    video_id = video['id']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    # 再生数と概要欄の取得は別のAPIリクエストが必要です

    embed = discord.Embed(title=title, url=video_url)
    # embed.add_field(name="再生数", value=再生数)
    # embed.add_field(name="概要", value=概要)
    await ctx.send(embed=embed)

token = os.getenv('DISCORD_TOKEN')

bot.run(token)
