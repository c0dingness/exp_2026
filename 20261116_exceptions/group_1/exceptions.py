import random


class Worker:
    def do_do(self):
        this_id = id(self)
        print(f'{this_id} Doing work')

        rnd_number = random.randint(1, 10)

        if rnd_number >= 5:
            raise RuntimeError(f'Worker job failed {this_id}')


class Manager:
    def __init__(self, workers: list[Worker] = None):
        if workers is None:
            self.workers = [Worker()]
        else:
            self.workers = workers

        self.failed_counters: dict[Worker, int] = {w: 0 for w in self.workers}


    def repair_some(self):
        print('rapaired!')


    def do_job(self):
        if not self.workers:
            raise RuntimeError('Not workers to do')

        try_attempts = 3

        self.failed_counters = {w: 0 for w in self.workers}
        for w in self.workers:
            for _ in range(try_attempts):
                try:
                    print(f'Try to make worker do job {_}')
                    w.do_do()
                    break
                except RuntimeError:
                    self.failed_counters[w] += 1
                    print('Manager process error from worker')
                    self.repair_some()

        print(self.failed_counters)

        for w, ta in self.failed_counters.items():
            if ta == try_attempts:
                raise RuntimeError(f'My worker failed: {id(w)}')





class GrandManager:
    def __init__(self, manager: Manager):
        self.manager = manager

    def start_work(self):
        try:
            self.manager.do_job()
        except RuntimeError as e:
            print(e)
            pass


def test():
    our_workers = [
        Worker(),
        Worker(),
        Worker(),
    ]

    manager_one = Manager(workers=our_workers)
    gm = GrandManager(manager=manager_one)

    gm.start_work()


if __name__ == '__main__':
    test()
