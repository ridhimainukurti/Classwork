class BubbleSort:
    """Initializer of class takes series parameter and returns Class Object"""
    list = []

    def __init__(self, series):
        """Built in validation and exception"""
        self.list = series
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.sorting()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

# Algorithm for building bubble sort, this id called from __init__"""
    def sorting(self):
    # We go through the list as many times as there are elements
        for i in range(len(self.list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
            for j in range(len(self.list) - 1):
                if self.list[j] > self.list[j+1]:
                    # Swap
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]

    def get_list (self):
        print ("Sorted array is:")
        for i in range(len(list)):
            print(list[i]),


    def set_data(self, num):
        self._value = num

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def value(self):
        return self._value

    @property
    def number(self):
        return self._value

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]


# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    # list = [17, 13, 6, 2, 18, 8]
    inputted_list = input('enter a list of numbers, characters, or words seperated by commas: ')
    list = inputted_list.split(',')

    '''Constructor of Class object'''
    my_sort = BubbleSort(list)
    # b_sort(list)

    '''Using getters to obtain data from object'''
    my_sort.get_list()
