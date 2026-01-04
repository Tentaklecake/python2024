# Task2: Преобразовании числа в строку
# Перевести число в строку минимум 3 способами

bd_id = 555

bd_id_str1 = str(bd_id)
bd_id_str2 = f"{bd_id}"
bd_id_str3 = format(bd_id)

# Task3: Работа с байтовой последовательностью
# Task3.1: Преобразование в utf-8
# С оборудования получили следующий вывод, нужно преобразовать его в unicode (utf-8) строку.

output = b"\r\nHuawei Versatile Routing Platform Software\r\nVRP (R) software, Version 8.220 (CE6857EI V200R022C00SPC500)\r\nCopyright (C) 2012-2022 Huawei Technologies Co., Ltd.\r\nHUAWEI CE6857-48S6CQ-EI uptime is 248 days, 3 hours, 14 minutes\r\n"
output = output.decode()

# Task3.2: Возврат каретки (CR)
# У полученной в Task3.1 строки избавится от символа возврата каретки.
output = output.replace("\r", "")

# Task3.3: Пробельные символы
# У полученной в Task3.2 строки удалить пробельные символы только с начала строки.
output = output.lstrip()

# Task4.1: Простейший шаблон

bd_id = 555
intf_start = "10GE1/0/1"
intf_end = "10GE1/0/48"
rid = "192.168.43.34"
bgp_as = 64512


template = f"""bridge-domain {bd_id}
 vlan {bd_id} access-port interface {intf_start} to {intf_end}
 vxlan vni 10{bd_id}
 #
 evpn
  route-distinguisher {rid}:10555
  vpn-target {bgp_as}:10555 export-extcommunity
  vpn-target {bgp_as}:10555 import-extcommunity
 arp broadcast-suppress enable"""
#

# Task4.2 and Task4.3: Преобразование в двоичную систему
a = f"{42:0^8b}"
b = f"{32:0^8b}"
c = f"{255:0^8b}"

### Task4.4: Преобразование в двоичную систему - 3

# Получить полное двоичное представление ip адреса (т.е. без разделения на октеты): 10.23.43.234 -> 00001010000101110010101111101010.

ip = "10.23.43.234"
ip_split = ip.split(".")
fi_oc = f"{int(ip_split[0]):0^8b}"
s_oc = f"{int(ip_split[1]):0^8b}"
t_oc = f"{int(ip_split[2]):0^8b}"
fo_oc = f"{int(ip_split[3]):0^8b}"

result = fi_oc + s_oc + t_oc + fo_oc

##print(result)

### Task4.5: RTP запись

# Сформировать RTP запись для адресов:

ip = "77.88.55.242"
ip_split = ip.split(".")
fi_oc = ip_split[3]
s_oc = ip_split[2]
t_oc = ip_split[1]
fo_oc = ip_split[0]
result = ".".join([fi_oc, s_oc, t_oc, fo_oc]) + ".in-addr.arpa"

# print(result)

### Task4.7: Удаление символов в строке

# Полностью (вместе с переводом строки) удалить из вывода строку со знаками `-`. При этом фиксировать число/границы удаляемой строки не нужно, вычислем необходимые параметры на основе исходных данных.

output = """
Local Interface         Exptime(s) Neighbor Interface            Neighbor Device
-------------------------------------------------------------------------------------
100GE1/0/1                    107  100GE1/0/1                    spine1.pod1.stg
10GE1/0/1                     105  10GE1/0/1                     test-server.stg
"""
hyphen = output.find("-")
result = output.replace("-", "")
result = result[0:81] + result[82:]
print(result)

### Task4.8: Нормализация имен интерфейсов

# Даны имена интерфейсов в коротком виде (Eth0/1, GE1/0/2, Тen4/3). Произвести преобразование коротких имен в полные

# - Eth0/1 -> Ethernet0/1
# - GE1/0/2 -> GigabitEthernet1/0/2
# - Тen4/3 -> TenGigabitEthernet4/3

if_name1 = "Eth0/1"
if_name2 = "GE1/0/2"
if_name3 = "Ten4/3"

if_name1 = if_name1.replace("Eth", "Ethernet")
if_name2 = if_name2.replace("GE", "GigabitEthernet")
if_name3 = if_name3.replace("Тen", "TenGigabitEthernet")

print(if_name1)
print(if_name2)
print(if_name3)
