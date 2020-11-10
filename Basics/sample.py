# Import classes from your brand new package 
from Bmw import Bmw 
from Audi import Audi 
from Nissan import Nissan 

# defining main function   
def main():
    # Create an object of Bmw class & call its method 
    ModBMW = Bmw() 
    ModBMW.outModels() 
    # Create an object of Audi class & call its method 
    ModAudi = Audi() 
    ModAudi.outModels() 
    # Create an object of Nissan class & call its method 
    ModNissan = Nissan() 
    ModNissan.outModels()

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()