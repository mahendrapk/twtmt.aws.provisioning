import sys
import json
from boto.ec2 import EC2Connection
from boto.ec2.securitygroup import SecurityGroup

group_name = sys.argv[1]
vpc_id = sys.argv[2]

ec2_connection = EC2Connection()

def get_security_group_facts():
  security_group = ec2_connection.get_all_security_groups(filters={'group-name': [group_name], 'vpc_id': vpc_id})

  security_group_details = dict()
  security_group_details["id"] = security_group[0].id
  security_group_details["tag"] = security_group[0].tags
  security_group_details["name"] = security_group[0].name
  security_group_details["description"] = security_group[0].description
  security_group_details["vpc_id"] = security_group[0].vpc_id

  return json.dumps(security_group_details)

print get_security_group_facts()