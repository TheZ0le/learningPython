from datenbank import myDict
import time

def main():
    result = sorted(myDict)
    result = tuple(result)
    print('Sorted Tuple :', result)

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))