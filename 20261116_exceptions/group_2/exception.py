import random


class Worker:
    def do_do_job(self):
        print(f'Worker {id(self)}: Starting doing job!')

        fail_chance_number = random.randint(1, 10)

        if fail_chance_number >= 5:
            raise RuntimeError(f'Worker {id(self)} failed!')

        print(f'Worker {id(self)}: Job is done!')


class Manager:  # Бригадир
    def __init__(self, workers: list[Worker]):
        if len(workers) < 1:
            raise ValueError('Needs at least one worker')

        self.workers = workers

    def start_jobs(self):
        print('Manager Starting doing job!')

        for w in self.workers:
            exception = None
            for i in range(3):
                try:
                    w.do_do_job()
                    break
                except RuntimeError as e:
                    exception = e
                    self.solve_problem()

            if exception is not None:
                raise exception

    def solve_problem(self):
        print('Problem solved...')


class GrandManager:
    def __init__(self, managers: list[Manager]):
        self.managers = managers

    def start_grand_work(self):
        print('Grand Manager Starting doing job!')
        for m in self.managers:
            try:
                m.start_jobs()
            except RuntimeError as e:
                print('ok with it!')


def tests():
    _workers = [
        Worker(),
        Worker(),
        Worker(),
    ]

    _managers = [
        Manager(workers=_workers)
    ]

    gm = GrandManager(managers=_managers)

    gm.start_grand_work()


if __name__ == '__main__':
    tests()
