import boto3
client=boto3.client("s3")
s3=boto3.resource("s3")
def create_s3_bucket():
    
    response = s3.create_bucket(
    Bucket='examplebucket-2234u4433-ayenco',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-2',
    },
    )

    #print(response)
    # Specify the bucket name you wish to create
    try:
         print(f"S3 bucket '{response}' created successfully")
         return response
    except Exception as e:
        
        print(f"An error occurred while creating the S3 bucket: {e}")
        return None
    

created_bucket = create_s3_bucket()  
