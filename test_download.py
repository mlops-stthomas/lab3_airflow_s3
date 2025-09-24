import boto3

def download_file():
    bucket_name = "my-example-bucket"   # change me
    object_name = "teaching_demo/hello.txt"

    s3 = boto3.client("s3")
    response = s3.get_object(Bucket=bucket_name, Key=object_name)

    # Read into memory
    content = response["Body"].read().decode("utf-8")

    print("✅ Downloaded object content:")
    print(content)

if __name__ == "__main__":
    download_file()