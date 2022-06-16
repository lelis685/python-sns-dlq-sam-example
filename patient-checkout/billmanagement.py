import logging

logger = logging.getLogger('billmanagement')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    logger.info('Message received: {}'.format(message))