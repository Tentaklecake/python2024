## Task1: Чтение данных из NetBox
"""
Создать аккаунт и токен на [demo netbox](https://demo.netbox.dev/).
Используя созданный токен запросить устройства с ролью "router" и 
распечатать список имен и моделей полученных устройств (список 
устройств может отличаться, так как это публичный ресурс с RW 
правами для подьзователей):

import pynetbox
nb = pynetbox.api(
    url="https://demo.netbox.dev",
    token="nbt_BWmZWoY3fbUO.liXTSFPXvGAMTY6DGtVRaWyD4cv3Al44ayaJlVr8",
    threading=True,
)
devices = nb.dcim.devices.filter(role='switch')
for device in devices:
    manufacturer = device.device_type.manufacturer.name
    model = device.device_type.model
    print(f"Device: {device.name} | Hardware: {manufacturer} {model}")
"""

#Task2: Создание объекта в NetBox
import pynetbox
nb = pynetbox.api(
    url="https://demo.netbox.dev",
    token="nbt_BWmZWoY3fbUO.liXTSFPXvGAMTY6DGtVRaWyD4cv3Al44ayaJlVr8",
    threading=True,
)

def create_device(name: str, site: str, role: str, model: str) -> int:
    <ваш код>


print(create_device("dmi01-buffalo-rtr01", "DM-Camden", "Router", "ISR 1111-8P"))
# >>> устройство с именем name='dmi01-buffalo-rtr01' уже существует
# >>> 0

print(create_device("dmi01-buffalo-rtr99", "DM-", "Router", "ISR 1111-8P"))
# >>> сайт не существует
# >>> 0

print(create_device("dmi01-buffalo-rtr99", "DM-Camden", "Roiter", "ISR 1111-8P"))
# >>> роль не существует
# >>> 0

print(create_device("dmi01-buffalo-rtr99", "DM-Camden", "Router", "ISR 1111-8Pdd"))
# >>> модель не существует
# >>> 0

print(create_device("dmi01-buffalo-rtr99", "DM-Camden", "Router", "ISR 1111-8P"))
# >>> устройство создано
# >>> 111

"""
Написать функцию, которая создает устройство в NetBox:

принимаемые параметры:
имя устройства
название роли устройства
название сайта
название модели устройства
если устройство, с переданны в качестве аргумента именем, 
уже есть в NetBox, тогда создание информация об этом пишется в stdout и 
создание пропускается, возвращается 0
если указанного а аргументах сайта/модели/роли нет в NetBox, 
информация об этом пишется в stdout и создание пропускается, возвращается 0
если устройство создано, информация об этом пишется в stdout и 
возвращается id созданного устройства
"""