#Create an iterator object
#To create an iterable you have to implement __iter__ and __next__ methods
#Similar to __init__() __iter__() initializes but should return self object.
#__next__() returns the next sequence.
#for loop creates an iterable and execute next for every time it loops.
class MyIterator():
    def __init__(self,start=0,end=1000):
        self.start = start
        self.end = end
    def __iter__(self):#
        self.no = self.start
        return self
    def __next__(self):
        if self.no < self.end:
            no = self.no
            self.no+=1
            return no
        else:
            raise StopIteration
if __name__ =='__main__':
    miter =  MyIterator(10)#Starting from 10 and ending = default parameter as 1000
    miter = iter(miter)
    print(next(miter))
    print(next(miter))
    print(next(miter))
    print(next(miter))
    print("Iter object will be reinitialized in the for loop:")
    for i in miter:#Re creating an iterable and executing next for every loop
        print(i)
