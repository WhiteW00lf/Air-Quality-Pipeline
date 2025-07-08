import boto3
import os

os.chdir('/home/ubuntu/DE_projects/Air-Quality-Pipeline/data')
s3 = boto3.client('s3')

def test_conn():
    try:
        s3.list_buckets()
        print("Connection successful")
    except Exception as e:
        print(f"Connection failed: {e}")    


def upload_to_s3():
    """
    Uploads the air quality data CSV file to an S3 bucket.
    """
    try:
        bucket_name = 'aqmumbaipipeline'  # Replace with your S3 bucket name
        file_name = 'airquality.csv'
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"File {file_name} uploaded to S3 bucket {bucket_name} successfully.")
    except Exception as e:
        print(f"Failed to upload file to S3: {e}")

test_conn()

upload_to_s3()