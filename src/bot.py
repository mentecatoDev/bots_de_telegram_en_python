from telegram.ext import Updater, CommandHandler, CallbackContext
from config.auth import token

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s \
    - %(message)s', level=logging.INFO)
logger = logging.getLogger('romerovargasbot')


def start(update: Updater, context: CallbackContext):
    logger.info('He recibido un comando start')
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Soy de Jerez de la Frontera, cuna del fino, de los caballos "
             "cartujanos y Capital Mundial del Motociclismo")


if __name__ == '__main__':

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
