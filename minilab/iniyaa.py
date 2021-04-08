
class lucas:
    def __init__(self, series):
        if series < 1 or series > 100:
            raise ValueError("Series must be between 1 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.lucas_series()

    def lucas_series(self):
        limit = self._series
        f = [0, 1]  # lucas starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [f[1], f[0] + f[1]]
            limit -= 1

    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    """Getters """
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    def get_sequence(self, nth):
        return self._dict[nth]

if __name__ == "__main__":
    n = 3
    lucas = lucas(n)

    print(f"Lucas Series number for {n} = {lucas.number}")
    print(f"Lucas Series for {n} = {lucas.list}")

    for i in range(n):
        print(f"Lucas sequence {i + 1} = {lucas.get_sequence(i)}")

