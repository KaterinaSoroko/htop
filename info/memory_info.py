import psutil
from info.data import Data


class Memory(Data):

    def get(self):
        self.info.update(virtual=(psutil.virtual_memory().used, psutil.virtual_memory().total))
        self.info.update(swap=(psutil.swap_memory().used, psutil.swap_memory().total))

    def prepare_data(self):
        self.info['virtual'] = list(map(lambda x: round((x / (1024**3)), 2), self.info['virtual']))
        self.info['swap'] = list(map(lambda x: round((x / (1024 ** 3)), 2), self.info['swap']))

    def prepare_template(self):
        load_virtual = int((self.info["virtual"][0]/self.info["virtual"][1]) * 20)
        virtual_str = "{:>5} [{:<20}]".format("Mem", "*" * load_virtual)
        self.template += virtual_str + "{virtual[0]}/{virtual[1]}G\n"
        load_swp = int((self.info["swap"][0] / self.info["swap"][1]) * 20)
        swp_str = "{:>5} [{:<20}]".format("Swp", "*" * load_swp)
        self.template += swp_str + "{swap[0]}/{swap[1]}G\n"
        return self.template
