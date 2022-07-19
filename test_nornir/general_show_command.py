from nornir import InitNornir
from nornir.core.filter import F

nr = InitNornir("config.yml")

from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

group = input("Enter group name(GROUP1,GROUP2,GROUP3,GROUP4,GROUP5,GROUP6) : ") 
command = input("Enter show command here: ")


devices = nr.filter((F(groups__contains=(group))))

result = devices.run(netmiko_send_command, command_string=(command))

print_result(result)
