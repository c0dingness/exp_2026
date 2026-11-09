class Server:
    def __init__(self, name, cpu: int, ram: int, disk: int):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.disk = disk


def tests():
    my_servers = [
        Server('mail-p', 2, 16, disk=2000),
        Server('wiki-p', 4, 32, disk=1000),
        Server('dns-p', 2, 8, disk=100),
        Server('dhcp', 1, 2, disk=20),
    ]

    def select_all_low_ram(servers: list[Server]) -> list[Server]:
        new_list = []

        for s in servers:
            if s.ram <= 8:
                new_list.append(s)

        return new_list

    print(select_all_low_ram(servers=my_servers))

    selection = [s for s in my_servers if s.ram <= 8]
    print(selection)

    def magic_func(x: Server) -> bool:
        # фильтрующая функция
        return x.ram <= 8

    my_lovely_filter = filter(magic_func, my_servers)

    print(list(my_lovely_filter))

    my_lovely_filter_w_lambda = filter(lambda x: x.ram <= 8, my_servers)

    print(list(my_lovely_filter_w_lambda))



if __name__ == '__main__':
    tests()
