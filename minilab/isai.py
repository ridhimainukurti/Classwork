"""Fibonacci algorithm contained within a class """


class Factorial:
    """Initializer of class takes series parameter and returns Class Objectg"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 100:
            raise ValueError("Series must be between 2 and 100")
        self._series = series
        self._list = [1]
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.factorialseries()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Fibonacci sequence, this id called from __init__"""
    def factorialseries(self):
        limit = self._series
        factorial =1  # fibonacci starting array/list
        for i in range(1,limit + 1):
            factorial = factorial*i
            self.set_data(factorial)



    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        #self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._list.append(num)
        self._dictID += 1

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]


# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 8
    '''Constructor of Class object'''
    factorial = Factorial(n)

    '''Using getters to obtain data from object'''
    print(f"Factorial of {n} = {factorial.number}")
    print(f"Fibonacci series for {n} = {factorial.list}")

    '''Using method to get data from object'''

    for i in range(n):
        print(f"Fibonacci sequence {i} = {factorial.get_sequence(i)}")



