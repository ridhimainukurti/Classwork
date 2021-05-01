
    # def __init__(self):
#         self._list = []
#         self._integerlist = []
#         self._characterlist = []
#         self._stringList = []
#
#
#     def integer(self):
#         output = bubbleSort(self._integerlist)
#         return output
#
#     def bubbleSort(arr):
#         n = len(arr)
#
#         # Traverse through all array elements
#         for i in range(n):
#
#             # Last i elements are already in place
#             for j in range(0, n-i-1):
#                 if arr[j] > arr[j+1] :
#                     arr[j], arr[j+1] = arr[j+1], arr[j]

class RidhimaBubblesort:
    list = []
    type = ""
    def __init__(self,inputlist):
        """Built in validation and exception"""
        self.prase_data(inputlist)

        self.bubsort()


    def prase_data(self,inputlist):
        self.list = list(inputlist.split(":"))

    def bubsort (self):
        n = len(self.list)
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if self.list[j] > self.list[j+1] :
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
        # return self.list

    @property
    def get_sorted_list (self):
        return self.list
