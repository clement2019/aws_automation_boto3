import boto3
client=boto3.client("s3")
s3=boto3.resource("s3")
#Bucket='examplebucket-2234u4433-ayenco',

bucketname=input("enter your bucket name ")
def uploadfile_s3(bucketname):
    
    fileupload=s3.Bucket(bucketname).upload_file('command.md','command.md')
    try:
         print(f"S3 bucket '{fileupload}' successfully")
         return True
    except Exception as e:
        
        print(f"An error occurred while uploading the file")
        return None
uploadfile_s3(bucketname)  

    