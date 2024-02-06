import boto3

from config import aws_access_key_id,aws_secret_access_key,create_bucket_name

def create_bucket(bucket_prefix):
    # s3_client = boto3.client('s3'
    #                         )
    #or
    s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key,
                         
                         config=boto3.session.Config(signature_version='s3v4'))


    
    bucket_name = create_bucket_name(bucket_prefix)
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print({"message":f"bucket {bucket_name}  created successfully! "})
    except Exception as e:
        print({"message": f"Failed to create bucket. Error: {str(e)}"})

create_bucket("mouri")

