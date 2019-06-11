import threading
import time
class MyThread(threading.Thread):
    def __init__(self,threadName,delay):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.delay = delay
    def run(self):
        print("Inside thread: ",self.threadName)
        time.sleep(self.delay)
        print("Exit from thread: ",self.threadName)
def threadFunction(delay):
    print("Using target function!!!")
    time.sleep(delay)
    print("Exiting the thread!!!")
if __name__ == "__main__":
    thread1 = MyThread("thread1",5)
    thread2 = MyThread("thread2",2)
    thread3 = threading.Thread(target=threadFunction(3),)
    thread3.start()
    thread1.start()
    thread2.start()
    print("Total active threads: ",threading.activeCount())
    thread1.join()
    thread2.join()
    thread3.join()
