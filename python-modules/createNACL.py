import sys
import ast
from boto.vpc import VPCConnection

def get_subnet_by_cidr(cidr):
    return vpc_connection.get_all_subnets(filters={"cidrBlock": cidr})[0]

def create_or_replace_network_acl_for(subnet_id):
    existing_network_acls = vpc_connection.get_all_network_acls(filters=[('association.subnet-id', subnet_id), ('default', 'false')])
    if len(existing_network_acls) > 0:
        vpc_connection.disassociate_network_acl(subnet_id)
        vpc_connection.delete_network_acl(existing_network_acls[0].id)
    subnet_acl_association = vpc_connection.associate_network_acl(network_acl.id,vpc_subnet.id)
    return subnet_acl_association

def create_network_acl_with_entries(network_acl_rules):
    nacl = vpc_connection.create_network_acl(vpc_id)
    for rule in network_acl_rules:
        vpc_connection.create_network_acl_entry(nacl.id, rule['rule_number'], rule['protocol'], rule['rule_action'], rule['cidr_block'], rule['egress'], rule.get('icmp_code',None), rule.get('icmp_type',None),rule['port_range_from'], rule['port_range_to'])
    return nacl

default_network_acl_rules = [{'rule_number' : 100, 'protocol' : -1, 'rule_action': 'allow', 'cidr_block': '0.0.0.0/0', 'egress': False,'icmp_type': -1,'icmp_code': -1, 'port_range_from': 0, 'port_range_to':65535}, {'rule_number' : 100, 'protocol' : -1, 'rule_action': 'allow', 'cidr_block': '0.0.0.0/0', 'egress': True,'icmp_type': -1,'icmp_code': -1, 'port_range_from': 0, 'port_range_to':65535}]
vpc_id = sys.argv[1]
subnet_configs = ast.literal_eval(sys.argv[2])

vpc_connection = VPCConnection()
vpc_subnet = get_subnet_by_cidr(subnet_configs['cidr'])
network_acl = create_network_acl_with_entries(subnet_configs.get("network_acl_rules", default_network_acl_rules))

print create_or_replace_network_acl_for(vpc_subnet.id)
