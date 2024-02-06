import uuid
import datetime
aws_access_key_id = "AKIARY57NE7BFASDDVEF"
aws_secret_access_key = "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"
region = "us-east-1"

def create_bucket_name(bucket_prefix):
    current_datetime = datetime.datetime.now().strftime('%Y%m%d%H%S')
    order_number = current_datetime 
    return ''.join([bucket_prefix,current_datetime])