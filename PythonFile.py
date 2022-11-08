from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# создадим класс Observer-а с мотодом выполняющимся при условии выполнения каких либо дейстивий в объекте
def modif():
        with open("writefile.txt", "r", encoding='utf8') as file:
            print(file.readlines()[-1])


class Watcher(FileSystemEventHandler):
    pass


observer = Observer()
observer.schedule(Watcher(), path="C:\\PyPR")
observer.start()
try:
    while 1:
        pass
except KeyboardInterrupt:
    observer.stop()

