import discord
from discord.ext import commands
import sqlite3 as sq
from datetime import *
conn=sq.connect("bot.dbs")
c=conn.cursor()
c.execute("""create table if not exists info
  (id integer primary key autoincrement, pseudo text)""")




client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot prêt !')
    activity = discord.Game(name="...Chargement", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)



@client.command(aliases=['add'])
async def Add(ctx, arg):
  now = str(datetime.now())
  c.execute("""insert into info (pseudo, now) values (?, ?);""", (arg, now))
  conn.commit()
  await ctx.send("Vous avez bien été rajouter à la base de donnée")
  print("Commande .add à été éxecuter " + str(datetime.now()))



@client.command(aliases=['resultas'])
async def result(ctx):
  c.execute("""select * from info""")
  item=c.fetchall()
  for items in item:
      await ctx.send(items)

      
  print("Commande .result à été éxecuter " + str(datetime.now()))

@client.command()
async def bddoff(ctx):
  conn.close()
  await ctx.send("Base de donées fermer avec succès !")
  print("Commande .bddoff à été éxecuter " + str(datetime.now()))


client.run('MTAxMDIxNDE2Nzk4NDIyMjI0OA.GpZycu.2w7PkJBl81PcP1Q6wng7yXtkizlzptyaPKSEOU')
