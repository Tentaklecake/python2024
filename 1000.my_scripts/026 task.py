#task1 создание генератора
"""
Написать генератор строчек конфигурации на основе конфигурации устройства. 
При выводе очередной строки нужно пропускать строки "!" или 
"exit-address-family":
"""
from typing import Generator

config = """
ip forward-protocol nd
no ip http server
!
interface Vlan1
 ip address 192.168.1.1 255.255.255.0
 no shutdown
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
line vty 0 4
 password cisco
!
""".strip()


def config_generator(config: str) -> Generator[str, None, None]:
    if elem in config == "!" or "exit-address-family":
        pass

for line in config_generator(config):
    print(line)