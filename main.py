#ログ削除的な？
import os

os.system('cls')
print('起動完了')

#モジュールロード
import tkinter as tk
from tkinter import messagebox , filedialog
import threading
import asyncio
import subprocess
import urllib.parse
import urllib.request
import urllib
import requests
import time
import datetime

#ツールロード
import tool.channel_load
import tool.spammer

root = tk.Tk()
root.title('ROSA-O2S')
root.geometry("1400x600")
root.configure(bg="gray1")

#初期値
all_message = 0
info_proxy = 0
use_proxy = False
spam_all = False

infolabel = tk.LabelFrame(root, width=400, height=220, fg="snow", font=("Questrial", 16, "bold"), bg="gray1", bd=6,text="INFO").place(x=1, y=1)
all_message_label = tk.Label(text=f'総メッセージ送信数:{all_message}', bg="gray1", fg="snow", font=("Questrial",16,"bold")).place(x=10, y=25)
info_proxy_label = tk.Label(text=f'Proxy:{info_proxy}', bg="gray1", fg="snow", font=("Questrial",16,"bold")).place(x=10, y=50)

def kari():
    print('OK')

def start():
    global subd_id
    global ita_id
    print(f'https://{subd_id}.open2ch.net/{ita_id}/')

def stop_now():
    exit()

def proxy_chenge():
    global use_proxy
    if use_proxy == True:
        use_proxy = False
        print(use_proxy)
    else:
        use_proxy = True
        print(use_proxy)

def spam_thread():
    global spam_thread
    if spam_thread == True:
        spam_thread = False
        print(spam_thread)
    else:
        spam_thread = True
        print(spam_thread)


#入力系統
dolabel = tk.LabelFrame(root, width=400, height=440, fg="snow", font=("Questrial", 16, "bold"), bg="gray1", bd=6,text="入力版").place(x=410, y=1)
tk.Label(text='板のID', bg="gray1", fg="snow", font=("Questrial",14,"bold")).place(x=420,y=30)
ita_id = tk.Entry(width=30).place(x=420, y=60)

tk.Label(text='スレッドのID', bg="gray1", fg="snow", font=("Questrial",14,"bold")).place(x=420,y=80)
sure_id = tk.Entry(width=30).place(x=420, y=110)

tk.Label(text='サブドメイン', bg="gray1", fg="snow", font=("Questrial",14,"bold")).place(x=420,y=130)
subd_id = tk.Entry(width=30).place(x=420, y=160)

tk.Label(text='メッセージ内容', bg="gray1", fg="snow", font=("Questrial",14,"bold")).place(x=420,y=180)
content = tk.Text(root, width=26, height=8).place(x=420, y=210)

tk.Checkbutton(root, text='ランダム(最後の方)',command=kari, bg="slate gray", fg="grey1", font=("Questrial", 12), relief="raised", width=17).place(x=615,y=35)
tk.Checkbutton(root, text='ランダムメッセージ',command=kari, bg="slate gray", fg="grey1", font=("Questrial", 12), relief="raised", width=17).place(x=615,y=65)
tk.Checkbutton(root, text='全スレッドにスパム',command=spam_thread, bg="slate gray", fg="grey1", font=("Questrial", 12), relief="raised", width=17).place(x=615,y=95)
tk.Checkbutton(root, text='Proxyを使う',command=proxy_chenge, bg="slate gray", fg="grey1", font=("Questrial", 12), relief="raised", width=17).place(x=615,y=125)


#ボタン類
buttonlabel = tk.LabelFrame(root, width=400, height=210, fg="snow", font=("Questrial", 16, "bold"), bg="gray1", bd=6,text="ボタン類").place(x=1, y=230)
tk.Button(root, font=("MSゴシック", "10", "bold"), text="START", bg="slate gray", relief="raised", width=23, height=1, justify=tk.CENTER, command=start).place(x=15, y=260)
tk.Button(root, font=("MSゴシック", "10", "bold"), text="STOP", bg="slate gray", relief="raised", width=23, height=1, justify=tk.CENTER, command=kari).place(x=15, y=295)
tk.Button(root, font=("MSゴシック", "10", "bold"), text="緊急停止ボタン", bg="red", relief="raised", width=23, height=1, justify=tk.CENTER, command=stop_now).place(x=15, y=400)
tk.Button(root, font=("MSゴシック", "10", "bold"), text="Proxyをロードする", bg="slate gray", relief="raised", width=21, height=1, justify=tk.CENTER, command=kari).place(x=214, y=260)

root.mainloop()

print('終了')