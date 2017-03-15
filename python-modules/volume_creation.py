import sys
import json
import ast
from boto.ec2 import EC2Connection

instance_volumes = ast.literal_eval(sys.argv[1])

print json.dumps(instance_volumes)
