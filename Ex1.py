import csv
import json
import random
import sys


class Elevator:
    def __init__(self, list):
        self.id = list["_id"]
        self.speed = list["_speed"]
        self.minFloor = list["_minFloor"]
        self.maxFloor = list["_maxFloor"]
        self.closeTime = list["_closeTime"]
        self.openTime = list["_openTime"]
        self.startTime = list["_startTime"]
        self.stopTime = list["_stopTime"]


class Building:
    def __init__(self, file_name):
        with open(file_name, 'r') as foo:
            obj = json.load(foo)
            self.maxFloor = obj["_maxFloor"]
            self.minFloor = obj["_minFloor"]
            list = obj["_elevators"]
            self.Elevator = []
            for i in list:
                self.Elevator.append(Elevator(i))
            self.expressElevator = fastest_elevator(self)
            self.p = (abs(self.minFloor - self.maxFloor))


class Call:
    def __init__(self, list):
        self.string = list[0]
        self.Time = list[1]
        self.soFloor = list[2]
        self.desFloor = list[3]
        self.ignore = list[4]
        self.elevAllocate = list[5]


def calculateTime(i: int, c: list, elevator: Elevator) -> float:
    call = c[i]
    time = ((abs(int(call.soFloor) - int(call.desFloor))) / elevator.speed) + (elevator.openTime * 2) + (
            elevator.closeTime * 2) + (elevator.startTime + elevator.stopTime)

    return time


def Calls(csvfile) -> list:
    calls1 = []
    with open(csvfile, "r") as file:
        reader = csv.reader(file)
        for i in reader:
            calls1.append(Call(i))

    return calls1


def Calculate(elevator: Elevator, call: Call):
    time = ((abs(int(call.soFloor) - int(call.desFloor))) * elevator.speed) + (elevator.openTime * 2) + (
            elevator.closeTime * 2) + (elevator.startTime + elevator.stopTime)

    return time


def ElevatorAlo(index, B: Building, C: list):
    if (floorsdes(index, C)) > (B.p / 2):
        C[index].elevAllocate = B.expressElevator
    elif (downcall(index, C) == True):
        choose = chooseElev(B)
        if (Calculate(B.Elevator[choose], C[index]) > (
                timediff(index, C))) and (
                callonway1(index, C)) and downcall(index + 1, C) == True:
            C[index].elevAllocate = choose
            C[index + 1].elevAllocate = choose

        else:

            curr = chooseElev(B)
            next = chooseElev(B)
            while (curr == next):
                curr = chooseElev(B)
                next = chooseElev(B)
            C[index].elevAllocate = curr
            C[index + 1].elevAllocate = next
    else:
        if (Calculate(B.Elevator[chooseElev(B)], C[index]) > timediff(index, C)) and callonway2(index, C) and upCall(
                index + 1,
                C) == True:
            choose = chooseElev(B)
            C[index].elevAllocate = choose
            C[index + 1].elevAllocate = choose
        else:
            C[index].elevAllocate = chooseElev(B)
            C[index + 1].elevAllocate = chooseElev(B)

    if (int(C[index].elevAllocate) < 0):
        C[index].elevAllocate = 0


def chooseElev(b: Building) -> int:
    res = random.randrange(len(b.Elevator))
    return res


def timediff(i: int, F: list) -> float:
    res = abs((float(F[i].Time) - (float(F[i + 1].Time))))
    return res


def callonway1(i: int, F: list) -> bool:
    res = (F[i + 1].soFloor >= F[i].soFloor)
    if res == True:
        return True
    else:
        return False


def callonway2(i: int, F: list) -> bool:
    res = (F[i + 1].soFloor >= F[i].soFloor)
    if res == True:
        return True
    else:
        return False


def downcall(i, F):
    if ((int(F[i].desFloor)) < (int(F[i].soFloor))):
        return True
    else:
        return False


def upCall(i, F):
    if ((int(F[i].desFloor)) > (int(F[i].soFloor))):
        return True
    else:
        return False


def floorsdes(i: int, F: list) -> int:
    res = abs(int(F[i].soFloor) - int(F[i].desFloor))
    return res


def fastest_elevator(building):
    elevators = building.Elevator
    min = 10000
    res = 0
    for i in range(len(elevators) - 1):
        time = (float)(elevators[i].openTime + elevators[i].closeTime + elevators[i].startTime + 1 / elevators[i].speed)
        if (time < min):
            min = time
            res = i
    return res


def write_calls(c, name):
    dataCalls = []
    for k in c:
        dataCalls.append(k.__dict__.values())
    with open(name, 'w', newline="") as fu:
        csvwriter = csv.writer(fu)
        csvwriter.writerows(dataCalls)


def inputs():
    if len(sys.argv) == 4:
        di = {
            "buildingName": sys.argv[1],
            "callsName": sys.argv[2],
            "outputName": sys.argv[3]
        }
    else:
        di = {
            "buildingName": "inputs\Ex1_Buildings\B2.json",
            "callsName": "inputs\Ex1_Calls\Calls_b.csv",
            "outputName": "out.csv"
        }
    return di


if __name__ == '__main__':
    data = inputs()
    c = Calls(data["callsName"])
    b = Building(data["buildingName"])
    i = 0
    if (len(b.Elevator) == 1):
        while i < len(c)-1:
            c[i].elevAllocate = int(0)
            i = i + 1

    else:
        j = 0
        while j < len(c)-1:
            if (int(c[j].elevAllocate) != -1):
                j = j + 1
            ElevatorAlo(j, b, c)
            j = j + 1

    write_calls(c, data["outputName"])

