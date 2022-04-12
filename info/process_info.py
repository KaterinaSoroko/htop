import psutil


class Processes:
    info = []
    count = {}
    template, header, template_process = "", "", ""
    count_thr, count_running = 0, 0

    def get(self):
        for proc in psutil.process_iter(['pid', 'name', 'username', 'status', 'num_threads',
                                         'memory_percent', 'cpu_percent']):
            self.info.append(proc.info)

    def prepare_data(self):
        self.count.update(tasks=len(self.info))
        for task in self.info:
            task["memory_percent"] = round(task["memory_percent"], 1)
            task["cpu_percent"] = round(task["cpu_percent"], 1)
            self.count_thr += task['num_threads']
            if task['status'] == 'running':
                self.count_running += 1
        self.count.update(threads=self.count_thr, running=self.count_running)
        return self.count

    def prepare_template(self):
        self.template = "Tasks {}, {} thr, {} running".format("{tasks}", "{threads}", "{running}")
        self.header = "{:>8}  {:<20}  {:<10}  {:>5}  {:>5}  {:<30}"\
            .format("PID", "Username", "Status", "CPU%", "MEM%", "Name")
        self.template_process = "{}  {}  {}  {}  {}  {}"\
            .format("{pid:>8}", "{username:<20}", "{status:<10}", "{cpu_percent:>5}",
                    "{memory_percent:>5}", "{name:<30}")
        return self.template, self.header, self.template_process

    def show(self):
        self.prepare_data()
        self.template, self.header, self.template_process = self.prepare_template()
        print(self.template.format(**self.count))
        print(self.header)
        for proc_dict in self.info:
            print(self.template_process.format(**proc_dict))
