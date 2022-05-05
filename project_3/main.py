import discord
import sqlite3
import PILTools
from PILTools import Image
from discord.ext import commands
from discord.ext.commands import Bot
import random

bot: Bot = commands.Bot(command_prefix="!")
base = sqlite3.connect('Statigr.db')
cur = base.cursor()
clas = 0
Newgame = False
Nab = False
p1 = True
p2 = True
p3 = True
p4 = True
att = False
sf = False
bue = True
turel = False
enemies = []
enemiesst = []
Fight = False
pl1 = []
pl2 = []
pl3 = []
pl4 = []
step = 0
pl = 0
coords = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]]
coordsf = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]]
spcord = [[[110, 695], [195, 645], [280, 695], [365, 645], [450, 695], [535, 645], [620, 695], [705, 645], [790, 695],
           [875, 645], [960, 695], [1045, 645], [1130, 695], [1215, 645], [1300, 695], [1385, 645], [1470, 695],
           [1555, 645], [1640, 695], [1725, 645], [1810, 695]],
          [[110, 780], [195, 730], [280, 780], [365, 730], [450, 780], [535, 730], [620, 780], [705, 730], [790, 780],
           [875, 730], [960, 780], [1045, 730], [1130, 780], [1215, 730], [1300, 780], [1385, 730], [1470, 780],
           [1555, 730], [1640, 780], [1725, 730], [1810, 780]],
          [[110, 865], [195, 815], [280, 865], [365, 815], [450, 865], [535, 815], [620, 865], [705, 815], [790, 865],
           [875, 815], [960, 865], [1045, 815], [1130, 865], [1215, 815], [1300, 865], [1385, 815], [1470, 865],
           [1555, 815], [1640, 865], [1725, 815], [1810, 865]],
          [[110, 950], [195, 900], [280, 950], [365, 900], [450, 950], [535, 900], [620, 950], [705, 900], [790, 950],
           [875, 900], [960, 950], [1045, 900], [1130, 950], [1215, 900], [1300, 950], [1385, 900], [1470, 950],
           [1555, 900], [1640, 950], [1725, 900], [1810, 950]],
          [[110, 1035], [195, 985], [280, 1035], [365, 985], [450, 1035], [535, 985], [620, 1035], [705, 985],
           [790, 1035], [875, 985], [960, 1035], [1045, 985], [1130, 1035], [1215, 985], [1300, 1035], [1385, 985],
           [1470, 1035], [1555, 985], [1640, 1035], [1725, 985], [1810, 1035]],
          [110, 1035]]


def coord(a, b):
    coords = []
    if (a > 1) and (a < 21):
        if (b > 1) and (b < 5):
            coords.append((a - 1, b - 1))
            coords.append((a, b - 1))
            coords.append((a - 1, b))
            coords.append((a, b + 1))
            coords.append((a + 1, b + 1))
            coords.append((a + 1, b))
        if b == 1:
            if a % 2 is True:
                coords.append((a - 1, b))
                coords.append((a + 1, b))
                coords.append((a, b + 1))
            else:
                coords.append((a - 1, b))
                coords.append((a + 1, b))
                coords.append((a, b + 1))
                coords.append((a + 1, b + 1))
                coords.append((a - 1, b - 1))
        if b == 5:
            if a % 2 is True:
                coords.append((a - 1, b))
                coords.append((a + 1, b))
                coords.append((a, b - 1))
                coords.append((a - 1, b - 1))
                coords.append((a + 1, b - 1))
            else:
                coords.append((a - 1, b))
                coords.append((a + 1, b))
                coords.append((a, b - 1))
    if a == 1:
        if b == 1:
            coords.append((a + 1, b))
            coords.append((a + 1, b + 1))
            coords.append((a, b + 1))
        elif b == 5:
            coords.append((a, b - 1))
            coords.append((a + 1, b))
        else:
            coords.append((a, b - 1))
            coords.append((a + 1, b + 1))
            coords.append((a + 1, b))
            coords.append((a, b + 1))
    if a == 21:
        if b == 1:
            coords.append((a - 1, b))
            coords.append((a - 1, b + 1))
            coords.append((a, b + 1))
        elif b == 5:
            coords.append((a - 1, b))
            coords.append((a, b - 1))
        else:
            coords.append((a, b - 1))
            coords.append((a - 1, b - 1))
            coords.append((a - 1, b))
            coords.append((a, b + 1))
    return coords


@bot.command()
async def Start_Game(message):
    global Newgame
    Newgame = True
    await message.channel.send('Все данные старой партии будут удалены, вы уверены что хотите продолжить("!Yes"/"!No")')


@bot.command()
async def Yes(message):
    global Newgame, Nab
    if Newgame is True:
        await message.channel.send('Для присоединения к игре напишите "!Im_(voin/luchnik/mag/inginer)" (лимит-4 '
                                   'человека), как только все будут готовы напишите "!Start"')
        cur.execute('DELETE FROM Igroki')
        base.commit()
        Newgame = False
        Nab = True
        cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', ('X', 'voin', 0, 0, 0, 0, 0, '', '', ''))
        cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    ('X', 'luchnik', 0, 0, 0, 0, 0, '', '', ''))
        cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', ('X', 'mag', 0, 0, 0, 0, 0, '', '', ''))
        cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    ('X', 'inginer', 0, 0, 0, 0, 0, '', '', ''))
        base.commit()


@bot.command()
async def Im_voin(message):
    global Nab
    if Nab is True:
        cur.execute('DELETE FROM Igroki where class == ?', ('voin',))
        base.commit()
        cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (str(message.author), 'voin', 200, 200,
                                                                                50, 50, 100, '2:0:0', '', ''))
        base.commit()
        await message.channel.send(f"{message.author.mention} взял класс война")


@bot.command()
async def Im_luchnik(message):
    global Nab
    if Nab is True:
        cur.execute('DELETE FROM Igroki where class == ?', ('luchnik',))
        base.commit()
        cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (str(message.author), 'luchnik', 100, 100,
                     75, 75, 100, '0:1:1', '', ''))
        base.commit()
        await message.channel.send(f"{message.author.mention} взял класс лучника")


@bot.command()
async def Im_mag(message):
    global Nab
    if Nab is True:
        cur.execute('DELETE FROM Igroki where class == ?', ('mag',))
        base.commit()
        cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (str(message.author), 'mag', 100, 100,
                                                                                150, 150, 100, '1:2:0', '', ''))
        base.commit()
        await message.channel.send(f"{message.author.mention} взял класс мага")


@bot.command()
async def Im_inginer(message):
    global Nab
    if Nab is True:
        cur.execute('DELETE FROM Igroki where class == ?', ('inginer',))
        base.commit()
        cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (str(message.author), 'inginer', 150, 150,
                     100, 100, 100, '0:0:2', '', ''))
        base.commit()
        await message.channel.send(f"{message.author.mention} взял класс инжинера")


@bot.command()
async def Start(message):
    global Nab, pl1, pl2, pl3, pl4
    pl1 = cur.execute('SELECT * FROM Igroki WHERE class == ?', ('voin',)).fetchall()
    pl2 = cur.execute('SELECT * FROM Igroki WHERE class == ?', ('luchnik',)).fetchall()
    pl3 = cur.execute('SELECT * FROM Igroki WHERE class == ?', ('mag',)).fetchall()
    pl4 = cur.execute('SELECT * FROM Igroki WHERE class == ?', ('inginer',)).fetchall()
    pl1[0] = list(pl1[0])
    pl2[0] = list(pl2[0])
    pl3[0] = list(pl3[0])
    pl4[0] = list(pl4[0])
    if pl1[0][0] == pl2[0][0] == pl3[0][0] == pl4[0][0] == 'X':
        await message.channel.send('В вашем героическом преключении должен принимать участие хотя бы 1 игрок')
    else:
        await message.channel.send('Все готовы? Значит преключение начинается!')
        await message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        await message.channel.send('Наша история берёт начало в королевстве Элипод. Жизнь в нём текла размерено и '
                                   'счастливо до ближайшего времени. С окраин королевства поползли служи о некой '
                                   'тьме. Люди рассказывали как сначало солнце тускнело, а потом и вовсе пропадало, '
                                   'при этом луны также становилось не видно, из за чего вокруг всё погружалось в '
                                   'непроглядную темень, а потом приходили они. Ужасающие чудовища, в чьём поведении '
                                   'нельзя было усмотреть логики или какого либо смыса, но они превосходили любого '
                                   'воина числом и выносливостью. Со временем королевство прлностью погрузилось во '
                                   'тьму. Но группа авантюристов решила избавить королевство от этого проклятья. Они '
                                   'пообещали уничтожить всех монстров, что будут ими найдены та территории '
                                   'королевства')
        await message.channel.send('Вы собираетесь в таверне, здесь вы можете восстановить силы и закупить'
                                   ' вещи ("Buy_Grenade(100)/Hpp(75)/Manap(50)_)')
        await message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        if pl1[0][0] == 'X':
            pl1 = None
        if pl2[0][0] == 'X':
            pl2 = None
        if pl3[0][0] == 'X':
            pl3 = None
        if pl4[0][0] == 'X':
            pl4 = None
        Nab = False

@bot.command()
async def Save(ctx: commands.context):
    global step, sf, bue
    if sf == False and bue == True:
        await ctx.message.channel.send('Подождите')
        if pl1 is not None:
            cur.execute('DELETE FROM Igroki where class == ?', ('voin',))
            cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (pl1[0][0], pl1[0][1], pl1[0][2], pl1[0][3],
                                                                                    pl1[0][4], pl1[0][5], pl1[0][6], pl1[0][7], str(step), pl1[0][8]))
        if pl2 is not None:
            cur.execute('DELETE FROM Igroki where class == ?', ('luchnik',))
            cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (pl2[0][0], pl2[0][1], pl2[0][2], pl2[0][3],
                                                                                    pl2[0][4], pl2[0][5], pl2[0][6], pl2[0][7], str(step), pl2[0][8]))
        if pl3 is not None:
            cur.execute('DELETE FROM Igroki where class == ?', ('mag',))
            cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (pl3[0][0], pl3[0][1], pl3[0][2], pl3[0][3],
                                                                                    pl3[0][4], pl3[0][5], pl3[0][6], pl3[0][7], str(step), pl3[0][8]))
        if pl4 is not None:
            cur.execute('DELETE FROM Igroki where class == ?', ('inginer',))
            cur.execute('INSERT INTO Igroki VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (pl4[0][0], pl4[0][1], pl4[0][2], pl4[0][3],
                                                                                    pl4[0][4], pl4[0][5], pl4[0][6], pl4[0][7], str(step), pl4[0][8]))
        await ctx.message.channel.send('Игра сохранена!')
    else:
        await ctx.message.channel.send('Вы не можете сохранить игру сейчас')


@bot.command()
async def Load(ctx:commands.context):
    global pl1,pl2,pl3,pl4
    await ctx.message.channel.send('Подождите')
    pl1 = cur.execute('SELECT * FROM Igroki WHERE class == ?', ('voin',)).fetchall()
    pl2 = cur.execute('SELECT * FROM Igroki WHERE class == ?', ('luchnik',)).fetchall()
    pl3 = cur.execute('SELECT * FROM Igroki WHERE class == ?', ('mag',)).fetchall()
    pl4 = cur.execute('SELECT * FROM Igroki WHERE class == ?', ('inginer',)).fetchall()
    pl1[0] = list(pl1[0])
    pl2[0] = list(pl2[0])
    pl3[0] = list(pl3[0])
    pl4[0] = list(pl4[0])
    if pl1[0][0] == 'X':
        pl1 = None
    if pl2[0][0] == 'X':
        pl2 = None
    if pl3[0][0] == 'X':
        pl3 = None
    if pl4[0][0] == 'X':
        pl4 = None
    await ctx.message.channel.send('Игра загружена')


@bot.command()
async def Showinv(ctx: commands.context):
    global pl1, pl2, pl3, pl4
    sp = []
    if pl1 is not None:
        zn = pl1[0][7].split(':')
        sp.append(f"Воин ({pl1[0][0]})|Зелья лечения:{zn[0]}, Зелья маны:{zn[1]}, Гранаты:{zn[2]}, Золото:{pl1[0][6]}|")
    if pl2 is not None:
        zn = pl2[0][7].split(':')
        sp.append(f"Лучник ({pl2[0][0]})|Зелья лечения:{zn[0]}, Зелья маны:{zn[1]}, Гранаты:{zn[2]}, Золото:{pl2[0][6]}|")
    if pl3 is not None:
        zn = pl3[0][7].split(':')
        sp.append(f"Маг ({pl3[0][0]})|Зелья лечения:{zn[0]}, Зелья маны:{zn[1]}, Гранаты:{zn[2]}, Золото:{pl3[0][6]}|")
    if pl4 is not None:
        zn = pl4[0][7].split(':')
        sp.append(f"Инжинер ({pl4[0][0]})|Зелья лечения:{zn[0]}, Зелья маны:{zn[1]}, Гранаты:{zn[2]}, Золото:{pl4[0][6]}|")
    for i in range(len(sp)):
        await ctx.message.channel.send(sp[i])

@bot.command()
async def Buy(cxt: commands.context):
    args = cxt.message.content.split(' ')
    global bue
    if bue is True:
        if args[2] == 'Voin':
            if args[1] == 'Hpp':
                if pl1[0][6] >= 75:
                    pl1[0][6] -= 75
                    zn = pl1[0][7].split(':')
                    zn[0] = str(int(zn[0]) + 1)
                    zn = ':'.join(zn)
                    pl1[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
            if args[1] == 'Manap':
                if pl1[0][6] >= 50:
                    pl1[0][6] -= 50
                    zn = pl1[0][7].split(':')
                    zn[1] = str(int(zn[1]) + 1)
                    zn = ':'.join(zn)
                    pl1[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
            if args[1] == 'Grenade':
                if pl1[0][6] >= 100:
                    pl1[0][6] -= 100
                    zn = pl1[0][7].split(':')
                    zn[2] = str(int(zn[2]) + 1)
                    zn = ':'.join(zn)
                    pl1[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
        if args[2] == 'Luchnik':
            if args[1] == 'Hpp':
                if pl2[0][6] >= 75:
                    pl2[0][6] -= 75
                    zn = pl2[0][7].split(':')
                    zn[0] = str(int(zn[0]) + 1)
                    zn = ':'.join(zn)
                    pl2[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
            if args[1] == 'Manap':
                if pl2[0][6] >= 50:
                    pl2[0][6] -= 50
                    zn = pl2[0][7].split(':')
                    zn[1] = str(int(zn[1]) + 1)
                    zn = ':'.join(zn)
                    pl2[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
            if args[1] == 'Grenade':
                if pl2[0][6] >= 100:
                    pl2[0][6] -= 100
                    zn = pl2[0][7].split(':')
                    zn[2] = str(int(zn[2]) + 1)
                    zn = ':'.join(zn)
                    pl2[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
        if args[2] == 'Mag':
            if args[1] == 'Hpp':
                if pl3[0][6] >= 75:
                    pl3[0][6] -= 75
                    zn = pl3[0][7].split(':')
                    zn[0] = str(int(zn[0]) + 1)
                    zn = ':'.join(zn)
                    pl3[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
            if args[1] == 'Manap':
                if pl3[0][6] >= 50:
                    pl3[0][6] -= 50
                    zn = pl3[0][7].split(':')
                    zn[1] = str(int(zn[1]) + 1)
                    zn = ':'.join(zn)
                    pl3[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
            if args[1] == 'Grenade':
                if pl3[0][6] >= 100:
                    pl3[0][6] -= 100
                    zn = pl3[0][7].split(':')
                    zn[2] = str(int(zn[2]) + 1)
                    zn = ':'.join(zn)
                    pl3[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
        if args[2] == 'Inginer':
            if args[1] == 'Hpp':
                if pl4[0][6] >= 75:
                    pl4[0][6] -= 75
                    zn = pl4[0][7].split(':')
                    zn[0] = str(int(zn[0]) + 1)
                    zn = ':'.join(zn)
                    pl4[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
            if args[1] == 'Manap':
                if pl4[0][6] >= 50:
                    pl4[0][6] -= 50
                    zn = pl4[0][7].split(':')
                    zn[1] = str(int(zn[1]) + 1)
                    zn = ':'.join(zn)
                    pl4[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
            if args[1] == 'Grenade':
                if pl4[0][6] >= 100:
                    pl4[0][6] -= 100
                    zn = pl4[0][7].split(':')
                    zn[2] = str(int(zn[2]) + 1)
                    zn = ':'.join(zn)
                    pl4[0][7] = zn
                    await cxt.message.channel.send('Покупка удачна')
                else:
                    await cxt.message.channel.send('Недостаточно золота')
    else:
        await cxt.message.channel.send('Вам негде купить предметы')
    await cxt.message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')





@bot.command()
async def SpAttack(ctx: commands.context):
    global sf, att, clas, coordsf, pl1, pl2, pl3, pl4, enemies, enemiesst, att, hod
    args = ctx.message.content.split(' ')
    if sf is True:
        if att is True:
            if clas == 'plf1':
                if pl1[0][5] - 50 >= 0:
                    enem = coordsf[int(args[2]) - 1][int(args[1]) - 1]
                    if type(enem) == str:
                        pl1[0][5] -= 50
                        for i in range(len(enemies)):
                            if enem == enemies[i]:
                                rand = random.randint(0, 100)
                                enemiesst[i][1] -= rand
                                await ctx.message.channel.send(f'Вы нанесли {rand} урона')
                                show_field(coordsf, [int(args[1]) - 1, int(args[2]) - 1], [int(args[1]) - 1,
                                                                                           int(args[2]) - 1, 'pl1'])
                                await ctx.message.channel.send(file=discord.File('fightim.png'))
                                att = False
                                break
                        hpbar = Hpbar(enemies, enemiesst)
                        hod = True
                        for j in range(len(hpbar)):
                            await ctx.message.channel.send(hpbar[j])
                    else:
                        await ctx.message.channel.send('нет противника')
                else:
                    await ctx.message.channel.send('Не хватает маны')
            if clas == 'plf2':
                if pl2[0][5] - 45 >= 0:
                    enem = coordsf[int(args[2]) - 1][int(args[1]) - 1]
                    if type(enem) == str:
                        pl2[0][5] -= 45
                        for i in range(len(enemies)):
                            if enem == enemies[i]:
                                rand = enemiesst[i][1] // 2
                                enemiesst[i][1] -= rand
                                await ctx.message.channel.send(f'Вы нанесли {rand} урона')
                                show_field(coordsf, [int(args[1]) - 1, int(args[2]) - 1], '')
                                await ctx.message.channel.send(file=discord.File('fightim.png'))
                                att = False
                                break
                        hpbar = Hpbar(enemies, enemiesst)
                        hod = True
                        for j in range(len(hpbar)):
                            await ctx.message.channel.send(hpbar[j])
                    else:
                        await ctx.message.channel.send('нет противника')
                else:
                    await ctx.message.channel.send('Не хватает маны')
            if clas == 'plf3':
                if pl3[0][5] - 50 >= 0:
                    pl3[0][5] -= 50
                    coordsf[int(args[2]) - 1][int(args[1]) - 1], coordsf[int(args[4]) - 1][int(args[3]) - 1] \
                        = coordsf[int(args[4]) - 1][int(args[3]) - 1], coordsf[int(args[2]) - 1][int(args[1]) - 1]
                    show_field(coordsf, [int(args[4]) - 1, int(args[3]) - 1],
                               [int(args[4]) - 1, int(args[3]) - 1, 'pl3'])
                    await ctx.message.channel.send(file=discord.File('fightim.png'))
                    att = False
                    hpbar = Hpbar(enemies, enemiesst)
                    hod = True
                    for j in range(len(hpbar)):
                        await ctx.message.channel.send(hpbar[j])
                else:
                    await ctx.message.channel.send('Не хватает маны')
            if clas == 'plf4':
                if pl4[0][5] - 100 >= 0:
                    pl4[0][5] -= 50
                    zn = pl4[0][7].split(':')
                    zn[2] = str(int(zn[2]) + 1)
                    zn = ':'.join(zn)
                    pl4[0][7] = zn
                    hod = True
                    att = False
                else:
                    await ctx.message.channel.send('Не хватает маны')
            if hod is True:
                name = yourhod(pl1, pl2, pl3, pl4)
                await ctx.message.channel.send(f"{name}, твой ход")
    await ctx.message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')


@bot.command()
async def Go(ctx: commands.context):
    global pl1, pl2, pl3, pl4, sf, bue, Fight, step
    step += 1
    if Fight is False:
        if sf is False:
            mesto = random.randint(0, 5)
            if mesto == 1:
                await ctx.message.channel.send('Из-за безконечно тянущихся мокрых ветвей деревьев начинает '
                                               'пробиваться тусклый свет, не проходит и пяти минут как из-за одного '
                                               'из деревьев выглядывает старая покосившаяся лочуга. Зайдя во внутрь, '
                                               'вы обнаруживаете что это таверна. Наконец то вы сможете отдохнуть и '
                                               'пополнить свои припасы')
                await ctx.message.channel.send(file=discord.File('tavern___concept_art_by_baukjespirit-d8z7n70.png'))
                bue = True
            else:
                Fight = True
                bue = False
                await ctx.message.channel.send('Вы идёте по тёмному лесу. Тьма смыкается перед вами. Вдруг вы слышите '
                                               'жуткий вопль. Несомненно, пора готовиться к битве!')
                await ctx.message.channel.send(file=discord.File('og_og_1455632740277065403.png'))
    else:
        await ctx.message.channel.send('Вы не можете перемещаться во время боя')
    await ctx.message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')


@bot.command()
async def Leave(ctx: commands.context):
    global enemies, Fight, pl1, pl2, pl3, pl4, sf
    g = 0
    for i in range(len(enemies)):
        if enemies[i] == 'dead':
            g += 1
    if len(enemies) == g:
        if pl1 is not None:
            pl1[0][6] += 100
        if pl2 is not None:
            pl2[0][6] += 100
        if pl3 is not None:
            pl3[0][6] += 100
        if pl4 is not None:
            pl4[0][6] += 100
        sf = False
        Fight = False
        await ctx.message.channel.send('ВЫ победили. Награда: 100 золота')
    else:
        if pl1 is not None:
            await ctx.message.channel.send(f"Воин {pl1[0][0]} пожертововал собой чтобы вы смогли уйти")
            pl1 = None
        else:
            if pl2 is not None:
                await ctx.message.channel.send(f"Лучник {pl2[0][0]} пожертововал собой чтобы вы смогли уйти")
                pl2 = None
            else:
                if pl3 is not None:
                    await ctx.message.channel.send(f"Маг {pl3[0][0]} пожертововал собой чтобы вы смогли уйти")
                    pl3 = None
                else:
                    if pl4 is not None:
                        await ctx.message.channel.send(f"Инжинер {pl4[0][0]} пожертововал собой чтобы вы смогли уйти")
                        pl4 = None
        sf = False
        Fight = False
    await ctx.message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')


@bot.command()
async def EnemyHod(ctx: commands.context):
    global coordsf, enemies, pl1, pl2, pl3, pl4, enemiesst, hod, att
    hod = True
    pk1 = (-1, -1)
    pk2 = (-1, -1)
    pk3 = (-1, -1)
    pk4 = (-1, -1)
    if sf is True:
        for j in range(5):
            for k in range(21):
                if coordsf[j][k] == 'plf1':
                    pk1 = (k + 1, j + 1)
                if coordsf[j][k] == 'plf2':
                    pk2 = (k + 1, j + 1)
                if coordsf[j][k] == 'plf3':
                    pk3 = (k + 1, j + 1)
                if coordsf[j][k] == 'plf4':
                    pk4 = (k + 1, j + 1)
        att = False
        for i in range(len(enemies)):
            enem = enemies[i]
            for j in range(5):
                for k in range(21):
                    if coordsf[j][k] == enem:
                        enemk = [k, j]
            spa = coord(enemk[0] + 1, enemk[1] + 1)
            for p in range(len(spa)):
                if spa[p] == pk1:
                    ath = random.randint(enemiesst[i][2][0], enemiesst[i][2][1])
                    pl1[0][3] -= ath
                    att = True
                    show_field(coordsf, [spa[p][0] - 1, spa[p][2] - 1], '')
                    await ctx.message.channel.send(file=discord.File('fightim.png'))
                else:
                    if spa[p] == pk2:
                        ath = random.randint(enemiesst[i][1][0], enemiesst[i][2][1])
                        pl2[0][3] -= ath
                        att = True
                        show_field(coordsf, [spa[p][0] - 1, spa[p][1] - 1], '')
                        await ctx.message.channel.send(file=discord.File('fightim.png'))
                    else:
                        if spa[p] == pk3:
                            ath = random.randint(enemiesst[i][2][0], enemiesst[i][2][1])
                            pl3[0][3] -= ath
                            att = True
                            show_field(coordsf, [spa[p][0] - 1, spa[p][1] - 1], '')
                            await ctx.message.channel.send(file=discord.File('fightim.png'))
                        else:
                            if spa[p] == pk4:
                                ath = random.randint(enemiesst[i][2][0], enemiesst[i][2][1])
                                pl4[0][3] -= ath
                                att = True
                                show_field(coordsf, [spa[p][0] - 1, spa[p][1] - 1], '')
                                await ctx.message.channel.send(file=discord.File('fightim.png'))
            if att is False:
                if pk1[1] == enemk[1] or pk2[1] == enemk[1] or pk3[1] == enemk[1] or pk4[1] == enemk[1]:
                    if pk1[0] != 0 and type(coordsf[enemk[1]][enemk[0] - 1]) == int:
                        coordsf[enemk[1]][enemk[0]] = 0
                        coordsf[enemk[1]][enemk[0] - 1] = enem
                        enemk[0] -= 1
                        show_field(coordsf, '', '')
                        await ctx.message.channel.send(file=discord.File('fightim.png'))
                else:
                    if enemk[1] != 0 and enemk[0] != 0:
                        if type(coordsf[enemk[1] - 1][enemk[0] - 1]) == int:
                            coordsf[enemk[1]][enemk[0]] = 0
                            coordsf[enemk[1] - 1][enemk[0] - 1] = enem
                            enemk[1] -= 1
                            enemk[0] -= 1
                            show_field(coordsf, '', '')
                            await ctx.message.channel.send(file=discord.File('fightim.png'))
                    else:
                        if enemk[0] != 0 and enemk[1] != 4:
                            if type(coordsf[enemk[1] + 1][enemk[0] - 1]) == int:
                                coordsf[enemk[1]][enemk[0]] = 0
                                coordsf[enemk[1] + 1][enemk[0] - 1] = enem
                                enemk[1] += 1
                                enemk[0] -= 1
                                show_field(coordsf, '', '')
                                await ctx.message.channel.send(file=discord.File('fightim.png'))
                        else:
                            spa = coord(enemk[0] + 1, enemk[1] + 1)
                            for p in range(len(spa)):
                                if spa[p] == pk1:
                                    ath = random.randint(enemiesst[i][2][0], enemiesst[i][2][1])
                                    pl1[0][3] -= ath
                                    show_field(coordsf, [spa[p][0] - 1, spa[p][2] - 1], '')
                                    await ctx.message.channel.send(file=discord.File('fightim.png'))
                                else:
                                    if spa[p] == pk2:
                                        ath = random.randint(enemiesst[i][1][0], enemiesst[i][2][1])
                                        pl2[0][3] -= ath
                                        show_field(coordsf, [spa[p][0] - 1, spa[p][1] - 1], '')
                                        await ctx.message.channel.send(file=discord.File('fightim.png'))
                                    else:
                                        if spa[p] == pk3:
                                            ath = random.randint(enemiesst[i][2][0], enemiesst[i][2][1])
                                            pl3[0][3] -= ath

                                            show_field(coordsf, [spa[p][0] - 1, spa[p][1] - 1], '')
                                            await ctx.message.channel.send(file=discord.File('fightim.png'))
                                        else:
                                            if spa[p] == pk4:
                                                ath = random.randint(enemiesst[i][2][0], enemiesst[i][2][1])
                                                pl4[0][3] -= ath
                                                show_field(coordsf, [spa[p][0] - 1, spa[p][1] - 1])
                                                await ctx.message.channel.send(file=discord.File('fightim.png'))
                                            else:
                                                show_field(coordsf, '', '')
                                                await ctx.message.channel.send(file=discord.File('fightim.png'))
        for j in range(5):
            for i in range(21):
                if coordsf[j][i] == 'plf1':
                    if pl1[0][3] <= 0:
                        coordsf[j][i] = 0
                        await ctx.message.channel.send(f'Воин {pl1[0][0]} погиб')
                        pl1 = None
                if coordsf[j][i] == 'plf2':
                    if pl2[0][3] <= 0:
                        coordsf[j][i] = 0
                        await ctx.message.channel.send(f'Лучник {pl2[0][0]} погиб')
                        pl2 = None
                if coordsf[j][i] == 'plf3':
                    if pl3[0][3] <= 0:
                        coordsf[j][i] = 0
                        await ctx.message.channel.send(f'Маг {pl3[0][0]} погиб')
                        pl3 = None
                if coordsf[j][i] == 'plf4':
                    if pl4[0][3] <= 0:
                        coordsf[j][i] = 0
                        await ctx.message.channel.send(f'Инжинер {pl4[0][0]} погиб')
                        pl4 = None
        if pl1 is None and pl2 is None and pl3 is None and pl4 is None:
            ctx.message.channel.send('Весь ваш отряд мёртв, игра окончена')
            exit()
        stat = YHpbar(pl1, pl2, pl3, pl4)
        for l in range(len(stat)):
            await ctx.message.channel.send(stat[l])
        att = False
        name = yourhod(pl1, pl2, pl3, pl4)
        await ctx.message.channel.send(f"{name}, твой ход!")
    else:
        await ctx.message.channel.send('Сейчас не идёт бой')
    await ctx.message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')


@bot.command()
async def Use(ctx: commands.context):
    global pl1, pl2, pl3, pl4, clas, coordsf, enemies, enemiesst, hod, att
    args = ctx.message.content.split(' ')
    if sf is True:
        if hod is True and att is False:
            if args[1] == 'Hpp':
                if clas == 'plf1':
                    if int(pl1[0][7].split(':')[0]) > 0:
                        zn = pl1[0][7].split(':')
                        zn[0] = str(int(zn[0]) - 1)
                        zn = ':'.join(zn)
                        pl1[0][7] = zn
                        rhp = pl1[0][2] - pl1[0][3]
                        if rhp < 100:
                            await ctx.message.channel.send(f'Вы восстановили {rhp}хп')
                            pl1[0][3] = pl1[0][2]
                        else:
                            await ctx.message.channel.send(f'Вы восстановили 100 хп')
                            pl1[0][3] += 100
                    else:
                        await ctx.message.channel.send('У вас не достаточно зелий лечения')
                if clas == 'plf2':
                    if (pl2[0][7].split(':')[0]) > 0:
                        zn = pl2[0][7].split(':')
                        zn[0] = str(int(zn[0]) - 1)
                        zn = ':'.join(zn)
                        pl2[0][7] = zn
                        rhp = pl2[0][2] - pl2[0][3]
                        if rhp < 100:
                            await ctx.message.channel.send(f'Вы восстановили {rhp}хп')
                            pl2[0][3] = pl2[0][2]
                        else:
                            await ctx.message.channel.send(f'Вы восстановили 100 хп')
                    else:
                        await ctx.message.channel.send('У вас не достаточно зелий лечения')
                if clas == 'plf3':
                    if int(pl3[0][7].split(':')[0]) > 0:
                        zn = pl3[0][7].split(':')
                        zn[0] = str(int(zn[0]) - 1)
                        zn = ':'.join(zn)
                        pl3[0][7] = zn
                        rhp = pl3[0][2] - pl3[0][3]
                        if rhp < 100:
                            await ctx.message.channel.send(f'Вы восстановили {rhp}хп')
                            pl3[0][3] = pl3[0][2]
                        else:
                            await ctx.message.channel.send(f'Вы восстановили 100 хп')
                            pl3[0][3] += 100
                    else:
                        await ctx.message.channel.send('У вас не достаточно зелий лечения')
                if clas == 'plf4':
                    if int(pl4[0][7].split(':')[0]) > 0:
                        zn = pl4[0][7].split(':')
                        zn[0] = str(int(zn[0]) - 1)
                        zn = ':'.join(zn)
                        pl4[0][7] = zn
                        rhp = pl4[0][2] - pl4[0][3]
                        if rhp < 100:
                            await ctx.message.channel.send(f'Вы восстановили {rhp}хп')
                            pl4[0][3] = pl4[0][2]
                        else:
                            await ctx.message.channel.send(f'Вы восстановили 100 хп')
                            pl4[0][3] += 100
                    else:
                        await ctx.message.channel.send('У вас не достаточно зелий лечения')
                stat = YHpbar(pl1, pl2, pl3, pl4)
                for l in range(len(stat)):
                    await ctx.message.channel.send(stat[l])
                name = yourhod(pl1, pl2, pl3, pl4)
                await ctx.message.channel.send(f"{name}, твой ход!")
            if args[1] == 'Manap':
                if clas == 'plf1':
                    if int(pl1[0][7].split(':')[1]) > 0:
                        zn = pl1[0][7].split(':')
                        zn[1] = str(int(zn[1]) - 1)
                        zn = ':'.join(zn)
                        pl1[0][7] = zn
                        rma = pl1[0][4] - pl1[0][5]
                        if rma < 75:
                            await ctx.message.channel.send(f'Вы восстановили {rma}маны')
                            pl1[0][5] = pl1[0][4]
                        else:
                            await ctx.message.channel.send(f'Вы восстановили 75 маны')
                            pl1[0][5] += 75
                    else:
                        await ctx.message.channel.send('У вас не достаточно зелий маны')
                if clas == 'plf2':
                    if int(pl2[0][7].split(':')[1]) > 0:
                        zn = pl2[0][7].split(':')
                        zn[1] = str(int(zn[1]) - 1)
                        zn = ':'.join(zn)
                        pl2[0][7] = zn
                        rma = pl2[0][4] - pl2[0][5]
                        if rma < 75:
                            await ctx.message.channel.send(f'Вы восстановили {rma}маны')
                            pl2[0][5] = pl2[0][4]
                        else:
                            await ctx.message.channel.send(f'Вы восстановили 75 маны')
                            pl2[0][5] += 75
                    else:
                        await ctx.message.channel.send('У вас не достаточно зелий маны')
                if clas == 'plf3':
                    if int(pl3[0][7].split(':')[1]) > 0:
                        zn = pl3[0][7].split(':')
                        zn[1] = str(int(zn[1]) - 1)
                        zn = ':'.join(zn)
                        pl3[0][7] = zn
                        rma = pl3[0][4] - pl3[0][5]
                        if rma < 75:
                            await ctx.message.channel.send(f'Вы восстановили {rma}маны')
                            pl3[0][5] = pl3[0][4]
                        else:
                            await ctx.message.channel.send(f'Вы восстановили 75 маны')
                            pl3[0][5] += 75
                    else:
                        await ctx.message.channel.send('У вас не достаточно зелий маны')
                if clas == 'plf4':
                    if int(pl4[0][7].split(':')[1]) > 0:
                        zn = pl4[0][7].split(':')
                        zn[1] = str(int(zn[1]) - 1)
                        zn = ':'.join(zn)
                        pl4[0][7] = zn
                        rma = pl4[0][4] - pl4[0][5]
                        if rma < 75:
                            await ctx.message.channel.send(f'Вы восстановили {rma}маны')
                            pl4[0][5] = pl4[0][4]
                        else:
                            await ctx.message.channel.send(f'Вы восстановили 75 маны')
                            pl4[0][5] += 75
                    else:
                        await ctx.message.channel.send('У вас не достаточно зелий маны')
                    stat = YHpbar(pl1, pl2, pl3, pl4)
                    for l in range(len(stat)):
                        await ctx.message.channel.send(stat[l])
                    name = yourhod(pl1, pl2, pl3, pl4)
                    await ctx.message.channel.send(f"{name}, твой ход!")
            if args[1] == 'Grenade':
                enem = coordsf[int(args[3]) - 1][int(args[2]) - 1]
                if clas == 'plf1':
                    if int(pl1[0][7].split(':')[2]) > 0:
                        zn = pl1[0][7].split(':')
                        zn[2] = str(int(zn[2]) - 1)
                        zn = ':'.join(zn)
                        pl1[0][7] = zn
                        non = False
                    else:
                        non = True
                if clas == 'plf2':
                    if int(pl2[0][7].split(':')[2]) > 0:
                        zn = pl2[0][7].split(':')
                        zn[2] = str(int(zn[2]) - 1)
                        zn = ':'.join(zn)
                        pl2[0][7] = zn
                        non = False
                    else:
                        non = True
                if clas == 'plf3':
                    if int(pl3[0][7].split(':')[2]) > 0:
                        zn = pl3[0][7].split(':')
                        zn[2] = str(int(zn[2]) - 1)
                        zn = ':'.join(zn)
                        pl3[0][7] = zn
                        non = False
                    else:
                        non = True
                if clas == 'plf4':
                    if int(pl4[0][7].split(':')[2]) > 0:
                        zn = pl4[0][7].split(':')
                        zn[2] = str(int(zn[2]) - 1)
                        zn = ':'.join(zn)
                        pl4[0][7] = zn
                        non = False
                    else:
                        non = True
                if non is False:
                    if type(enem) == str:
                        ran = random.randint(0, 10)
                        if ran >= 5:
                            for i in range(len(enemies)):
                                if enem == enemies[i]:
                                    enemiesst[i][1] -= 100
                                    await ctx.message.channel.send('Граната взорвалась')
                                    break
                        else:
                            await ctx.message.channel.send('Граната не взорвалась')
                        hpbar = Hpbar(enemies, enemiesst)
                        for j in range(len(hpbar)):
                            await ctx.message.channel.send(hpbar[j])
                        name = yourhod(pl1, pl2, pl3, pl4)
                        await ctx.message.channel.send(f"{name}, твой ход!")
                    else:
                        await ctx.message.channel.send('Вы промахнулисы гранатой')
                        name = yourhod(pl1, pl2, pl3, pl4)
                        await ctx.message.channel.send(f"{name}, твой ход!")
                else:
                    await ctx.message.channel.send('У вас недостаточно гранат')
        else:
            await ctx.message.channel.send('Вы не можете сейчас исрользовать предметы из инвенторя')
    else:
        await ctx.message.channel.send('Сейчас не идёт бой')
    await ctx.message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')


@bot.command()
async def Hod(ctx: commands.context):
    global clas, hod, coordsf, att
    args = ctx.message.content.split(' ')
    if sf is True:
        if hod is True:
            if args[1] != 'skip':
                for i in range(5):
                    for j in range(21):
                        if coordsf[i][j] == clas and 1 <= int(args[1]) <= 21 and 1 <= int(args[2]) <= 5 \
                                and (int(args[1]), int(args[2])) in coord(j + 1, i + 1) and type(coordsf[i][j]) != int:
                            coordsf[i][j] = 0
                            coordsf[int(args[2]) - 1][int(args[1]) - 1] = clas
                            show_field(coordsf, '', '')
                            await ctx.message.channel.send(file=discord.File('fightim.png'))
                            att = True
                            hod = False
                            await ctx.message.channel.send(
                                '=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                            return
                        else:
                            if coordsf[i][j] == clas:
                                await ctx.message.channel.send('Вы не можете совершить этот ход')
            else:
                await ctx.message.channel.send('Вы пропустили перемещение')
                att = True
                hod = False
        else:
            await ctx.message.channel.send('Вы не можете передвигаться сейчас')
    else:
        await ctx.message.channel.send('Сейчас не идёт бой')
    await ctx.message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')


@bot.command()
async def Attack(ctx: commands.context):
    global clas, coordsf, enemies, enemiesst, pl1, pl2, pl3, pl4, att, hod
    args = ctx.message.content.split(' ')
    if sf is True:
        if att is True:
            if args[1] != 'skip':
                if clas == 'plf1' or clas == 'plf4':
                    for j in range(5):
                        for k in range(21):
                            if coordsf[j][k] == clas:
                                x = k
                                y = j
                                break
                    if coordsf[int(args[2]) - 1][int(args[1]) - 1] in enemies and (int(args[1]), int(args[2])) in coord(
                            x + 1, y + 1):
                        for i in range(len(enemies)):
                            if enemies[i] == coordsf[int(args[2]) - 1][int(args[1]) - 1]:
                                if clas == 'plf1':
                                    ran = random.randint(35, 55)
                                else:
                                    ran = random.randint(25, 35)
                                enemiesst[0][1] -= ran
                                if enemiesst[0][1] <= 0:
                                    coordsf[int(args[2]) - 1][int(args[1]) - 1] = 0
                                await ctx.message.channel.send(file=discord.File('fightim.png'))
                                await ctx.message.channel.send(f"Вы нанесли {ran} урона!")
                                await ctx.message.channel.send(f"{yourhod(pl1, pl2, pl3, pl4)}, твой ход!")
                                show_field(coordsf, '', '')
                                await ctx.message.channel.send(file=discord.File('fightim.png'))
                                hpbar = Hpbar(enemies, enemiesst)
                                for j in range(len(hpbar)):
                                    await ctx.message.channel.send(hpbar[j])
                                att = False
                                hod = True
                                await ctx.message.channel.send(
                                    '=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                                return
                    else:
                        await ctx.message.channel.send('Подобная атака невозможна')
                if clas == 'plf2' or clas == 'plf3':
                    if clas == 'plf1' or 'plf4' and args[1] != 'skip':
                        if coordsf[int(args[2]) - 1][int(args[1]) - 1] in enemies:
                            for i in range(len(enemies)):
                                if enemies[i] == coordsf[int(args[2]) - 1][int(args[1]) - 1]:
                                    if clas == 'plf2':
                                        ran = random.randint(35, 50)
                                    else:
                                        ran = random.randint(10, 40)
                                    enemiesst[0][1] -= ran
                                    if enemiesst[0][1] <= 0:
                                        coordsf[int(args[2]) - 1][int(args[1]) - 1] = 0
                                    show_field(coordsf, [int(args[1]) - 1, int(args[2]) - 1], '')
                                    await ctx.message.channel.send(file=discord.File('fightim.png'))
                                    await ctx.message.channel.send(f"Вы нанесли {ran} урона!")
                                    await ctx.message.channel.send(f"{yourhod(pl1, pl2, pl3, pl4)}, твой ход!")
                                    show_field(coordsf, '', '')
                                    await ctx.message.channel.send(file=discord.File('fightim.png'))
                                    hpbar = Hpbar(enemies, enemiesst)
                                    for j in range(len(hpbar)):
                                        await ctx.message.channel.send(hpbar[j])
                                    att = False
                                    hod = True
                                    await ctx.message.channel.send(
                                        '=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                                    return
            else:
                await ctx.message.channel.send('Вы пропустили атаку')
                att = False
                hod = True
            if hod is True:
                name = yourhod(pl1, pl2, pl3, pl4)
                await ctx.message.channel.send(f"{name}, твой ход!")
        else:
            await ctx.message.channel.send('Вы не можете сейчас атаковать')
    else:
        await ctx.message.channel.send('Сейчас не идёт бой')
    await ctx.message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')


@bot.command()
async def Sfight(message):
    global Fight, pl1, pl2, pl3, pl4, clas, hod, coordsf, p1, p2, p3, p4, enemies, enemiesst, sf
    if Fight is False:
        await message.channel.send('Невозможно начать битву')
    else:
        if sf is False:
            sf = True
            hod = True
            coordsf, enemies, enemiesst = Startf(pl1, pl2, pl3, pl4)
            show_field(coordsf, '', '')
            await message.channel.send('БИТВА НАЧАЛАСЬ!')
            await message.channel.send(file=discord.File('fightim.png'))
            if hod is True and pl1 is not None:
                await message.channel.send(f"{pl1[0][0]}, твой ход!")
                clas = 'plf1'
                p1 = False
            else:
                if hod is True and pl2 is not None:
                    await message.channel.send(f"{pl2[0][0]}, твой ход!")
                    clas = 'plf2'
                    p2 = False
                else:
                    if hod is True and pl3 is not None:
                        await message.channel.send(f"{pl3[0][0]}, твой ход!")
                        clas = 'plf3'
                        p3 = False
                    else:
                        if hod is True and pl4 is not None:
                            await message.channel.send(f"{pl4[0][0]}, твой ход!")
                            clas = 'plf4'
                            p4 = False
        else:
            await message.channel.send('Битва уже началась')
    await message.channel.send('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')


def yourhod(pl1, pl2, pl3, pl4):
    global p1, p2, p3, p4, clas, hod
    if pl1 is not None and p1 is not False:
        clas = 'plf1'
        p1 = False
        return pl1[0][0]
    else:
        p1 = False
        if pl2 is not None and p2 is not False:
            clas = 'plf2'
            p2 = False
            return pl2[0][0]
        else:
            p2 = False
            if pl3 is not None and p3 is not False:
                clas = 'plf3'
                p3 = False
                return pl3[0][0]
            else:
                p3 = False
                if pl4 is not None and p4 is not False:
                    clas = 'plf4'
                    p4 = False
                    return pl4[0][0]
                else:
                    p4 = False
                    if p1 is False and p2 is False and p3 is False and p4 is False:
                        p1 = True
                        p2 = True
                        p3 = True
                        p4 = True
                        hod = False
                        return 'enemy'


def Hpbar(enemise, enemiesst):
    stat = []
    dl = len(enemise)
    for i in range(len(enemise)):
        a = ''
        if enemise[i] == 'lifearm':
            a += 'Живая борня:['
        if enemise[i] == 'zombie':
            a += 'Зомби:['
        if enemise[i] == 'sceleton':
            a += 'Скелкт:['
        if enemiesst[i][1] > 0:
            a += str(enemiesst[i][0]) + '/' + str(enemiesst[i][1]) + ']'
            stat.append(a)
        else:
            enemise[i] = 'dead'
            enemiesst[i] = 'dead'
            dl -= 1
    p = 0
    while p != dl:
        if enemise[p] == 'dead':
            del enemise[p]
            del enemiesst[p]
            dl -= 1
        else:
            p += 1

    return stat


def YHpbar(pl1, pl2, pl3, pl4):
    stat = []
    if pl1 is not None:
        a = f"Воин {pl1[0][0]}|HP:[{pl1[0][2]}/{pl1[0][3]}]|Mana:[{pl1[0][4]}/{pl1[0][5]}]|"
        stat.append(a)
    if pl2 is not None:
        a = f"Лучник {pl2[0][0]}|HP:[{pl2[0][2]}/{pl2[0][3]}]|Mana:[{pl2[0][4]}/{pl2[0][5]}]|"
        stat.append(a)
    if pl3 is not None:
        a = f"Маг {pl3[0][0]}|HP:[{pl3[0][2]}/{pl3[0][3]}]|Mana:[{pl3[0][4]}/{pl3[0][5]}]|"
        stat.append(a)
    if pl4 is not None:
        a = f"Инжинер {pl4[0][0]}|HP:[{pl4[0][2]}/{pl4[0][3]}]|Mana:[{pl4[0][4]}/{pl4[0][5]}]|"
        stat.append(a)
    return stat


def Startf(pl1, pl2, pl3, pl4):
    enemis = []
    enemisst = []
    y = 0
    coordsf = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]]
    for i in range(random.randint(1, 4)):
        ran = random.randint(1, 3)
        if ran == 1 and 'lifearm' not in enemis:
            enemis.append('lifearm')
            enemisst.append([200, 200, [25, 35]])
        if ran == 2 and 'zombie' not in enemis:
            enemis.append('zombie')
            enemisst.append([100, 100, [35, 45]])
        if ran == 3 and 'sceleton' not in enemis:
            enemis.append('sceleton')
            enemisst.append([150, 150, [30, 40]])
    for i in range(len(enemis)):
        coordsf[y][-1] = enemis[i]
        y += 1
    if pl1 is not None:
        coordsf[0][0] = 'plf1'
    if pl2 is not None:
        coordsf[1][0] = 'plf2'
    if pl3 is not None:
        coordsf[2][0] = 'plf3'
    if pl4 is not None:
        coordsf[3][0] = 'plf4'
    return coordsf, enemis, enemisst


def show_field(coordsf, cordat, cordsp):
    global turel
    if cordsp != '':
        if cordsp[2] == 'pl1':
            del cordsp[2]
            im3 = Image.open('spel1.png').convert("RGBA")
        else:
            if cordsp[2] == 'pl3':
                del cordsp[2]
                im3 = Image.open('spel2.png').convert("RGBA")
    im1 = Image.open("pole.jpg")
    if turel is True:
        im1.paste(Image.open(''))
    for y in range(5):
        for x in range(21):
            if coordsf[y][x] == 'plf1':
                if cordat == [x, y]:
                    im2 = Image.open('voinat.png').convert("RGBA")
                else:
                    im2 = Image.open('voin.png').convert("RGBA")
                cord = spcord[y][x]
                im1.paste(im2, (cord[0] - 30, cord[1] - 130), im2)
                im1.save('fightim.png')
                im1 = Image.open('fightim.png')
            if coordsf[y][x] == 'plf2':
                if cordat == [x, y]:
                    im2 = Image.open('luchnikat.png').convert("RGBA")
                else:
                    im2 = Image.open('luchnik.png').convert("RGBA")
                cord = spcord[y][x]
                im1.paste(im2, (cord[0] - 30, cord[1] - 130), im2)
                im1.save('fightim.png')
                im1 = Image.open('fightim.png')
            if coordsf[y][x] == 'plf3':
                if cordat == [x, y]:
                    im2 = Image.open('magat.png').convert("RGBA")
                else:
                    im2 = Image.open('mag.png').convert("RGBA")
                cord = spcord[y][x]
                im1.paste(im2, (cord[0] - 30, cord[1] - 130), im2)
                im1.save('fightim.png')
                im1 = Image.open('fightim.png')
            if coordsf[y][x] == 'plf4':
                if cordat == [x, y]:
                    im2 = Image.open('inginerat.png').convert("RGBA")
                else:
                    im2 = Image.open('inginer.png').convert("RGBA")
                cord = spcord[y][x]
                im1.paste(im2, (cord[0] - 30, cord[1] - 130), im2)
                im1.save('fightim.png')
                im1 = Image.open('fightim.png')
            if coordsf[y][x] == 'lifearm':
                if cordat == [x, y] and cordat == cordsp:
                    im2 = Image.open('lifearmorat.png').convert("RGBA")
                    im2.paste(im3, (0, 0), im3)
                else:
                    if cordat == [x, y]:
                        im2 = Image.open('lifearmorat.png').convert("RGBA")
                    else:
                        im2 = Image.open('lifearmor.png').convert("RGBA")
                cord = spcord[y][x]
                im1.paste(im2, (cord[0] - 30, cord[1] - 130), im2)
                im1.save('fightim.png')
                im1 = Image.open('fightim.png')
            if coordsf[y][x] == 'zombie':
                if cordat == [x, y] and cordat == cordsp:
                    im2 = Image.open('zombieat.png').convert("RGBA")
                    im2.paste(im3, (0, 0), im3)
                else:
                    if cordat == [x, y]:
                        im2 = Image.open('zombieat.png').convert("RGBA")
                    else:
                        im2 = Image.open('zombie.png').convert("RGBA")
                cord = spcord[y][x]
                im1.paste(im2, (cord[0] - 30, cord[1] - 130), im2)
                im1.save('fightim.png')
                im1 = Image.open('fightim.png')
            if coordsf[y][x] == 'sceleton':
                if cordat == [x, y] and cordat == cordsp:
                    im2 = Image.open('sceletonat.png').convert("RGBA")
                    im2.paste(im3, (0, 0), im3)
                else:
                    if cordat == [x, y]:
                        im2 = Image.open('sceletonat.png').convert("RGBA")
                    else:
                        im2 = Image.open('sceleton.png').convert("RGBA")
                cord = spcord[y][x]
                im1.paste(im2, (cord[0] - 30, cord[1] - 130), im2)
                im1.save('fightim.png')
                im1 = Image.open('fightim.png')


bot.run('OTU4Nzc5ODYwODAzODA1MjI1.YkSTVA.lDAI-H34GZPfEODM2OAsp9RBUnU')
