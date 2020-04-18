import boto3
import sys

region = sys.argv[1]
accesskey = sys.argv[2]
secretkey = sys.argv[3]

client = boto3.client('ec2', region_name=region, aws_access_key_id=accesskey, aws_secret_access_key=secretkey)

#Demo to edit to trgger webhook
test1 = {}
des_ins = client.describe_instances()

for step1 in des_ins['Reservations']:
	for step2 in step1['Instances']:
		test1['InstancID'] = step2['InstanceId']
		test1['Lanunch time'] = step2['LaunchTime']
		print (test1)




