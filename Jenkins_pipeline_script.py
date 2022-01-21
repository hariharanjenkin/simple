import boto3
import sys
from datetime import date
from datetime import date, datetime, timedelta, timezone
import csv

accesskey = sys.argv[1]
secretkey = sys.argv[2]
client = boto3.client('iam', aws_access_key_id=accesskey, aws_secret_access_key=secretkey)

def accesskey_fun(writer):
	access_key_dict = {}
	list_usr = client.list_users()
	for usrname in list_usr['Users']:
		list_acckey = client.list_access_keys(UserName=usrname['UserName'])
		for accessky_details in list_acckey['AccessKeyMetadata']:
			current_date = datetime.now(timezone.utc)
			age = (current_date-accessky_details['CreateDate']).days
			if age >= 10:
				access_key_dict["USERNAME"] = accessky_details['UserName']
				access_key_dict["CURRENT_ACCESSKEY"] = accessky_details['AccessKeyId']
				access_key_dict["CREATED_DATE"] = accessky_details['CreateDate']
				writer.writerow(access_key_dict)
				print (access_key_dict)

def main():
	fieldnames = ["USERNAME","CURRENT_ACCESSKEY","CREATED_DATE"]
	file_name = "access_key_dict.csv"
	with open (file_name,"w") as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		accesskey_fun(writer)

main()
