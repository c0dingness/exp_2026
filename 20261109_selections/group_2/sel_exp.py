class Server:
    def __init__(self, role: str, cpu, ram, disk):
        self.role = role
        self.cpu = cpu
        self.ram = ram
        self.disk = disk


servers_list = [
    Server(role='mail', cpu=2, ram=8, disk=1000),
    Server(role='wiki', cpu=4, ram=16, disk=2000),
    Server(role='ad_controller', cpu=2, ram=4, disk=50),
    Server(role='gateway', cpu=1, ram=2, disk=20),
    Server(role='vpn', cpu=4, ram=8, disk=30),
]


# 1 Выборка как функция
def select_low_ram_servers(
        servers: list[Server]) -> list[Server]:
    new_lits = list()

    for s in servers:
        if s.ram <= 8:
            new_lits.append(s)

    return new_lits


selected = select_low_ram_servers(servers=servers_list)

# 2 Однострочники
selected = [s for s in servers_list if s.ram <= 8]


# 3 Фильтр

def choice_func(x: Server) -> bool:
    return x.ram <= 8


my_filter = filter(choice_func, servers_list)
selected = list(my_filter)
print(selected)

# 4 Фильтр с лямбдой

my_filter_2 = filter(lambda x: x.ram <= 8, servers_list)
selected = list(my_filter_2)
print(selected)
