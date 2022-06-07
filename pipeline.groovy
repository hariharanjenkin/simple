pipeline {
	agent {label 'master'} 
		
		stages {
			stage('Cleanws') {
				steps {
					 cleanWs()
					}
			}
			
			stage('Git Clone') {
				steps {
					
					git credentialsId: 'GitHub_Access', url: 'https://github.com/hariharanjenkin/simple.git',branch: 'master'
	  
				}
			}
			
			stage('Verify the Clone') {
				steps {
					
					sh '''
					
						pwd
						ls
						
					'''
				}
			}
			
			stage('Executing Java Script') {
				steps {
					
					sh '''
					
						javac helloworld.java

						java helloworld
						
					'''
				}
			}
			
			stage('Terraform Plan') {
				steps {
					
					sh '''
					    cd /var/lib/jenkins/workspace/AWS-Pipelie/AWS-Pipeline-26-may-2022/
                        pwd
						sudo terraform init
						sudo terraform plan
						
					'''
				}
			}
			
	}
}		
