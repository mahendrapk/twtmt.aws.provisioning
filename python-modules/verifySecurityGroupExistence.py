import sys
import ast
from boto.ec2 import EC2Connection
from boto.ec2.securitygroup import SecurityGroup

dependencies_names = ast.literal_eval(sys.argv[1])
vpc_id = sys.argv[2]

ec2_connection = EC2Connection()

existing_security_groups = ec2_connection.get_all_security_groups(filters={'group-name': dependencies_names, 'vpc-id': vpc_id})

existing_security_group_names = map ( lambda group: group.name, existing_security_groups)

absent_security_group_names = list( set(dependencies_names) - set(existing_security_group_names))

print absent_security_group_names