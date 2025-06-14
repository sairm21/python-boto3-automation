import boto3

#use the nameed profile
session = boto3.Session(profile_name='boto3-practice')

# Create an EC2 client
ec2 = session.client('ec2')

# Create a new EC2 instance
response = ec2.run_instances(
    ImageId='ami-02521d90e7410d9f0',  # Example AMI ID, replace with a valid one
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='Python_for_automation',  # Replace with your key pair name
    SecurityGroupIds=['sg-07c91e3b6c617e1ec'],  # <-- Add this line
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 20,  # Size in GB
                'DeleteOnTermination': False,
                'VolumeType': 'gp3'  # General Purpose SSD
            }
        }
    ],  
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'MyEC2Instance'
                }
            ]
        }
    ],
UserData='''#!/bin/bash
    #update the system
    sudo apt update -y
    #install apache2
    sudo apt install apache2 -y 
    #start apache2 service
    sudo systemctl start apache2
    #enable apache2 service
    sudo systemctl enable apache2
    #create a simple index.html file
    echo "<h1>Welcome to my EC2 instance!</h1><h2>This instance is created and configured using Python boto3 module</h2>" | sudo tee /var/www/html/index.html
    #restart apache2 service
    sudo systemctl restart apache2
    '''
)
# Print the response
print("EC2 Instance created successfully:")
