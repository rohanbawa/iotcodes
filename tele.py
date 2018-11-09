import time
import telepot
from telepot.loop import MessageLoop
def action(msg):
    chat_id=msg['chat']['id']
    command=msg['text']
    print('received %s' %command)
    if command=='/hi':
        t_bot.sendMessage(chat_id,str("hiii"))
    elif command=='/bye':
        t_bot.sendMessage(chat_id,str('byee'))
    elif command=='/image':
        t_bot.sendPhoto(chat_id, photo = "https://charactersrealnames.com/wp-content/uploads/2015/03/jethalal_gada_dilip_joshi.jpg")
    elif command=='/video':
        t_bot.sendVideo(chat_id, video = "F:\H drive\ketan\Sacred Games 2018 S01 Complete Season 1 Hindi 720p NetFlix x264 DDP 5.1 ESub - xRG/Sacred Games 2018  Hindi S01EP01 (Ashwatthama) 720p NetFlix x264 DDP 5.1 ESub - xRG.mkv")
t_bot=telepot.Bot('622633559:AAE_EBeNPv5F6Lp6VvzGL9KJKWE35oqm83Y')
print(t_bot.getMe())
MessageLoop(t_bot,action).run_as_thread()
print('run hotay re bagh.......')
while True:
    time.sleep(10)
