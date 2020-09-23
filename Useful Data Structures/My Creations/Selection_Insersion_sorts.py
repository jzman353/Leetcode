import random
import time


# list -> None
# Takes a list, sorts it in-place (mutation) using selection sort
def selection_sort(list):
    #comparisons = 0
    for i in range(len(list) - 1):
        min_spot = i
        for j in range(i + 1, len(list)):
            #comparisons+=1
            if list[j] < list[min_spot]:
                min_spot = j
        #comparisons+=1
        if i != min_spot:
            swap(list, i, min_spot)
    #print(comparisons)
    return True

# numList, int, int -> None
def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    
def insertion_sort(list):
    #comparisons = 0
    for i in range(1, len(list)):
        #comparisons += 1
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            #comparisons += 1
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    #print(comparisons)
    return True


def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

