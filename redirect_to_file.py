# program to explain the concept of redirecting stdout and stderr output
# to a file.
'''
Multiline comments should be preferably done using #
Exceptions and exception handling concepts also demonstrated
'''
import sys
import time
temp = sys.stdout
fp = open("output.txt","w")
sys.stdout = fp
print("First line of output stream")
print("Second line of output file")
sys.stdout = temp
fp.close()
print("Output in terminal")

# Now for stderr

print("Redirecting standard error stderr to a file")
temp = sys.stderr
fp = open("error.txt","w")
sys.stderr = fp

try:
    a = 12/0#This error which will not be redirected to file
    print("Check if the line works or not::") #it will not work
except Exception as e:
    print("This is the exception:- ",e)
finally:
    print("In finally:")
print("The error is handled by the Exception handling block so nothing is written in error.txt file:")
#create another error which will be redirected to error.txt and program will exit 
print("See the contents of error.txt")
#a = 45/0
#absurd
print("Press ctrl+c :-")
time.sleep(3) 
print("Time Over for ctrl+c!! Check the new error")
arr =[1,2,3]
x = arr[18]
print("Program exited so everything is  meaningless!!!")
print("stderr reverted to terminal")
sys.stderr = temp
fp.close()
b = 15/0 #again some error which will be displayed in terminal
