import boto3
import os
from dotenv import load_dotenv


# Read from .env file.
load_dotenv()
env = os.environ.get

# Create Session With Boto3.
session = boto3.Session(
    aws_access_key_id=env("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=env("AWS_SECRET_ACCESS_KEY")
)

# Create S3 Resource From the Session.
s3 = session.resource("s3")

srcbucket = s3.Bucket(env("SOURCE_BUCKET_NAME"))

destbucket = s3.Bucket(env("TARGET_BUCKET_NAME"))

# Iterate All Objects in Source Bucket Over the For Loop
for file in srcbucket.objects.all():
    
    # Create a Source Dictionary that Specifies Bucket Name and Key Name of the Object to be Copied
    copy_source = {
        "Bucket": env("SOURCE_BUCKET_NAME"),
        "Key": file.key
    }

    # Copy Source Bucket to Destination Bucket
    destbucket.copy(copy_source, file.key)
    
    print(file.key +"- File Copied")