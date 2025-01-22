import boto3

client=boto3.client("s3")
   

s3=boto3.resource("s3")

bucket_name=input ("enter bucket name to delete ")
def delete_s3_bucket(bucket_name):
    
    response = client.delete_bucket(
    Bucket=bucket_name,
   
    
    )

    
    try:
         print(f"S3 bucket with name  '{bucket_name}' deleted successfully")
         return True
    except Exception as e:
        
        print(f"An error occurred while deleting the bucket")
        return None
    

delete_s3_bucket(bucket_name)  
