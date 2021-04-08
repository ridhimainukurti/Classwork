
class Addition:

    def __init__(self, series):
        if series < 0 or series > 10:
            raise ValueError("Series must be between 2 and 100")
        self._series = series
        self._list = [1]
        self._dict = {}
        self._dictID = 0

        self.additionseries()


    """Algorithm for building Fibonacci sequence, this id called from __init__"""
    def additionseries(self):
        limit = self._series
        print(limit)
        addition = 1
        for i in range(0,limit + 1):
            addition = addition+i
            self.set_data(addition)



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

    n = 2

    addition = Addition(n)

    print(f"Addition of {n} = {addition.number}")
    print(f"Addition series for {n} = {addition.list}")



    for i in range(n):
        print(f"Adding sequence {i} = {addition.get_sequence(i)}")
