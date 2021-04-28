import telebot
from time import sleep
import random


TOKEN='1777813467:AAG8Cd5FM1_jbIt7XybzZK4bgRByqg_DtBI'
bot=telebot.TeleBot(TOKEN)
yes='CAACAgQAAxkBAAECPTpgiUlWrpTERtdXCxVRrfXEEWJcswACkwEAAjPl4hVchh0Om9EIth8E'
no='CAACAgQAAxkBAAECPTZgiUlNis1SpHVo7IZ6L95xTNiK6QACkQEAAjPl4hUAATXKzK6Do7IfBA'
aga='CAACAgQAAxkBAAECPThgiUlSrnH_tUa4kqouhhAa37M4twACkgEAAjPl4hWqAbtFfYNHTB8E'
yra='CAACAgQAAxkBAAECPT5giUleliY0R1Rex19MsAnnml8AAQ4AAsABAAIz5eIVSH0V0QJZ484fBA'
@bot.message_handler(content_types=['text'])
#@bot.message_handler(content_types=['data'])
#@bot.message_handler(content_types=['sticker'])


def text(message):
    str=message.text.lower()
    str.split(" ")
    if len(str)>=3:
        if len(str)==4:
            if ('а' in str[-1] and 'д' in str[-2] and str[-3]==' '):

                bot.send_sticker(message.chat.id, yes,reply_to_message_id=message.id)

        elif len(str)>4:
            if str[-1] == '!' or str[-1] == "." or str[-1]=="?":
                if ('а' in str[-2] and 'д' in str[-3] and str[-4] == ' '):
                    bot.send_sticker(message.chat.id, yes, reply_to_message_id=message.id)
            else:
                if ('а' in str[-1] and 'д' in str[-2] and str[-3] == ' '):
                    bot.send_sticker(message.chat.id, yes, reply_to_message_id=message.id)
        else:
            if str[-1] == '!' or str[-1] == "." or str[-1]=="?":
                if ('а' in str[-2] and 'д' in str[-3]):
                    bot.send_sticker(message.chat.id, yes, reply_to_message_id=message.id)
    else:
        if len(str)==2:
            if 'а' in str[-1] and 'д' in str[-2]:
                bot.send_sticker(message.chat.id, yes, reply_to_message_id=message.id)

    if message.text.lower() == "нет":
        bot.send_sticker(message.chat.id, no, reply_to_message_id=message.id)
    elif message.text.lower() == "ага":
        bot.send_sticker(message.chat.id, aga, reply_to_message_id=message.id)
    elif message.text.lower() == "ура":
        bot.send_sticker(message.chat.id, yra, reply_to_message_id=message.id)

    elif 'улитка' in str or 'улитку' in str or 'улитке' in str or 'улитки' in str or 'улиток' in str:
        bot.send_document(message.chat.id,data='https://gifer.com/ru/EAuD', reply_to_message_id=message.id)

    # else:
    #      list = [1, 2, 3, 4, 5]
    #      list = random.choice(list)
    #      print(list)
    #         #if message.id='399559419':
    #      if list == 1:
    #         bot.send_document(message.chat.id,data='https://tenor.com/view/bts-dynamite-gif-18149737',reply_to_message_id=message.id)
    #      elif list==2:
    #          bot.send_document(message.chat.id, data='https://tenor.com/view/bts-dynamite-bts-gif-18188803', reply_to_message_id=message.id)
    #
    #      elif list == 3:
    #         bot.send_document(message.chat.id,data='https://tenor.com/view/jungkook-bts-dynamite-jeonjungkook-jeon-gif-18184277',reply_to_message_id=message.id)
    #      elif list==4:
    #          bot.send_document(message.chat.id, data='https://tenor.com/view/dynamite-bts-%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8-%EB%B0%A9%ED%83%84-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%A7%88%EC%9D%B4%ED%8A%B8-gif-18181901', reply_to_message_id=message.id)
    #
    #      elif list == 5:
    #         bot.send_document(message.chat.id, data='https://tenor.com/view/bts-bts-dynamite-dynamite-bts-mma-mma2020-gif-19452198',
    #                           reply_to_message_id=message.id)



bot.polling()