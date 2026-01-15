# Task1: Цикл for

mac_list = [
    "50-46-5D-6E-8C-20",
    "50-46-5d-6e-8c-20",
    "50:46:5d:6e:8c:20",
    "5046:5d6e:8c20",
    "50465d6e8c20",
    "50465d:6e8c20",
]

# for mac in mac_list:
#    if mac[2] == "-":
#        if mac == mac.upper():
#            print(f"нотация {mac}: IEEE EUI-48")
#        else:
#            print(f"нотация {mac}: IEEE EUI-48 lowercase")
#    elif mac[2] == ":":
#        print(f"нотация {mac}: UNIX")
#    elif mac[4] == ":":
#        print(f"нотация {mac}: cisco")
#    elif (":" in mac) == False:
#        print(f"нотация {mac}: bare")
#    else:
#        print(f"нотация для {mac}: неизвестна")
#

# Task2: Составление списков

# devices = [
#    "rt1.lan.hq.net",
#    "p1.mpls.hq.net",
#    "p2.mpls.hq.net",
#    "sw1.lan.hq.net",
#    "dsw1.lan.hq.net",
# ]

# list_devices = [device for device in devices if device.endswith('lan.hq.net')]

# Task3.1: Составление словарей
# Цикл for

from copy import deepcopy

SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}

hostnames = ["rt1", "rt2", "sw1", "sw2"]

devices = {}

# for hostname in hostnames:
#    devices[hostname] = SCRAPLI_TEMPLATE

# print(devices)

# Task3.2: Генератор словарей
# devices = {hostname : SCRAPLI_TEMPLATE for hostname in hostnames}
# print(devices)

# Task4: Комбинация условий и циклов
"""
Проверить, входит ли:

vlan 400
vlan 800
в список разрешенных на trunk'е vlan.
"""
line = "switchport trunk allowed vlan 100,200,300-500,600"


line_start_vlan = line.find("vlan") + 5
line_vlan = line[line_start_vlan:]
list_vlan = line_vlan.split(",")
for vlan in list_vlan:
    if "-" in vlan:
        list_range = vlan.split("-")
        min_list_range = int(list_range[0])
        max_list_range = int(list_range[1])
        if min_list_range <= 400 and 400 <= max_list_range:
            print("Vlan 400 входит")
        if min_list_range <= 800 and 800 <= max_list_range:
            print("Vlan 800 входит")
    else:
        if int(vlan) == 400:
            print("Vlan 400 входит")
        if int(vlan) == 800:
            print("Vlan 800 входит")
