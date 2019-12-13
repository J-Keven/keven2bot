import telebot

KEY = "902749089:AAEj5X-1HCeTDdeKMZ-CfWEPRnvFRbOtYOA"
bot = telebot.TeleBot(KEY)

@bot.message_handler(commands=["oi", "cafe", "pipoca", "programar", "cansado"])
def commands(session):
    if session.text == "/cafe":
        gif = "https://media.giphy.com/media/hGB45pbAj1CHm/giphy.gif"
    
    elif session.text == "oi":
        gif = "https://media.giphy.com/media/hUGInbVaRV1J5L1XUu/giphy.gif"

    elif session.text == "/pipoca":
        gif = "https://media.giphy.com/media/TiDV76pqa7AgT3cEZy/giphy.gif"
    
    elif session.text == "/programar":
        gif = "https://media.giphy.com/media/7J4P7cUur2DlErijp3/giphy.gif"

    elif session.text == "/cansado":
        gif = "https://media.giphy.com/media/cuPm4p4pClZVC/giphy.gif"

    # print(session.text)
    bot.send_document(session.chat.id, gif)
    # print(dir(bot))

@bot.message_handler(func=lambda i: True)
def interagindo(session):
    mensenge = {"oi": "https://media.giphy.com/media/hUGInbVaRV1J5L1XUu/giphy.gif", "tudo bem?": "Sim, e com vc?", 
                "Tudo otimo": "Que legal, Shoow", "faz o que da vida?":"Faco programas", "ahh legal":"https://media.giphy.com/media/MfJzOyQnqpHTa/giphy.gif",
                "Ola": "olá, aceita um café? kkkkkkkkkk", "Sim": "https://media.giphy.com/media/hGB45pbAj1CHm/giphy.gif"}
    if session.text in mensenge:
        bot.reply_to(session,mensenge[session.text])

bot.polling()
