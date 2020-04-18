import boto3
import sys
from datetime import date, datetime, timedelta,timezone
from datetime import date
import csv

accesskey = sys.argv[1]
secretkey = sys.argv[2]

client = boto3.client('iam', aws_access_key_id=accesskey, aws_secret_access_key=secretkey)

def accesskey_10days_data(writer):

	accessskey10days_age = {}

#get the list of users
	listing_usr = client.list_users()
	for usr_name in listing_usr['Users']:


#get the Access_key details of users
		accessky_data = client.list_access_keys(UserName=usr_name['UserName'])
		for usr_data_frm_acckey in accessky_data['AccessKeyMetadata']:

		
#getting the current date using python datetime.now defuly function
			current_date = datetime.now(timezone.utc)
			age = (current_date-usr_data_frm_acckey['CreateDate']).days
			if age >= 10:
				accessskey10days_age['USERNAME'] = usr_data_frm_acckey['UserName']
				accessskey10days_age['CURRENT_ACCESSKEY'] = usr_data_frm_acckey['AccessKeyId']
				accessskey10days_age['AGE'] = usr_data_frm_acckey['CreateDate']
				writer.writerow(accessskey10days_age)
				print (accessskey10days_age)


def main():
	fieldnames = ['USERNAME','CURRENT_ACCESSKEY','AGE']
	file_name = "accessskey10days_age.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		
		accesskey_10days_data(writer)

main()
