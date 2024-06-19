import time
import threading

start = time.perf_counter()

def do_something():
    print("Sleeping 1 second")
    time.sleep(10)
    print("Done sleeping ....")


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t3 = threading.Thread(target=do_something)
t4 = threading.Thread(target=do_something)

t1.start()
t2.start()
t3.start()
t4.start()


t1.join()
t2.join()
finish = time.perf_counter


finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds(s)')