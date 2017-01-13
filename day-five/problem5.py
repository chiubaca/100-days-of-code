import time
from timeit import default_timer as timer

start = timer()

counter = 5
while True: 
    if counter % 1 == 0 and counter % 2 == 0 and counter % 3 == 0 and counter % 4 == 0 and counter % 5 == 0 and counter % 6 == 0 and counter % 7 == 0 and counter % 8 == 0 and counter % 9 == 0 and counter % 10 == 0 and counter % 11 == 0 and counter % 12 == 0 and counter % 13 == 0 and counter % 14 == 0 and counter % 15 == 0 and counter % 15 == 0 and counter % 16 == 0 and counter % 17 == 0 and counter % 18 == 0 and counter % 19 == 0 and counter % 20 == 0:
        print str(counter) + " IS THE WINNER"
        break
    else:
        print counter
        counter += 1
    
end = timer()

print(end - start)  
