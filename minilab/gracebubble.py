import sys
import numpy as np

class bubblesorting:
    def __init__(self):
        self._lst=[]

    def g_original(g_test):
        g_var1 =  g_test
        return g_var1.split(',')

    def bubbleSort(value_1):

        n = len(value_1)-3
        value_g = value_1
        arr = value_g.split(',')
        value = arr
        #value = value_1


        #g_var1 = value_1[1]
        #g_var2 = value_1[2]
        #g_var3 = value_1[3]
        #g_var4 = value_1[4]
        #value = [g_var1, g_var2, g_var3, g_var4, g_var1, g_var2, g_var3, g_var4,]

        #sys.stdout.write(n)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n-i-1):
                if value[j] > value[j+1]:
                    value[j], value[j+1] = value[j+1], value[j]
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
        return value
