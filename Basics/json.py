# JOSN in python
import json # importing JSON

def json():
# convering python objects into JOSN string
    print(json.dumps({"name": "John", "age": 30})) # dict
    print(json.dumps(["apple", "bananas"])) # list
    print(json.dumps(("apple", "bananas"))) # tuple
    print(json.dumps("hello")) # string
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None))

# main function
def main():
    json()

# main execution
if __name__ == '__main__':
    main()



