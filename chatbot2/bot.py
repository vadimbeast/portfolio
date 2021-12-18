import telebot, wikipedia, re

bot = telebot.TeleBot('5093020235:AAH2qlCAWsrdPdOgbUZ9rWHMIzb2uQWPDDU')



#Запросы к википедии
wikipedia.set_lang('ru')

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                    wikitext2 = wikitext2 + x +'.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом.'

#Функция для запроса юзера
@bot.message_handler(commands = ['start'])
def start(m, res = False):
    bot.send_message(m.chat.id, 'Википедия на связи. Спроси меня о чем-нибудь')

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Ты написал: ' + '"' + message.text + '". ' +\
        getwiki(message.text))
                        



bot.polling(none_stop = True, interval = 0)
