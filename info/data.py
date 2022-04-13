from abc import ABC, abstractmethod


class Data(ABC):
    info = {}
    template = ""

    @abstractmethod
    def get(self):
        ...

    @abstractmethod
    def prepare_data(self):
        ...

    @abstractmethod
    def prepare_template(self):
        ...

    def show(self):
        self.prepare_data()
        self.prepare_template()
        print(self.template.format(**self.info))


