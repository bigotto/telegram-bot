#coding: utf-8
import telegram
from telegram.ext import Updater, CommandHandler
import speedtest

def typing(bot, update):
    # Send typing action aprox for 6s
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)

def start(bot, update):
    me = bot.get_me()
    # Message
    msg = ("Olá!\n")
    #msg += ('Eu sou %s e estou aqui para ajudá-lo\n' % me.first_name)
    msg += ('Comandos disponíveis:\n')
    msg += ('/speedtest - Velocidade da internet')
    
    # Commands menu
    main_menu_keyborad = [[telegram.KeyboardButton('/speedtest')]]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyborad, resize_keyboard=True, one_time_keyboard=True)

    #Send message with menu
    bot.send_message(chat_id=update.message.chat_id, text=msg, reply_markup=reply_kb_markup)

def network(bot, update):
    typing(bot, update)
    s = speedtest.Speedtest()

    typing(bot, update)
    s.get_best_server()

    typing(bot, update)
    down = s.download()
    
    typing(bot, update)
    up = s.upload() 
    
    typing(bot, update)
    result = s.results.dict()
    down_mb = down / 1000000
    up_mb =  up / 1000000

    typing(bot, update)
    msg = ('Ping: %d\n' %result["ping"])
    msg += ('Download: %.2f Mbps\n' % down_mb)
    msg += ('Upload: %.2f Mbps\n' % up_mb)
    update.message.reply_text(msg)

#Configurando o Bot
updater = Updater('793281209:AAFaAxdxZ_9JC5BSm0eyJbDswbKfYkJFnxg')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('speedtest', network))

updater.start_polling()
updater.idle()
