from time import sleep
from threading import Thread
class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)

class Hii(Thread):
    def run(self):
        for i in range(10):
            print("Hii")
            sleep(1)

t1=Hello()
t2=Hii()
t1.start()
sleep(0.2)
t2.start()
#print("bois")
t1.join()
t2.join()
print("bye")