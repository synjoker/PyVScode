import time
import sys

def main():
    start_time = time.time()

    evens = []
    for i in range(100000000):
        if i % 2 == 0:
            evens.append(i)

    end_time = time.time()
    
    # print(evens)
    print(end_time - start_time)
    print(start_time)
    print(end_time)

if __name__ == "__main__":
    main()