import sys

from telegram.ext import MessageHandler, CommandHandler, Application, filters, ConversationHandler

import configuration, parsing


async def start(update, context):
    await update.message.reply_text("Привет! Я твой новый бот!")
    await update.message.reply_text(configuration.command)


async def help(update, context):
    await update.message.reply_text(configuration.command)


async def echo(update, context):
    await update.message.reply_text('"' + update.message.text[6:] + '" Эти слова для меня многое значат.')


async def weather(update, context):
    if parsing.getWeather(update.message.text[8:], configuration.openWeather_token) != "not exist":
        list = parsing.getWeather(update.message.text[8:], configuration.openWeather_token)
        await update.message.reply_text(
            f"Город: {list[0]},\nТемпература: {list[1]} °С,\nВлажность: {list[2]}%,\nСкорость ветра: {list[3]} м/с.")
    else:
        await update.message.reply_text("Город не найден. Пожалуйста, введите существующий город на английском языке.")


async def news(update, context):
    str = ""
    for title in parsing.parseNews(configuration.urlRia):
        str += title + "\n\n"
    await update.message.reply_text(str)


async def joke(update, context):
    await update.message.reply_text(parsing.parseJoke(configuration.urlRandstuff))


async def stop(update, context):
    await update.message.reply_text("Вот так ты со мной, да? Я тебе помогал, развлекал, а ты решил меня выключить? "
                                    "Ну и ладно! Больно ты мне нужен!")
    sys.exit()


def main():
    application = Application.builder().token(configuration.bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("echo", echo))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("weather", weather))
    application.add_handler(CommandHandler("news", news))
    application.add_handler(CommandHandler("joke", joke))
    application.add_handler(CommandHandler("stop", stop))

    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), weather))

    application.run_polling()



