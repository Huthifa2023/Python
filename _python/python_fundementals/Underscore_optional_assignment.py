class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i]=callback(i)        
        print(iterable)



_ = Underscore()
_.map([1,2,3], lambda x: x*2) 

