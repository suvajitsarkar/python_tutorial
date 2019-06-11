#Count number of line in a file
def method1():
    count = 0
    try:
        fp = open("error.txt","r")
        while fp.readline():
            count+=1
        print("No. of lines in file are:- ",count)
    finally:
        print("Finally block..Closing the file!!!")
        fp.close()

#Using with statement to access file. It would use try ... finally to reassure closing of the file.
def method2():
    count = 0
    with open("error.txt","r") as f:
        while f.readline():
            count+=1
        print("No. of lines in file are:- ",count)
method1()
method2()

#Method2 should be used to when working with unmaneged resources(such as file streams)...
