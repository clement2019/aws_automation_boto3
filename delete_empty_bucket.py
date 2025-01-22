import boto3

# Set up access credentials
#access_key =input("enter access key ")
#secret_key =input("enter secret key ")
region =input("enter region ")


#def empty_s3_bucket(access_key,secret_key,region_name):#
def empty_s3_bucket(region):
    
    # Create an S3 client
    #s3_client = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)
    s3_client = boto3.client("s3",region_name=region)
    # Create an S3 resource
    #s3 = boto3.resource("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)
    s3 = boto3.resource("s3", region_name=region)
    # List all of the S3 buckets in the account
    response = s3_client.list_buckets()
    buckets = response["Buckets"]

    # Filter out the empty buckets with versioning disabled
    empty_buckets = []
    for bucket in buckets:
        bucket_name = bucket["Name"]
        result = s3_client.list_objects_v2(Bucket=bucket_name)
        if "Contents" not in result:
            
            versioning = s3_client.get_bucket_versioning(Bucket=bucket_name)
            if versioning.get("Status") != "Enabled":
                
                empty_buckets.append(bucket_name)
                print(empty_buckets)

                # Delete the empty buckets
                for bucket_name in empty_buckets:
                    
                    s3.Bucket(bucket_name).delete()
                    print(f"Bucket {bucket_name} deleted.")


empty_s3_bucket(region)                    
