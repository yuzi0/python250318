strName = "Not Class Member"

class DemoString:
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        print(strName)  #버그 발생
        print(self.strName)

d = DemoString()
d.set("First Message")
d.print()
