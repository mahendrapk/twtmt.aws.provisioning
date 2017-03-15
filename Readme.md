Ansible project to provision aws enviornment for TWTMT.

1. Setup Ansible controller machine, from where the ansible playbooks are run
	1.1 packages and frameworks
		- xcode-select --install
		- sudo easy_install pip
		- sudo pip install ansible
		- sudo pip install boto
	1.2 Enviornment variable
		- AWS_DEFAULT_REGION must be specified(e.g. "ap-south-1")
	1.3 AWS credentials location for boto are store at ~/.aws/credentials in following format
		- 	[default]
			aws_access_key_id = "abcd"
			aws_secret_access_key = "1234"
	1.4 EC2 settings for boto(location: ~/.boto):
			[Boto]
			ec2_version = 2012-12-01
			ec2_region_name = ap-south-1
			ec2_region_endpoint = ec2.ap-south-1.amazonaws.com

2. Dependencies for Anible playbooks:
	2.1 aws_credentials.yml requirements:
        - Create "aws_credentials.yml" file at \group_vars\{{companyName}}\aws_credentials.yml
        - edit this file and store the aws credentials in following format
          ---
          aws_access_key: abcd
          aws_secret_key: 1234
        - Should you ever need to commit this file, first encrypt using ansible-vault and a very very strong password.
        - If encrypted file is supplied, then vault password file has to be mentioned in ansible.cfg so that at run time it is decrypted automatically.

4. Allocate required elastic IP addresses from AWS and set them in configs/{{companyName}}/{{slice}}/{{instance_name}} 

5. Ansible playbook commands:
ansible-playbook launch_vpc.yml --extra-vars "env={{companyName}}" -vvv
ansible-playbook launch_instance.yml --extra-vars "env={{companyName}} slice=build instance_name=JenkinsServer"
ansible-playbook launch_instance.yml --extra-vars "env={{companyName}} slice=build instance_name=TestMachine1"