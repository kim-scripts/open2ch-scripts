#ログ削除的な？
import os

os.system('cls')
print('起動完了')

#モジュールロード
import tkinter as tk

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

#情報見る場所
infolabel = tk.LabelFrame(root, width=400, height=220, fg="snow", font=("Questrial", 16, "bold"), bg="gray1", bd=6,text="INFO")
infolabel.place(x=1, y=1)

all_message_label = tk.Label(text=f'総メッセージ送信数:{all_message}', bg="gray1", fg="snow", font=("Questrial",16,"bold"))
all_message_label.place(x=10, y=25)

info_proxy_label = tk.Label(text=f'Proxy:{info_proxy}', bg="gray1", fg="snow", font=("Questrial",16,"bold"))
info_proxy_label.place(x=10, y=50)



def kari():
    print('OK')

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
dolabel = tk.LabelFrame(root, width=400, height=440, fg="snow", font=("Questrial", 16, "bold"), bg="gray1", bd=6,text="入力版")
dolabel.place(x=410, y=1)
ita_label = tk.Label(text='板のID', bg="gray1", fg="snow", font=("Questrial",14,"bold"))
ita_label.place(x=420,y=30)
ita_id = tk.Entry(root,width=30)
ita_id.place(x=420, y=60)

surelabel = tk.Label(text='スレッドのID', bg="gray1", fg="snow", font=("Questrial",14,"bold"))
surelabel.place(x=420,y=80)
sure_id = tk.Entry(root,width=30)
sure_id.place(x=420, y=110)

subdlabel = tk.Label(text='サブドメイン', bg="gray1", fg="snow", font=("Questrial",14,"bold"))
subdlabel.place(x=420,y=130)
subd_id = tk.Entry(root,width=30)
subd_id.place(x=420, y=160)

content_label = tk.Label(text='メッセージ内容', bg="gray1", fg="snow", font=("Questrial",14,"bold"))
content_label.place(x=420,y=180)
content = tk.Text(root, width=26, height=8)
content.place(x=420, y=210)

random = tk.Checkbutton(root, text='ランダム(最後の方)',command=kari, bg="slate gray", fg="grey1", font=("Questrial", 12), relief="raised", width=17)
random.place(x=615,y=35)
random_message = tk.Checkbutton(root, text='ランダムメッセージ',command=kari, bg="slate gray", fg="grey1", font=("Questrial", 12), relief="raised", width=17)
random_message.place(x=615,y=65)
all_spam = tk.Checkbutton(root, text='全スレッドにスパム',command=spam_thread, bg="slate gray", fg="grey1", font=("Questrial", 12), relief="raised", width=17)
all_spam.place(x=615,y=95)
proxy_true = tk.Checkbutton(root, text='Proxyを使う',command=proxy_chenge, bg="slate gray", fg="grey1", font=("Questrial", 12), relief="raised", width=17)
proxy_true.place(x=615,y=125)

#スパマー本体
def start():
    tool.spammer.spammer(tool.channel_load.sq_o2ch(ita_id.get(),subd_id.get()))

#ボタン類
buttonlabel = tk.LabelFrame(root, width=400, height=210, fg="snow", font=("Questrial", 16, "bold"), bg="gray1", bd=6,text="ボタン類")
buttonlabel.place(x=1, y=230)
button_start = tk.Button(root, font=("MSゴシック", "10", "bold"), text="START", bg="slate gray", relief="raised", width=23, height=1, justify=tk.CENTER, command=start)
button_start.place(x=15, y=260)
button_stop =tk.Button(root, font=("MSゴシック", "10", "bold"), text="STOP", bg="slate gray", relief="raised", width=23, height=1, justify=tk.CENTER, command=kari)
button_stop.place(x=15, y=295)
button_stop_kinkyu =tk.Button(root, font=("MSゴシック", "10", "bold"), text="緊急停止ボタン", bg="red", relief="raised", width=23, height=1, justify=tk.CENTER, command=stop_now)
button_stop_kinkyu.place(x=15, y=400)
button_proxy =tk.Button(root, font=("MSゴシック", "10", "bold"), text="Proxyをロードする", bg="slate gray", relief="raised", width=21, height=1, justify=tk.CENTER, command=kari)
button_proxy.place(x=214, y=260)

root.mainloop()

print('終了')