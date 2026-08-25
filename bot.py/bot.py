    import telebot
    import os
    TOKEN = os.getenv("TOKEN")
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message, "Bot Aktif 24 Jam 🔥")

    bot.polling(none_stop=True)
