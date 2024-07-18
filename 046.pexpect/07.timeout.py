import re

import pexpect

username = "admin"
password = "P@ssw0rd"
ip = "192.168.122.101"


def get_show_version(username: str, password: str, ip: str) -> str:
    password_pattern: re.Pattern = re.compile("password:", flags=re.IGNORECASE)

    with pexpect.spawn(
        command=f"ssh {username}@{ip}",
        timeout=5,
        encoding="utf-8",
    ) as ssh:
        ssh.expect(password_pattern)
        ssh.sendline(password)
        ssh.expect(">")

        ssh.sendline("terminal length 0")
        ssh.expect("#")

        ssh.sendline("show version")
        ssh.expect("#")
        output = ssh.before

    return output


try:
    output = get_show_version(username, password, ip)
except pexpect.exceptions.TIMEOUT as exc:
    print("PEXPECT TIMEOUT!")
    output = ""

with open("./046.pexpect/07.timeout.log", "w") as f:
    f.write(output)
