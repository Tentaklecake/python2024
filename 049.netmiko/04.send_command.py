import netmiko

params = {
    "device_type": "cisco_xe",
    "host": "192.168.122.101",
    "username": "admin",
    "password": "P@ssw0rd",
    "secret": "P@ssw0rd",
}

with netmiko.ConnectHandler(**params) as ssh:
    output = ssh.send_command("show ip int br")

print(output)
