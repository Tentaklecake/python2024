
##Task1: Нотация МАС адреса
#mac_list = [
#    "50-46-5D-6E-8C-20",
#    "50-46-5d-6e-8c-20",
#    "50:46:5d:6e:8c:20",
#    "5046:5d6e:8c20",
#    "50465d6e8c20",
#    "50465d:6e8c20",
#]
#
#def get_mac_notation(mac):
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
#for mac in mac_list:
#    print(get_mac_notation(mac)) 


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


#if_name1 = if_name1.replace("Eth", "Ethernet")
#if_name2 = if_name2.replace("GE", "GigabitEthernet")
#if_name3 = if_name3.replace("Тen", "TenGigabitEthernet")

def get_full_interface_name(short_int):
    if short_int.startswith('Eth'):
        short_int = short_int.replace("Eth", "Ethernet")
    elif short_int.startswith('Fa'):
        short_int = short_int.replace("Fa", "FastEthernet")
    elif short_int.startswith('Gig') or short_int.startswith('GE'):
        if short_int.startswith('Gig'):
            short_int = short_int.replace("Gig", "GigabitEthernet")
        else: 
            short_int = short_int.replace("GE", "GigabitEthernet")
    elif short_int.startswith('Ten') or short_int.startswith('TE') or short_int.startswith('XGE'):
        if short_int.startswith('Ten'):
            short_int = short_int.replace("Ten", "TenGigabitEthernet")
        elif short_int.startswith('TE'):
            short_int = short_int.replace("TE", "TenGigabitEthernet")
        else:
            short_int = short_int.replace("XGE", "TenGigabitEthernet")
    return short_int

for interface in interfaces:
    print(get_full_interface_name(interface))