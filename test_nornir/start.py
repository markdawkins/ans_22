from nornir import InitNornir
from nornir.core.filter import F

nr = InitNornir("config.yml")

from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

devices = nr.filter((F(hostname__contains="172.19.")))

result = devices.run(netmiko_send_command, command_string="sh ip int brief")

print_result(result)
