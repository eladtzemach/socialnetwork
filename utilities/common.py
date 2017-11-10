import time
import boto3
import datetime
import arrow
import bleach

def utc_now_ts():
    return int(time.time())
    
def utc_now_ts_ms():
    return lambda: int(round(time.time() * 1000))
    
def ms_stamp_humanize(ts):
    ts = datetime.datetime.fromtimestamp(ts)
    return arrow.get(ts).humanize()
    
def linkify(text):
    text = bleach.clean(text, tags=[], attributes={},styles=[], strip=True)
    return bleach.linkify(text)
    
def email(to_email, subject, body_html, body_text):
    client = boto3.client('ses', region_name='us-east-1', aws_access_key_id='', aws_secret_access_key='')
    return client.send_email(
        Source='elad2007@gmail.com',
        Destination={
            'ToAddresses':[
                to_email,]
        },
        
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': body_text,
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': body_html,
                    'Charset': 'UTF-8'
                },
            }
        }
    )