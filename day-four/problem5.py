#
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
###not equal check
#counter % 1 != 0 and counter % 2 != 0 and counter % 3 != 0 and counter % 4 != 0 and counter % 5 != 0 and counter % 6 != 0 and counter % 7 != 0 and counter % 8 != 0 and counter % 9 != 0 and counter % 10 != 0: 

#counter % 1 == 0 and counter % 2 == 0 and counter % 3 == 0 and counter % 4 == 0 and counter % 5 == 0 and counter % 6 == 0 and counter % 7 == 0 and counter % 8 == 0 and counter % 9 == 0 and counter % 10 == 0:  

counter = 1

ticker= 1

while True: 
    if counter % 1 == 0 and counter % 2 == 0 and counter % 3 == 0 and counter % 4 == 0 and counter % 5 == 0 and counter % 6 == 0 and counter % 7 == 0 and counter % 8 == 0 and counter % 9 == 0 and counter % 10 == 0 and counter % 11 == 0 and counter % 12 == 0 and counter % 13 == 0 and counter % 14 == 0 and counter % 15 == 0 and counter % 15 == 0 and counter % 16 == 0 and counter % 17 == 0 and counter % 18 == 0 and counter % 19 == 0 and counter % 20 == 0:
        print str(counter) + " IS THE WINNER"
        break
    else:
        print counter
        counter += 1
    

# write a function which iterantes ? 
#while iterateFucand iterate though a function?
    # for i in list_check:
    #     if counter % i == 0.0:
    # break 
    #     else:
    #         counter += 1.0

##While loop example
# counter_test = 1
# while True: 
#     for i in list_check:
#         if i < 9:
#             print str(i) +" thats below 9"
#             counter_test += 1
#             print counter_test
#     else:
#         print str(i) + "not below 9"
#         print "breaking out of the while loop"
#         break

# print "out of the loop"



