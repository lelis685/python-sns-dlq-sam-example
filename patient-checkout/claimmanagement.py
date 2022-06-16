import logging

logger = logging.getLogger('claimmanagement')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info('Claim management received {} messages'.format(len(event['Records'])))
    for record in event['Records']:
        print(record['body'])
