import time


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

