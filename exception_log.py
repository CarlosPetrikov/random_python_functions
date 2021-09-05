import sys
from datetime import datetime
import telebot
import logging

# logging file configuration
log_file = 'C:/LOGS/Exception_script.log'
logging.basicConfig(filename = log_file,
                    level = logging.ERROR,
                    format = '%(asctime)s - %(levelname)s | %(message)s')
#You can use logger object with following methods: logger.debug|info|warning|error|critical
logger = logging.getLogger()
  
# Function to notify a exception to a telegram user (or group) and log the exception in a file
def exception_log(token_bot, id_notify, error):
    bot = telebot.TeleBot(token_bot)
    var_check = False
    while var_check == False:
        try:            
            logger.error(f'EXCEPTION: {error} ON LINE {sys.exc_info()[2].tb_lineno}')         
            bot.send_message(id_notify, f'🙃 EXCEPTION: {error} ON LINE {sys.exc_info()[2].tb_lineno}')              
            var_check = True
        except Exception as error_2:
            #In case of Telegram notify error, both exceptions will be logged in a file
            logger.error(f'EXCEPTION 1: {error} ON LINE {sys.exc_info()[2].tb_lineno}')
            logger.error(f'EXCEPTION 2: {error_2} ON LINE {sys.exc_info()[2].tb_lineno}')
            
#Example:
try:
    a = 1/0
except Exception as error:
    exception_log('123456789abcdefgh', '-12345678', error)