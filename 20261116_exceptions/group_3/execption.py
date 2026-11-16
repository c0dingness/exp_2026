import random


class Worker:
    def do_do(self):
        print(f'{id(self)} Doing job')

        chance_number = random.randint(1,10)
        if chance_number >= 5:
            raise RuntimeError(f'{id(self)} Cannot do work')

        print(f'{id(self)} Job is done!')

class Manager:
    def __init__(self, group_workers: list[Worker]):
        if len(group_workers) < 1:
            raise ValueError('Must be at least one worker')


        self.group_workers = group_workers

    def force_to_work(self):
        for w in self.group_workers:
            ex = None
            for _ in range(3):
                try:
                    w.do_do()
                    break
                except RuntimeError as e:
                    ex = e
                    self.repair()


            if ex is not None:
                raise ex

    def repair(self):
        print('repairing stuff...')


class GrandManager:
    def __init__(self, manager: Manager):
        self.manager = manager

    def start_work(self):
        try:
            self.manager.force_to_work()
        except RuntimeError:
            print('ok thats fine!')


def test():
    group = [
        Worker(),
        Worker(),
        Worker(),
    ]

    m = Manager(group_workers=group)

    gm = GrandManager(manager=m)

    gm.start_work()

if __name__ == '__main__':
    test()







