import boto3 
s3 = boto3.client('s3')

def test_conn():
    try:
        s3.list_buckets()
        print("Connection successful")
    except Exception as e:
        print(f"Connection failed: {e}")    


test_conn()