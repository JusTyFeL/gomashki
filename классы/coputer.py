def Coputer():
    def __int__(self, cpu_freq, cpu_cores, ram , hdd = None, ssd = None):
        self.cpu_freq = cpu_freq
        self.cpu_cores = cpu_cores
        self.ram = ram
        self.hdd = hdd
        self.ssd = ssd

ps = Coputer(1,2,3)
ps2 = Coputer(1,2,3, hdd="kingston", ssd = "kingston")