'''
## Task1: Определение нотации MAC

"""Существуют несколько нотаций предствления MAC адреса, например:

- IEEE EUI-48: `50-46-5D-6E-8C-20`
- IEEE EUI-48 lowercase: `50-46-5d-6e-8c-20`
- UNIX: `50:46:5d:6e:8c:20`
- cisco: `5046:5d6e:8c20`
- bare: `50465d6e8c20`

Нужно написать код, который определяет тип нотации адреса из перечисленных выше.

Входные данные: строка, содержащая MAC адрес.

- 50-46-5D-6E-8C-20
- 50-46-5d-6e-8c-20
- 50:46:5d:6e:8c:20
- 5046:5d6e:8c20
- 50465d6e8c20
- 50465d:6e8c20

Результат: напечатанный тип нотации. Если определить не удалось - напечать `нотация для 50465d:6e8c20: неизвестна` (это для последнего примера)

```python
mac = "50-46-5D-6E-8C-20"

<...код...>
    mac_notation = <...>

print(f"нотация {mac}: {mac_notation}")
>>> 'нотация 50-46-5D-6E-8C-20: IEEE EUI-48'
"""

IEEE_EUI = "IEEE EUI-48"
IEEE_EUI_lowercase = "IEEE EUI-48 lowercase"
UNIX = "UNIX"
cisco = "cisco"
bare = "bare"

mac1 = "50-46-5D-6E-8C-20"
#mac1 = "50-46-5d-6e-8c-20"
#mac1 = "50:46:5d:6e:8c:20"
#mac1 = "5046:5d6e:8c20"
#mac1 = "50465d6e8c20"
#mac1 = "50465d:6e8c20"
a = ":" in mac1


if mac1[2] == "-":
    if mac1 == mac1.upper():
        print(f"нотация {mac1}: {IEEE_EUI}")
    else:
        print(f"нотация {mac1}: {IEEE_EUI_lowercase}")
elif mac1[2] == ":":
    print(f"нотация {mac1}: {UNIX}")
elif mac1[4] == ":":
    print(f"нотация {mac1}: {cisco}")
elif (':' in mac1) == False:
    print(f"нотация {mac1}: {bare}")
else:
    print(f"нотация для {mac1}: неизвестна")
'''

## Task2: Определение класса ip адреса

# Есть переменная с ip адресом (строка), нужно опрделить класс (A/B/C/D/E) ip адреса.

# ip1 = "10.3.2.1"
# A_ip_class = "A"
# B_ip_class = "B"
# C_ip_class = "C"
# D_ip_class = "D"
# E_ip_class = "E"
#
# ip = ip1.split(".")
#
# if 0 < int(ip[0]) <= 127:
#    print(f"класс ip {ip1}: {A_ip_class}")
# elif 128 <= int(ip[0]) <= 191:
#    print(f"класс ip {ip1}: {B_ip_class}")
# elif 192 <= int(ip[0]) <= 223:
#    print(f"класс ip {ip1}: {C_ip_class}")
# elif 224 <= int(ip[0]) <= 239:
#    print(f"класс ip {ip1}: {D_ip_class}")
# elif 240 <= int(ip[0]) <= 255:
#    print(f"класс ip {ip1}: {E_ip_class}")


## Task3: Использование dict вместо if

access = """
interface {if_name}
   switchport mode access
   switchport access vlan {vlan}
!
""".strip()

trunk = """
interface {if_name}
   switchport mode trunk
   switchport trunk allowed vlan {vlan}
!
""".strip()


intf1 = {
    "if_name": "gi0/1",
    "vlan": 102,
    "mode": "access",
}

intf2 = {
    "if_name": "gi0/2",
    "vlan": 103,
    "mode": "trunk",
}

if "access" in intf1["mode"]:
    intf1_config = access.format(**intf1)
