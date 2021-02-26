import boto3

client = boto3.client('ec2', region_name="ap-south-1", aws_access_key_id="AKIAQZWM3ITJU2LFIUGF",aws_secret_access_key="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")

print ("Enter the CIDR For VPC:")
vpc_cidr = input()
create_vpc = client.create_vpc(CidrBlock=vpc_cidr)
print (create_vpc['Vpc']['VpcId'])
vpcid = create_vpc['Vpc']['VpcId']

print ("Enter the CIDR For Subnet:")
subnet_cidr = input()
create_subnet = client.create_subnet(CidrBlock=subnet_cidr,VpcId=vpcid)
subnetid = create_subnet['Subnet']['SubnetId']
print(subnetid)



Internet gateway

Route table