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

