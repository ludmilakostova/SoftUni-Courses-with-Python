from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def work(self):
        raise NotImplementedError


class Worker(BaseWorker):

    def work(self):
        print("I'm working!!")


class Manager(BaseWorker):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if "BaseWorker" in [el.__name__ for el in worker.__class__.mro()]:
            self.worker = worker
        else:
            raise AssertionError("manager fails to support super_worker....")

    def manage(self):
        if self.worker is not None:
            self.worker.work()

    def work(self):
        print("Going through papers...")


class SuperWorker(BaseWorker):
    def work(self):
        print("I work very hard!!!")


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")

