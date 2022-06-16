import json
import boto3
import os
import logging

s3 = boto3.client('s3')
sns = boto3.client('sns')
topic = os.environ.get('PATIENT_CHECKOUT_TOPIC')
logger = logging.getLogger('patientlogger')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    logger.info('Reading {} from {}'.format(file_key,bucket_name))

    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = obj['Body'].read().decode('UTF-8')

    checkout_patients = json.loads(file_content)
    for patient in checkout_patients:
        logger.info("Message being sent")
        logger.info(patient)
        sns.publish(
            TopicArn=topic,
            Message=json.dumps({'default': json.dumps(patient)}),
            MessageStructure='json'
        )



