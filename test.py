from algovis import sorting
import random

my_list = [20 - i for i in range(20)]

# random.shuffle(my_list)

bs_object = sorting.QuickSort(my_list)

# bs_object.visualize(interval=1)

bs_object.sort(pivot="random")

#bs_object.visualize(interval=250, pivot="random")
