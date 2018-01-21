import time
import multiprocessing
from timeit import default_timer as timer
def random_nums(main_list):
    import random
    lotto_num = [] #list of valid 6 numbers
    while True:
        while len(lotto_num)!= 6 :
            
            if len(lotto_num) >=3:
                x= random.randint(30,49)
            else:
                x = random.randint(1,30)
                
            if x not in lotto_num:
                lotto_num.append(x)
            
        sum_lotto = sum(lotto_num)
        
        if sum_lotto <= 209 and sum_lotto >= 121 and lotto_num not in main_list: 
            lotto_num.sort()
            main_list.append(lotto_num)
            return main_list                

def main():
    global main_list
    main_list = [] #main list of the 10000, lists of valid 6 numbers
    

    for i in range(1000):
        #print(i)
        main_list = random_nums(main_list)
    return main_list

start_timer = timer()
if __name__ == "__main__":
    jobs= []
    for i in range(1):
        p = multiprocessing.Process(target=main())
        jobs.append(p)
        p.start()
    
end_timer = timer()

run_time = end_timer - start_timer #run time duration
print("The run time was: %f seconds" % run_time)
print(main_list)
