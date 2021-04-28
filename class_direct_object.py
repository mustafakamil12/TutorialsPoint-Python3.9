import time

class Andromeda:
    def __init__(self):
        self.time_t = time.time()
        #print("self.time_t: ", self.time_t)

    def __repr__(self):
        return repr(self.time_t)

    def get_time_t(self):
        cleanTime = int(self.time_t)
        return cleanTime


    def as_text(self, strTime):
        self.time_t = strTime
        print("self.time_t: ", self.time_t)



prod_time = Andromeda()
print("prod_time: ", prod_time.get_time_t())

prod_time.as_text('1619122569')
