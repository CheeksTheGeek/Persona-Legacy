# BASIC_IMPORTS


from __future__ import print_function

import discord

from discord.ext import commands

import asyncio

from discord import Spotify

import emoji

import mysql.connector

from omdb import OMDBClient

import os

import random

import time

from discord import Member

import string as s

import asyncio

import requests

from jikanpy import Jikan

import binascii

import struct

from PIL import Image

import numpy as np

import scipy

import scipy.misc

import scipy.cluster

imdbx = OMDBClient(apikey="13fa8e20")

jikan = Jikan()


# DEFINING_DICTIONARY_CLASS_AND_INITIALIZE
class DictLikeClass:

    def __init__(self):

        super(DictLikeClass, self).__init__()
    def __getitem__(self, key):
        return getattr(self, key)
    def __setitem__(self, key, value):

        setattr(self, key, value)

d = DictLikeClass()

d["id"] = 0

d["channel"] = 0

d["guild"]=0



d2 = DictLikeClass()

d2["id"] = 0



d2["channel"] = 0



d2["guild"]=0



# BEGIN_OF_COG



class animecommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



 # HELP_COMMAND_TO_DM_LIST_OF_ALL_THE_COMMANDS



@commands.command()

async def help(self,ctx):
    embed = discord.Embed(title="Help",description="Help For Persona Bot",color=3800852)

    embed.add_field(name="1. .join" , value="> ``Joins the vc user is currently in``",inline=False)

    embed.add_field(name="2. .leave" , value="> ``Leaves the vc an clears the queue``",inline=False)

    embed.add_field(name="3. .play(.p) [url/song_name]", value="> ``Plays the given song using youtube``",inline=False)
    embed.add_field(name="4. .pl [yt_playlist_url]" , value="> ``Gets the playlist using youtube url``",inline=False)

    embed.add_field(name="5. .sp [spotify_playlist_url]" , value="> ``Gets the playlist using spotify url``",inline=False)
    embed.add_field(name="6. .pause" , value="> ``Pauses the song currently playing``",inline=False)

    embed.add_field(name="7. .resume" , value="> ``Resumes the song currently playing``",inline=False)

    embed.add_field(name="8. .skip" , value="> ``Skips the song currently playing``",inline=False)

    embed.add_field(name="9. .move [song_position_1 song_position_2" , value="> ``Swaps the position of   the
    two songs given ``",inline=False)

    embed.add_field(name="10. .shuffle" , value="> ``Shuffles the playlist``",inline=False)

    embed.add_field(name="11. .loop" , value="> ``Toggles the song loop``",inline=False)

    embed.add_field(name="12. .nowplaying (.np)" , value="> ``Shows the status of the song currently
    playing``",inline=False)

    embed.add_field(name="13. .queue(.q) [queue_page_number (writing nothing shows first page)]" ,
    value="> ``Shows the list of songs in queue`",inline=False)

    embed.add_field(name="14. .stop" , value="> ``Stops the current song playing and removes all the    songs
    from the queue``",inline=False)



    embed.set_author(name="Persona Bot",icon_url=self.bot.user.avatar_url)

    embed.set_footer(text="Requested By:"+str(ctx.author),icon_url=ctx.author.avatar_url,)

    await ctx.author.send(embed=embed)

    await ctx.send("Help Commands Sent In DM ")



 # GETTING_DATA_OF_MOVIE/SERIES_FROM_IMDB

 @commands.command()

 async def imdb(self,ctx,*,strx:str):

 print(strx)

 movie=imdbx.get(title=strx)

 # await ctx.send(movie['title'])

 # await ctx.send(movie['imdb_rating'])

 # await ctx.send(movie['plot'])

 # await ctx.send(movie['year'])

 # await ctx.send(movie['poster'])

 typex=movie['type'].title()



 embed=discord.Embed(title=f"{movie['title']}({typex})",color=16711708)

 embed.set_thumbnail(url=movie['poster'])

 embed.add_field(name="Rating", value=movie['imdb_rating'], inline=True)

 embed.add_field(name="Release Date", value=movie['released'], inline=True)

embed.add_field(name="Length", value=movie['runtime'], inline=True)

 embed.add_field(name="Director(s)", value=movie['director'], inline=False)
embed.add_field(name="Actors", value=movie['actors'] , inline=False)

 embed.add_field(name="Plot", value=movie['plot'], inline=False)

 await ctx.send(embed=embed)




 # ADDING_ALIAS_TO_WALLPAPER_FOLDERS

 @commands.command()

 async def addalias(self,ctx,*,rep):

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031', database='discord')

cursor = db.cursor()

 cursor.execute("select name,alias from list")

 results = cursor.fetchall()

 Z=[]

 for i in range(len(results)):

 # print(results[i][0],results[i][1])

 if rep.lower() in str(results[i][0]).lower() or rep in str(results[i][1]).lower():

Z.append(results[i])

 print(Z)

 if len(Z)>1:

 msg=await ctx.send("Please Be More Specific")

 await asyncio.sleep(4)

 await msg.delete()

 return

 strx="update list set alias= "

 print(Z)

 if Z[0][1]==None:

 # al=input("Enter Alias")

 await ctx.send(f"Enter the alias for: {Z[0][0]} or type exit to exit")

print("entering alias")

 def check(m):

 return m.author == ctx.message.author and m.channel == ctx.message.channel   msg = await

self.bot.wait_for('message',check=check,timeout=30)

 al=str(msg.content)

 if al.lower=="exit":
 await ctx.send("Exited Succesfully")
 return

 print(al)

 strx+=f"'{al}' where name='{Z[0][0]}'"

 else:

 # al=input("Enter Alias")

 await ctx.send(f"Enter the alias for: {Z[0][0]} or type exit to exit")   def

check(m):

 return m.author== ctx.message.author and m.channel == ctx.message.channel      msg = await

self.bot.wait_for('message',check=check,timeout=30)

 al=str(msg.content)



 if al.lower=="exit":

 await ctx.send("Exited Succesfully")

 return

 print("message received")

 print(al)

 al=al+" "+Z[0][1]

 strx+=f"'{al}' where name='{Z[0][0]}'"

 print(strx)

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031', database='discord')

cursor = db.cursor()

 cursor.execute(strx)

 await ctx.send(f"Alias {al} added to {Z[0][0]} ")

 db.commit()

 db.close()



 # WALLPAPER_COMMAND



 @commands.command(aliases=['a'])

 async def anime(self,ctx,*,rep=None):



 if rep!=None:

 if len(rep)<3:

 await ctx.send("You just wanna break my bot don't you")

 return

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031', database='discord')
 cursor = db.cursor()
 cursor.execute("select name,alias from list")

 results = cursor.fetchall()

 L=[]

 Repeat=[]



  try:

 if rep==None:

 await ctx.send("`The Correct Syntax Is $anime [animename]`")   return




 fetching=await ctx.send("**Fetching The Wallpaper** <a:loading:715841171540279306> ")   if

rep=="random" or rep=="Random":

 lenl=len(results)

 rand=random.randint(0,lenl)

 rep=results[rand-1][0]

 print(rep,"rep")

 for i in range(len(results)):

 if str(results[i][1])!="None":

 x=str(results[i][0])+"__"+(results[i][1])

 y=x.lower()

 z=str(results[i][0]).lower()

 else:

  x=str(results[i][0])

 y=x.lower()

 z=y




 if str(rep).lower() in y :

 print(x,str(rep))

 rep=x.split("__")[0]

 record=i

 print(record,"record")

 print(rep)

 z=z.split("__")[0]

 Repeat.append(z)
 # print("Hello")

 print(Repeat)
 if len(Repeat)>1:

 repstr=""



 for i in range(len(Repeat)):

 zenn=Repeat[i]

 zenn=s.capwords(zenn)

 repstr=repstr+" ** "+ str(i+1)+". "+zenn+" **\n \n"

 embed = discord.Embed(title=" There Are 2 Or More Anime With The Same Word In It \nPlease   Give the Number
Along the Anime Name which you wanted to specify: \n",description=repstr, color=16711708)

 embed.set_author(name=self.bot.user.name,icon_url=self.bot.user.avatar_url)



 msg2=await ctx.send(embed=embed)

 # await ctx.send(repstr)

 channel = ctx.channel

 print(channel)

 def check(m):

 return m.content.isnumeric() and m.channel == channel and ctx.author == m.author   msg = await

self.bot.wait_for('message',check=check,)



 x=(msg.content)

 print(x)

 recordx=Repeat[int(x)-1]

 print(recordx)

 # recordx=str(L[record])

 dirx=r"C:\\Users\\aakas\\Desktop\\Discord Wallpaper"+"\\" + str(recordx)   onlyfiles =

next(os.walk(dirx))[2]

 x=(len(onlyfiles))

 num=random.randint(1,x)

 name=str(num)+".jpg"

 dirx=dirx+"/"+str(num)+".jpg"



 colour = "07c4e1"

 msg3=(f"{s.capwords(recordx)}")

 file = discord.File(dirx, filename=name)
 embed = discord.Embed(title=msg3,color=int(colour,16))

 embed.set_footer(text="Requested By:"+str(ctx.author),icon_url=ctx.author.avatar_url,)

embed.set_image(url=f"attachment://{name}")
 await ctx.send(file=file, embed=embed)

 await fetching.delete()

 await msg2.delete()

 print(rep)




 elif len(Repeat)==1:

 print(x)

 print(L)

 print(record)

 rep=rep.split("__")[0]

 print("Rep:",rep)



 # recordx=str(L[record])

 dirx=r"C:\\Users\\aakas\\Desktop\\Discord Wallpaper"+"\\" + rep   print(dirx)

 onlyfiles = next(os.walk(dirx))[2]

 x=(len(onlyfiles))

 num=random.randint(1,x)

 name=str(num)+".jpg"

 dirx=dirx+"/"+str(num)+".jpg"

 print(dirx)

 try:



 NUM_CLUSTERS = 3

 im = Image.open(dirx)

 im = im.resize((350, 350))

 ar = np.asarray(im)

 shape = ar.shape

 ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)   codes, dist =

scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

 vecs, dist = scipy.cluster.vq.vq(ar, codes)

 counts, bins = scipy.histogram(vecs, len(codes))
 index_max = scipy.argmax(counts)

 peak = codes[index_max]

 colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')   if

int(colour,16)>16777215:
 colour = "07c4e1"

 except:

 colour="07c4e1"

 msg3=(f"{s.capwords(rep)}")

 file = discord.File(dirx, filename=name,)

  embed = discord.Embed(title=msg3,color=int(colour,16))

 embed.set_footer(text="Requested By:"+str(ctx.author),icon_url=ctx.author.avatar_url,)

embed.set_image(url=f"attachment://{name}")

 await ctx.send(file=file, embed=embed)

 await fetching.delete()

 print(rep)

 elif rep==None:

 ctx.send("The Correct Syntax Is $anime [animename]")

 else:

 print("Hello")

 print(rep)

 request= str(ctx.guild)+" : #"+str(ctx.channel)+" : "+str(ctx.author)+" --> "+str(rep)

print(request)

 with open('animerequest.txt','a',encoding="utf-8") as p:

 p.write(request)

 p.write("\n")

 p.close()

 await fetching.delete()

 await ctx.send("Anime Doesn't Exist \nThis Anime Will Be Added Soon...")




 except Exception as E:

 raise E



 # SYNC_THE_DATABASE_TO_ALL_THE_FOLDERS_FOR_WALLPAPER



 @commands.command()
 async def sync(self,ctx):

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031', database='discord')   L=[]

 lis=[]

 cursor = db.cursor()
 cursor.execute("select name from list")

 results = cursor.fetchall()

 start=len(results)

 for i in results:

 L.append(i[0])

 strx="insert into list(sno,name) values "

 print(L)



 for i,j,y in os.walk(r"C:\\Users\\aakas\\Desktop\\Discord Wallpaper\\"):

 print(j)

 if j!=[]:

 lis=j

 print("Hello")

 print(lis)

 for i in lis:

  if i not in L:

 print(i)

 start+=1

 strx+=f"({start},'{i}'),"

 print(strx.rstrip(","))

 if strx!="insert into list(sno,name) values ":

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031', database='discord')   cursor =

db.cursor()

 cursor.execute(strx.rstrip(","))

 db.commit()



 # LIST_OF_ALL_THE_ANIME_IN_THE_DATABASE_IN_A_SCROLLABLE_FORMAT

 @commands.command(aliases=['al'])

 async def animelist(self,ctx,a :int=1):

 print("starting")

 if d["id"]!=0 and d["channel"]==ctx.channel and d["guild"]==ctx.guild.id:

 print(id)
 xid=d["id"]

 msg = await ctx.fetch_message(xid)

 await msg.delete()

 d["id"]=0
 elif d["id"]!=0 and d["channel"]!=ctx.channel and d["guild"]!= ctx.guild.id:

d["channel"]=ctx.channel

 d["guild"]=ctx.guild.id

 z=0

 m=0

 while m!=123456:

 z+=1

 print(ctx.channel)

 page = (10*(a-1))+1

 b=a

 NO=[]

 NAME=[]

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031', database='discord',   )

 cursor = db.cursor()

 cursor.execute("select * from list order by name asc")

 results = cursor.fetchall()

 k=1

 for x in results:

 print(x)

 NO.append(k)

 NAME.append(x[1])

 k+=1



 num = len(NO)

 print(num)

 print(len(NAME))




 strxx=""

 rem = len(NO)%10

 if rem!=0:

 rem = len(NO)//10+1

 else:
 rem = len(NO)//10

 pagenumber=(' Page {}/{}'.format(a,rem))

 print(page+9)

 print(len(NO)+1)
 if (page+9) >= (len(NO)):



 for i in range(page-1,(len(NO))):



 repx=NAME[i]



 dirx=r"C:\\Users\\aakas\\Desktop\\Discord Wallpaper\\" + str(repx)

 onlyfiles = next(os.walk(dirx))[2]



 x=(len(onlyfiles))

 strxx=strxx+"\n \n"+str(NO[i])+"--->"+str(NAME[i]+"["+str(x)+"]")    else:

 for i in range(page-1,(page+9)):

 repx=NAME[i]



 dirx=r"C:\\Users\\aakas\\Desktop\\Discord Wallpaper\\" + str(repx) +"/"



 onlyfiles = next(os.walk(dirx))[2]

 # print(onlyfiles)



 x=(len(onlyfiles))

 strxx=strxx+"\n \n"+str(NO[i])+"--->"+str(NAME[i]+"["+str(x)+"]")    embed =

discord.Embed(title="Anime List",description=strxx, color=16711708)

embed.set_author(name=self.bot.user.name,icon_url=self.bot.user.avatar_url)

embed.set_footer(text=pagenumber,icon_url=ctx.author.avatar_url,)



 if z==1:

 msg = await ctx.send(embed=embed)

 message=ctx.message

 channel=ctx.message

 await message.delete()

 d["id"]= msg.id
 d["channel"]=msg.channel

 d["guild"]=msg.guild.id



 else:

 if d["id"]!=0 and d["guild"]==ctx.guild.id:

 msg2 = await msg.edit(embed=embed)
 if z==1:

 await msg.add_reaction('<a:left_arrow:712339584796852324>')

 await msg.add_reaction("<a:right_arrow:712339647333793903>")

 def check(reaction, user):

 return user == ctx.author and str(reaction.emoji) == ' ',

 try:

 reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=check)   except

asyncio.TimeoutError:

 if d["id"]!=0 and d["guild"]==ctx.guild.id:

 # message=ctx.message

 d["channel"]=ctx.channel

 d["guild"]=msg.guild.id

 await msg.delete()

 # await message.delete()

 # await message.delete()

 d["id"]=0

 break



 else:

 if self.bot.user!=user and user==ctx.author:

 if str(reaction) == "<a:right_arrow:712339647333793903>":

 print(rem,"rem")

 if a==rem:

 a=0

 if a<=rem-1:

 a=a+1

 await msg.remove_reaction("<a:right_arrow:712339647333793903>",ctx.author)   elif str(reaction)==

'<a:left_arrow:712339584796852324>':   if a==1:

 a=rem+1

 if a>=2:

 a=a-1

 await msg.remove_reaction('<a:left_arrow:712339584796852324>' ,ctx.author)



# GETS_INFO_ABOUT_AN_ANIME_WITH_SCROLLABLE_INFO_ABOUT_SEQUAL_AND_PREQUEL
 @commands.command()

 async def manime(self,ctx,*,rep):



 print("it works")

 if d2["id"]!=0 and d2["channel"]==ctx.channel and d2["guild"]==ctx.guild.id:

xid=d2["id"]

 msg = await ctx.fetch_message(xid)

 await msg.delete()

 d2["id"]=0

 elif d2["id"]!=0 and d2["channel"]!=ctx.channel and d2["guild"]!= ctx.guild.id:

d2["channel"]=ctx.channel

 d2["guild"]=ctx.guild.id

 msg=await ctx.send("**Loading** <a:loading:715841171540279306>")

 z=0

 L1=(jikan.search('anime',rep))

 id=(L1["results"][0]["mal_id"])

 id1=id

 id2=id

 while True:

 z+=1

 L2=(jikan.anime(id))

 rating=L2['rating']

 title=(L2['title'])

 status=L2['status']

 genres2=L2['genres']

 if 'Prequel' in dict.keys(L2['related']):

 prequel=L2['related']['Prequel'][0]['mal_id']

 Prequel=L2['related']['Prequel'][0]['name']

 else:

 prequel=None
 if 'Sequel' in dict.keys(L2['related']):

 sequel=L2['related']['Sequel'][0]['mal_id']

 Sequel=L2['related']['Sequel'][0]['name']

 else:

 sequel=None

 genresx=""
 for i in genres2:

 cat=(i['name'])

 if i['name']!=genres2[len(genres2)-1]['name']:

 genresx += cat + " **|** "

 else:

 genresx += cat

 synopsis=L2['synopsis'][:346]+"... Read More On The MAL SITE"



 if L2['airing']==True:

 airing="airing"

 else:

 airing="not airing"

 url=L2['url']

 episodes=L2['episodes']

 type=L2['type']

 image_url=L2['image_url']

 duration=L2["duration"]

 score=L2['score']

 rank=L2['rank']

 trailer_url=L2['trailer_url']

 strx="[{}]({})".format("Watch The trailer",trailer_url)    embed =

discord.Embed(title=title,url=url,color=0xeee657)

embed.set_thumbnail(url=image_url)

 embed.add_field(name="Type", value=type, inline=True)

embed.add_field(name="Episodes", value=episodes, inline=True)

embed.add_field(name="Status", value=status, inline=True)

embed.add_field(name="Episodes Duration", value=duration, inline=True)

embed.add_field(name="Score", value=score, inline=True)

embed.add_field(name="Rank", value=rank, inline=True)     embed.add_field(name="Age

Rating", value=rating, inline=False)

 embed.add_field(name="Genres", value=genresx, inline=True)

 embed.add_field(name="Description", value=synopsis, inline=False)

 if prequel:

 embed.add_field(name="Prequel", value=Prequel, inline=True)

 if sequel:
 embed.add_field(name="Sequel", value=Sequel, inline=True)

 embed.add_field(name="Trailer", value=strx, inline=False)

 embed.set_author(name=self.bot.user.name,icon_url=self.bot.user.avatar_url)

embed.set_footer(text="Requested By:"+str(ctx.author),icon_url=ctx.author.avatar_url,)



 if z==1:

 msg4 = await ctx.send(embed=embed)

 embed2=embed

 # print(msg4)

 await msg.delete()

 message=ctx.message

 await message.delete()

 d2["id"]= msg4.id

 d2["channel"]=msg4.channel

 d2["guild"]=msg4.guild.id

 else:

 if editx=="yes":

 print(prequel)

 if d2["id"]!=0 and d2["guild"]==ctx.guild.id:

 msgxx=await msg4.edit(embed=embed)



 if z==1:

 editx="no"

 await msg4.add_reaction('<a:left_arrow:712339584796852324>')

 await msg4.add_reaction("<a:right_arrow:712339647333793903>")

 def check(reaction, user):

 return user == ctx.author and (str(reaction.emoji) == '<a:left_arrow:712339584796852324>' or
str(reaction.emoji)== '<a:right_arrow:712339647333793903>')

 reaction, user = await self.bot.wait_for('reaction_add',check=check)

 if self.bot.user!=user and user==ctx.author:

 if str(reaction) == '<a:right_arrow:712339647333793903>':

 if sequel!=None:

 if id!= sequel:
 id = sequel

 editx="yes"

 else:

 editx="no"
 await msg4.remove_reaction('<a:right_arrow:712339647333793903>',ctx.author)



 elif str(reaction)== '<a:left_arrow:712339584796852324>':



 if prequel!=None:

 if id!=prequel:

 id = prequel

 editx="yes"

 else:

  editx="no"



 await msg4.remove_reaction('<a:left_arrow:712339584796852324>' ,ctx.author)



 @animelist.error

 async def animelist_error(self, ctx, error):

 if isinstance(error, commands.BadArgument):

 await ctx.send("You need to enter a integer after `$animelist`")



# DEFINING_THE_COG



def setup(bot):

 bot.add_cog(animecommands(bot))

