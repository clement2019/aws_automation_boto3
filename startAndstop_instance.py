import boto3

print("please enter your region")
region=input()
print("please enter instance_ID")
instances=input()
ec2 = boto3.client('ec2', region_name=region)

def startAndstop_instance(region,instances):
    ec2.start_instances(InstanceIds=instances)
   # ec2.stop_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
    #print('stopped your instances: ' + str(instances))
    
startAndstop_instance(region,instances)    