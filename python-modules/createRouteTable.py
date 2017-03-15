import sys
from boto.vpc import VPCConnection
from boto.ec2 import EC2Connection

vpc_connection = VPCConnection()
ec2_connection = EC2Connection()

vpc_id = sys.argv[1]
route_table_type = sys.argv[2]
route_table_name = sys.argv[3]

tags = { 'Name' : route_table_name, 'Type': route_table_type }

route_table = vpc_connection.create_route_table(vpc_id)

ec2_connection.create_tags([route_table.id],tags)

print route_table.id
