from collections import deque
from collections import namedtuple

# Task1: Удаление элементов

intf_list = ["gi0/0", "gi0/1", "gi0/22", "gi0/23", "gi0/3", "gi0/4"]
# Нужно преобразовть к вот такому виду ["gi0/0", "gi0/1", "gi0/2", "gi0/3", "gi0/4"] (gi0/22, gi0/23 лишние элементы, gi0/2 не хватает)

intf_list.remove("gi0/22")
intf_list.remove("gi0/23")
intf_list.append("gi0/2")
intf_list.sort()
# print(intf_list)

# Task2: Добавление элементов

intf_list = ["gi0/1"]
# Добавить слева к нему элемент "gi0/0", справа - "gi0/2"
queue = deque(intf_list)
queue.appendleft("gi0/0")
queue.append("gi0/2")
# print(queue)

# Task3: Список списков

mtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# Получить два листа, в которых будут элементы диагоналей матрицы:

# diag1
# >>> [1, 5, 9]

# diag2
# >>> [3, 5, 7]

diag1 = [(mtx[0])[0], (mtx[1])[1], (mtx[2])[2]]
diag2 = [(mtx[0])[2], (mtx[1])[1], (mtx[2])[0]]

# Task4: Преобразование строки

output = "switchport trunk allowed vlan 2,101,104"
# Нужно получить список vlan (типа int).
# vlans
# >>> [2, 101, 104]

vlan = output.find("vlan") + 5
vlan_output = output[vlan::]
vlans = vlan_output.split(",")
vlans = [int(vlans[0]), int(vlans[1]), int(vlans[2])]


# Task5: Namedtuple

output = """
Interface             IP-Address      OK?    Method Status      Protocol
GigabitEthernet0/2    192.168.190.235 YES    unset  up          up
GigabitEthernet0/4    192.168.191.2   YES    unset  up          down
TenGigabitEthernet2/1 unassigned      YES    unset  up          up
Te36/45               unassigned      YES    unset  down        down
"""
# Создать namedtuple InterfaceStatus и сделать список intf_brief = <...> из
# 4ех элементов типа InterfaceStatus, в каждом из котором будет разобранные из
# соответсвующей строки входных данных (заголовок пропускаем, он не нужен,
# только данные по интерфейсам).

"""isinstance(intf_brief, list)
>>> True

len(intf_brief)
>>> 4

intf_brief[0].name
>>> 'GigabitEthernet0/2'

intf_brief[0].ip
>>> '192.168.190.235'

intf_brief[0].status
>>> 'up'"""


interface_tuple = namedtuple("intf_brief", ["name", "ip", "status"])
output = output[74:]
# fist_name = output[:20]
# first_line = output[74:140]
# second_line = output[141:209]
# third_line = output[141:209]
# print(second_line)
out_list = output.split(" ")
#interface
