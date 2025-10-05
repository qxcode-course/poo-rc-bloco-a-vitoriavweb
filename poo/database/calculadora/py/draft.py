class Calculator:
    def __init__(self,batteryMax:int):
        self.batteryMax:int=batteryMax
        self.battery:int=0
        self.display:float=0.0
    
    def __str__(self):
        return (f"display = {self.display:.2f}, battery = {self.battery}")
    
    def Charge(self, increment:int)->None:
        self.battery+=increment
        if self.battery>self.batteryMax:
            self.battery=self.batteryMax
    
    def Sum(self, num1:float, num2:float)->None:
        if self.battery==0:
            print("fail: bateria insuficiente")
            return
        else:
            self.display=num1+num2
            self.battery-=1
    
    def Div(self, num1:float, num2:float)->None:
        if self.battery==0:
            print("fail: bateria insuficiente")
            return
        if num2==0:
            print("fail: divisao por zero")
            self.battery-=1
            return
        else:
            self.display=num1/num2
            self.battery-=1
        
def main():
    calculator:Calculator=None
    while True:
        line:str=input()
        print("$"+line)
        args:list[str]=line.split(" ")   
        
        if args[0]=="end":
            break
        if args[0]=="init":
            batteryMax:int=int(args[1])
            calculator=Calculator(batteryMax)
        if args[0]=="charge":
            increment:int=int(args[1])
            calculator.Charge(increment)
        if args[0]=="show":
            print(calculator)
        if args[0]=="sum":
            num1:float=float(args[1])
            num2:float=float(args[2])
            calculator.Sum(num1,num2)
        if args[0]=="div":
            num1:float=float(args[1])
            num2:float=float(args[2])
            calculator.Div(num1,num2)

main()