##Task1: Нотация МАС адреса
# mac_list = [
#    "50-46-5D-6E-8C-20",
#    "50-46-5d-6e-8c-20",
#    "50:46:5d:6e:8c:20",
#    "5046:5d6e:8c20",
#    "50465d6e8c20",
#    "50465d:6e8c20",
# ]
#
# def get_mac_notation(mac):
#    mac_notation = ''
#    if mac[2] == "-":
#        if mac == mac.upper():
#           mac_notation = 'IEEE EUI-48'
#        else:
#           mac_notation = "IEEE EUI-48 lowercase"
#    elif mac[2] == ":":
#       mac_notation = "UNIX"
#    elif mac[4] == ":":
#       mac_notation = "cisco"
#    elif (":" in mac) == False:
#       mac_notation = "bare"
#    else:
#       mac_notation = "неизвестна"
#    return mac_notation
#
# for mac in mac_list:
#    print(get_mac_notation(mac))


# Task2: Нормализация имени интерфейса

# interfaces = [
#     "Eth0/0",
#     "Gig0/4/3",
#     "GE4/4",
#     "Po3",
#     "Ten5/4",
#     "XGE4/1",
#     "Eth-Trunk4",
# ]
#
#
# #if_name1 = if_name1.replace("Eth", "Ethernet")
# #if_name2 = if_name2.replace("GE", "GigabitEthernet")
# #if_name3 = if_name3.replace("Тen", "TenGigabitEthernet")
#
# def get_full_interface_name(short_int):
#     if short_int.startswith('Eth'):
#         short_int = short_int.replace("Eth", "Ethernet")
#     elif short_int.startswith('Fa'):
#         short_int = short_int.replace("Fa", "FastEthernet")
#     elif short_int.startswith('Gig') or short_int.startswith('GE'):
#         if short_int.startswith('Gig'):
#             short_int = short_int.replace("Gig", "GigabitEthernet")
#         else:
#             short_int = short_int.replace("GE", "GigabitEthernet")
#     elif short_int.startswith('Ten') or short_int.startswith('TE') or short_int.startswith('XGE'):
#         if short_int.startswith('Ten'):
#             short_int = short_int.replace("Ten", "TenGigabitEthernet")
#         elif short_int.startswith('TE'):
#             short_int = short_int.replace("TE", "TenGigabitEthernet")
#         else:
#             short_int = short_int.replace("XGE", "TenGigabitEthernet")
#     return short_int
#
# for interface in interfaces:
#     print(get_full_interface_name(interface))

# Task3: Замыкания

from time import perf_counter


def timer():
    start = perf_counter()

    def inner():
        print(f"{perf_counter() - start:.2f}")

    return inner


t = timer()

# Task4: Парсинг конфигурации в словарь

import pprint

config = """
spanning-tree mode rapid-pvst
spanning-tree logging
spanning-tree extend system-id
spanning-tree pathcost method long
!
lldp run
!
interface FastEthernet0/1
 switchport access vlan 10
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/2
 switchport access vlan 11
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/3
 switchport access vlan 51
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/4
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface GigabitEthernet0/1
 description mgmt1.core - FastEthernet0/32
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50-70,80,90
 mls qos trust cos
 ip dhcp snooping trust
!
interface GigabitEthernet0/2
 description mgmt2.core - FastEthernet0/32
 switchport mode trunk
 mls qos trust cos
 ip dhcp snooping trust
!
interface GigabitEthernet0/3
  description mgmt3.core - FastEthernet0/32
  switchport mode trunk
  switchport trunk allowed vlan 10,20,30,40,50-70,80,90
  switchport trunk allowed vlan add 150,151
  mls qos trust cos
  ip dhcp snooping trust
!
interface GigabitEthernet0/4
 description mgmt4.core - FastEthernet0/32
 ip address 1.2.3.4 255.255.255.0
!
line vty 0 4
 password cisco
!
"""
list_junk = ["", "!", "building", "exit"]


def parse_config(config):
    result = {}
    parent_line = []
    list_config = config.split("\n")
    # pprint.pprint(list_config)
    for line in list_config:
        for junk_line in list_junk:
            if line == junk_line:
                list_config.remove(line)
                break
    if list_config[-1] in list_junk:
        list_config.remove(list_config[-1])
    for line in list_config:
        if not line.startswith(" "):
            parent_line = line
            result[line] = []
        else:
            result[parent_line].append(line.lstrip())
    return result


print(parse_config(config))

# pprint.pprint(config)
