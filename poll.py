#from .response import *
import logging

def parse_params(msg):
    params = msg.split(' ')[1:]
    logging.info('Num of pool params: {}'.format(len(params)))
    for i, opt in enumerate(params):
        logging.info('Param {}: {}'.format(i, opt))
    return params

def poll_handler(bot, update):
    """Handles all polls commands."""
    params = parse_params(update.message.text)

    logging.info('/param command')

    # single params: list
    if len(params) == 1:
        if params[0] == 'list':
            # ...
            logging.info('List of available polls is requested!')
    elif len(params) > 1:
        if params[0] == 'create':
            # ...
            logging.info('Creation of a new poll is requested!')
            return
        
        if params[0] == 'delete':
            # ...
            logging.info('Deletion of a new poll is requested!')
            return

        if params[0] == 'view':
            # ...
            logging.info('View of a poll is requested!')
            return


    