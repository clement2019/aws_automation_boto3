import json
import boto3
iam=boto3.resource('iam')
def list_iam_users_group():
    
    print('connecting to Iam')
   # iam=boto3.resource('iam')
    group=iam.Group('admin-terraform').users.all()
   
    #create list of users
    print('list of users')
    names=[i.name for i in group]
   
    print(names)
    #return names

list_iam_users_group()