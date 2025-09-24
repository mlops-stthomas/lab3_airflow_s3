import boto3

def upload_file():
    bucket_name = "my-example-bucket"   # change me
    file_name = "./data/sample_data.json"
    object_name = "upload/sample_data.json"
    
    s3 = boto3.client("s3")
    s3.upload_file(file_name, bucket_name, object_name)
    
    print(f"✅ Uploaded {file_name} to s3://{bucket_name}/{object_name}")

if __name__ == "__main__":
    upload_file()
