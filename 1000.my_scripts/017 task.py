# Task1: Плоский словарь
# Создать два словаря c параметрами оборудования (ниже перечисление в виде "ключ = значение")

device1 = {
    "hostname": "r1.abcd.net",
    "ip": "192.168.1.1",
    "username": "cisco",
    "password": "secret",
    "platform": "cisco_ios",
    "enable": True,
}

device2 = dict(
    hostname="sw1.abcd.net",
    ip="192.168.1.2",
    username="admin",
    password="secret",
    platform="huawei_vrp",
    enable=False,
)

# Task2: Список словарей
# Создать список devices_list, содержащий словари device1 и device2 из задания Task1

# Структура: [{}, {}]

devices_list = [
    device1,
    device2,
]
# И добавить в него третье устройство с параметрами

device3 = dict(
    hostname="wlc.abcd.net",
    ip="192.168.1.3",
    username="wlc_admin",
    password="password",
    enable=False,
)
# Структура: [{}, {}, {}]

devices_list.append(device3)

# Task3: Вложенный словарь (словарь словарей)
# На основе списка из Task2 создать словарь devices_dict
# в котором в качестве ключей будут выступать hostname устройств,
# а в качестве значений - соответсвующие элементы списка devices_list.

devices_dict = {
    (devices_list[0]).get("hostname"): devices_list[0],
    (devices_list[1]).get("hostname"): devices_list[1],
    (devices_list[2]).get("hostname"): devices_list[2],
}
# print(devices_dict)


# Task4: Обновление словаря
# Есть базовая заготовка (шаблон)

SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}
# Создать список из двух словарей на основе шаблона SCRAPLI_TEMPLATE
# дополнив/обновив его парами ключ = значение (сам шаблон при этом меняться не должен)

# для первого словаря
f_dict = {
    "hostname": "sw1.abcd.net",
}
# для второго словаря
s_dict = dict(
    hostname="sw1.abcd.net",
    transport="telnet",
    port=23,
)

device10 = SCRAPLI_TEMPLATE | f_dict
device11 = SCRAPLI_TEMPLATE | s_dict
