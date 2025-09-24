import boto3

def upload_file():
    bucket_name = "my-example-bucket"   # change me
    file_name = "local_test.txt"
    object_name = "data/sample_data.json"
    
    # Write a simple file
    with open(file_name, "w") as f:
        f.write("Hello from test_upload.py!\n")
    
    s3 = boto3.client("s3")
    s3.upload_file(file_name, bucket_name, object_name)
    
    print(f"✅ Uploaded {file_name} to s3://{bucket_name}/{object_name}")

if __name__ == "__main__":
    upload_file()
