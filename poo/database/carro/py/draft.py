class Carro:
    def __init__(self):
        self.pas: int = 0
        self.pasMax: int = 2
        self.gas: int = 0
        self.gasMax: int = 100
        self.km: int = 0

    def __str__(self) -> str:
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def enter(self) -> None:
        if self.pas < self.pasMax:
            self.pas+=1
        else:
            print("fail: limite de pessoas atingido")
    
    def leave(self) -> None:
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.pas-=1
    
    def fuel(self, increment: int) -> None:
        self.gas+=increment
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance: int) -> None:
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print("fail: tanque vazio")
        elif self.gas < distance:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0
        else:
            self.km += distance
            self.gas -= distance

def main():
    carro = Carro()

    while True:
        line: str = input()
        print("$"+line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            increment = int(args[1])
            carro.fuel(increment)
        elif args[0] == "drive":
            distance = int(args[1])
            carro.drive(distance)
        elif args[0] == "show":
            print(carro)
            
main()