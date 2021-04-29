import asyncio
from json import encoder
import threading
import time
import discord
from discord.ext import tasks
import schedule
import math
import os
import sys
import types
import json
import random
import datetime
import subprocess
from googletrans import Translator
import socket
import threading
import xml.etree.ElementTree as ET
import importlib

intents = discord.Intents.default()
intents.members = True

#げっちコーナー


class Main:
    def __init__(self):
        super().__init__()
        self.prifix = []
        self.EVENT = [">>success>>","Error:type:exists","<< Error:type:RecvData <<","Error:type:NotEntry","Error:Exception<SEND> ","SCES<SEND> "]
        self.Sdata = "STARTUP"
        self.Rdata = ""
        self.server_status = False
    def input_data(self):
        while True:
            self.Sdata = input("")
    def start(self):
        self.__CNCT = threading.Thread(target=self.__contact)
        self.__CNCT.start()
    def check_contact(self):
        IP = socket.gethostbyname(socket.gethostname())
        PORT = 48123
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                try:
                    s.connect((IP, PORT))
                except ConnectionRefusedError:
                    print("< SystemError >\n'接続できませんでした。'")
                    self.server_status = False
                    return
            except ConnectionAbortedError:
                print("< SystemError >\n'接続できませんでした。'")
                self.server_status = False
                return
    def __contact(self):
        IP = socket.gethostbyname(socket.gethostname())
        PORT = 48123
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((IP, PORT))
            except ConnectionRefusedError:
                print("< SystemError >\n'接続できませんでした。'")
                self.__CNCT._delete()
                self.server_status = False
                return
            self.server_status = True
            while True:
                if self.Sdata != None:
                    try:
                        try:
                            s.sendall(self.Sdata.encode())
                            data = s.recv(1024)
                        except ConnectionResetError:
                            print("< SystemError >\n'接続が遮断されました'")
                            self.__CNCT._delete()
                            self.server_status = False
                            return
                    except ConnectionAbortedError:
                        print("< SystemError >\n'接続が遮断されました'")
                        self.__CNCT._delete()
                        self.server_status = False
                        return
                    self.Rdata = data.decode()
                    print(self.Rdata)
                    self.Sdata = None

service = Main()
service.start()

client = discord.Client(intents=intents)
TOKEN = "NzA3NjQwNTE3NzA5NzkxMzMy.XrLvlg.N3NOFJnUkKGBCFrv2F4LcvX5LAM"
admin = []
global_channel = []
user_say = {}
user_kick = {}
user_channel = {}
after_user = 0
after_channel = 0
after_guild = 0
first_global_c = []
check = 0
second = 0
hour = 0
kick_reset = 0
user_level_object = {}
all_user_data = {}
use_user = {}
use_guild = {}
global_ban = []
lsl = False
out_message = []
keep_ch = None
prifix = "!c:"
clear_content = ""
cannot_access_code = ["TOKEN","all_user_data","os.","json.","subprocess","sys.","bot.http.token","asyncio","__file__","__name__","import ","out_message","user_channel","cannot_access_code",".sleep(","_sleep(","input(","quit(","exit(","help()",".append(",".update(",".remove","del ","help(",".http.token",".logout(",".wait_for(","client.close("]
cannot_acs_incode = [TOKEN]
command_d = {
    f"{prifix}help":{
        "ept":"これを表示するよ!"
    },
    f"{prifix}ADMIN":{
        "ept":"(admin限定) 指定のユーザーをadmin登録します (ロールではありません)\n今日から君も親友さ！",
        "useing":f"{prifix}ADMIN <ユーザーid>"
    },
    f"{prifix}ADMIN_DESTROY":{
        "ept":"(admin限定) 指定のユーザーのadminを解除します\nお前だけは友達だと思ってたのに！",
        "useing":f"{prifix}ADMIN_DESTROY <ユーザーid>"
    },
    "!open-global":{
        "ept":"(admin限定) チャンネルをグローバル化します\nこれすごいうっさいからね",
        "useing":"!open-global"
    },
    f"{prifix}lose-global":{
        "ept":"(admin限定) チャンネルのグローバル化を解除します\n話はオワリだ",
        "useing":f"{prifix}lose-global"
    },
    f"{prifix}create_chat":{
        "ept":"ユーザー指定のチャンネルを作ることができます",
        "useing":f"{prifix}create_chat <チャンネル名>"
    },
    f"{prifix}my-channel":{
        "ept":"ユーザーが所有しているチャンネルを表示します\nIt's mine !!",
        "useing":f"{prifix}my-channel"
    },
    "!add-user":{
        "ept":"チャンネルに入室できるユーザーを追加します\n召喚に応じ参上した！！",
        "useing":"!add-user <ユーザーid>"
    },
    "!del-user":{
        "ept":"チャンネルからユーザーを退場させます\nあれ？なんで、チャンネルがないんだっ？",
        "useing":"!del-user <ユーザーid>"
    },
    "!delete":{
        "ept":"(作成者限定) チャンネルを★ぶっ壊す！★",
        "useing":"!delete"
    },
    f"{prifix}status":{
        "ept":"ユーザーのステータスを表示します\n非常に便利、はっきりわかんだね",
        "useing":f"{prifix}status"
    },
    f"{prifix}restoration":{
        "ept":"意図せず削除されたユーザーのチャンネルを復元\n注意 : 復元は完璧ではありません",
        "useing":f"{prifix}restoration <削除済みのチャンネル名>"
    },
    f"{prifix}server:gban_channel":{
        "ept":"発言したチャンネルをGBANチャンネルに指定します。\nGBANされたときすべてのログがそこで表示されます",
        "useing":f"{prifix}server:gban_channel"
    },
    f"{prifix}server:log-channel":{
        "ept":"発言したチャンネルをlogチャンネルに指定します。\nColoのすべてのログがそこで表示されます",
        "useing":f"{prifix}server:log-channel"
    },
    f"{prifix}Colo":{
        "ept":"MANAGEMENTを表示します。"
    },
    f"{prifix}Colo[ADMIN]":{
        "ept":"ADMINのリストを表示します。\n(実行した鯖にいないメンバーは名前だけが表示されます)",
        "useing":f"{prifix}olo[ADMIN]"
    },
    f"{prifix}GBAN":{
        "ept":"ADMINユーザーが使える、グローバルBANコマンドです",
        "useing":f"{prifix}GBAN <ユーザーID>"
    },
    f"{prifix}GBAN_DEL":{
        "ept":"ADMINユーザーのみが使える、グルーバルBANを解除するコマンドです",
        "useing":f"{prifix}GBAN_DEL <ユーザーID>"
    },
    f"{prifix}server:messageFilter:true":{
        "ept":"サーバー全体にメッセージフィルターをかけます",
        "useing":f"{prifix}server:messageFilter:true"
    },
    f"{prifix}server:messageFilter:false":{
        "ept":"サーバー全体のフィルターをはずします",
        "useing":f"{prifix}server:messageFilter:false"
    },
    f"{prifix}server:gban:true":{
        "ept":"サーバーのGBANを有効化します",
        "useing":f"{prifix}server:gban:true"
    },
    f"{prifix}server:gban:false":{
        "ept":"サーバーのGBANを無効化します",
        "useing":f"{prifix}server:gban:false"
    },
    f"{prifix}server:mute":{
        "ept":"サーバー内のユーザーをミュートします",
        "useing":f"{prifix}server:mute (json形式のデータ)\n>args ['id','seconds','minutes','hours']"
    },
    f"{prifix}server:CustomPrifix":{
        "ept":"カスタムprifixを設定します",
        "useing":f"{prifix}server:CustomPrifix <prifix name>"
    },
    f"{prifix}py":{
        "ept":"受け取った値をpythonで演算しその値を直接送信します",
        "useing":f"{prifix}py <value>"
    },
    f"{prifix}say":{
        "ept":"coloに喋らせます",
        "useing":f"{prifix}say (内容)\n<only>をつけるとコマンドメッセージが自動で削除されます"
    },
    f"{prifix}dm-send":{
        "ept":"ユーザーに直接DMをします",
        "useing":f"{prifix}dm-send <id:(ユーザーid)> <content:(内容)>"
    },
    f"{prifix}trc:ja":{
        "ept":"日本語に文章を翻訳します\nTranslate to Japanese",
        "useing":f"{prifix}trc:ja <文章>"
    },
    f"{prifix}trc:en":{
        "ept":"英語に文章を翻訳します\nTranslate to English",
        "useing":f"{prifix}trc:en <文章>"
    },
    f"{prifix}ping":{
        "ept":"botのpingを表示します",
        "useing":f"{prifix}ping"
    },
    f"{prifix}invite":{
        "ept":"botの招待URLを発行します",
        "useing":f"{prifix}invite"
    },
    f"{prifix}system:in-module":{
        "ept":"botのメインコードにimportされているモジュールの一覧を表示します",
        "useing":f"{prifix}system:in-module"
    },
    f"{prifix}math:PF":{
        "ept":"入力された値を素因数分解します",
        "useing":f"{prifix}math:PF (value)"
    },
    f"{prifix}service:status":{
        "ept":"データサーバーの状態を表示します",
        "useing":f"{prifix}service:status"
    },
    f"{prifix}service:connect":{
        "ept":"データサーバーに再接続します",
        "useing":f"{prifix}service:connect"
    },
    f"{prifix}service:registration":{
        "ept":"データサーバーに登録します\n(登録されていない場合サーバーシステムにはアクセスできません)",
        "useing":f"{prifix}service:registration"
    },
    f"{prifix}svc:eval":{
        "ept":"サーバー上でdictを管理します",
        "useing":f"{prifix}svc:eval (data)"
    },
    "|SCEL|":{
        "ept":"これはsvc:evalコマンドの代入版です\n例えば`!c:say |SVEL ['挨拶']|`とするとsvc:evalの結果が直接代入されそのままメインコマンドが実行されます",
        "useing":"|SCEL <value>|"
    },
    f"{prifix}svc:del":{
        "ept":"dictの要素を削除します",
        "useing":f"{prifix}svc:del (value)"
    }

}
os_event = {
    "UserinServer":{
        "content":""
    },
    "ServerLeftUser":{
        "content":""
    }
}

pass_object = []
delete_object = {}


#deploy ↓・code・↓
#git add . & git commit -am "make it better" & git push heroku main

@client.event
async def on_ready():
    global all_user_data,admin,global_channel,user_say,first_global_c,user_channel,user_level_object,global_ban,second,hour,out_message,delete_object,cannot_acs_incode
    print("login create")
    c = 0
    #jsonファイルからデータの読み込み
    if not (os.path.exists("data.json")):
        with open("data.json","w") as f:
            f.write("{}")
            print("jsonがなかったため作成し終了しました。")
            quit(0)
    with open("data.json","r",encoding="UTF-8") as f:
        JD = json.load(f)
        print("保存データを読み込み中...")
        all_user_data = JD
    ch = client.get_channel(all_user_data["LC"])
    print("")
    print("<データロード開始>")
    print("ADMIN読み込み中...")
    try:
        admin = all_user_data["admin"]
    except KeyError:
        print("admin読み込み失敗")
        quit(0)
    print("<成功>")
    print("グローバルチャットを読み込み中...")
    try:
        global_channel = all_user_data["global-chat"]
    except KeyError:
        print("global-channel読み込み失敗")
        quit(0)
    c += len(all_user_data["global-chat"])
    print("<成功>")
    print("FGチャンネルを読み込み中...")
    try:
        first_global_c = all_user_data["FGC"]
    except KeyError:
        print("FGC読み込み失敗")
        quit(0)
    c += len(all_user_data["FGC"])
    print("<成功>")
    print("ユーザーチャンネルを読み込み中...")
    try:
        all_user_data["user-chat"]
    except KeyError:
        print("user-channel読み込み失敗")
        quit(0)
    for i in all_user_data["user-chat"]:
        print("ユーザー:" + i + "さんのチャンネルを読み込み開始")
        for n in all_user_data["user-chat"][i]["chat"]:
            user_channel[n] = {"id":all_user_data["user-chat"][i]["chat"][n]["id"],"category":all_user_data["user-chat"][i]["chat"][n]["category"],"guild":all_user_data["user-chat"][i]["chat"][n]["guild"],"admin":all_user_data["user-chat"][i]["chat"][n]["admin"],"user":all_user_data["user-chat"][i]["chat"][n]["in-user"],"role":all_user_data["user-chat"][i]["chat"][n]["role"],"logs":all_user_data["user-chat"][i]["chat"][n]["logs"],"delete":all_user_data["user-chat"][i]["chat"][n]["delete"],"msg_logs":all_user_data["user-chat"][i]["chat"][n]["msg_logs"],"in-role":all_user_data["user-chat"][i]["chat"][n]["in-role"]}
            c += 1
    print("<完了>")
    print("ユーザーのsay-countを読み込み中...")
    try:
        all_user_data["user-say"]
    except KeyError:
        print("user-sayの読み込みに失敗")
        quit(0)
    for i in all_user_data["user-say"]:
        print(i + "さんのデータを読み込み中...")
        user_say[i] = all_user_data["user-say"][i]
        c += 1
    print("ユーザーのレベルを読み込み中...")
    try:
        all_user_data["user-level"]
    except KeyError:
        print("ユーザーのレベルの読み込みに失敗")
        quit(0)
    for i in all_user_data["user-level"]:
        print(i + "さんのレベルを読み込み中...")
        user_level_object[i] = {}
        user_level_object[i]["level"] = all_user_data["user-level"][i]["level"]
        print("level : " + str(all_user_data["user-level"][i]["level"]))
        user_level_object[i]["max_xp"] = all_user_data["user-level"][i]["cost"]
        print("cost : " + str(all_user_data["user-level"][i]["cost"]))
        user_level_object[i]["xp"] = all_user_data["user-level"][i]["xp"]
        print("xp : " + str(all_user_data["user-level"][i]["xp"]))
        c += 1
    print("<完了>")
    for i in all_user_data["use-user"]:
        use_user[i] = all_user_data["use-user"][i]
        c += 1
    print("ユーザーのkick回数を読み込み開始")
    try:
        all_user_data["user-kick"]
    except KeyError:
        print("キーを発見できなかったため、終了しました")
        quit(0)
    for i in all_user_data["user-kick"]:
        user_kick[i] = all_user_data["user-kick"][i]
        print(user_kick)
        c += 1
    try:
        all_user_data["guild"]
    except KeyError:
        print("キーを発見できなかったため、終了しました。")
        quit(0)
    print("サーバーデータを読み込み開始")
    for i in all_user_data["guild"]:
        print("{}のデータを読み込み中...".format(i))
        use_guild[i] = all_user_data["guild"][i]
        c += 1
    print("グローバルBANデータを読み込み開始")
    try:
        all_user_data["global_ban"]
    except KeyError:
        print("キーを発見できなかったため、終了しました。")
        quit(0)
    global_ban = all_user_data["global_ban"]
    c += len(all_user_data["global_ban"])
    try:
        all_user_data["out_message"]
    except KeyError:
        print("キーを発見できなかったため、終了しました。")
        quit(0)
    out_message = all_user_data["out_message"]
    c += len(out_message)
    c += len(delete_object)
    print(str(delete_object))
    print(str(global_ban))
    print(all_user_data)
    print("<COUNTER>")
    print(len(all_user_data))
    print("-----V-COUNTER-----")
    print(c)
    #スレッドコーナー
    try:
        al = threading.Thread(target=all_custom)
        wh = threading.Thread(target=w)
        sd = threading.Thread(target=say_down)
        al.start()
        wh.start()
        sd.start()
        schedule.every(1).second.do(all_custom)
        load_now_custom.start()
        mute_load.start()
        UPDATE.start()
    except RuntimeError:
        return

@client.event
async def on_message(message):
    global after_user,after_channel,user_channel,after_guild,first_global_c,all_user_data,use_user,lsl,global_ban,second,hour,out_message,keep_ch,clear_content,cannot_access_code,os_event,pass_object,command_d,delete_object,service,prifix,cannot_acs_incode
    channel = message.channel
    author = message.author
    guild = message.guild
    try:
        mct = message.content
        f = open("data.json","w",encoding="UTF-8")
        f.write(json.dumps(all_user_data,indent=4))
        f.close()
        try:
            try:
                if message.guild.name in use_guild:
                    if "mute" in use_guild[message.guild.name]["system"]:
                        if message.author.id in use_guild[message.guild.name]["system"]["mute"]:
                            await message.delete()
                            return
            except AttributeError:
                pass
        except KeyError:
            pass
        if not message.author.bot:
            #メッセージフィルターシステム
            clear_content = message.content
            try:
                if use_guild[message.guild.name]["MF"]:
                    c = mct
                    chk = False
                    for i in out_message:
                        if i in c:
                            chk = True
                            break
                    print(chk)
                    if chk:
                        await message.delete()
                        count = 0
                        for i in out_message:
                            count += c.count(i)
                            c = c.replace(i,"×" * len(i))
                        clear_content = c
                        print(clear_content)
                        fv1 = int(len(out_message) % 10)
                        fv2 = int(len(out_message) / 10)
                        fv3 = int(len(out_message) / 100)
                        embed = discord.Embed(title="- filter -",description=c + f"\n\n_ID:{message.id} count:{count}_\n_filter-ver:{str(fv3)}.{str(fv2)}.{str(fv1)}_",color=discord.Colour.magenta())
                        embed.set_author(name=message.author.name,icon_url=message.author.avatar_url)
                        await message.channel.send(embed=embed)
                        return
                    clear_content = c
            except KeyError:
                pass
            #カスタムprifix
            try:
                if not "prifix" in use_guild[message.guild.name]["system"]:
                    use_guild[message.guild.name]["system"].update({"prifix":"!c:"})
                    all_user_data["guild"][message.guild.name]["system"].update({"prifix":"!c:"})
                prifix = use_guild[message.guild.name]["system"]["prifix"]
            except KeyError:
                pass
            #コマンドログ
            print(f"{mct} ({message.author.name}) - ({message.author.id})")
            if mct.startswith(prifix + ":"):
                if not any(mct.startswith(i) for i in command_d):
                    await message.channel.send("書き方間違えてない？\nコマンドがわからなかったら`!c:help`で確認してね！")
                    return
            #DMにメッセージを送信するコマンド
            if mct.startswith(f"{prifix}dm-send "):
                content = mct[len(f"{prifix}dm-send "):]
                ch = message.channel
                if "<id:" in content:
                    p1 = content.find("<id:") + len("<id:")
                    if ">" in content:
                        p2 = content.find(">")
                        try:
                            user_id = int(content[p1:p2])
                        except ValueError:
                            await ch.send("無効な値が含まれています")
                            return
                    else:
                        await ch.send("対象のidが正常に記述されていません")
                        return
                else:
                    await ch.send("対象のidの記述が見つかりませんでした")
                    return
                content = content.replace(content[p1 - len("<id:"):p2 + len(">")],"")
                user = client.get_user(user_id)
                if user == None:
                    await ch.send("ユーザーが見つかりませんでした")
                    return
                if "<content:" in content:
                    p1 = content.find("<content:") + len("<content:")
                    if ">" in content:
                        p2 = content.find(">")
                        msg_content = content[p1:p2]
                    else:
                        await ch.send("送信する内容が正常に記述されていません")
                        return
                else:
                    await ch.send("送信する内容が記述されていません")
                try:
                    try:
                        try:
                            dm = await user.create_dm()
                        except AttributeError:
                            await ch.send("bot自体には送信できません")
                            return
                    except discord.errors.HTTPException:
                        await ch.send("このユーザーには送信できません")
                        return
                except discord.errors.Forbidden:
                    await ch.send("このユーザーには送信できません")
                    return
                await dm.send(msg_content)
                return
            try:
                if mct == f"!{client.user.name}":
                    embed = discord.Embed(title="\ BOT MANAGEMENT /",color=discord.Colour.green(),description="運営の公式サーバー:```https://discord.gg/AmyHABv```\nbot主:```ty#2829```\nbotは動いていない時がありますが、ご了承ください。\nprovide by python.")
                    await message.channel.send(embed=embed)
                    return
                if mct:
                    if message.author != client.user:
                        #log-chの確認
                        for i in use_guild:
                            try:
                                use_guild[i]["system"]["log_ch"]
                            except KeyError:
                                continue
                            ch = client.get_channel(use_guild[i]["system"]["log_ch"])
                            if ch == None:
                                del use_guild[i]["system"]["log_ch"]
                                del all_user_data["guild"][i]["system"]["log_ch"]
                        if not message.guild.name in pass_object:
                            try:
                                use_guild[message.guild.name]
                                all_user_data["guild"][message.guild.name]
                            except KeyError:
                                use_guild.update({message.guild.name:{"id":message.guild.id,"GOI":message.guild.owner_id,"system":{"level_up_ch":0,"global_ban":False,"global_channel":0}}})
                                all_user_data["guild"].update({message.guild.name:{"id":message.guild.id,"GOI":message.guild.owner_id,"system":{"global_ban":False,"global_channel":0}}})
                                await message.channel.send(f"はじめまして、{client.user.name}を導入していただき誠にありがとうございます!\nこのbotのヘルプは`!c:help`で確認できますのでご確認のほどよろしくお願いします\nbot prifix:`{prifix}`\nbot id:`{client.user.id}`\ncoding language:`python`\nbot owner:`ty#2829`")
                        else:
                            pass_object.remove(message.guild.name)
                            print("PASS OBJCT")
                        #botのシステムにアクセスできるユーザー
                        try:
                            all_user_data["use-user"][message.author.name]
                        except KeyError:
                            all_user_data["use-user"].update({message.author.name:{"id":message.author.id}})
                            use_user.update({message.author.name:{"id":message.author.id}})
                        #ユーザーデータフォルダの自動作成
                        if not os.path.exists("Users"):
                            msg = await message.channel.send("`[ SystemDetailedLog ]`\n`ユーザーデータフォルダを作成しています...`")
                            os.mkdir("Users")
                            await msg.edit(content="`作成完了`")
                            await msg.delete()
                        if not os.path.exists(f"Users/{message.author.id}"):
                            msg = await message.channel.send("`[ SystemDetailedLog ]`\n`making UserData tree...`")
                            os.makedirs(f"Users/{message.author.id}/py-files")
                            with open(f"Users/{message.author.id}/pack.json","w") as f:
                                d = {
                                    "setting":None
                                }
                                f.write(json.dumps(d,indent=4))
                            await msg.edit(content="`作成完了`")
                            await msg.delete()
                        #global_channelの確認
                        for i in list(global_channel):
                            CH = client.get_channel(i)
                            if CH == None:
                                global_channel.remove(i)
                                all_user_data["global-chat"].remove(i)
                        #コマンド処理
                        #招待コード
                        if mct == f"{prifix}leave":
                            if message.author.id in admin:
                                await message.guild.leave()
                            else:
                                await message.channel.send("`ACのみ使用できるコマンドです`")
                        if mct == f"{prifix}invite":
                            embed = discord.Embed(title="invite URL",description=f"https://discord.com/api/oauth2/authorize?client_id=707640517709791332&permissions=1622539862&scope=bot\n\n_ClientId:{client.user.id}_",color=discord.Colour.green())
                            await message.channel.send(embed=embed)
                            
                            return
                        #importされているモジュールリスト
                        if mct == f"{prifix}system:in-module":
                            l = []
                            for name, val in globals().items():
                                if isinstance(val, types.ModuleType):
                                    l.append(val.__name__)
                            await message.channel.send("```\n" + str(l) + "\n```")
                            return
                        #ping計測
                        if mct == f"{prifix}ping":
                            Ntime = time.monotonic()
                            msg = await message.channel.send("Please wait...")
                            ping = int(1000 * (time.monotonic() - Ntime))
                            await msg.edit(content=f"**_Ping > {ping}ms_**")
                            
                            return
                        #代入式python
                        while "|py " in mct:
                            value = cut_out(mct,"|py ","|")
                            n_value = value
                            value = value.replace("'",'"')
                            check_value = value
                            ch = message.channel
                            while True:
                                cut_value = cut_out(check_value,'"','"')
                                if cut_value != None:
                                    cut_f_value = cut_out(check_value,"{","}")
                                    if cut_f_value != None:
                                        value = value.replace("{" + cut_f_value + "}","`<CUF>`")
                                        check_value = check_value.replace("{" + cut_f_value + "}","")
                                    check_value = check_value.replace(f'"{cut_value}"',"")
                                else:
                                    break
                            value = value.replace("@everyone","`<Can'tEveryone>`")
                            try:
                                if any(i in check_value for i in cannot_access_code):
                                    await ch.send("```[AccessError] > Refers to object that you do not have access to (Errortype:original)```")
                                    return
                                value = eval(value)
                                if type(value) == str:
                                    value = value.replace("@everyone","`<Can'tEveryone>`")
                                if value == None:
                                    value = "`None`"
                            except Exception as a:
                                await ch.send(f"```[{a.__class__.__name__}] > {a} (ErrorType:python)```")
                                return
                            mct = mct.replace(f"|py {n_value}|",str(value))
                        #代入式データeval
                        while "|SCEL " in mct:
                            ch = message.channel
                            value = cut_out(mct,"|SCEL ","|")
                            normal_value = value
                            value = value.replace(".up",".update")
                            if "<simple>" in value:
                                value = value.replace("<simple>","")
                                value = f"[{value}]"
                                value = value.replace(".","][")
                            if "<type:str>" in value:
                                value = value.replace("<type:str>","")
                                value = value.replace("[",'["')
                                value = value.replace("]",'"]')
                                value = value.replace("{",'{"')
                                value = value.replace("}",'"}')
                                value = value.replace('"}"}','}}')
                                value = value.replace(":",'":"')
                                value = value.replace(",",'","')
                                value = value.replace(':"{',":{")
                                value = value.replace(':"[',":[")
                            while "str<" in value:
                                str_value = cut_out(value,"str<",">")
                                if str_value != None:
                                    normal_str_value = str_value
                                    str_value = str_value.replace("[",'["')
                                    str_value = str_value.replace("]",'"]')
                                    str_value = str_value.replace("{",'{"')
                                    str_value = str_value.replace("}",'}"')
                                    str_value = str_value.replace(":",'":"')
                                    value = value.replace(f"str<{normal_str_value}>",str_value)
                            if "<none>" in value:
                                value = value.replace("<none>","")
                            SEND_DATA = {
                                "USER_ID":str(message.author.id),
                                "VALUE":value
                            }
                            service.Sdata = "SDS>" + str(SEND_DATA)
                            time.sleep(0.3)
                            if any(service.Rdata.startswith(i) for i in service.EVENT):
                                if service.Rdata.startswith(service.EVENT[3]):
                                    await message.channel.send("**あなたはDSUに登録されていないようです...**")
                                    
                                    return
                                if service.Rdata.startswith(service.EVENT[4]):
                                    await message.channel.send("```" + service.Rdata[len(service.EVENT[4]):] + "```")
                                    
                                    return
                                if service.Rdata.startswith(service.EVENT[5]):
                                    mct = mct.replace(f"|SCEL {normal_value}|",service.Rdata[len(service.EVENT[5]):])
                            else:
                                embed = discord.Embed(title="< データ受信 >",description="受信したデータは**無効**なものです\nこの受信データは任意のものではありませんでした\n```< help >\nサーバー側が受信を受け付けないか\nもしくはサーバーが起動していない可能性があります```")
                                embed.set_thumbnail(url="https://www.silhouette-illust.com/wp-content/uploads/2017/09/program_binary_file_38456-300x300.jpg")
                                await ch.send(embed=embed)
                                return
                        #数学コマンド
                        if mct.startswith(f"{prifix}math:PF "):
                            content = mct[len(f"{prifix}math:PF "):]
                            try:
                                value = int(mct[len(f"{prifix}math:PF "):])
                            except ValueError:
                                await message.channel.send("✖ **無効な値のようです...**")
                                return
                            if value == 0:
                                raise TypeError("ゼロは素因数分解できないようだ...")
                                return
                            if 100000000000000000000000000000000000000 < value:
                                await message.channel.send("```値が大きすぎます...```")
                                return
                            asr = pf(value)
                            await message.channel.send(f"**{value}**を素因数分解した結果...\n```{asr}```になりました！")
                            return
                        #say
                        if mct.startswith(f"{prifix}say "):
                            ctnt = mct[len(f"{prifix}say "):]
                            while True:
                                mention = cut_out(ctnt,"<@",">")
                                if mention != None:
                                    user = client.get_user(int(mention.replace("!","")))
                                    if user != None:
                                        ctnt = ctnt.replace(f"<@{mention}>","`<Cannot mention>`")
                                    else:
                                        break
                                else:
                                    break
                            if "<only>" in ctnt:
                                await message.delete()
                                ctnt = ctnt.replace("<only>","")
                            await message.channel.send(ctnt)
                            
                            return
                        #python
                        if mct.startswith(f"{prifix}py "):
                            value = mct[len(f"{prifix}py "):]
                            value = value.replace("'",'"')
                            check_value = value
                            ch = message.channel
                            while True:
                                cut_value = cut_out(check_value,'"','"')
                                if cut_value != None:
                                    cut_f_value = cut_out(check_value,"{","}")
                                    if cut_f_value != None:
                                        value = value.replace("{" + cut_f_value + "}","`<CUF>`")
                                        check_value = check_value.replace("{" + cut_f_value + "}","")
                                    check_value = check_value.replace(f'"{cut_value}"',"")
                                else:
                                    break
                            try:
                                if any(i in check_value for i in cannot_access_code):
                                    await ch.send("```[AccessError] > Refers to object that you do not have access to (Errortype:original)```")
                                    return
                                await eval(value)
                            except Exception as a:
                                await ch.send(f"```[{a.__class__.__name__}] > {a} (ErrorType:python)```")
                                return
                            return
                        if mct.startswith(f"{prifix}create_support"):
                            ch = message.channel
                            hook = await ch.create_webhook(name="CHCHHCH",reason="botのサポーターを作成しました")
                            
                            return
                        #翻訳(日本語)
                        if mct.startswith(f"{prifix}trc:ja "):
                            ch = message.channel
                            try:
                                value = mct[len(f"{prifix}trc:ja "):]
                                translator = Translator()
                                detact = translator.detect(value)
                                traced = translator.translate(value,src=detact.lang,dest="ja")
                                embed = discord.Embed(description=f"{traced.text}\n_TraceMessageId:{message.id}_  _lang:Japanese_",color=discord.Colour.blue())
                                embed.set_author(name="Word Trace",icon_url="https://addd-link.co.jp/wp-content/uploads/2017/03/Google_Translate_Icon.png")
                                embed = await ch.send(embed=embed)
                                delete_object.update({
                                    str(message.id):{
                                        "with":embed.id
                                    }
                                })
                                return
                            except Exception as a:
                                await ch.send(f"```[{a.__class__.__name__}] > {a}```")
                                return
                        #翻訳(日本語)
                        if mct.startswith(f"{prifix}trc:en "):
                            ch = message.channel
                            try:
                                value = mct[len(f"{prifix}trc:en "):]
                                translator = Translator()
                                detact = translator.detect(value)
                                traced = translator.translate(value,src=detact.lang,dest="en")
                                embed = discord.Embed(description=f"{traced.text}\n_TraceMessageId:{message.id}_  _lang:English_",color=discord.Colour.blue())
                                embed.set_author(name="Word Trace",icon_url="https://addd-link.co.jp/wp-content/uploads/2017/03/Google_Translate_Icon.png")
                                embed = await ch.send(embed=embed)
                                delete_object.update({
                                    str(message.id):{
                                        "with":embed.id
                                    }
                                })
                                return
                            except Exception as a:
                                await ch.send(f"```[{a.__class__.__name__}] > {a}```")
                                return
                        #データサーバーコマンド↓
                        #データサーバーの状態を表示
                        if mct == f"{prifix}service:status":
                            service.check_contact()
                            if service.server_status:
                                embed = discord.Embed(title="<< データサーバーの現在の状態 >>",description="現在システムデータサーバーは**オンライン**です\nシステムは正常に動作しています",color=discord.Colour.green())
                                embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/2PkH5DZhn4YNxXrY2l7crsYNKCwF6hkDVpwUq59VNbnOayKLj8DM4AX5zqiItkYd0TlxrOTPUAHx0IE3Xs92nkMwxD3IeaLYG-yOV9A2V0TgBLStcS5WQ-zN2Y1cCg")
                                await message.channel.send(embed=embed)
                            else:
                                embed = discord.Embed(title="<< データサーバーの現在の状態 >>",description="現在システムデータサーバーは**オフライン**です\n```< Tips >\n'サーバーが起動している場合\n!c:service:connectで再接続できます'```")
                                embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/2PkH5DZhn4YNxXrY2l7crsYNKCwF6hkDVpwUq59VNbnOayKLj8DM4AX5zqiItkYd0TlxrOTPUAHx0IE3Xs92nkMwxD3IeaLYG-yOV9A2V0TgBLStcS5WQ-zN2Y1cCg")
                                await message.channel.send(embed=embed)
                            
                            return
                        #データサーバーへ接続
                        if mct == f"{prifix}service:connect":
                            if not service.server_status:
                                service.start()
                                time.sleep(3)
                                if service.server_status:
                                    embed = discord.Embed(title="< データサーバーへ接続 >",description="**接続完了**しました\n```< tips >\n'データサーバーが接続済みの場合\nさまざまな機能が使用可能になります'```",color=discord.Colour.blue())
                                    embed.set_thumbnail(url="https://mates-app.jp/reco/img/nyutai_icon.jpg")
                                    await message.channel.send(embed=embed)
                                else:
                                    embed = discord.Embed(title="< データサーバーへ接続 >",description="**接続できません**でした...\n```<help>\n'bot作成者にデータサーバーの起動を申請する必要があります```",color=discord.Colour.blue())
                                    embed.set_thumbnail(url="https://media.istockphoto.com/vectors/vector-illustration-of-single-isolated-access-forbidden-icon-vector-id1149082125?s=170x170")
                                    await message.channel.send(embed=embed)
                                
                                return
                            else:
                                await message.channel.send("**データサーバーは既に接続されています**")
                            
                            return
                        #ユーザーの登録
                        if mct == f"{prifix}service:registration":
                            ch = message.channel
                            service.Sdata = f"UserEntry>{message.author.id}"
                            time.sleep(0.3)
                            if any(service.Rdata.startswith(i) for i in service.EVENT):
                                if service.Rdata == service.EVENT[0]:
                                    await ch.send("**登録が完了しました**")
                                if service.Rdata.startswith(service.EVENT[1]):
                                    await ch.send("**すでに登録されています**")
                                
                                return
                            else:
                                embed = discord.Embed(title="< データ受信 >",description="受信したデータは**無効**なものです\nこの受信データは任意のものではありませんでした\n```< help >\nサーバー側が受信を受け付けないか\nもしくはサーバーが起動していない可能性があります```")
                                embed.set_thumbnail(url="https://www.silhouette-illust.com/wp-content/uploads/2017/09/program_binary_file_38456-300x300.jpg")
                                await ch.send(embed=embed)
                            
                            return
                        #ユーザーの個人保存データ
                        if mct.startswith(f"{prifix}svc:eval "):
                            ch = message.channel
                            value = mct[len(f"{prifix}svc:eval "):]
                            value = value.replace(".up",".update")
                            if "<simple>" in value:
                                value = value.replace("<simple>","")
                                value = f"[{value}]"
                                value = value.replace(".","][")
                            if "<t:s>" in value:
                                value = value.replace("<type:str>","")
                                value = value.replace("[",'["')
                                value = value.replace("]",'"]')
                                value = value.replace("{",'{"')
                                value = value.replace("}",'"}')
                                value = value.replace('"}"}','}}')
                                value = value.replace(":",'":"')
                                value = value.replace(",",'","')
                                value = value.replace(':"{',":{")
                                value = value.replace(':"[',":[")
                            while "str<" in value:
                                str_value = cut_out(value,"str<",">")
                                normal_str_value = str_value
                                str_value = str_value.replace("[",'["')
                                str_value = str_value.replace("]",'"]')
                                str_value = str_value.replace("{",'{"')
                                str_value = str_value.replace("}",'}"')
                                str_value = str_value.replace(":",'":"')
                                value = value.replace(f"str<{normal_str_value}>",str_value)
                            if "<none>" in value:
                                value = value.replace("<none>","")
                            SEND_DATA = {
                                "USER_ID":str(message.author.id),
                                "VALUE":value
                            }
                            service.Sdata = "SDS>" + str(SEND_DATA)
                            time.sleep(0.3)
                            if any(service.Rdata.startswith(i) for i in service.EVENT):
                                if service.Rdata.startswith(service.EVENT[3]):
                                    await message.channel.send("**あなたはDSUに登録されていないようです...**")
                                    return
                                if service.Rdata.startswith(service.EVENT[4]):
                                    await message.channel.send("```" + service.Rdata[len(service.EVENT[4]):] + "```")
                                    return
                                if service.Rdata.startswith(service.EVENT[5]):
                                    if service.Rdata[len(service.EVENT[5]):] == "None":
                                        await message.channel.send("```Saved successfully```")
                                        return
                                    await message.channel.send(service.Rdata[len(service.EVENT[5]):])
                                    return
                            else:
                                embed = discord.Embed(title="< データ受信 >",description="受信したデータは**無効**なものです\nこの受信データは任意のものではありませんでした\n```< help >\nサーバー側が受信を受け付けないか\nもしくはサーバーが起動していない可能性があります```")
                                embed.set_thumbnail(url="https://www.silhouette-illust.com/wp-content/uploads/2017/09/program_binary_file_38456-300x300.jpg")
                                await ch.send(embed=embed)
                                return
                            return
                        if mct.startswith(f"{prifix}svc:del "):
                            ch = message.channel
                            value = mct[len(f"{prifix}svc:del "):]
                            if "<simple>" in value:
                                value = value.replace("<simple>","")
                                value = f"[{value}]"
                                value = value.replace(".","][")
                            if "<type:str>" in value:
                                value = value.replace("<type:str>","")
                                value = value.replace("[",'["')
                                value = value.replace("]",'"]')
                                value = value.replace("{",'{"')
                                value = value.replace("}",'"}')
                                value = value.replace('"}"}','}}')
                                value = value.replace(":",'":"')
                                value = value.replace(",",'","')
                                value = value.replace(':"{',":{")
                                value = value.replace(':"[',":[")
                            if "<none>" in value:
                                value = value.replace("<none>","")
                            SEND_DATA = {
                                "USER_ID":str(message.author.id),
                                "VALUE":value
                            }
                            service.Sdata = "SDD>" + str(SEND_DATA)
                            time.sleep(0.3)
                            if any(service.Rdata.startswith(i) for i in service.EVENT):
                                if service.Rdata.startswith(service.EVENT[3]):
                                    await message.channel.send("**あなたはDSUに登録されていないようです...**")
                                    return
                                if service.Rdata.startswith(service.EVENT[4]):
                                    await message.channel.send("```" + service.Rdata[len(service.EVENT[4]):] + "```")
                                    return
                                if service.Rdata.startswith(service.EVENT[5]):
                                    if service.Rdata[len(service.EVENT[5]):] == "None":
                                        await message.channel.send("```Saved successfully```")
                                        return
                                    await message.channel.send(service.Rdata[len(service.EVENT[5]):])
                                    return
                            else:
                                embed = discord.Embed(title="< データ受信 >",description="受信したデータは**無効**なものです\nこの受信データは任意のものではありませんでした\n```< help >\nサーバー側が受信を受け付けないか\nもしくはサーバーが起動していない可能性があります```")
                                embed.set_thumbnail(url="https://www.silhouette-illust.com/wp-content/uploads/2017/09/program_binary_file_38456-300x300.jpg")
                                await ch.send(embed=embed)
                                return
                            return
                        #ADMINをリスト表示
                        if mct == f"!{client.user.name}[ADMIN]":
                            n = ""
                            c = 0
                            for i in admin:
                                user = client.get_user(i)
                                c += 1
                                if not user in message.guild.members:
                                    n += f"({user.name}) "
                                    continue
                                n += user.mention + " "
                            embed = discord.Embed(title=f"<< ADMIN LIST ({c}) >>",description=n,color=discord.Colour.green())
                            await message.channel.send(embed=embed)
                            return
                        #globalBANの対象を追加
                        if mct.startswith(f"{prifix}GBAN "):
                            if not use_guild[message.guild.name]["system"]["global_ban"]:
                                await message.channel.send("```✖ このサーバーはGBANが許可されていません```")
                                return
                            if message.author.id in admin:
                                try:
                                    int(mct[len(f"{prifix}GBAN "):])
                                except ValueError:
                                    await message.channel.send("無効な値です。")
                                    return
                                if int(mct[len(f"{prifix}GBAN "):]) in global_ban:
                                    await message.channel.send("すでにそのユーザーはGBANされています。")
                                    return
                                user = client.get_user(int(mct[len(f"{prifix}GBAN "):]))
                                if not user == None:
                                    guild = client.get_guild(message.guild.id)
                                    embed = discord.Embed(title=f"**GLOBAL-BAN LOG [{user.name}]**",description=f"{user.name}さんをグローバルBANしました。",color=discord.Colour.blue())
                                    embed.set_author(name=user.name,icon_url=user.avatar_url)
                                    try:
                                        await message.guild.kick(user)
                                        global_ban.append(user.id)
                                    except discord.errors.Forbidden:
                                        embed = discord.Embed(title=f"+System Error-",description=f"{user.name}さんをBANする権限がありません。",color=discord.Colour.red())
                                        embed.set_author(name=user.name,icon_url=user.avatar_url)
                                        await message.channel.send(embed=embed)
                                        all_user_data["global_ban"].append(user.id)
                                        global_ban.append(user.id)
                                        return
                                    if "gban_ch" in use_guild[guild.name]["system"].keys():
                                        CH = client.get_channel(use_guild[guild.name]["system"]["gban_ch"])
                                        if CH == None:
                                            del use_guild[guild.name]["system"]["gban_ch"]
                                            del all_user_data["guild"][guild.name]["system"]["gban_ch"]
                                            await message.channel.send(embed=embed)
                                            all_user_data["global_ban"].append(user.id)
                                            
                                            return
                                        await CH.send(embed=embed)
                                        
                                        all_user_data["global_ban"].append(user.id)
                                        global_ban.append(user.id)
                                        
                                        return
                                    
                                    
                                    return
                                else:
                                    await message.channel.send("そのユーザーIDは見つかりませんでした。")
                                    
                                    
                                    return
                            else:
                                await message.channel.send("あなたはADMINに登録されていないため、コマンドを実行できません。")
                                
                                
                                return
                        #GBANの解除
                        if mct.startswith(f"{prifix}GBAN_DEL "):
                            if message.author.id in admin:
                                try:
                                    ID = int(mct[len(f"{prifix}GBAN_DEL "):])
                                except ValueError:
                                    await message.channel.send("無効な値です。")
                                    
                                    
                                    return
                                if ID in global_ban:
                                    global_ban.remove(ID)
                                    await message.channel.send("解除しました。")
                                    all_user_data["global_ban"].remove(ID)
                                    
                                    
                                    return
                                else:
                                    await message.channel.send("そのIDは登録されていません。")
                                    
                                    
                                    return
                            else:
                                await message.channel.send("あなたはADMINに登録されていないため、コマンドを実行できません。")
                                
                                
                                return
                        #GBANのLIST表示
                        if mct == f"{prifix}GBAN[LIST]":
                            if message.author.id in admin or message.author.guild_permissions.administrator:
                                embed = discord.Embed(title="<GbanList>",color=discord.Colour.orange())
                                c = "\n"
                                l = []
                                for i in list(global_ban):
                                    if i in l:
                                        continue
                                    USER = client.get_user(i)
                                    try:
                                        c += "```\n" + USER.name + "```"
                                    except AttributeError:
                                        c += "```\nID:" + str(i) + " (Baned)```"
                                    l.append(i)
                                if c == "\n":
                                    c += "・No list・"
                                embed.add_field(name="--- USER ---",value=c)
                                await message.channel.send(embed=embed)
                                return
                            else:
                                await message.channel.send("ADMINもしくは管理者権限をもっていないため実行できません")
                                return
                        #ADMIN追加処理
                        if client.user != message.author:
                            if mct.startswith(f"{prifix}ADMIN "):
                                if int(message.author.id) in admin:
                                    if int(mct[len(f"{prifix}ADMIN "):]) in admin:
                                        await message.channel.send("すでに登録済みのIDです。")
                                        return
                                    if not message.guild.get_member(int(mct[len(f"{prifix}ADMIN "):])):
                                        await message.channel.send("このidのユーザーは見つかりませんでした")
                                        return
                                    admin.append(int(mct[len(f"{prifix}ADMIN "):]))
                                    #データの保存
                                    if not int(mct[len(f"{prifix}ADMIN "):]) in all_user_data["admin"]:
                                        all_user_data["admin"].append(int(mct[len(f"{prifix}ADMIN "):]))
                                    await message.channel.send("OK")
                                    return
                                else:
                                    await message.channel.send("登録するにはすでにadminのユーザーに申請する必要があります。")
                                    return
                        #ADMIN解除処理
                        if client.user != message.author:
                            if mct.startswith(f"{prifix}ADMIN_DESTROY "):
                                if int(message.author.id) in admin:
                                    if message.author.id == int(mct[len(f"{prifix}ADMIN_DESTROY "):]):
                                        await message.channel.send("自己のadminは解除できません。")
                                        return
                                    if int(mct[len(f"{prifix}ADMIN_DESTROY "):]) in admin:
                                        admin.remove(int(mct[len(f"{prifix}ADMIN_DESTROY "):]))
                                        #データの保存
                                        try:
                                            all_user_data["admin"].remove(int(mct[len(f"{prifix}ADMIN_DESTROY "):]))
                                        except ValueError:
                                            return
                                        await message.channel.send("OK")
                                    else:
                                        await message.channel.send("このIDは登録されていません。")
                                    return
                                else:
                                    await message.channel.send("すでに登録してある必要があります。")
                                    return
                        #グローバルチャット追加 (ADMIN)
                        if mct == "!open-global":
                            if message.author.id in admin:
                                if message.channel.id in global_channel:
                                    await message.channel.send("すでにglobal化されています。")
                                    return
                                first_global_c.append(message.channel.id)
                                global_channel.append(message.channel.id)
                                await message.channel.send("OK")
                                return
                            else:
                                await message.channel.send("あなたのアカウントはadminに登録されていません\n登録するにはすでにadminのユーザーに申請する必要があります。")
                                return
                        #グローバルチャット解除 (ADMIN)
                        if mct == f"{prifix}lose-global":
                            if message.author.id in admin:
                                if message.channel.id in global_channel:
                                    global_channel.remove(message.channel.id)
                                    await message.channel.send("OK")
                                else:
                                    await message.channel.send("このチャンネルはglobal化されていません")
                                return
                            else:
                                await message.channel.send("あなたのアカウントはadminに登録されていません\n登録するにはすでにadminのユーザーに申請する必要があります。")
                                return
                        #help call
                        if mct == f"{prifix}help":
                            embed = discord.Embed(title="COLO HELP",color=discord.Colour.green())
                            c = ""
                            for i in command_d:
                                c += "`" + i + "`\n"
                            embed.add_field(name="リスト",value="\n\n" + c,inline=False)
                            embed.add_field(name="詳細",value=f"```\n{prifix}help-(コマンド名)\n```\nで説明を確認できます",inline=False)
                            await message.channel.send(embed=embed)
                            return
                        #コマンドの補足
                        if mct.startswith(f"{prifix}help-"):
                            value = mct[len(f"{prifix}help-"):]
                            ch = message.channel
                            if any(value == i for i in command_d):
                                embed = discord.Embed(color=discord.Colour.green())
                                embed.add_field(name="-----description-----",value="```\n" + command_d[value]["ept"] + "\n```")
                                try:
                                    command_d[value]["useing"]
                                except KeyError:
                                    pass
                                else:
                                    embed.add_field(name="使い方",value="```\n" + command_d[value]["useing"] + "\n```",inline=False)
                                embed.set_author(name="< HELP CALL >",icon_url="https://cdn.pixabay.com/photo/2016/06/26/23/32/information-1481584_960_720.png")
                                await ch.send(embed=embed)
                                return
                            else:
                                await ch.send("**<コマンドが見つかりませんでした>**\n```Tips > 'helpコマンドでリストを確認してみてください'```")
                                return
                        #チャットの追加
                        if mct.startswith(f"{prifix}create_chat "):
                            try:
                                CT = await message.guild.create_text_channel(mct[len(f"{prifix}create_chat "):],category=message.channel.category)
                            except discord.errors.HTTPException:
                                await message.channel.send("チャンネル名は100文字以下にしてください。")
                                return
                            if CT.name in user_channel:
                                await message.channel.send("すでに使われている名前です。")
                                await CT.delete()
                                return
                            role = await message.guild.create_role(name=CT.name)
                            every = discord.utils.find(lambda r: r.name == '@everyone', message.guild.roles)
                            await CT.send(message.author.mention + "作成に成功しました")
                            await CT.set_permissions(role,read_messages=True,send_messages=True,read_message_history=True,view_channel=True,send_tts_messages=True,attach_files=True,embed_links=True)
                            await CT.set_permissions(every,read_messages=False,send_messages=False,read_message_history=False)
                            await message.author.add_roles(role)
                            user_channel.update({CT.name:{"id":CT.id,"category":CT.category.name,"user":[message.author.id],"role":role.name,"guild":message.guild.id,"admin":message.author.id,"logs":[],"delete":False,"msg_logs":{},"in-role":[]}})
                            #データの保存
                            try:
                                all_user_data["user-chat"][message.author.name]["chat"]
                            except KeyError:
                                all_user_data["user-chat"][message.author.name] = {}
                                all_user_data["user-chat"][message.author.name]["chat"] = {}
                            all_user_data["user-chat"][message.author.name]["chat"].update({CT.name:{"id":CT.id,"category":CT.category.name,"in-user":[message.author.id],"role":role.name,"guild":message.guild.id,"admin":message.author.id,"logs":[],"delete":False,"msg_logs":{},"in-role":[]}})
                            return
                        #作成したチャンネル限定のコマンド
                        #入室を許可するロールの指定
                        if mct.startswith("!add-role "):
                            if message.channel.name in user_channel:
                                if message.author.id == user_channel[message.channel.name]["admin"]:
                                    CH = client.get_channel(message.channel.id)
                                    role_name = mct[len("!add-role "):]
                                    role = discord.utils.find(lambda r: r.name == f'{role_name}', message.guild.roles)
                                    ch_role = discord.utils.find(lambda r: r.name == f'{user_channel[CH.name]["role"]}', message.guild.roles)
                                    if not role == None:
                                        if role.name in user_channel[message.channel.name]["in-role"]:
                                            await message.channel.send("このロールはすでに許可されてるよっ")
                                            return
                                        await CH.send(f"{role.name}を入室許可しました")
                                        user_channel[CH.name]["in-role"].append(role.name)
                                        all_user_data["user-chat"][message.author.name]["chat"][CH.name]["in-role"].append(role.name)
                                        await CH.send("ロールを所有しているユーザーを加入中...")
                                        n = "<ADD-LOG>\n"
                                        c = 0
                                        for i in role.members:
                                            if i.id in user_channel[CH.name]["user"]:
                                                continue
                                            user_channel[CH.name]["user"].append(i.id)
                                            await i.add_roles(ch_role)
                                            all_user_data["user-chat"][message.author.name]["chat"][CH.name]["in-user"].append(i.id)
                                            c += 1
                                            n += f"・{i.name}さんを加入しました\n"
                                        if c == 0:
                                            n += "・Not Found・"
                                        await CH.send(n)
                                        return
                                    else:
                                        await message.channel.send("ロールが見つからなかったよっ")
                                        return
                                else:
                                    await message.channel.send("このチャンネルの管理者ではないため、実行できません")
                                    return
                            else:
                                await message.channel.send("コマンドが適用されないチャンネルです")
                                return
                        #入室を無効するロールの指定
                        if mct.startswith("!del-role "):
                            if message.channel.name in user_channel:
                                if message.author.id == user_channel[message.channel.name]["admin"]:
                                    CH = client.get_channel(message.channel.id)
                                    role_name = mct[len("!del-role "):]
                                    role = discord.utils.find(lambda r: r.name == f'{role_name}', message.guild.roles)
                                    ch_role = discord.utils.find(lambda r: r.name == f'{user_channel[CH.name]["role"]}', message.guild.roles)
                                    if role.name in user_channel[CH.name]["in-role"]:
                                        user_channel[CH.name]["in-role"].remove(role.name)
                                        all_user_data["user-chat"][message.author.name]["chat"][CH.name]["in-role"].remove(role.name)
                                        await CH.send("設定を変更しました")
                                        await CH.send("ロールを所有しているメンバーを除外中...")
                                        n = "<DEL-LOG>\n"
                                        c = 0
                                        for i in role.members:
                                            if i.id in user_channel[CH.name]["user"]:
                                                if i.id == user_channel[CH.name]["admin"]:
                                                    continue
                                                user_channel[CH.name]["user"].remove(i.id)
                                                await i.remove_roles(ch_role)
                                                all_user_data["user-chat"][message.author.name]["chat"][CH.name]["in-user"].remove(i.id)
                                                c += 1
                                                n += f"・{i.name}さんを除外しました\n"
                                        if c == 0:
                                            n += "・Not Found・"
                                        await CH.send(n)
                                        return
                                    else:
                                        await CH.send("<Not Found>")
                                        return
                                else:
                                    await message.channel.send("このチャンネルの管理者ではないため、実行できません")
                                    return
                            else:
                                await message.channel.send("コマンドが適用されないチャンネルです")
                                return
                        #入室を許可するユーザーの指定
                        if mct.startswith("!add-user "):
                            if message.channel.name in user_channel:
                                if message.author.id in user_channel[message.channel.name]["user"]:
                                    mid = int(mct[len("!add-user "):])
                                    if message.guild.get_member(mid):
                                        mb = message.guild.get_member(mid)
                                        if mid in user_channel[message.channel.name]["user"]:
                                            await message.channel.send(mb.mention + "さんはすでに加入しています")
                                            return
                                        role = discord.utils.find(lambda r: r.name == user_channel[message.channel.name]["role"], message.guild.roles)
                                        await mb.add_roles(role)
                                        await message.channel.send(mb.mention + "さんを招待しました")
                                        user_channel[message.channel.name]["user"].append(mid)
                                        user_channel[message.channel.name]["logs"].append("<ユーザー:" + mb.name + "さんを招待しました>\n")
                                        #データの保存
                                        all_user_data["user-chat"][message.author.name]["chat"][message.channel.name]["in-user"].append(mid)
                                        all_user_data["user-chat"][message.author.name]["chat"][message.channel.name]["logs"].append("<ユーザー:" + mb.name + "さんを招待しました>\n")
                                    else:
                                        await message.channel.send("そのidのユーザーは見つかりませんでした")
                                    return
                            else:
                                await message.channel.send("このチャンネルはコマンドで作成されたものではありません")
                                return
                        #ユーザー退場処理
                        if mct.startswith("!del-user "):
                            if message.channel.name in user_channel:
                                if message.author.id in user_channel[message.channel.name]["user"]:
                                    mid = int(mct[len("!del-user "):])
                                    if mid == user_channel[message.channel.name]["admin"]:
                                        await message.channel.send("このチャンネルの管理者を退場させることはできません")
                                        return
                                    if mid in user_channel[message.channel.name]["user"]:
                                        mb = message.guild.get_member(mid)
                                        await message.channel.send(mb.mention + "さんをチャンネルからキックしました>")
                                        user_channel[message.channel.name]["logs"].append("<" + mb.name + "さんを退場させました>\n")
                                        user_channel[message.channel.name]["user"].remove(mb.id)
                                        #データの保存
                                        all_user_data["user-chat"][message.author.name]["chat"][message.channel.name]["in-user"].remove(mb.id)
                                        all_user_data["user-chat"][message.author.name]["chat"][message.channel.name]["logs"].append("<" + mb.name + "さんを退場させました>\n")
                                        role = discord.utils.find(lambda r: r.name == user_channel[message.channel.name]["role"], message.guild.roles)
                                        await mb.remove_roles(role)
                                    else:
                                        await message.channel.send("そのidのユーザーは見つかりませんでした")
                                    
                                    
                                    return
                            else:
                                await message.channel.send("このチャンネルはコマンドで作成されたものではありません")
                                
                                
                                return
                        #チャンネル削除処理
                        if mct == "!delete":
                            if message.channel.name in user_channel:
                                if message.author.id == user_channel[message.channel.name]["admin"]:
                                    ad = client.get_user(user_channel[message.channel.name]["admin"])
                                    dm = await ad.create_dm()
                                    role = discord.utils.find(lambda r: r.name == user_channel[message.channel.name]["role"], message.guild.roles)
                                    await role.delete()
                                    await dm.send("'" + message.channel.name + "'チャンネルを削除しました")
                                    c = 0
                                    n = "\n\n<チャンネルプロセス>\n"
                                    for i in user_channel[message.channel.name]["logs"]:
                                        c += 1
                                        n += i
                                    if c == 0:
                                        n += "・アクセスはありませんでした・"
                                    await dm.send(n)
                                    del user_channel[message.channel.name]
                                    #データの保存
                                    del all_user_data["user-chat"][message.author.name]["chat"][message.channel.name]
                                    await message.channel.delete()
                                    
                                    
                                    return
                                else:
                                    await message.channel.send("このコマンドは作成者専用です")
                                    
                                    
                                    return
                            else:
                                await message.channel.send("このチャンネルは削除できません")
                                
                                
                                return
                        #サーバー用コマンド
                        #メッセージフィルターをかける
                        if mct == f"{prifix}server:messageFilter:true":
                            if message.author.id == use_guild[message.guild.name]["GOI"] or message.author.guild_permissions.administrator or message.author.id in admin:
                                try:
                                    use_guild[message.guild.name]["MF"]
                                except KeyError:
                                    use_guild[message.guild.name]["MF"] = True
                                    await message.channel.send("設定を変更しました👍")
                                    return
                                if use_guild[message.guild.name]["MF"] == False:
                                    use_guild[message.guild.name]["MF"] = True
                                    await message.channel.send("設定を変更しました👍")
                                    return
                                else:
                                    await message.channel.send("すでに設定済みです。")
                                    return
                            else:
                                await message.channel.send("あなたは本当にサーバー権限所有者ですか？")
                                
                                return
                        #メッセージフィルターをはずす
                        if mct == f"{prifix}server:messageFilter:false":
                            if message.author.id == use_guild[message.guild.name]["GOI"] or message.author.guild_permissions.administrator or message.author.id in admin:
                                try:
                                    use_guild[message.guild.name]["MF"]
                                except KeyError:
                                    use_guild[message.guild.name]["MF"] = False
                                    await message.channel.send("設定を変更しました👍")
                                    
                                    return
                                if use_guild[message.guild.name]["MF"] == True:
                                    use_guild[message.guild.name]["MF"] = False
                                    await message.channel.send("設定を変更しました👍")
                                    
                                    return
                                else:
                                    await message.channel.send("すでに設定済みです。")
                                    
                                    return
                            else:
                                await message.channel.send("あなたは本当にサーバー権限所有者ですか？")
                                
                                return
                        #特定のユーザーが所有しているチャットリスト
                        if mct.startswith(f"{prifix}my-channel"):
                            c = 0
                            n = ""
                            warning_msg_view = False
                            for i in user_channel:
                                if message.author.id == user_channel[i]["admin"]:
                                    c += 1
                                    g = client.get_guild(user_channel[i]["guild"])
                                    n += "・`" + g.name + " > " + user_channel[i]["category"] + " > " + i + ""
                                    if user_channel[i]["delete"]:
                                        n += " (削除済み)"
                                        warning_msg_view = True
                                    n += "`\n"
                            if c == 0:
                                n += "`チャンネルがありません`\n"
                            if warning_msg_view:
                                n += "```<  チャンネルを復元する場合は\n!c:restoration (削除済みのチャンネル名から引用する)\n注意 : 復元した場合削除したメッセージも復元されるため、ご注意ください\n復元も完璧なものではないですが、ご了承ください  >```"
                            embed = discord.Embed(color=discord.Colour.green(),description=n)
                            embed.set_author(name=f"< {message.author.name} >",icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                            return
                        #ユーザーのステータス表示
                        if client.user != message.author:
                            if mct == f"{prifix}status":
                                embed = discord.Embed(title="--  Status  --",color=discord.Colour.gold())
                                embed.set_thumbnail(url=message.author.avatar_url)
                                embed.add_field(name="<  Level  >",value="|   `" + str(math.floor(user_level_object[message.author.name]["level"])) + "`   |",inline=False)
                                embed.add_field(name="<<  XP  >>",value="|  `" + str(math.floor(user_level_object[message.author.name]["xp"])) + "`   |",inline=False)
                                embed.add_field(name=">>  COST  <<",value="<    `" + str(math.floor(user_level_object[message.author.name]["max_xp"])) + "`    >",inline=False)
                                await message.channel.send(embed=embed)
                                return
                        #チャンネルの復元
                        if client.user != message.author:
                            if mct.startswith(f"{prifix}restoration "):
                                c_name = mct[len(f"{prifix}restoration "):]
                                user = client.get_user(message.author.id)
                                if c_name in user_channel:
                                    if user.id == user_channel[c_name]["admin"]:
                                        if user_channel[c_name]["delete"]:
                                            RM = await message.channel.send("<チャンネルを復元開始>")
                                            role = await message.guild.create_role(name=c_name)
                                            channel = await message.guild.create_text_channel(c_name,category=message.channel.category)
                                            every = discord.utils.find(lambda r: r.name == '@everyone', message.guild.roles)
                                            await RM.edit(content="<権限をセットアップ中...>")
                                            await channel.set_permissions(role,read_messages=True,send_messages=True,read_message_history=True,view_channel=True,send_tts_messages=True,attach_files=True,embed_links=True)
                                            await channel.set_permissions(every,read_messages=False,send_messages=False,read_message_history=False)
                                            await RM.edit(content="<メッセージ履歴を復元開始>")
                                            c = 0
                                            for i in user_channel[c_name]["msg_logs"]:
                                                print(i)
                                                TARGET_USER = client.get_user(int(user_channel[c_name]["msg_logs"][i]["user"]))
                                                if 252 <= len(i):
                                                    i = i[:252]
                                                    i += "..."
                                                    print(len(i))
                                                embed = discord.Embed(title=i)
                                                try:
                                                    embed.set_author(name=TARGET_USER.name,icon_url=TARGET_USER.avatar_url)
                                                except AttributeError:
                                                    pass
                                                await channel.send(embed=embed)
                                                c += 1
                                                await RM.edit(content="<SET-UP[MSG]...>\n{} / {}".format(str(len(user_channel[c_name]["msg_logs"])),str(c)))
                                                time.sleep(0.3)
                                            user_channel[c_name]["msg_logs"] = {}
                                            await RM.edit(content="<ロールシステムをセットアップ開始>")
                                            #ロールの再付与
                                            sc = len(user_channel[c_name]["user"])
                                            c = 0
                                            for i in user_channel[c_name]["user"]:
                                                TU = message.guild.get_member(i)
                                                if TU == None:
                                                    sc -= 1
                                                    continue
                                                await TU.add_roles(role)
                                                c += 1
                                                await RM.edit(content="<SET-UP[USER]...>\n{} / {}".format(str(sc),str(c)))
                                            await RM.edit(content="<システムデータを更新中...>")
                                            #データの更新
                                            all_user_data["user-chat"][user.name]["chat"][c_name]["msg_logs"] = {}
                                            user_channel[c_name]["delete"] = False
                                            user_channel[c_name]["id"] = channel.id
                                            user_channel[c_name]["category"] = channel.category.name
                                            user_channel[c_name]["guild"] = message.guild.id
                                            #データの更新
                                            all_user_data["user-chat"][user.name]["chat"][c_name]["delete"] = False
                                            all_user_data["user-chat"][user.name]["chat"][c_name]["id"] = channel.id
                                            all_user_data["user-chat"][user.name]["chat"][c_name]["guild"] = message.guild.id
                                            all_user_data["user-chat"][user.name]["chat"][c_name]["category"] = channel.category.name
                                            await RM.edit(content="<修復完了>")
                                            return
                                        else:
                                            await message.channel.send("指定のチャンネルは存在しています。")                                            
                                            return
                                    else:
                                        await message.channel.send("このチャンネルの管理者ではないため、復元できません。")
                                        return
                                else:
                                    await message.channel.send("指定したチャンネルは復元できませんでした。")
                                    return
                        #サーバーコマンド
                        if mct == f"{prifix}server:gban_channel":
                            guild = client.get_guild(message.guild.id)
                            if message.author.id == use_guild[guild.name]["GOI"] or message.author.id in admin:
                                try:
                                    use_guild[guild.name]["system"]["gban_ch"]
                                except KeyError:
                                    use_guild[guild.name]["system"].update({"gban_ch":0})
                                use_guild[guild.name]["system"]["gban_ch"] = message.channel.id
                                await message.channel.send("登録完了しました。")
                                
                                
                                return
                            else:
                                await message.channel.send("サーバー管理者もしくはADMINではないため、実行できません")
                                
                                
                                return
                        #GBANの有効化
                        if mct == f"{prifix}server:gban:true":
                            guild = client.get_guild(message.guild.id)
                            if message.author.id == use_guild[guild.name]["GOI"] or message.author.id in admin:
                                try:
                                    use_guild[guild.name]["system"]["global_ban"]
                                except KeyError:
                                    use_guild[guild.name]["system"].update({"global_ban":True})
                                    all_user_data["guild"][guild.name]["system"].update({"global_ban":True})
                                else:
                                    if use_guild[guild.name]["system"].update({"global_ban":False}):
                                        await message.channel.send("```✔ すでに設定されています```")
                                use_guild[guild.name]["system"]["global_ban"] = True
                                all_user_data["guild"][guild.name]["system"]["global_ban"] = True
                                await message.channel.send("```設定完了しました。```")
                                
                                
                                return
                            else:
                                await message.channel.send("```サーバー管理者もしくはADMINではないため、実行できません```")
                                
                                
                                return
                        #GBANの無効化
                        if mct == f"{prifix}server:gban:false":
                            guild = client.get_guild(message.guild.id)
                            if message.author.id == use_guild[guild.name]["GOI"] or message.author.id in admin:
                                try:
                                    use_guild[guild.name]["system"]["global_ban"]
                                except KeyError:
                                    use_guild[guild.name]["system"].update({"global_ban":False})
                                    all_user_data["guild"][guild.name]["system"].update({"global_ban":False})
                                else:
                                    if not use_guild[guild.name]["system"].update({"global_ban":False}):
                                        await message.channel.send("```✔ すでに設定されています```")
                                use_guild[guild.name]["system"]["global_ban"] = False
                                all_user_data["guild"][guild.name]["system"]["global_ban"] = False
                                await message.channel.send("```設定完了しました。```")
                                return
                            else:
                                await message.channel.send("```サーバー管理者もしくはADMINではないため、実行できません```")
                                return
                        #Coloのデータログ
                        if mct == f"{prifix}server:log-channel":
                            guild = client.get_guild(message.guild.id)
                            if message.author.id == use_guild[guild.name]["GOI"] or message.author.id in admin:
                                ch = message.channel
                                try:
                                    use_guild[guild.name]["system"]["log_ch"]
                                    all_user_data["guild"][guild.name]["system"]["log_ch"]
                                except KeyError:
                                    use_guild[guild.name]["system"].update({"log_ch":message.channel.id})
                                    all_user_data["guild"][guild.name]["system"].update({"log_ch":message.channel.id})
                                    await ch.send("設定しました👍")
                                    
                                    return
                                if use_guild[guild.name]["system"]["log_ch"] == ch.id:
                                    await ch.send("すでに設定されているチャンネルです👍")
                                else:
                                    use_guild[guild.name]["system"]["log_ch"] = ch.id
                                    all_user_data["guild"][guild.name]["system"]["log_ch"] = ch.id
                                    await ch.send("設定を上書きしました👍")
                                
                                return
                            else:
                                await message.channel.send("サーバー管理者もしくはADMINではないため、実行できません")
                                
                                return
                        #ユーザーのミュート
                        if mct.startswith(f"{prifix}server:mute "):
                            ch = message.channel
                            jdv = mct[len(f"{prifix}server:mute "):]
                            guild = message.guild
                            if message.author.guild_permissions.administrator or message.author.id in admin:
                                pass
                            else:
                                await ch.send("`残念ながらあなたはこのサーバーの管理者もしくはCAユーザーではないようです...`")
                                return
                            try:
                                jdv = json.loads(jdv)
                            except json.decoder.JSONDecodeError:
                                await ch.send("`デコードエラー : '読み込みに失敗しました'`")
                                return
                            if "id" in jdv:
                                user_id = jdv["id"]
                                user = client.get_user(int(user_id))
                                if user == None:
                                    await ch.send("`FindError > '指定のidは見つかりませんでした'`")
                                    return
                                if user.id == client.user.id:
                                    await ch.send("`AccessError > 'クライアントをミュートすることはできません'`")
                                    return
                            else:
                                await ch.send("`Argument error > '必須引数[id]が見つかりませんでした'`")
                                return
                            seconds = 0
                            s = 0
                            m = 0
                            h = 0
                            if "seconds" in jdv:
                                seconds += jdv["seconds"]
                                s = jdv["seconds"]
                            if "minutes" in jdv:
                                seconds += jdv["minutes"] * 60
                                m = jdv["minutes"]
                            if "hours" in jdv:
                                seconds += jdv["hours"] * (60 * 60)
                                h = jdv["hours"]
                            if not "mute" in use_guild[guild.name]["system"]:
                                #keyがなかった時の処理
                                use_guild[guild.name]["system"].update({"mute":{}})
                                all_user_data["guild"][guild.name]["system"].update({"mute":{}})
                            #保存
                            use_guild[guild.name]["system"]["mute"].update({user_id:{"time(s)":seconds,"now":0,"channel":message.channel.id}})
                            all_user_data["guild"][guild.name]["system"]["mute"].update({user_id:{"time(s)":seconds,"now":0,"channel":message.channel.id}})
                            await ch.send(f"```py\nユーザー : '{user.name}'さんをミュートしました\n```**ミュート時間**:`{h}時間{m}分{s}秒`")
                            return
                        #カスタムprifix
                        if mct.startswith(f"{prifix}server:CustomPrifix "):
                            if message.author.guild_permissions.administrator or message.author.id in admin:
                                value = mct[len(f"{prifix}server:CustomPrifix "):]
                                use_guild[message.guild.name]["system"]["prifix"] = value
                                all_user_data["guild"][message.guild.name]["system"]["prifix"] = value
                                await message.channel.send(f"```py\nprifixが'{value}'に変更されました\n```")
                                return
                            else:
                                await message.channel.send("`残念ながらあなたはこのサーバーの管理者もしくはCAユーザーではないようです...`")
                                return
                        #settingの確認
                        with open(f"Users/{message.author.id}/pack.json","r") as f:
                            setting = json.loads(f.read())
                            if setting["setting"] != None:
                                file_name = setting["setting"]
                                try:
                                    file = open(f"Users/{message.author.id}/py-files/{file_name}")
                                    file.close()
                                except FileNotFoundError:
                                    with open(f"Users/{message.author.id}/pack.json","w") as f:
                                        setting["setting"] = None
                                        f.write(json.dumps(setting,indent=4))
                        #ファイルの作成
                        if message.content.startswith(f"{prifix}python:create "):
                            file_name = message.content[len(f"{prifix}python:create "):]
                            if not f"{file_name}" in os.listdir(f"Users/{message.author.id}/py-files"):
                                with open(f"Users/{message.author.id}/py-files/{file_name}","w") as f:
                                    pass
                                await message.channel.send("`作成しました\nワークファイルの設定は上書きされます、ご注意ください`")
                            else:
                                await message.channel.send("`そのファイルは既に存在します\n作成するファイル名を変更して再度試してください`")
                            return
                        #ファイルの一覧を表示
                        if message.content == f"{prifix}python:dir":
                            n = ""
                            for i in os.listdir(f"Users/{message.author.id}/py-files"):
                                n += f"・`{i}`\n"
                            if n == "":
                                n = "`✖ファイルは見つかりませんでした`"
                            embed = discord.Embed(color=discord.Colour.green(),description=n)
                            embed.set_author(name="< ALL FILES >",icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                            return
                        #ファイル削除
                        if message.content.startswith(f"{prifix}python:delete "):
                            file_name = message.content[len(f"{prifix}python:delete "):]
                            if os.path.exists(f"Users/{message.author.id}/py-files/{file_name}"):
                                os.remove(f"Users/{message.author.id}/py-files/{file_name}")
                                with open(f"Users/{message.author.id}/pack.json","r") as f:
                                    setting = json.loads(f.read())
                                if setting["setting"] == file_name:
                                    with open(f"Users/{message.author.id}/pack.json") as f:
                                        d = {
                                            "setting":None
                                        }
                                        f.write(json.dumps(d,indent=4))
                                await message.channel.send(f"`{file_name}`を削除しました\n`注意:ワークファイルはリセットされます`")
                            else:
                                await message.channel.send("`ファイルが見つかりませんでした...`")
                            return
                        #ワークファイル設定
                        if message.content.startswith(f"{prifix}python:set "):
                            file_name = message.content[len(f"{prifix}python:set "):]
                            if os.path.exists(f"Users/{message.author.id}/py-files/{file_name}"):
                                path = f"Users/{message.author.id}/py-files/{file_name}"
                                with open(f"Users/{message.author.id}/pack.json","w") as f:
                                    d = {
                                        "setting":file_name
                                    }
                                    f.write(json.dumps(d,indent=4))
                                await message.channel.send("`ワークファイルをセットアップしました`")
                                await FILE_VIEW(message.channel,message.author.id)
                            else:
                                await message.channel.send("`ファイルが見つかりませんでした...`")
                            return
                        #viewコマンド
                        if message.content == f"{prifix}python:view":
                            await FILE_VIEW(message.channel,message.author.id)
                            return
                        #書き込みコマンド
                        if message.content.startswith(f"{prifix}python:write"):
                            with open(f"Users/{message.author.id}/pack.json") as f:
                                setting = json.loads(f.read())
                            if setting["setting"] != None:
                                setting_file = setting["setting"]
                                file_name = setting["setting"]
                                setting_file = f"Users/{message.author.id}/py-files/{setting_file}"
                                data = message.content[len(f"{prifix}python:write"):]
                                if "\n" in data:
                                    data = data[data.find("\n") + 1:]
                                    data = data.replace("\n```","")
                                    with open(setting_file,"w",encoding="UTF-8") as f:
                                        f.write(data)
                                    with open(setting_file,"r",encoding="UTF-8") as f:
                                        lang = await find_last(file_name,".")
                                        lang = file_name[lang + 1:]
                                        n = f"```{lang}\n"
                                        for count,i in enumerate(f.readlines()):
                                            n += i
                                        n += "```"
                                        embed = discord.Embed(description=n,color=discord.Colour.green())
                                        embed.set_author(name=f"[ {file_name} preview ]",icon_url="https://www.silhouette-illust.com/wp-content/uploads/2017/09/program_binary_file_38457-300x300.jpg")
                                        await message.channel.send(embed=embed)
                                else:
                                    await message.channel.send("`書き込みの初めは改行を入れてください`")
                            else:
                                await message.channel.send("`[ FileError ]ワークファイルが指定されていません`")
                            return
                        #スクリプトの簡易実行
                        if message.content == f"{prifix}xml:run":
                            with open(f"Users/{message.author.id}/pack.json","r") as f:
                                setting = json.loads(f.read())
                            xfile_name = setting["setting"]
                            try:
                                tree = ET.parse(f"Users/{message.author.id}/py-files/{xfile_name}")
                            except ET.ParseError:
                                await message.channel.send("`xmlファイルがセットされていません`")
                                return
                            root = tree.getroot()
                            if root.find("execution") != None:
                                file_name = root.find("execution").text
                                await run_python(message.channel,message.author.id,file_name,xfile_name)
                            else:
                                await message.channel.send("`Execution`を指定してください")
                            return
                        #スクリプト実行
                        if message.content == f"{prifix}python:run":
                            with open(f"Users/{message.author.id}/pack.json","r") as f:
                                setting = json.loads(f.read())
                            if setting["setting"] != None:
                                file_name = setting["setting"]
                                with open(f"Users/{message.author.id}/py-files/{file_name}","r",encoding="UTF-8") as f:
                                    file_name2 = file_name.replace(".py","")
                                    if os.path.exists(f"Users/{message.author.id}/py-files/pack-{file_name2}.xml"):
                                        await run_python(message.channel,message.author.id,file_name2,f"pack-{file_name2}.xml")
                                    else:
                                        await message.channel.send(f"xmlファイルを検出できませんでした\n`pack-{file_name2}.xml`を作成してデータを記述してください")
                                return
                            else:
                                await message.channel.send("`[ FileError ]ワークファイルが指定されていません`")
                            return
                        #処理システム
                        #グローバルチャットシステム
                        if message.channel.id in global_channel:
                            if client.user != message.author:
                                msg = mct
                                u = message.author.name
                                u_id = message.author.id
                                l = []
                                for i in global_channel:
                                    if i == message.channel.id:
                                        continue
                                    if i in l:
                                        continue
                                    c = client.get_channel(i)
                                    if i in first_global_c:
                                        embed = discord.Embed(title="< " + message.guild.name + " >\n| " + message.channel.name + " |",description=msg,color=discord.Colour.blue())
                                        user = client.get_user(u_id)
                                        embed.set_author(name=user.name,icon_url=user.avatar_url)
                                        await c.send(embed=embed)
                                        first_global_c.remove(i)
                                        l.append(i)
                                        continue
                                    if message.author.id == after_user and message.channel.id == after_channel and message.guild.id == after_guild:
                                        embed = discord.Embed(description=msg,color=discord.Colour.blue())
                                        await c.send(embed=embed)
                                        l.append(i)
                                        continue
                                    else:
                                        embed = discord.Embed(title="< " + message.guild.name + " >\n| " + message.channel.name + " |",description=msg,color=discord.Colour.blue())
                                        user = client.get_user(u_id)
                                        embed.set_author(name=user.name,icon_url=user.avatar_url)
                                        await c.send(embed=embed)
                                        l.append(i)
                                        continue
                                after_user = message.author.id
                                after_channel = message.channel.id
                                after_guild = message.guild.id
                                return
                        #サーバーシステム構成コマンド
                        guild = message.guild
                        if mct == f"{prifix}server:operating":
                            if message.author.id == use_guild[message.guild.name]["GOI"]:
                                try:
                                    use_guild[guild.name]["GOS"]
                                except KeyError:
                                    use_guild[guild.name].update({"GOS":{"load":None,"ch":message.channel.id,"setting_package":None,"package":{}}})
                                    embed = discord.Embed(title="<<サーバーオペレーティングへようこそ>>",description="専用のコマンド使用してサーバーをカスタマイズしてみよう！",color=discord.Colour.blue())
                                    embed.add_field(name="[コマンドリスト]",value="\n`:create-unit <name:>`\n`:load`\n`:help`\n`:setting`",inline=False)
                                    embed.add_field(name="[サブコマンドリスト]",value="\n`>join (jsonデータ)`\n`>view`\n`>end`",inline=False)
                                    c = ""
                                    for i in os_event:
                                        c += i + "\n"
                                    embed.add_field(name="[条件リスト]",value=c,inline=False)
                                    await message.channel.send(embed=embed)
                                    return
                                else:
                                    try:
                                        use_guild[guild.name]["GOS"]["ch"]
                                    except KeyError:
                                        pass
                                    else:
                                        if use_guild[guild.name]["GOS"]["ch"] == message.author.channel.id:
                                            await message.channel.send("すでにデータテンプレートは作成済みです\nわからないことがあれば```:help```で確認してみましょう")
                                            return
                                        else:
                                            await message.channel.send(f"すでにオペレーション専用のチャンネルが用意されています\nチャンネルを変更する場合は```{prifix}server:OP-channel```で変更してください")
                                            return
                            else:
                                await message.channel.send("残念ながらあなたはサーバーオーナーではないみたいです...")
                                return
                        #オペレーションチャンネルを変更
                        if mct == f"{prifix}server:OP-channel":
                            if message.author.id == use_guild[message.guild.name]["GOI"]:
                                use_guild[message.guild.name]["GOS"]["ch"] = message.channel.id
                                await message.channel.send("変更しました。")
                                return
                            else:
                                await message.channel.send("残念ながらあなたはサーバーオーナーではないみたいです...")
                                return
                        #サブコマンド
                        guild = message.guild
                        prifex = [">",":"]
                        main_command = [":create_unit ",":help",":load ",":setting "]
                        sub_command = [">join ",">view",">end"]
                        try:
                            use_guild[guild.name]["GOS"]
                        except KeyError:
                            pass
                        else:
                            content = mct
                            ch = message.channel
                            if ch.id == use_guild[guild.name]["GOS"]["ch"]:
                                if message.author.id == use_guild[guild.name]["GOI"] or message.author.id in admin:
                                    if any(mct.startswith(i) for i in prifex):
                                        command_exists = False
                                        if any(mct.startswith(i) for i in main_command):
                                            command_exists = True
                                            if mct.startswith(main_command[0]):
                                                package_name = mct[len(main_command[0]):]
                                                package = use_guild[guild.name]["GOS"]["package"]
                                                status_message = await ch.send("セットアップ中...")
                                                if use_guild[guild.name]["GOS"]["setting_package"] != None:
                                                    setting_package = use_guild[guild.name]["GOS"]["setting_package"]
                                                    await status_message.edit(content=f"現在`{setting_package}`の設定が**進行中**です\n終了するには`>end`でパッケージ操作を終了します")
                                                    return
                                                if package_name in package:
                                                    await status_message.edit(content=f"パッケージ名`{package_name}`はすでに使われています")
                                                    return
                                                use_guild[guild.name]["GOS"]["package"].update({package_name:{"data":os_event}})
                                                use_guild[guild.name]["GOS"]["setting_package"] = package_name
                                                all_user_data["guild"][guild.name]["GOS"]["package"].update({package_name:{"data":os_event}})
                                                all_user_data["guild"][guild.name]["GOS"]["setting_package"] = package_name
                                                await status_message.edit(content="packageの設定が完了いたしました！\nパッケージ操作は`>join`をご利用ください")
                                                return
                                            if mct.startswith(main_command[3]):
                                                name = mct[len(main_command[3]):]
                                                packages = use_guild[guild.name]["GOS"]["package"]
                                                if name in packages:
                                                    use_guild[guild.name]["GOS"]["setting_package"] = name
                                                    all_user_data["guild"][guild.name]["GOS"]["setting_package"] = name
                                                    await ch.send(f"パッケージ`{name}`をセットしました！")
                                                else:
                                                    await ch.send(f"パッケージ`{name}`は見つからないようです...")
                                                return
                                        if any(mct.startswith(i) for i in sub_command):
                                            command_exists = True
                                            package = use_guild[guild.name]["GOS"]["setting_package"]
                                            content = mct
                                            if content.startswith(sub_command[0]):
                                                try:
                                                    content = json.loads(content[len(sub_command[0]):])
                                                except json.decoder.JSONDecodeError:
                                                    await ch.send("読み込みに失敗しました...")
                                                    return
                                                status_message = await ch.send("データの読み込みを開始...")
                                                #読み込み処理
                                                try:
                                                    exec(f"use_guild['{guild.name}']['GOS']['package']['{package}']['data'].update({content})")
                                                    exec(f"all_user_data['guild']['{guild.name}']['GOS']['package']['{package}']['data'].update({content})")
                                                except KeyError:
                                                    await status_message.edit(content="`不明な要素です`")
                                                    return
                                                await status_message.edit(content="`保存完了！`")
                                                return
                                            if content.startswith(sub_command[1]):
                                                setting_package = use_guild[guild.name]["GOS"]["setting_package"]
                                                if setting_package != None:
                                                    n = ""
                                                    for i in use_guild[guild.name]["GOS"]["package"][setting_package]["data"]:
                                                        data = use_guild[guild.name]["GOS"]["package"][setting_package]["data"][i]
                                                        n += f"・`{i} > {data}`\n"
                                                    if n == "":
                                                        n = "`オブジェクトは見つかりませんでした`\n```py\nシステム的なエラーの場合運営に報告してください\n```"
                                                    embed = discord.Embed(color=discord.Colour.blue(),description=n)
                                                    embed.set_author(name="< SETTING VIEW >",icon_url="https://www.silhouette-illust.com/wp-content/uploads/2019/10/gear_haguruma_47219-300x300.jpg")
                                                    await ch.send(embed=embed)
                                                else:
                                                    await ch.send("進行中のパッケージはありません。")
                                                return
                                            if content.startswith(sub_command[2]):
                                                setting_package = use_guild[guild.name]["GOS"]["setting_package"]
                                                if setting_package != None:
                                                    use_guild[guild.name]["GOS"]["setting_package"] = None
                                                    all_user_data["guild"][guild.name]["GOS"]["setting_package"] = None
                                                    await ch.send(f"パッケージ`{setting_package}`の操作を終了しました")
                                                else:
                                                    await ch.send("進行中のパッケージはありません。")
                                                return
                                        if not command_exists:
                                            await ch.send("```fix\n不明なコマンドです\n```")
                                    else:
                                        await message.delete()
                                        return
                                else:
                                    await message.delete()
                                    return
                    #sayデータ
                    if client.user != message.author:
                        try:
                            user_say[message.author.name]
                        except KeyError:
                            user_say[message.author.name] = 0
                        try:
                            all_user_data["user-say"][message.author.name]
                            all_user_data["user-kick"][message.author.name]
                        except KeyError:
                            all_user_data["user-say"].update({message.author.name:0})
                            all_user_data["user-kick"].update({message.author.name:0})
                        user_say[message.author.name] += 1
                        #データの保存
                        all_user_data["user-say"][message.author.name] += 1
                        print(message.author.name + " : " + str(user_say[message.author.name]))
                        #警告&キック処理
                        if not message.author.guild_permissions.administrator:
                            if user_say[message.author.name] > 5:
                                try:
                                    user_kick[message.author.name]
                                except KeyError:
                                    user_kick[message.author.name] = {}
                                    user_kick[message.author.name] = 0
                                if user_kick[message.author.name] >= 5:
                                    user_kick[message.author.name] = 0
                                    user = message.guild.get_member(message.author.id)
                                    await message.guild.kick(user)
                                    for i in user_channel:
                                        if user_channel[i]["admin"] == message.author.id:
                                            role = discord.utils.find(lambda r: r.name == user_channel[i]["role"], message.guild.roles)
                                            await role.delete()
                                            channel = client.get_channel(i)
                                            await channel.delete()
                                    user_kick.remove(message.author.name)
                                    user_say.remove(message.author.name)
                                    await message.channel.send(message.author.name + "さんは、警告を無視したため\nキックされました")
                                    return
                                user_kick[message.author.name] += 1
                                user_say[message.author.name] = 0
                                await message.channel.send(message.author.mention + "さん、過度な送信は迷惑につながるのでやめてください\nよろしくおねがいします。\n(5 / " + str(user_kick[message.author.name]) + "回目の警告、回数は10分ごとに減っていきます)")
                                all_user_data["user-say"][message.author.name] = 0
                                all_user_data["user-kick"][message.author.name] += 1
                    #レベリング処理
                    if client.user != message.author:
                        try:
                            user_level_object[message.author.name]
                        except KeyError:
                            user_level_object[message.author.name] = {}
                            user_level_object[message.author.name]["level"] = 0
                            user_level_object[message.author.name]["xp"] = 0
                            user_level_object[message.author.name]["max_xp"] = 10
                        try:
                            all_user_data["user-level"][message.author.name]
                        except KeyError:
                            #データセットアップ
                            all_user_data["user-level"].update({message.author.name:{"level":0,"cost":10,"xp":0}})
                        if user_level_object[message.author.name]["level"] <= 100:
                            user_level_object[message.author.name]["xp"] += 1
                            #データの保存
                            all_user_data["user-level"][message.author.name]["xp"] += 1
                            if user_level_object[message.author.name]["xp"] >= user_level_object[message.author.name]["max_xp"]:
                                user_level_object[message.author.name]["level"] += 1
                                #データの保存
                                all_user_data["user-level"][message.author.name]["level"] += 1
                                embed = discord.Embed(title=f" -----  {message.author.name}  -----\n<< + レベルアップ + >>",description=f"  | level |\n``` <  " + str(user_level_object[message.author.name]["level"] - 1) + "  >  >>>>>  <  " + str(user_level_object[message.author.name]["level"]) + "  >```\n  <<  COST  >>\n```" + str(math.floor(user_level_object[message.author.name]["max_xp"])) + "   > > >   " + str(math.floor(user_level_object[message.author.name]["max_xp"] * 1.2)) + "```\n\n_ID:" + str(message.author.id) + f"_",color=discord.Colour.blue())
                                embed.set_thumbnail(url=message.author.avatar_url)
                                g = message.guild
                                user_level_object[message.author.name]["max_xp"] *= 1.2
                                user_level_object[message.author.name]["xp"] = 0
                                #データの保存
                                all_user_data["user-level"][message.author.name]["cost"] *= 1.2
                                all_user_data["user-level"][message.author.name]["xp"] = 0
                                try:
                                    use_guild[g.name]["system"]["log_ch"]
                                except KeyError:
                                    await message.channel.send(embed=embed)
                                for g in client.guilds:
                                    try:
                                        use_guild[g.name]["system"]["log_ch"]
                                    except KeyError:
                                        continue
                                    ch = client.get_channel(use_guild[g.name]["system"]["log_ch"])
                                    if not ch == None:
                                        await ch.send(embed=embed,content=message.author.mention)
                                    time.sleep(0.3)
                                if user_level_object[message.author.name]["level"] >= 100:
                                    await message.channel.send("👑<//レベルカンスト//>👑\nレベルMAX、なのでADMINにID登録されました!!。")
                                    admin.append(message.author.id)
                                print(user_level_object[message.author.name]["max_xp"])
                        else:
                            user_level_object[message.author.name]["xp"] = 0
                            #データ保存
                            all_user_data["user-level"][message.author.name]["xp"] = 0
                #ユーザーチャンネルの場合のlog追加処理
                if client.user != message.author:
                    if message.channel.name in user_channel:
                        if message.author.id in user_channel[message.channel.name]["user"]:
                            user_channel[message.channel.name]["msg_logs"].update({clear_content.replace('"',"'"):{"user":message.author.id,"id":message.id}})
                        else:
                            await message.delete()
                        #データの保存
                        print(clear_content)
                        for i in all_user_data["user-chat"]:
                            for n in all_user_data["user-chat"][i]["chat"]:
                                if n == message.channel.name:
                                    if message.author.id in all_user_data["user-chat"][i]["chat"][n]["in-user"]:
                                        all_user_data["user-chat"][i]["chat"][n]["msg_logs"].update({clear_content:{"user":message.author.id,"id":message.id}})
                    #msgデータ
            except AttributeError as a:
                print(a)
        
    except Exception as error:
        embed = discord.Embed(title="<< システムエラー >>",description=f"`[ {error.__class__.__name__} ]`\n",color=discord.Colour.orange())
        embed.add_field(name="- ErrorLog -",value=f"`{error}`")
        await message.channel.send(embed=embed)

def say_down():
    while True:
        time.sleep(5)
        for i in user_say:
            if user_say[i] - 1 < 0:
                continue
            user_say[i] -= 1
            all_user_data["user-say"][i] -= 1

@client.event
async def on_raw_message_delete(payload):
    global delete_object
    if str(payload.message_id) in delete_object:
        server = client.get_guild(payload.guild_id)
        channel = server.get_channel(payload.channel_id)
        try:
            message = await channel.fetch_message(delete_object[str(payload.message_id)]["with"])
        except discord.errors.NotFound:
            del delete_object[str(payload.message_id)]
            return
        await message.delete()
        del delete_object[str(payload.message_id)]
        return

@tasks.loop(seconds=1)
async def UPDATE():
    try:
        #ユーザー名の確認
        for i in list(use_user):
            user = client.get_user(use_user[i]["id"])
            if user == None:
                continue
            for guild in client.guilds:
                if i != user.name:
                    try:
                        data = use_user[i]
                        del use_user[i]
                        del all_user_data["use-user"][i]
                        use_user.update({user.name:data})
                        all_user_data["use-user"].update({user.name:data})
                        #level
                        data = user_level_object[i]
                        del user_level_object[i]
                        user_level_object.update({user.name:data})
                        data = all_user_data["user-level"][i]
                        del all_user_data["user-level"][i]
                        all_user_data["user-level"].update({user.name:data})
                        #user-kick
                        data = user_kick[i]
                        del user_kick[i]
                        del all_user_data["user-kick"][i]
                        user_kick.update({user.name:data})
                        all_user_data["user-kick"].update({user.name:data})
                        #user-say
                        data = all_user_data["user-say"][i]
                        del user_say[i]
                        del all_user_data["user-say"][i]
                        user_say.update({user.name:data})
                        all_user_data["user-say"].update({user.name:data})
                    except KeyError:
                        pass
                    try:
                        use_guild[guild.name]["system"]["log_ch"]
                    except KeyError:
                        continue
                    ch = client.get_channel(use_guild[guild.name]["system"]["log_ch"])
                    await ch.send(f"📒ユーザー{i}さんの名前が変更されました\n**{i} -> {user.name}**")
                    time.sleep(0.3)
        #ユーザーチャンネルの確認
        for i in list(user_channel):
            if not client.get_channel(user_channel[i]["id"]):
                if user_channel[i]["delete"]:
                    continue
                user = client.get_user(user_channel[i]["admin"])
                dm = await user.create_dm()
                n = "\n\n" + user.mention + "\nあなたの '" + i + "' チャンネルが削除されていました\n"
                n += "<アクセス>\n"
                for si in user_channel[i]["logs"]:
                    n += si
                if len(user_channel[i]["logs"]) == 0:
                    n += "・アクセスはありません・"
                await dm.send(n)
                #データの保存
                all_user_data["user-chat"][user.name]["chat"][i]["logs"] = []
                g = client.get_guild(user_channel[i]["guild"])
                role = discord.utils.find(lambda r: r.name == user_channel[i]["role"], g.roles)
                await role.delete()
                user_channel[i]["delete"] = True
                #データの保存
                all_user_data["user-chat"][user.name]["chat"][i]["delete"] = True
                time.sleep(0.3)
        #SERVERテンプレート確認
        for i in list(use_guild):
            guild = client.get_guild(use_guild[i]["id"])
            if guild == None:
                del use_guild[i]
                continue
            if i != guild.name:
                data = use_guild[i]
                del use_guild[i]
                del all_user_data["guild"][i]
                use_guild.update({guild.name:data})
                all_user_data["guild"].update({guild.name:data})
                pass_object.append(guild.name)
                print(guild.name)
                for n in use_guild:
                    try:
                        use_guild[n]["system"]["log_ch"]
                    except KeyError:
                        continue
                    CH = client.get_channel(use_guild[n]["system"]["log_ch"])
                    await CH.send(f"📒サーバー名が変更されたためデータを更新しました。\n**{i} -> {guild.name}**")
        #GBANシステム
        for guild in client.guilds:
            try:
                use_guild[guild.name]["system"]["global_ban"]
            except KeyError:
                continue
            else:
                if not use_guild[guild.name]["system"]["global_ban"]:
                    continue
            for i in guild.members:
                if i.id in global_ban:
                    try:
                        await guild.kick(i)
                    except discord.errors.Forbidden:
                        continue
                    embed = discord.Embed(title=f"**SAFETY-KICK LOG [{i.name}]**",description=f"{i.name}さんを発見したためKICKしました。\n\n_EVENT POS : ({guild.name})_\n_USER:ID {i.id}_",color=discord.Colour.green())
                    embed.set_author(name=i.name,icon_url=i.avatar_url)
                    for n in use_guild:
                        if "gban_ch" in use_guild[n]["system"].keys():
                            CH = client.get_channel(use_guild[n]["system"]["gban_ch"])
                            print(CH.name)
                            if CH == None:
                                use_guild[n]["system"]["gban_ch"] = 0
                                all_user_data["guild"][n]["system"]["gban_ch"] = 0
                                continue
                            await CH.send(embed=embed)
        #サーバーの存在確認
        for i in list(use_guild):
            guild = client.get_guild(use_guild[i]["id"])
            if guild == None:
                print(f"false > {i}")
                for n in list(use_guild):
                    try:
                        use_guild[n]["system"]["log_ch"]
                    except KeyError:
                        continue
                    else:
                        ch = client.get_channel(use_guild[n]["system"]["log_ch"])
                        embed = discord.Embed(description=f"サーバー **{i}** から退出しました",color=discord.Colour.blue())
                        embed.set_author(name=f"<< SERVER LEFT [{i}] >>",icon_url="https://mates-app.jp/reco/apt-sp/img/nyutai_icon.jpg")
                        await ch.send(embed=embed)
                    try:
                        del all_user_data["guild"][i]
                        del use_guild[i]
                    except KeyError:
                        continue
    except Exception as a:
        print(f"SEFTY-{a.__class__.__name__}>{a}")
        for i in range(6):
            print(f"sleep {i}...")
            await asyncio.sleep(1)
        print("REstart")

@tasks.loop(seconds=3)
async def load_now_custom():
    global second,hour,check,global_ban,use_guild
    try:
        users = 0
        for i in client.users:
            users += 1
        guilds = 0
        for i in client.guilds:
            guilds += 1
        actv = discord.Game(name=f"prefix: !c | Users < " + str(users) + " > Servers < " + str(guilds) + " > botが起動してからの時間 < " + str(hour) + ":" + str(second) + ":" + str(check) + " >")
        await client.change_presence(status=discord.Status.do_not_disturb,activity=actv)
        
    except Exception as a:
        print(f"SEFTY-{a.__class__.__name__}>{a}")
        for i in range(6):
            print(f"sleep {i}...")
            await asyncio.sleep(1)
        print("REstart")



def w():
    while True:
        schedule.run_pending()

@tasks.loop(seconds=1)
async def mute_load():
    for i in list(use_guild):
        if not "mute" in use_guild[i]["system"]:
            continue
        for n in list(use_guild[i]["system"]["mute"]):
            use_guild[i]["system"]["mute"][n]["now"] += 1
            if use_guild[i]["system"]["mute"][n]["time(s)"] <= use_guild[i]["system"]["mute"][n]["now"]:
                ch = client.get_channel(use_guild[i]["system"]["mute"][n]["channel"])
                user = client.get_user(int(n))
                if not ch == None and not user == None:
                    await ch.send(f"{user.mention}さんのミュートが解除されました")
                try:
                    del use_guild[i]["system"]["mute"][n]
                    del all_user_data["guild"][i]["system"]["mute"][n]
                except KeyError:
                    pass
                f = open("data.json","w",encoding="UTF-8")
                f.write(json.dumps(all_user_data,indent=4))
                f.close()

def all_custom():
    global check,kick_reset,second,hour
    check += 1
    if 60 <= check:
        check = 0
        second += 1
    if 60 <= second:
        second = 0
        hour += 1
    kick_reset += 1
    if kick_reset >= 60 * 10:
        for i in list(user_kick):
            if user_kick[i] > 0:
                user_kick[i] -= 1
                all_user_data["user-kick"][i] -= 1
                print(i + " : " + str(user_kick[i]))
        kick_reset = 0

def pf(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

async def find_last(text,p):
    last_point = 0
    while True:
        point = text.find(p)
        last_point += point + len(p)
        if p in text[point + len(p):]:
            text = text[point + len(p):]
        else:
            return last_point - len(p)

async def FILE_VIEW(channel,author_id):
    with open(f"Users/{author_id}/pack.json") as f:
        setting = json.loads(f.read())
    if setting["setting"] != None:
        setting_file = setting["setting"]
        file_name = setting["setting"]
        setting_file = f"Users/{author_id}/py-files/{setting_file}"
        with open(setting_file,"r",encoding="UTF-8") as f:
            lang = await find_last(file_name,".")
            lang = file_name[lang + 1:]
            n = f"```{lang}\n"
            for count,i in enumerate(f.readlines()):
                n += i
            n += "```"
            embed = discord.Embed(description=n,color=discord.Colour.green())
            embed.set_author(name=f"[ {file_name} preview ]",icon_url="https://www.silhouette-illust.com/wp-content/uploads/2017/09/program_binary_file_38457-300x300.jpg")
            await channel.send(embed=embed)
    else:
        await channel.send("`[ FileError ]ワークファイルが指定されていません`")

async def run_python(channel,author_id,run_file,xml_file_name):
    funcs = []
    xlog = "loading xml...\n"
    tree = ET.parse(f"Users/{author_id}/py-files/{xml_file_name}")
    root = tree.getroot()
    for data in root:
        for f in data.iter("function"):
            if f.find("call") != None:
                func_name = f.find("call").text
                funcs.append({func_name:{"args":[]}})
                number = len(funcs) - 1
            else:
                xlog += "[ERROR] - element `call` is not Found\n"
                continue
            for arg in f.iter("arg"):
                funcs[number][func_name]["args"].append(arg.text)
            for arg in f.iter("argInt"):
                i = arg.text
                i = int(i)
                funcs[number][func_name]["args"].append(i)
    xlog += "`----------result----------`"
    await channel.send(xlog)
    print(funcs)
    for func_ele in funcs:
        func = func_ele
        for i in func_ele:
            module = importlib.import_module(f"Users.{author_id}.py-files.{run_file}")
            importlib.reload(module)
            args = str(func[i]["args"])
            args = args.replace("]","").replace("[","")
            if args != "":
                args = eval(args)
            print(args)
            print(type(args))
            try:
                func = getattr(module,i)
            except AttributeError:
                await channel.send(f"**[ERROR] - attribute**`{i}`**is not Found**")
                continue
            try:
                if type(args) == tuple:
                    data = func(*args)
                elif args == "":
                    data = func()
                else:
                    data = func(args)
            except Exception as error:
                embed = discord.Embed(title="< コードエラー >",description=f"`| {error.__class__.__name__} |`",color=discord.Colour.red())
                embed.add_field(name="- Traceback -",value=f"`{error}`")
                await channel.send(embed=embed)
                continue
            if data == None:
                data = "`No ResultView`"
            await channel.send(data)

async def cut_off(text,p1="",p2=""):
    if p1 in text:
        if p1 == "":
            if p2 in text:
                p1p = text.find(p2)
                return text[:p1p]
            else:
                return None
        p1p = text.find(p1)
        p1p += len(p1)
        if p2 == "":
            return text[p1p:]
        if p2 in text[p1p:]:
            p2p = text[p1p:].find(p2) + p1p
            print(text[p1p:p2p])
            return text[p1p:p2p]
        else:
            return None
    else:
        return None

def cut_out(content,start,end):
    if start in content:
        p1 = content.find(start) + len(start)
        if end in content[p1:]:
            p2 = content[p1:].find(end) + p1
            return content[p1:p2]
        else:
            return None
    else:
        return None

client.run(TOKEN)
