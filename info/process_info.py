import psutil
from info.data import Data


class Processes(Data):
    processes = []
    header, template_process = "", ""
    count_thr, count_running = 0, 0

    def get(self):
        for proc in psutil.process_iter(['pid', 'name', 'username', 'status', 'num_threads',
                                         'memory_percent', 'cpu_percent']):
            self.processes.append(proc.info)

    def prepare_data(self):
        self.info.update(tasks=len(self.processes))
        for task in self.processes:
            task["memory_percent"] = round(task["memory_percent"], 1)
            task["cpu_percent"] = round(task["cpu_percent"], 1)
            self.count_thr += task['num_threads']
            if task['status'] == 'running':
                self.count_running += 1
        self.info.update(threads=self.count_thr, running=self.count_running)
        return self.info

    def prepare_template(self):
        self.template = "Tasks {}, {} thr, {} running".format("{tasks}", "{threads}", "{running}")
        return self.template

    def prepare_template_processes(self):
        self.header = "{:>8}  {:<20}  {:<10}  {:>5}  {:>5}  {:<30}" \
            .format("PID", "Username", "Status", "CPU%", "MEM%", "Name")
        self.template_process = "{}  {}  {}  {}  {}  {}" \
            .format("{pid:>8}", "{username:<20}", "{status:<10}", "{cpu_percent:>5}",
                    "{memory_percent:>5}", "{name:<30}")
        return self.header, self.template_process

    def show(self):
        super().show()
        self.header, self.template_process = self.prepare_template_processes()
        print(self.header)
        for proc_dict in self.processes:
            print(self.template_process.format(**proc_dict))
