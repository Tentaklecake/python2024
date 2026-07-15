"""
##Task1: Нотация МАС адреса
mac_list = [
    "50-46-5D-6E-8C-20",
    "50-46-5d-6e-8c-20",
    "50:46:5d:6e:8c:20",
    "5046:5d6e:8c20",
    "50465d6e8c20",
    "50465d:6e8c20",
]

def get_mac_notation(mac):
    if mac[2] == '-':
        if mac == mac.upper():
            mac_notation = (f'Mac {mac} notation is type1')
        else:
            mac_notation = (f'Mac {mac} notation is type2')
    elif mac[2] == ":":
       mac_notation = (f"нотация {mac}: UNIX")
    elif mac[4] == ":":
        mac_notation = (f"нотация {mac}: cisco")
    elif (":" in mac) == False:
        mac_notation = (f"нотация {mac}: bare")
    else:
        mac_notation = (f"нотация для {mac}: неизвестна")
    return mac_notation

for mac in mac_list:
    answer = get_mac_notation(mac)
    print(answer)

#Task2: Нормализация имени интерфейса

interfaces = [
    "Eth0/0",
    "Gig0/4/3",
    "GE4/4",
    "Po3",
    "Ten5/4",
    "XGE4/1",
    "Eth-Trunk4",
]

def interface_changer(interface):
    if interface.startswith('Eth') and '/' in interface:
        new_interface = interface.replace('Eth','Ethernet')
        return new_interface
    elif interface.startswith('Fa') and '/' in interface:
        new_interface = interface.replace('Fa','FastEthernet')
        return new_interface
    elif (interface.startswith('Gig') and '/' in interface) or (interface.startswith('GE') and '/' in interface):
        new_interface = interface.replace('Gig','GigabitEtherne')
        new_interface = interface.replace('GE','GigabitEtherne')
        return new_interface
    elif interface.startswith('Ten') and '/' in interface or interface.startswith('TE') and '/' in interface or interface.startswith('XGE') and '/' in interface:
        new_interface = interface.replace('Ten','TenGigabitEthernet')
        new_interface = interface.replace('TE','TenGigabitEthernet')
        new_interface = interface.replace('XGE','TenGigabitEthernet')
        return new_interface
    else:
        return interface

list_new_int = []
for interface in interfaces:
    new_interface = interface_changer(interface)
    list_new_int.append(new_interface)
print(list_new_int)

"""
#Task4: Парсинг конфигурации в словарь

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


def parse_config(config):
    result = {}
    config = config.split('\n')
    for config_strings in config:
        if (config_strings == '!') or (config_strings == '') or (config_strings == 'exit'):
            config.remove(config_strings)
    del config[-1]
    for config_strings in config:
        if not config_strings.startswith(' '):
            result[config_strings] = []
            key = config_strings
        else:
            result[key].append(config_strings.strip())
    return result

result = parse_config(config)
print(result)


#task 5 Filter vs list comprehension

seq = ["rt1", "RT2", "SW1", "sw2"]

list(filter(str if 'rt' in str.lower() else None, seq)) 


#Task7 Параметры функции

def foo(var1, var2=None, var3=None):
    print(var1,var2,var3)

#foo(var1=32)
# var1 = 32

foo(var1=32, var3="test")
# var1 = 32
# var3 = test
"""