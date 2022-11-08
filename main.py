import multiprocessing
from multiprocessing import Process
from datetime import datetime

def getData(queue):
    while True:
        if queue.empty():
            continue
        number, degree = queue.get()
        numberInDegree = number ** degree
        dateTime = datetime.now()
        summa = sum(range(numberInDegree + 1))
        with open("writefile.txt", "a", encoding='utf8') as file:
            file.write(str(dateTime) + " >> " + str(number) + " ^ " + str(degree) + " = " + str(numberInDegree) + " Сумма от 0 до " + str(numberInDegree) + " = " + str(summa) + "\n")


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process = Process(target=getData, args=(queue,))
    process.start()
    while True:
        try:
            str = input("Введите число и степень, в которую нужно возвести число: ")
            number, degree = (str.split(' '))# получаем значения от пользователя
            numberInInt: int = int(number)
            DegreeInInt: int = int(degree)
            dataCarteg = [numberInInt, DegreeInInt]
            queue.put(dataCarteg)
        except:
            print("Error!")