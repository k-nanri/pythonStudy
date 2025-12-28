import ipaddress


def execute_ip() -> None:

    net = ipaddress.ip_network("192.168.10.0/28", strict=True)
    print(net)

    # ネットワークアドレス
    ip = "192.168.10.32"
    net = ipaddress.ip_address(ip)

    # IPアドレスのインクリメント
    print(f"ip address = {net + 1}")

    ip = "192.168.10.30/28"
    net = ipaddress.ip_network(ip, strict=False)
    print(net.network_address)


if __name__ == "__main__":
    execute_ip()
