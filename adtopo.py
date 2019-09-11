# from mininet. import 
from mininet.topo import Topo
# You may want to define a custom switch here
# class switch():


class adtopo(Topo):
    def __init__(self, **argv):
        Topo.__init__(self, **argv)
        #change loss=1 to get bonus
        linkopts = dict(bw=1000,delay='10ms',loss=0)
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')
        h15 = self.addHost('h15')
        h16 = self.addHost('h16')
        #Add more switches
        # s1 = self.addSwitch('s1')


        #Add links your links must contains **linkopts
        # self.addLink(s1, s2 , **linkopts)
        # self.addLink(s1, h2 , **linkopts)


topos = { 'adtopo': ( lambda: adtopo() ) }
