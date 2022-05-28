#BASIC_IMPORTS

import discord

from discord.ext import commands

import asyncio

import emoji

import mysql.connector

import random

import time

from discord import Member

import string as s

import asyncio

from jikanpy import Jikan

from wallhaven import Wallhaven

import os



prejectx={}

prejectx['channel']=None

class project(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
    
@commands.command()

async def project(self,ctx):

    channel=ctx.message.channel

    prejectx['channel']=channel

    prejectx['author']=ctx.message.author



#MENU_FOR_THE_PROJECT



async def menu():

    channel=prejectx['channel']
    c="y"

    while (c=="Y" or c=="y"):

        ch="n"

        menustr='''``` MENU\n=========================\n1. Access Level Records\n2.   Enter New Records\n3. Update Records\n4. Delete Records\n5. Export Records\n6. Exit```'''

        msg1=await channel.send(menustr)

    await msg1.add_reaction("1️⃣")

    await msg1.add_reaction("2️⃣")

    await msg1.add_reaction("3️⃣")

    await msg1.add_reaction("4️⃣")

    await msg1.add_reaction("5️⃣")

    await msg1.add_reaction("6️⃣")

    emoji=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']
    def check(reaction, user):

        return user == ctx.author and (str(reaction.emoji) in emoji)   
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0,check=check)   except

            asyncio.TimeoutError:

    await channel.send("You took too long to respond")

    return

 if self.bot.user!=user and user==ctx.author:

 if str(reaction)==emoji[0]:

 print(1)

 await msg1.delete()

 await submenu()

 # await msg1.delete()



 await menustring.delete()

 await smenu.delete()




 elif str(reaction)==emoji[1]:

 await adddata()

 #await msg1.delete()

  await msg1.delete()

 await menustring.delete()


 print(2)

 elif str(reaction)==emoji[2]:

 await updatedata()

 await msg1.delete()

 await menustring.delete()



 print(3)

 elif str(reaction)==emoji[3]:

 await deldata()

 await msg1.delete()

 await menustring.delete()



 print(4)

 elif str(reaction)==emoji[4]:
 await exportdata()

 await msg1.delete()

 await menustring.delete()



 print(5)

 elif str(reaction)==emoji[5]:

 print(6)

 exiting=await channel.send("`Exiting.... Thank For Using The Program`")



 await msg1.delete()

 await menustring.delete()

 await exiting.delete()

 break



 return

 ch="n"



 #DEFINING_DELETE_DATA_PROCESS



 async def deldata():

 channel=prejectx['channel']

 author=prejectx['author']

 def check(m):
 return m.author==author and m.channel == channel

 while True:

 await channel.send("`Enter the PID of the record you want to delete:`")   msg = await

self.bot.wait_for('message', check=check)

 pid=msg.content

 #pid=int(input("Enter the PID of the record you want to delete:"))   import

mysql.connector

 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords', )

 cursor = db.cursor()

 cursor.execute("SELECT * FROM Information where PID="+str(pid))   results =

cursor.fetchall()

 if results!=[]:
 await channel.send(results[0])



 except Exception as e:

 if str(e)=="1146 (42S02): Table 'criminalrecords.information' doesn't exist":     import

mysql.connector

 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',     database='CriminalRecords',)

 cursor = db.cursor()

 cursor.execute("create table information (PID integer primary key,Name   varchar(20),EntryDate
date,ExitDate date,PLevel integer,Contact varchar(20))" )

 await channel.send("`Table Information Does Not Exist.....`")   time.sleep(.75)

  await channel.send("`Creating Table Information.....`")   time.sleep(.75)

 await channel.send("`Table Created`")

 db.commit()

 break

 except Exception as e:

 print(e)

 break

 else:

 await channel.send ("PID was incorrect")

 break
 if results ==[]:

 await channel.send("`No Record With Such PID Exists`")

 break

 await channel.send("`Are you sure you want to delete the record (Y/N):`")    msg = await

self.bot.wait_for('message', check=check)

 ans=msg.content

 #ans=input("Are you sure you want to delete the record (Y/N):")   if ans=="Y" or

ans == "y":

 import mysql.connector

 try:

 db=mysql.connector.connect(host='localhost',user='root',password='aak20f031',
database='CriminalRecords', )

 cursor = db.cursor()

 abc="Delete from information where PID="+str(pid)

 cursor.execute(abc)

 db.commit()
strx="`Record with PID "+str(pid)+" deleted succesfully`"   await channel.send(strx)

break

except Exception as e:

raise e



#DEFINING_EXPORT_DATA_PROCESS



async def exportdata():

channel=prejectx['channel']

author=prejectx['author']

def check(m):

return m.author==author and m.channel == channel

no=0

with open("Record.txt", "a") as f:

f.truncate(0)

f.close()

abc=""

import datetime

import mysql.connector

 try:
 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords',)

cursor = db.cursor()

cursor.execute("SELECT * FROM Information " )

results = cursor.fetchall()

for x in results:

for i in x:

abc=abc+str(i)+"/"

no+=1

with open("Record.txt", "a") as f:

f.write(abc)

f.write("\n")

f.close()

abc=""

strx=f"`{no} Records Exported Succesfully`"



await channel.send(strx)
 dirx=r"C:\Users\aakas\Desktop\Persona 11-12\Persona Bot\Record.txt"   await

ctx.send(file=discord.File(dirx))

 except Exception as e:

 if str(e)=="1146 (42S02): Table 'criminalrecords.information' doesn't exist":      import

mysql.connector

 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords',)

 cursor = db.cursor()

 cursor.execute("create table information (PID integer primary key,Name    varchar(20),EntryDate
date,ExitDate date,PLevel integer,Contact varchar(20))" )

 await channel.send("Table Information Does Not Exist.....")   time.sleep(.75)

 await channel.send("Creating Table Information.....")   time.sleep(.75)

 await channel.send("Table Created")

 db.commit()

 except Exception as e:

 print(e)

 else:

 await channel.send("Error: unable to fetch data")
 #DEFINING_UPDATE_DATA_PROCESS



 async def updatedata():

 channel=prejectx['channel']

 author=prejectx['author']

 def check(m):

 return m.author==author and m.channel == channel

 ch=await channel.send("Enter The Id Of The Record You Want To Change:")    msg =

await self.bot.wait_for('message', check=check)

 pid=msg.content

 import mysql.connector

 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords', )

 cursor = db.cursor()

 cursor.execute("SELECT * FROM information where PID="+str(pid ))

 results = cursor.fetchall()

 Data=[]

 for x in results:
 Data.append(x)

 if Data==[]:

 await channel.send("No Records Available")

 await ch.delete()

 return



 else:

 await channel.send(Data)

 except Exception as e:

 if str(e)=="1146 (42S02): Table 'criminalrecords.information' doesn't exist":    import

mysql.connector

 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',    database='CriminalRecords',)

 cursor = db.cursor()

 cursor.execute("create table information (PID integer primary key,Name    varchar(20),EntryDate
date,ExitDate date,PLevel integer,Contact varchar(20))" )

 await channel.send("Table Information Does Not Exist.....")
  time.sleep(.75)

 await channel.send("Creating Table Information.....")   time.sleep(.75)

 await channel.send("Table Created")

 db.commit()

 except Exception as a:

 print(a)



 else:

 print(e)

 strx='''```Which Field Would You Like To Change:\n1. Name\n2. Entry Date:\n3. Exit Date:\n4.      PLevel\n5.
Contact\n6. Exit```'''

 msgfield=await channel.send(strx)

 await msgfield.add_reaction("1️⃣")

 await msgfield.add_reaction("2️⃣")

 await msgfield.add_reaction("3️⃣")

 await msgfield.add_reaction("4️⃣")

 await msgfield.add_reaction("5️⃣")

 await msgfield.add_reaction("6️⃣")

 emoji=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']

 def check(reaction, user):
 return user == ctx.author and (str(reaction.emoji) in emoji)

 try:

 reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0,check=check)          except

asyncio.TimeoutError:

 await channel.send("You took too long to respond")

 return

 if self.bot.user!=user and user==ctx.author:

 if str(reaction)==emoji[0]:

 choice=1

 elif str(reaction)==emoji[1]:

 choice=2

 elif str(reaction)==emoji[2]:

 choice=3

 elif str(reaction)==emoji[3]:

 choice=4

 elif str(reaction)==emoji[4]:
 choice=5

 elif str(reaction)==emoji[5]:

 choice=6

 choice=int(choice)

 print(choice)

 def check2(m):

 return m.author == ctx.message.author and m.channel == ctx.message.channel        if choice==1:

 await channel.send("Enter The New Name For The Field:")   msg = await

self.bot.wait_for('message', check=check2)   new=str(msg.content)

 string='UPDATE INFORMATION SET NAME="'+new+'" where PID='+str(pid)      elif

choice==2:

 await channel.send("Enter The New Entry Date For The Field (yyyy-mm-dd) :")           msg = await

self.bot.wait_for('message', check=check2)   new=str(msg.content)

 string='UPDATE INFORMATION SET EntryDate="'+new+'" where PID='+str(pid)         elif

choice==3:

 await channel.send("Enter The New Exit Date For The Field (yyyy-mm-dd) :")        msg = await

self.bot.wait_for('message', check=check2)   new=str(msg.content)

 string='UPDATE INFORMATION SET ExitDate="'+new+'" where PID='+str(pid)         elif

 choice==4:

 await channel.send("Enter The New PLevel For The Field:")   msg = await
self.bot.wait_for('message', check=check2)   new=str(msg.content)

 string='UPDATE INFORMATION SET PLevel="'+str(new)+'" where PID='+str(pid)      elif

choice==5:

 await channel.send("Enter The New Contact For The Field:")   msg = await

self.bot.wait_for('message', check=check2)   new=str(msg.content)

 string='UPDATE INFORMATION SET Contact="'+new+'" where PID='+str(pid)   elif

choice==6:

 msgfield.delete()

 return

 print("hello")

 print(string)
 import mysql.connector

 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords',)

 cursor = db.cursor()

 cursor.execute(string)

 db.commit()

 await channel.send("Record Updated Succesfully")

 except Exception as e:

 print(e)



 #DEFINING_ADD_DATA_PROCESS



 async def adddata():

 channel=prejectx['channel']

 author=prejectx['author']

 def check(m):

 return m.author==author and m.channel == channel   abc="INSERT INTO

information Values ("

 await channel.send("`Please Type The PID`")

 msg = await self.bot.wait_for('message', check=check)

 PID=msg.content

 abc=abc+str(PID)+","

  await channel.send("`Please Type The Name`")

 msg = await self.bot.wait_for('message', check=check)

 Name=msg.content
 abc=abc+"'"+Name+"'"+","

 await channel.send("`Enter The Date of Entry (yyyy-mm-dd)`")   msg =

await self.bot.wait_for('message', check=check)

 EDate=msg.content

 abc=abc+"'"+EDate+"'"+","

 await channel.send("`Enter The Date of Exit (yyyy-mm-dd)`")    msg =

await self.bot.wait_for('message', check=check)

 ExDate=msg.content

 abc=abc+"'"+ExDate+"'"+","

 await channel.send("`Enter The PLevel`")

 msg = await self.bot.wait_for('message', check=check)

 PLvl=msg.content
 abc=abc+str(PLvl)+","

 await channel.send("`Enter The Contact Information`")

 msg = await self.bot.wait_for('message', check=check)

 Contact=msg.content

 abc=abc+"'"+Contact+"'"+")"

 import mysql.connector

 try:

 db=mysql.connector.connect(host='localhost',user='root',password='aak20f031',
database='CriminalRecords' , )

 cursor = db.cursor()

 cursor.execute(abc)

 db.commit()

 await channel.send("Record Added Succesfully")

 except Exception as e:

 if str(e)=="1146 (42S02): Table 'criminalrecords.information' doesn't exist":    import

mysql.connector

 try:


db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',

database='CriminalRecords')    cursor = db.cursor()

                                     cursor.execute("create table information (PID integer primary key,Name
varchar(20),EntryDate date,ExitDate date,PLevel integer,Contact varchar(20))" )

          await channel.send("Table Information Does Not Exist.....") time.sleep(.75)

                                     await channel.send("Creating Table Information.....")

 time.sleep(.75)

                                      await channel.send("Table Created")
                                    db.commit()

 except Exception as a:

 print(a)



 else:

 print(e)



 #DEFINING_FETCH_SPECIFIC_DATA_PROCESS



 async def fetchspecificdata():

 channel=prejectx['channel']
 author=prejectx['author']

 def check(m):

 return m.author==author and m.channel == channel

 acc=await channel.send("`Please Type The PID Of The Record You Want To Access`")   msg =

await self.bot.wait_for('message', check=check)

 pid=int(msg.content)

 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords', )

 cursor = db.cursor()

 abcd="SELECT PLevel FROM information where PID="+str(pid)

 cursor.execute(abcd)

 results = cursor.fetchall()

 Data=[]

 if results==[]:

 await channel.send("`No Records Available For This PID`")

 await acc.delete()

 return

 for x in results:

 if x==1:

 cursor = db.cursor()

 abcd="SELECT * FROM information where PID="+str(pid)

 cursor.execute(abcd)

 results = cursor.fetchall()

 Data=[]

 for x in results:
 await channel.send(x)

 await acc.delete()

 else:

 await channel.send("`Please Enter The Password To Enter This High Level Record`")       msg2 = await

self.bot.wait_for('message', check=check)   pas=msg2.content

 if pas=="Admin":

 cursor = db.cursor()

 abcd="SELECT * FROM information where PID="+str(pid)    cursor.execute(abcd)

 results = cursor.fetchall()

 Data=[]
 for x in results:

 await channel.send(x)

 await acc.delete()

 else:

           await channel.send("Password Is Incorrect")   await acc.delete()

 except Exception as e:

 if str(e)=="1146 (42S02): Table 'criminalrecords.information' doesn't exist":

 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords', )

 cursor = db.cursor()

 cursor.execute("create table information (PID integer primary key,Name       varchar(20),EntryDate
date,ExitDate date,PLevel integer,Contact varchar(20))" )

 await channel.send("`Table Information Does Not Exist.....`")    time.sleep(.75)

 await channel.send("`Creating Table Information.....`")    time.sleep(.75)

 await channel.send("`Table Created`")

 db.commit()

 except Exception as a:

 raise a

 else:

 raise e



 #DEFINING_FETCH_GENERAL_DATA_PROCESS



 async def fetchdata():

 print("fetching data ")

 channel=prejectx['channel']
 author=prejectx['author']

 #import mysql.connector

 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords',)

 cursor = db.cursor()

 cursor.execute("SELECT * FROM information where PLevel=1" )
 results = cursor.fetchall()

 Data=[]

 for x in results:

 await channel.send(x)

 Data.append(x)

 if Data==[]:

 await channel.send("`No Records Available`")

 except Exception as e:

 if str(e)=="1146 (42S02): Table 'criminalrecords.information' doesn't exist":     #import

mysql.connector

 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords')

 cursor = db.cursor()

 cursor.execute("create table information (PID integer primary key,Name   varchar(20),EntryDate
date,ExitDate date,PLevel integer,Contact varchar(20))" )

 await channel.send("`Table Information Does Not Exist.....`")   time.sleep(.75)

 await channel.send("`Creating Table Information.....`")   time.sleep(.75)

 await channel.send("`Table Created`")

 db.commit()

 except Exception as a:

 print(a)

 else:

 print(e)



 #DEFINING_FETCH_DATA_USING_PID_PROCESS



 async def fetchdata2():

 channel=prejectx['channel']

 author=prejectx['author']

 def check(m):
 return m.author==author and m.channel == channel

 await channel.send("`Please Enter The Password To Enter This High Level Record`")      msg2 =

await self.bot.wait_for('message', check=check)

 pas=msg2.content

 if pas=="Admin":
 try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords', )

 cursor = db.cursor()

 cursor.execute("SELECT * FROM information where PLevel=2 or PLevel=3" )    results =

cursor.fetchall()

 Data=[]

 for x in results:

 await channel.send(x)

 Data.append(x)

 if Data==[]:

 await channel.send("`No Records Available`")

 except Exception as e:

 if str(e)=="1146 (42S02): Table 'criminalrecords.information' doesn't exist":     try:

 db=mysql.connector.connect(host="localhost",user="root",password='aak20f031',
database='CriminalRecords',)

 cursor = db.cursor()

 cursor.execute("create table information (PID integer primary key,Name    varchar(20),EntryDate
date,ExitDate date,PLevel integer,Contact varchar(20))" )

 await channel.send("`Table Information Does Not Exist.....`")   time.sleep(.75)

 print("`Creating Table Information.....`")

 time.sleep(.75)

 await channel.send("`Table Created`")

 db.commit()

 except Exception as a:

 print(a)

 else:

 print(e)

 else:

 await channel.send("`Passkey was incorrect`")

 #SUBMENU_TO_ACCESS_DATA



 async def submenu():
channel=prejectx['channel']

author=prejectx['author']

 strx='''``` ACCESS RECORDS MENU\n===============================\n1. Access Specific   Records\n2. Access
Level 1 Records\n3. Access Level 2 and 3 Records```'''