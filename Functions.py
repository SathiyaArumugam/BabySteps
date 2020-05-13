# Functions
def hello():
    print("hello")
    print("hello again")
hello()

#calling function
hello()

#function with main
def getInteger():
    result = int(input("Enter value: "))
    return result
def Main():
    print("Started")

    #calling the getInteger function and
    #storing its returned value in the output variable
    output=getInteger()
    print(output)

#now we required to tell python 
#for 'main' function existence
if __name__ == "__main__":
    Main()