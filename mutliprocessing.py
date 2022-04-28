import multiprocessing

from threading import *
import threading
import time

def startThreads():
	t1 = threading.Thread(target=func1,)
	t2 = threading.Thread(target=func2,)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
    
def func1():
    list_1 = []
    for i in range(5000000):
        #time.sleep(1)
        list_1.append(i)

def func2():
    list_1 = []
    for i in range(5000000):
        #time.sleep(1)
        list_1.append(i)

if __name__ == "__main__":

    #without any thread and process
    start = time.time()
    func1()
    func2()
    end = time.time()

    print("time taken when executing without process",end-start)

    #with multiple thread
    thread_1 = Thread(target = func1)
    thread_2 = Thread(target = func2)
    start = time.time()
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    end = time.time()
    print("time taken when executing with multithread",end-start)

    #with multiple process
    process_1 = multiprocessing.Process(target=func1)
    process_2 = multiprocessing.Process(target=func2)
    start = time.time()
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
    end = time.time()

    print("time taken when executing with multiple process", end-start)

    # one process with multiple thread 
    p = multiprocessing.Process(target=startThreads)
    start = time.time()
    p.start()
    p.join()
    end = time.time()
    print("time taken when one process with multiple thread",end - start)
    print("=====================================")