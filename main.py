import telebot


dict = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


bot = telebot.TeleBot("5947477164:AAGcETvCF-_Po3I6YzRHhZBQ8n7XfJ6jHc0")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "This bot converts messages to morse code and morse code to messages\nrules of morse code are each letter is seperated by 1 space and each word is seperated by 2 spaces")


@bot.message_handler(func=lambda msg: msg.text is not None)
def mes_input(message):
    a=message.text
    lis=list(a.lower())
    if lis[0]=='-':
        tostr=''
        temp=''
        for i in lis:
            if(i!=' '):
                j=0
                temp=temp+i
            else:
                j=j+1
                if j==2:
                    tostr=tostr+' '
                else:
                    tostr=tostr+list(dict.keys())[list(dict.values()).index(temp)]
                    temp=''
        bot.reply_to(message,tostr)
    else:
        tostr=''
        for i in lis:
            if i!=' ':
                tostr=tostr+dict[i]+' '
            else:
                tostr=tostr+' '
        bot.reply_to(message,tostr)


bot.polling()