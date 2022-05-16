from sqlite3 import Timestamp
from utils.helper import *
import time
import discord
from discord.ext import commands
from discord import guild, Embed
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from dotenv import load_dotenv

load_dotenv()
BOT_ID = os.getenv("BOT_ID")

servers = [681260962472656906]


driverpath = chromedriver_init.get_path()
driver = chromedriver_init.start(driverpath)


#bot stuff
client = commands.Bot(command_prefix='*')
slash = SlashCommand(client,sync_commands=True)
@client.event
async def on_ready():
    print("Bot online and ready.")

@slash.slash(
    name="lostsector",
    description='Checks current lost sector',
    guild_ids=servers
)
async def _lostsector(ctx:SlashContext):
    await ctx.defer()
    ls_dat = tid_lookup.LS()
    embed = Embed(title=ls_dat['sectorname'],description=ls_dat['desc'])
    embed.set_author(name='Lost Sector',icon_url='https://www.media.todayindestiny.com/images/headerIcon/lost_sector_legs.png')
    embed.add_field(name='Champions:',value=ls_dat['champs'])
    embed.add_field(name='Shield:',value=ls_dat['shield'])
    embed.add_field(name='Burn:',value=ls_dat['burn'])
    embed.add_field(name='Next Reset: ',value=ls_dat['time'],inline=False)
    file = discord.File("LS.png", filename="LS.png")
    embed.set_image(url="attachment://LS.png")
    await ctx.send(file=file,embed=embed)
    os.system('del LS.png')
@slash.slash(
    name='vog',
    description='Checks master VOG weapons',
    guild_ids=servers
)
async def _vog(ctx:SlashContext):
    await ctx.defer()
    vogdat = tid_lookup.VOG()
    embed = Embed(title='VAULT OF GLASS',description='Beneath Venus, evil stirs...')
    embed.set_author(name='Raid',icon_url='https://www.media.todayindestiny.com/images/headerIcon/raid.png')
    file = discord.File("vog.png", filename="vog.png")
    embed.set_image(url="attachment://vog.png")
    await ctx.send(file=file,embed=embed)
    os.system('del vog.png')
@slash.slash(
    name='nightfall',
    description='Checks nightfall drops and map',
    guild_ids=servers
)
async def _nightfall(ctx:SlashContext):
    await ctx.defer()
    nfdat=tid_lookup.NIGHTFALL()
    embed = Embed(title=nfdat['name'],description="The Vanguard seeks Guardians to undertake high-priority missions against the City's enemies.")
    embed.set_author(name='Nightfall',icon_url='https://www.media.todayindestiny.com/images/headerIcon/damage_type_void.png')
    file = discord.File("nf.png", filename="nf.png")
    embed.set_image(url="attachment://nf.png")
    await ctx.send(file=file,embed=embed)
    os.system('del nf.png')
client.run(BOT_ID)
