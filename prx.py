import discord
import time
import pandas as pd
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import sqlite3
from tabulate import tabulate
import dbexec
#import json
#import asyncio
#from discord.ext.commands import Bot
#from discord.utils import get

con = sqlite3.connect('database.db')
c = con.cursor()

bot = commands.Bot("!")

roletouse = ""

#list(pd.read_sql('SELECT * FROM dsbot_roles', con))


@bot.event
async def on_ready():
            print("BOT ON")

@bot.command(name='editperm', pass_context=True)
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def mod_ban(ctx, varx):
            global roletouse
            name = ctx.author.name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                query = "INSERT INTO dsbot_roles VALUES ('1', '"+varx+"', '"+date+"')"
                #selectquery = "SELECT discord_role_name FROM dsbot_roles"
                c.execute(query)
                con.commit()
                c.execute("SELECT discord_role_name FROM dsbot_roles")
                roletouse = c.fetchone()[0]
                await ctx.send('**{0}** O Cargo foi alterado para:' + format(str(varx)))
            except:
                c.execute(
                    """UPDATE dsbot_roles 
                       SET discord_role_name =:discord_role_name, 
                       date =:date 
                       WHERE id = 1
                    """,
                    {"discord_role_name": "" + varx + "", "date": "" + date + ""}
                )
                con.commit()
                c.execute("SELECT discord_role_name FROM dsbot_roles")
                roletouse = c.fetchone()[0]
                print("Permissão alterada para:" + roletouse + " ("+name+")")
                await ctx.send('**{0}** O Cargo foi alterado para:' + format(str(varx)))

@bot.command(name="sairdapraça")
async def exitp(ctx):
            c.execute("SELECT discord_role_name FROM dsbot_roles")
            roleuse = str(c.fetchone()[0])
            role = discord.utils.get(ctx.guild.roles, name=roleuse)
            if role in ctx.author.roles:
                date = time.strftime('%H:%M:%S', time.localtime())
                name = ctx.message.author.display_name
                username = ctx.message.author.id
                try:
                    c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                    c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                    c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                    c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                    c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                    con.commit()
                except:
                    ...
                embed = discord.Embed(
                    title="Praça Mágica",
                    description="Você saiu da praça mágica",
                    color=discord.Color.blue())
                embed.set_thumbnail(
                    url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
                await ctx.send("Você Saiu da sala com sucesso!")
                print(name + " saiu da praça mágica" + " ("+date+")")
                time.sleep(20)
                await ctx.channel.purge(limit=2)

#@bot.command(pass_context=True)
@bot.command(name="stone1")
async def regstone1(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot VALUES ('" + name + "','" + date + "','Stone I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Stone I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone I - " + name + " entrou na praça mágica" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p2 VALUES ('" + name + "','" + date + "','Stone I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Stone I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 2F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone I - " + name + " entrou na praça mágica 2F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p3 VALUES ('" + name + "','" + date + "','Stone I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Stone I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 3F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone I - " + name + " entrou na praça mágica 3F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p4 VALUES ('" + name + "','" + date + "','Stone I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Stone I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 4F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone I - " + name + " entrou na praça mágica 4F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p5 VALUES ('" + name + "','" + date + "','Stone I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Stone I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 5F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone I - " + name + " entrou na praça mágica 5F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)



@bot.command(name="stone2")
async def regstone2(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot VALUES ('" + name + "','" + date + "','Stone II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Stone II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 1F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone II - " + name + " entrou na praça mágica 1F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p2 VALUES ('" + name + "','" + date + "','Stone II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Stone II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 2F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone II - " + name + " entrou na praça mágica 2F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p3 VALUES ('" + name + "','" + date + "','Stone II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Stone II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 3F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone II - " + name + " entrou na praça mágica 3F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p4 VALUES ('" + name + "','" + date + "','Stone II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Stone II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 4F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone II - " + name + " entrou na praça mágica 4F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p5 VALUES ('" + name + "','" + date + "','Stone II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Stone II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 5F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone II - " + name + " entrou na praça mágica 5F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)



@bot.command(name="stone3")
async def regstone3(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot VALUES ('" + name + "','" + date + "','Stone III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Stone III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone III - " + name + " entrou na praça mágica" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p2 VALUES ('" + name + "','" + date + "','Stone III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Stone III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 2F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone III - " + name + " entrou na praça mágica 2F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p3 VALUES ('" + name + "','" + date + "','Stone III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Stone III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 3F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone III - " + name + " entrou na praça mágica 3F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p4 VALUES ('" + name + "','" + date + "','Stone III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Stone III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 4F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone III - " + name + " entrou na praça mágica 4F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p5 VALUES ('" + name + "','" + date + "','Stone III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Stone III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 5F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Stone III - " + name + " entrou na praça mágica 5F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)

@bot.command(name="gold1")
async def reggold1(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot VALUES ('" + name + "','" + date + "','Gold I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Gold I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 1F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold I - " + name + " entrou na praça mágica 1F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p2 VALUES ('" + name + "','" + date + "','Gold I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Gold I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 2F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold I - " + name + " entrou na praça mágica 2F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p3 VALUES ('" + name + "','" + date + "','Gold I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Gold I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 3F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold I - " + name + " entrou na praça mágica 3F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p4 VALUES ('" + name + "','" + date + "','Gold I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Gold I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 4F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold I - " + name + " entrou na praça mágica 4F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p5 VALUES ('" + name + "','" + date + "','Gold I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Gold I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 5F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold I - " + name + " entrou na praça mágica 5F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)

@bot.command(name="gold2")
async def reggold2(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot VALUES ('" + name + "','" + date + "','Gold II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Gold II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 1F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold II - " + name + " entrou na praça mágica 1F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p2 VALUES ('" + name + "','" + date + "','Gold II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Gold II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 2F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold II - " + name + " entrou na praça mágica 2F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p3 VALUES ('" + name + "','" + date + "','Gold II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Gold II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 3F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold II - " + name + " entrou na praça mágica 3F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p4 VALUES ('" + name + "','" + date + "','Gold II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Gold II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 4F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold II - " + name + " entrou na praça mágica 4F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p5 VALUES ('" + name + "','" + date + "','Gold II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Gold II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 5F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold II - " + name + " entrou na praça mágica 5F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)


@bot.command(name="gold3")
async def reggold3(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot VALUES ('" + name + "','" + date + "','Gold III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Gold III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 1F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold III - " + name + " entrou na praça mágica 1F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p2 VALUES ('" + name + "','" + date + "','Gold III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Gold III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 2F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold III - " + name + " entrou na praça mágica 2F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p3 VALUES ('" + name + "','" + date + "','Gold III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Gold III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 3F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold III - " + name + " entrou na praça mágica 3F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p4 VALUES ('" + name + "','" + date + "','Gold III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Gold III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 4F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold III - " + name + " entrou na praça mágica 4F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p5 VALUES ('" + name + "','" + date + "','Gold III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Gold III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 5F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("Gold III - " + name + " entrou na praça mágica 5F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)


@bot.command(name="exp1")
async def regexp1(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot VALUES ('" + name + "','" + date + "','EXP I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "EXP I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 1F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP I - " + name + " entrou na praça mágica 1F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p2 VALUES ('" + name + "','" + date + "','EXP I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "EXP I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 2F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP I - " + name + " entrou na praça mágica 2F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p3 VALUES ('" + name + "','" + date + "','EXP I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "EXP I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 3F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP I - " + name + " entrou na praça mágica 3F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p4 VALUES ('" + name + "','" + date + "','EXP I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "EXP I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 4F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP I - " + name + " entrou na praça mágica 4F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p5 VALUES ('" + name + "','" + date + "','EXP I')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "EXP I"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 5F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP I - " + name + " entrou na praça mágica 5F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)


@bot.command(name="exp2")
async def regexp2(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot VALUES ('" + name + "','" + date + "','EXP II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "EXP II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 1F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP II - " + name + " entrou na praça mágica 1F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p2 VALUES ('" + name + "','" + date + "','EXP II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "EXP II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 2F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP II - " + name + " entrou na praça mágica 2F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p3 VALUES ('" + name + "','" + date + "','EXP II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "EXP II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 3F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP II - " + name + " entrou na praça mágica 3F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p4 VALUES ('" + name + "','" + date + "','EXP II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "EXP II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 4F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP II - " + name + " entrou na praça mágica 4F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p5 VALUES ('" + name + "','" + date + "','EXP II')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "EXP II"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 5F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP II - " + name + " entrou na praça mágica 5F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)


@bot.command(name="exp3")
async def regexp2(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot VALUES ('" + name + "','" + date + "','EXP III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "EXP III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 1F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP III - " + name + " entrou na praça mágica 1F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p2 VALUES ('" + name + "','" + date + "','EXP III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "EXP III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 2F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP III - " + name + " entrou na praça mágica 2F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p3 VALUES ('" + name + "','" + date + "','EXP III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "EXP III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 3F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP III - " + name + " entrou na praça mágica 3F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p4 VALUES ('" + name + "','" + date + "','EXP III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "EXP III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 4F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP III - " + name + " entrou na praça mágica 4F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p5 VALUES ('" + name + "','" + date + "','EXP III')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "EXP III"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 5F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("EXP III - " + name + " entrou na praça mágica 5F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)


@bot.command(name="ds")
async def regdark(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot VALUES ('" + name + "','" + date + "','DarkSteel')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "DarkSteel"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 1F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("DarkSteel - " + name + " entrou na praça mágica 1F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p2 VALUES ('" + name + "','" + date + "','DarkSteel')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "DarkSteel"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 2F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("DarkSteel - " + name + " entrou na praça mágica 2F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p3 VALUES ('" + name + "','" + date + "','DarkSteel')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "DarkSteel"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 3F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("DarkSteel - " + name + " entrou na praça mágica 3F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p4 VALUES ('" + name + "','" + date + "','DarkSteel')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "DarkSteel"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 4F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("DarkSteel - " + name + " entrou na praça mágica 4F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name
            date = time.strftime('%H:%M:%S', time.localtime())
            try:
                c.execute("DELETE FROM dsbot WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p2 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p3 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p4 WHERE discord_name = '" + name + "'")
                c.execute("DELETE FROM dsbot_p5 WHERE discord_name = '" + name + "'")
                c.execute("INSERT INTO dsbot_p5 VALUES ('" + name + "','" + date + "','DarkSteel')")
                con.commit()
            except:
                ...
            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "DarkSteel"', con)
            df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
            output = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Veja quem esta farmando em tempo real",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="" + output + "", value="Você ingressou na praça 5F!", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            print("DarkSteel - " + name + " entrou na praça mágica 5F" + " (" + date + ")")
            time.sleep(20)
            await ctx.channel.purge(limit=2)



@bot.command(name="pr")
async def regview(ctx, andar: int):
    if andar == 1:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name

            df = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Stone I"', con)
            df2 = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Stone II"', con)
            df3 = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Stone III"', con)
            df4 = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Gold I"', con)
            df5 = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Gold II"', con)
            df6 = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "Gold III"', con)
            df7 = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "EXP I"', con)
            df8 = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "EXP II"', con)
            df9 = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "EXP III"', con)
            df10 = pd.read_sql('SELECT * FROM dsbot WHERE plocal = "DarkSteel"', con)

            outputstone1 = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone2 = ("```" + "\n\n" + tabulate(df2, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone3 = ("```" + "\n\n" + tabulate(df3, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone4 = ("```" + "\n\n" + tabulate(df4, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone5 = ("```" + "\n\n" + tabulate(df5, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone6 = ("```" + "\n\n" + tabulate(df6, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone7 = ("```" + "\n\n" + tabulate(df7, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone8 = ("```" + "\n\n" + tabulate(df8, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone9 = ("```" + "\n\n" + tabulate(df9, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone10 = ("```" + "\n\n" + tabulate(df10, tablefmt="plain",
                                                       headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")

            embed = discord.Embed(
                title="Praça Mágica",
                description="Lista Comandos",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="!stone1", value="" + outputstone1 + "", inline=False)
            embed.add_field(name="!stone2", value="" + outputstone2 + "", inline=False)
            embed.add_field(name="!stone3", value="" + outputstone3 + "", inline=False)
            embed.add_field(name="!gold1", value="" + outputstone4 + "", inline=False)
            embed.add_field(name="!gold2", value="" + outputstone5 + "", inline=False)
            embed.add_field(name="!gold3", value="" + outputstone6 + "", inline=False)
            embed.add_field(name="!exp1", value="" + outputstone7 + "", inline=False)
            embed.add_field(name="!exp2", value="" + outputstone8 + "", inline=False)
            embed.add_field(name="!exp3", value="" + outputstone9 + "", inline=False)
            embed.add_field(name="!ds", value="" + outputstone10 + "", inline=False)
            # embed.add_field(name="!pr", value="Visualizar tudo", inline=False)
            # embed.add_field(name="!sairdapraça", value="Sair", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            # time.sleep(90)
            # await ctx.channel.purge(limit=2)
    if andar == 2:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name

            df = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Stone I"', con)
            df2 = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Stone II"', con)
            df3 = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Stone III"', con)
            df4 = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Gold I"', con)
            df5 = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Gold II"', con)
            df6 = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "Gold III"', con)
            df7 = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "EXP I"', con)
            df8 = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "EXP II"', con)
            df9 = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "EXP III"', con)
            df10 = pd.read_sql('SELECT * FROM dsbot_p2 WHERE plocal = "DarkSteel"', con)

            outputstone1 = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone2 = ("```" + "\n\n" + tabulate(df2, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone3 = ("```" + "\n\n" + tabulate(df3, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone4 = ("```" + "\n\n" + tabulate(df4, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone5 = ("```" + "\n\n" + tabulate(df5, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone6 = ("```" + "\n\n" + tabulate(df6, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone7 = ("```" + "\n\n" + tabulate(df7, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone8 = ("```" + "\n\n" + tabulate(df8, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone9 = ("```" + "\n\n" + tabulate(df9, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone10 = ("```" + "\n\n" + tabulate(df10, tablefmt="plain",
                                                       headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")

            embed = discord.Embed(
                title="Praça Mágica 2F",
                description="Lista Comandos",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="!stone1", value="" + outputstone1 + "", inline=False)
            embed.add_field(name="!stone2", value="" + outputstone2 + "", inline=False)
            embed.add_field(name="!stone3", value="" + outputstone3 + "", inline=False)
            embed.add_field(name="!gold1", value="" + outputstone4 + "", inline=False)
            embed.add_field(name="!gold2", value="" + outputstone5 + "", inline=False)
            embed.add_field(name="!gold3", value="" + outputstone6 + "", inline=False)
            embed.add_field(name="!exp1", value="" + outputstone7 + "", inline=False)
            embed.add_field(name="!exp2", value="" + outputstone8 + "", inline=False)
            embed.add_field(name="!exp3", value="" + outputstone9 + "", inline=False)
            embed.add_field(name="!ds", value="" + outputstone10 + "", inline=False)
            # embed.add_field(name="!pr", value="Visualizar tudo", inline=False)
            # embed.add_field(name="!sairdapraça", value="Sair", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            # time.sleep(90)
            # await ctx.channel.purge(limit=2)
    if andar == 3:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name

            df = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Stone I"', con)
            df2 = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Stone II"', con)
            df3 = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Stone III"', con)
            df4 = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Gold I"', con)
            df5 = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Gold II"', con)
            df6 = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "Gold III"', con)
            df7 = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "EXP I"', con)
            df8 = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "EXP II"', con)
            df9 = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "EXP III"', con)
            df10 = pd.read_sql('SELECT * FROM dsbot_p3 WHERE plocal = "DarkSteel"', con)

            outputstone1 = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone2 = ("```" + "\n\n" + tabulate(df2, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone3 = ("```" + "\n\n" + tabulate(df3, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone4 = ("```" + "\n\n" + tabulate(df4, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone5 = ("```" + "\n\n" + tabulate(df5, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone6 = ("```" + "\n\n" + tabulate(df6, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone7 = ("```" + "\n\n" + tabulate(df7, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone8 = ("```" + "\n\n" + tabulate(df8, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone9 = ("```" + "\n\n" + tabulate(df9, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone10 = ("```" + "\n\n" + tabulate(df10, tablefmt="plain",
                                                       headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")

            embed = discord.Embed(
                title="Praça Mágica 3F",
                description="Lista Comandos",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="!stone1", value="" + outputstone1 + "", inline=False)
            embed.add_field(name="!stone2", value="" + outputstone2 + "", inline=False)
            embed.add_field(name="!stone3", value="" + outputstone3 + "", inline=False)
            embed.add_field(name="!gold1", value="" + outputstone4 + "", inline=False)
            embed.add_field(name="!gold2", value="" + outputstone5 + "", inline=False)
            embed.add_field(name="!gold3", value="" + outputstone6 + "", inline=False)
            embed.add_field(name="!exp1", value="" + outputstone7 + "", inline=False)
            embed.add_field(name="!exp2", value="" + outputstone8 + "", inline=False)
            embed.add_field(name="!exp3", value="" + outputstone9 + "", inline=False)
            embed.add_field(name="!ds", value="" + outputstone10 + "", inline=False)
            # embed.add_field(name="!pr", value="Visualizar tudo", inline=False)
            # embed.add_field(name="!sairdapraça", value="Sair", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            # time.sleep(90)
            # await ctx.channel.purge(limit=2)
    if andar == 4:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name

            df = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Stone I"', con)
            df2 = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Stone II"', con)
            df3 = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Stone III"', con)
            df4 = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Gold I"', con)
            df5 = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Gold II"', con)
            df6 = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "Gold III"', con)
            df7 = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "EXP I"', con)
            df8 = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "EXP II"', con)
            df9 = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "EXP III"', con)
            df10 = pd.read_sql('SELECT * FROM dsbot_p4 WHERE plocal = "DarkSteel"', con)

            outputstone1 = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone2 = ("```" + "\n\n" + tabulate(df2, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone3 = ("```" + "\n\n" + tabulate(df3, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone4 = ("```" + "\n\n" + tabulate(df4, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone5 = ("```" + "\n\n" + tabulate(df5, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone6 = ("```" + "\n\n" + tabulate(df6, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone7 = ("```" + "\n\n" + tabulate(df7, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone8 = ("```" + "\n\n" + tabulate(df8, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone9 = ("```" + "\n\n" + tabulate(df9, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone10 = ("```" + "\n\n" + tabulate(df10, tablefmt="plain",
                                                       headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")

            embed = discord.Embed(
                title="Praça Mágica 4F",
                description="Lista Comandos",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="!stone1", value="" + outputstone1 + "", inline=False)
            embed.add_field(name="!stone2", value="" + outputstone2 + "", inline=False)
            embed.add_field(name="!stone3", value="" + outputstone3 + "", inline=False)
            embed.add_field(name="!gold1", value="" + outputstone4 + "", inline=False)
            embed.add_field(name="!gold2", value="" + outputstone5 + "", inline=False)
            embed.add_field(name="!gold3", value="" + outputstone6 + "", inline=False)
            embed.add_field(name="!exp1", value="" + outputstone7 + "", inline=False)
            embed.add_field(name="!exp2", value="" + outputstone8 + "", inline=False)
            embed.add_field(name="!exp3", value="" + outputstone9 + "", inline=False)
            embed.add_field(name="!ds", value="" + outputstone10 + "", inline=False)
            # embed.add_field(name="!pr", value="Visualizar tudo", inline=False)
            # embed.add_field(name="!sairdapraça", value="Sair", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            # time.sleep(90)
            # await ctx.channel.purge(limit=2)
    if andar == 5:
        c.execute("SELECT discord_role_name FROM dsbot_roles")
        roleuse = str(c.fetchone()[0])
        role = discord.utils.get(ctx.guild.roles, name=roleuse)
        if role in ctx.author.roles:
            name = ctx.message.author.display_name

            df = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Stone I"', con)
            df2 = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Stone II"', con)
            df3 = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Stone III"', con)
            df4 = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Gold I"', con)
            df5 = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Gold II"', con)
            df6 = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "Gold III"', con)
            df7 = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "EXP I"', con)
            df8 = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "EXP II"', con)
            df9 = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "EXP III"', con)
            df10 = pd.read_sql('SELECT * FROM dsbot_p5 WHERE plocal = "DarkSteel"', con)

            outputstone1 = ("```" + "\n\n" + tabulate(df, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone2 = ("```" + "\n\n" + tabulate(df2, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone3 = ("```" + "\n\n" + tabulate(df3, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone4 = ("```" + "\n\n" + tabulate(df4, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone5 = ("```" + "\n\n" + tabulate(df5, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone6 = ("```" + "\n\n" + tabulate(df6, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone7 = ("```" + "\n\n" + tabulate(df7, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone8 = ("```" + "\n\n" + tabulate(df8, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone9 = ("```" + "\n\n" + tabulate(df9, tablefmt="plain",
                                                      headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")
            outputstone10 = ("```" + "\n\n" + tabulate(df10, tablefmt="plain",
                                                       headers=["#", "Nome", "Hora de inicio", "Local"]) + "```")

            embed = discord.Embed(
                title="Praça Mágica 5F",
                description="Lista Comandos",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="!stone1", value="" + outputstone1 + "", inline=False)
            embed.add_field(name="!stone2", value="" + outputstone2 + "", inline=False)
            embed.add_field(name="!stone3", value="" + outputstone3 + "", inline=False)
            embed.add_field(name="!gold1", value="" + outputstone4 + "", inline=False)
            embed.add_field(name="!gold2", value="" + outputstone5 + "", inline=False)
            embed.add_field(name="!gold3", value="" + outputstone6 + "", inline=False)
            embed.add_field(name="!exp1", value="" + outputstone7 + "", inline=False)
            embed.add_field(name="!exp2", value="" + outputstone8 + "", inline=False)
            embed.add_field(name="!exp3", value="" + outputstone9 + "", inline=False)
            embed.add_field(name="!ds", value="" + outputstone10 + "", inline=False)
            # embed.add_field(name="!pr", value="Visualizar tudo", inline=False)
            # embed.add_field(name="!sairdapraça", value="Sair", inline=False)
            # embed.set_footer(text="Você ingressou na praça!")
            await ctx.send(embed=embed)
            # time.sleep(90)
            # await ctx.channel.purge(limit=2)




@bot.command(name="helpb")
async def regview(ctx):
            embed = discord.Embed(
                title="Praça Mágica",
                description="Lista Comandos",
                color=discord.Color.blue())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrN6cunsqQ1kJ8nyVEBu3n-R2UXX7l6pbCS7mkg0PiSLe3_HLDO8iMxV5rpSnI8QGuZ0&usqp=CAU")
            embed.add_field(name="!stone1", value="Pedra Mágica 1!", inline=False)
            embed.add_field(name="!stone2", value="Pedra Mágica 2!", inline=False)
            embed.add_field(name="!stone3", value="Pedra Mágica 3!", inline=False)
            embed.add_field(name="!gold1", value="Praça de Gold 1!", inline=False)
            embed.add_field(name="!gold2", value="Praça de Gold 2!", inline=False)
            embed.add_field(name="!gold3", value="Praça de Gold 3!", inline=False)
            embed.add_field(name="!exp1", value="Praça de Exp 1!", inline=False)
            embed.add_field(name="!exp2", value="Praça de Exp 2!", inline=False)
            embed.add_field(name="!exp3", value="Praça de Exp 3!", inline=False)
            embed.add_field(name="!ds", value="Praça de DarkSteel!", inline=False)
            embed.add_field(name="!pr", value="Visualizar tudo", inline=False)
            embed.add_field(name="!sairdapraça", value="Sair", inline=False)
            embed.set_footer(text="local + numero do andar ex: '!stone1 1' (Pedra Mágica 1)")
            await ctx.send(embed=embed)

bot.run("OTEyMDE3NDUwMzkwOTM3Njkw.YZp0cA.vZiQbDO8hbkG-FWmPstHrLkksO4")
    #"OTEyMDE3NDUwMzkwOTM3Njkw.YZp0cA.LbVxQoSRBKYEI-y42pU60dSUt6w"