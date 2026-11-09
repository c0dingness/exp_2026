class Server:
    def __init__(self,
                 hostname: str,
                 cpu: int,
                 ram: int,
                 disk: int):
        self.hostname = hostname
        self.cpu = cpu
        self.ram = ram
        self.disk = disk


def tests():
    test_servers = [
        Server("srv-mail-p", 2, 16, 20),
        Server("srv-db-p", 4, 64, 200),
        Server("srv-vpn-p", 6, 16, 20),
        Server("srv-portal-p", 2, 32, 20),
        Server("srv-wiki-p", 2, 8, 1000),
    ]

    def selection(servers: list[Server]) -> list[Server]:
        new_list = []

        for s in servers:
            if s.ram <= 16:
                new_list.append(s)
                print(f'Selected: {s.hostname}')

        return new_list

    s1 = selection(servers=test_servers)
    print(s1)

    s2 = [x for x in test_servers if x.ram <= 16]
    print(s2)

    def my_selection_func(x: Server) -> bool:
        return x.ram <= 16

    s3 = filter(my_selection_func, test_servers)

    list_s3 = list(s3)

    for s in list_s3:
        print(s.hostname)

    print(list_s3)

    s4 = filter(lambda x: x.ram <= 16, test_servers)
    print(list(s4))


if __name__ == '__main__':
    tests()
