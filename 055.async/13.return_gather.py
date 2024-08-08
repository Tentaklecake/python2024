import asyncio

from scrapli import AsyncScrapli
from scrapli.response import Response

device_scrapli = {
    "transport": "asynctelnet",
    "platform": "cisco_iosxe",
    "auth_username": "admin",
    "auth_password": "P@ssw0rd",
    "auth_strict_key": False,
    "transport_options": {
        "open_cmd": [
            "-o",
            "KexAlgorithms=+diffie-hellman-group-exchange-sha1",
            "-o",
            "HostKeyAlgorithms=+ssh-rsa",
        ]
    },
}


async def get_output_scrapli(ip: str, cmd: str) -> Response:
    print(f"{ip:>15}: connecting ...")
    device = device_scrapli | {"host": ip}
    async with AsyncScrapli(**device) as ssh:
        output = await ssh.send_command(cmd)
    print(f"{ip:>15}: done")
    return output


async def get_output(ip_addresses: list[str], cmd: str) -> dict[str, str]:
    result = {}
    coros = await asyncio.gather(
        *[asyncio.create_task(get_output_scrapli(ip, cmd)) for ip in ip_addresses],
        return_exceptions=True,
    )
    for ip, output in zip(ip_addresses, coros):
        if isinstance(output, Exception):
            print(f"{ip:>15}: (False) {output.__class__.__name__}, {str(output)}")
            result[ip] = ""
        elif isinstance(output, Response):
            print(f"{ip:>15}: ({not output.failed}) {output.channel_input} -> {output.result[:50]}")
            result[ip] = output.result
        else:
            print(f"{ip:>15}: (False) неизвестный формат ответа {type(output)}")
            result[ip] = ""

    return result


async def main(cmd: str) -> dict[str, str]:
    r = await get_output(ip_addresses, cmd)
    return r


ip_addresses = [
    "192.168.122.109",
    "192.168.122.110",
    "192.168.122.111",
    "192.168.122.112",
    "192.168.122.113",
    "192.168.122.114",
    "192.168.122.115",
    "192.168.122.116",
    "192.168.122.117",
    "192.168.122.101",
    "192.168.122.118",
]


if __name__ == "__main__":
    r = asyncio.run(main("sh clock"))
    print(r)
    # parsing
    # save
    # r = asyncio.run(main("show ip arp vrf mgmt"))
    # print(r)
