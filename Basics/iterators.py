# iterators in python

def iterators(num):
    it = iter(num) # using iterator
    print(it.__next__()) # next method used in iterators to print values of list iteratively
    print(it.__next__())
    print(next(it)) # another way of using next

# print top 10 num
class Topten: # creating class
    def __init__(self): # init here we using to define counter variable
        self.num = 1

    def __iter__(self): # it will give object of iterator
        return self

    def __next__(self): # it will give next value
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


# main function
def main():
    num = [8,0,5,2,6]
    iterators(num)
    values = Topten()
    for i in values:
        print(i)



# main execution
if __name__ == '__main__':
    main()






