from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from DataProcessing.Fordata import main, big_chats


def bot():
    # ввобдим имя бота (при новом запуске с обним и тем же именем, бота обучать не обязательно)
    chat_bot = ChatBot('Emil Bot')
    # обучаем бота на массиве подряд идущих сообшений
    trainer = ListTrainer(chat_bot)
    trainer.train(big_chats('DataProcessing/chat.txt', False))

    while True:
        text = input()
        print(chat_bot.get_response(text))


bot()
