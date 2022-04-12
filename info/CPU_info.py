import psutil


class Cpu:
    info = {}
    template = ""

    def get(self):
        self.info.update(cpu_percent=psutil.cpu_percent(interval=0.1, percpu=True))
        self.info.update(cpu_loadavg=psutil.getloadavg())
        self.info.update(cpu_time=psutil.cpu_times().user)

    def prepare_data(self):
        time = self.info['cpu_time']
        self.info['cpu_time'] = f'{int(time//3600)}:{int((time%3600)//60)}:{int(time%60)}'

    def prepare_template(self):
        self.prepare_data()
        for index, value in enumerate(self.info["cpu_percent"]):
            percent_str = "{:>5} [{:<20}]".format(index, "*"*int(value//5))
            self.template += percent_str + "{cpu_percent[" + str(index) + "]}%\n"
        self.template += "Uptime: {cpu_time}\n"
        self.template += "Load average: "
        for index in range(len(self.info["cpu_loadavg"])):
            self.template += "{cpu_loadavg[" + str(index) + "]}  "
        return self.template

    def show(self):
        self.prepare_template()
        print(self.template.format(**self.info))
