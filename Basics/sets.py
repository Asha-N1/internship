# sets in python
def main():
    a = {"x","y","z","l","m","n"} 
    print(a)

    print(len(a)) # length of set

    a.remove("x") # remove element of x
    print(a)

    a.clear() # display empty set
    print(a)

    set1 = {"s1","s2","s3"}
    set2 = {"o","r","n"}
    set2.update(set1) # updating elements
    print(set2)

    set2.union(set1) #c ombining elements
    print(set2)

# main execution
if __name__ == '__main__':
    main()

