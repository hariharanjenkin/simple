properties([

	parameters ([
		string (defaultValue: '', description: 'Enter the AWS account ID', name: 'AWS_Account_ID', trim: false),
		string (defaultValue: '', description: 'Enter the AWS Accesskey', name: 'Accesskey', trim: false),
		string (defaultValue: '', description: 'Enter the AWS Secretkey', name: 'Secretkey', trim: false),
	])
])


pipeline {
	agent {label 'master'}
	
	stages {
		stage('CLEAN WORKSPACE IN JENKINS SERVER'){
			steps {
				cleanWs()
			} // Steps Completed	
		}  // Stage Completed
	

		stage('CLONE THE SOURCE CODE FROM GIT-HUB'){
			steps {
				echo 'In SCM Stage'
				
				git credentialsId: 'ba83a296-46b4-4e0d-af8a-fb5cd085c784', url: 'https://github.com/hariharanjenkin/simple',branch: 'master'


			} // Steps Completed
		}  // Stage Completed



		stage('Java Script Execution'){
			steps {
				
				
				
				sh '''
			
				pwd
				ls
				
                echo "Java Script Execution"
				
				javac helloworld.java
				java helloworld
				
		
				


				'''
				
				
			}  // Steps Completed
		}  // Stage Completed

		stage('Terraform Execution for Account Security'){
			steps {
				
				
				
				sh '''
			

                echo "Terraform init-1"
				
				mkdir hitech
				mkdir Hitech02
				ls
				pwd
				
				cat Jenkins_pipeline_script.py
			


				'''
				
				
			}  // Steps Completed
		}  // Stage Completed	

		stage('Executing Boto3 Script Python'){
			steps {
				
				
				
				sh '''
			

                pwd
				python3 boto3_list_vpc.py
				
			


				'''
				
				
			}  // Steps Completed
		}  // Stage Completed	
		
		
	}
}
