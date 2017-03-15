import sys
from boto.vpc import VPCConnection

vpc_connection = VPCConnection()

route_table_id = sys.argv[1]
subnet_id = sys.argv[2]

vpc_connection.associate_route_table(route_table_id,subnet_id)
