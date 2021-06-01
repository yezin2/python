class JindoDog:
    def __init__(self):
        self.power_bark = 0
    def train (self):
        self.power_bark += 1

class SokchoSeagull():
    def __init__(self):
        self.flag_fly = False
    def flight(self):
        self.flag_fly = True

class gaesae(JindoDog,SokchoSeagull):
    def __init__(self):
        JindoDog.__init__(self)
        SokchoSeagull.__init__(self)

gs = gaesae()
print(gs.power_bark)
print(gs.flag_fly)
gs.train()
gs.flight()
print(gs.power_bark)
print(gs.flag_fly)
