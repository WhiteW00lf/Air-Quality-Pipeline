import boto3
import os
from botocore.exceptions import ClientError

s3 = boto3.client("s3")


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

    bucket_name = "aqmumbaipipeline"  # Replace with your S3 bucket name
    file_name = "/home/ubuntu/DE_projects/Air-Quality-Pipeline/data/airquality.csv"
    s3_key = "airquality.csv"
    try:
        s3.head_object(Bucket=bucket_name, Key=s3_key)
        print(f"File {s3_key} already exists in bucket {bucket_name}.")
        s3.delete_object(Bucket=bucket_name, Key=s3_key)
    except s3.exceptions.ClientError:
        print(
            f"File {s3_key} does not exist in bucket {bucket_name}. Proceeding to upload."
        )
        print(f"Deleted old file - {s3_key} from bucket {bucket_name}.")
        print(f"Uploading new file - {s3_key} to bucket {bucket_name}.")
        s3.upload_file(file_name, bucket_name, s3_key)
        print(f"File {s3_key} uploaded to S3 bucket {bucket_name} successfully.")
    except Exception as e:
        print(f"Failed to upload file to S3: {e}")
