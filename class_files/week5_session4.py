class Computer(object):
    def __init__(self,ram=4,os="linux"):
        self.cpu = "i5",
        self.ram = ram,
        self.hard_drive = "Seagate",
        self.os = os,
        self.turned_on = False
    def boot(self):
        self.turned_on = True
        print "powered on"

    def run_program(self, program):
        if self.turned_on:
            print "running {}".format(program)

    def about(self):
        if self.turned_on:
            print "I'm running {} with {}gb of ram".format(self.os, self.ram)

my_pc = Computer(16,"macOS")
my_pc.boot()
my_pc.run_program('Atom')
my_pc.about()
