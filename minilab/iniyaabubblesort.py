class Bubblesort:
    """Initializer of class takes series parameter and returns Class Object"""

    def __init__(self, list):
        """Built in validation and exception"""
        self.sort = list.copy()
        self.bubbles()

    # Algorithm for building bubble sort, this id called from __init__"""
    def bubbles(self):
        n = len(self.sort)
        for i in range(n):
            for j in range(0,n-i-1):
                if list[j] > list[j+1] :
                    list[j], list[j+1] = list[j+1], list[j]

    @property
    def result(self):
        return self.sort


if __name__ == "__main__":
    list = [23, 45, 12, 67, 11, 84, 93]

    a = Bubblesort(list)

    print("This is the initial list of numbers:")
    print(list)
    print("This is the list post bubble sort:")
    print(a.result),
