# Ansible provisioning in aws enviornment for TWTMT.CSW project.

### Setup Ansible controller machine, from where the ansible playbooks are run

 #### packages and frameworks
 * xcode-select --install
 * sudo easy_install pip
 * sudo pip install ansible
 * sudo pip install boto
 #### Enviornment variable
 * AWS_DEFAULT_REGION must be specified(e.g. "ap-south-1")
 #### AWS credentials location for boto are store at ~/.aws/credentials in following format
```
[default]
aws_access_key_id = "abcd"
aws_secret_access_key = "1234"
```
#### EC2 settings for boto(location: ~/.boto)
```
[Boto]
ec2_version = 2012-12-01
ec2_region_name = ap-south-1
ec2_region_endpoint = ec2.ap-south-1.amazonaws.com
```
### Dependencies for Anible playbooks

#### aws_credentials.yml file requirements:
* Create "aws_credentials.yml" file at \group_vars\{{companyName}}\aws_credentials.yml
* Edit this file and store the aws credentials in following format
  ``` 
  # below 3 dashes are important!
  ---
  aws_access_key: abcd
  aws_secret_key: 1234
  ```
* Should you ever need to commit this file, first encrypt using ansible-vault and a very very strong password.
* If encrypted file is supplied, then vault password file has to be mentioned in ansible.cfg so that at run time it is decrypted automatically.
#### IP address management
* Allocate required elastic IP addresses from AWS and set them in configs/{{companyName}}/{{slice}}/{{instance_name}}
#### Ansible playbook commands:
* ansible-playbook launch_vpc.yml --extra-vars "env={{companyName}}"
* ansible-playbook launch_instance.yml --extra-vars "env={{companyName}} slice=build instance_name=JenkinsServer"
* ansible-playbook launch_instance.yml --extra-vars "env=thoughtworks slice=build instance_name=JenkinsNode1"
* ...



