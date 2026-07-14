## Task1: Чтение из файла
"""
В текущем каталоге размещен файл `029.config.txt`.
Нужно открыть его для чтения и читая построчно выводить
на экран содержимое файла.
Если строка равна "!",
тогда её нужно пропускать (не выводить в stdout).
"""

import pprint

with open("029.config.txt", "r") as f:
    for line in f:
        # pprint.pprint(line)
        if line == "!\n" or line == " !\n":
            continue
        else:
            print(line)
            pass

## Task2: Сохранение в файл

#Есть конфигурация двух устройств в виде словаря 
# со структурой \<hostname\>:\<config\>:

rt01_config = """
!
interface Vlan1
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
line vty 0 4
 password cisco
!
""".strip()

rt02_config = """
!
router bgp 64512
 bgp router-id 192.168.1.1
 bgp log-neighbor-changes
 !
 address-family ipv4
  redistribute connected route-map LAN
 exit-address-family
 !
 address-family vpnv4 unicast
  neighbor 1.2.3.4 activate
 exit-address-family
!
""".strip()

configs = {
    "rt01": rt01_config,
    "rt02": rt02_config,
}