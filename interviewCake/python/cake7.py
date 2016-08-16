temps = [1, 3, 6, 3, 1, 3]
temps = {
    1: 2,
    2: 0,
    3: 3,
    4: 0,
    5: 0,
    6: 1
}

class temp_tracker():
    temps = {}

    def __init__(self):
        for temp in range(150): # Viable temps
            self.temps[temp - 10] = 0
        # print self.temps
        self.mode = []
        self.max = None
        self.min = None
        self.count = 0
        self.sum = 0

    def insert(self, temp):
        self.temps[temp] += 1
        self.count += 1
        self.sum += temp
        # mode_count = temps[self.mode[0]] or None
        if self.count is 1: # First insert
            self.mode.append(temp)
            self.max = self.min = temp
        else:
            # Check mode
            mode_count = self.temps[self.mode[0]]
            curr_count = self.temps[temp]
            if curr_count == mode_count: # Add to mode
                self.mode.append(temp)
            elif curr_count > mode_count:
                self.mode = [temp]

            if temp < self.min: # Check Min
                self.min = temp
            elif temp > self.max: # Check Max
                self.max = temp

    def get_max(self):
        print self.max
        return self.max

    def get_min(self):
        print 'Min: ', self.min
        return self.min

    def get_mean(self):
        print 'Mean: ', self.sum / self.count
        return self.sum / self.count

    def get_mode(self):
        print 'Mode: ', self.mode
        return self.mode

mine = temp_tracker()
mine.insert(5)
mine.insert(12)
mine.insert(5)
mine.insert(5)
mine.insert(3)

mine.get_max()
mine.get_min()
mine.get_mean()
mine.get_mode()
