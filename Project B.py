#Scan a range of ports, 1-1025, writing results to a file

#Import required modules
import socket
import subprocess
from datetime import datetime
import time
import os

#Create a function to use the connect command for a given host and port
def CheckPort(host, port):
    s = socket.socket()
    try:
        s.connect((host,port))
    except:
        return False
    else:
        return True
#Every scan should create a new file. Check if file exists. If so, delete it.
if os.path.exists("C:/Users/majar/Documents/ProjectBResults.txt"):
    os.remove("C:/Users/majar/Documents/ProjectBResults.txt")
# open file in append+read mode, create if not exist
xfile = open("C:/Users/majar/Documents/ProjectBResults.txt", "a+")

# User Input
host = input("Enter target host IP address: ")
MinRange = int(input("Enter starting port number: "))
MaxRange = int(input("Enter ending port number: "))
CheckRange = range(MinRange, MaxRange+1, 1)

#Get current time
#datetime object containing current date and time
now = datetime.now()
# dd/mm/yy H:M:S
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
start = time.time()

#verify status of host is up before proceeding
command_line = (["ping -n 1"], host)
HostCheck = subprocess.Popen(command_line, stdout=subprocess.PIPE).communicate()[0]
cResult = str(HostCheck)
#print(cResult)
if (cResult.find("unreachable") != -1):
    print(host, "Unreachable")
    RespTup = [host, "is unreachable. Scan aborted at", dt_string, "\n"]
    RespOut = ' '.join(RespTup)
    xfile.write(RespOut)
    xfile.close()
    exit()
elif (cResult.find( "Received = 0" ) != -1):
    print(host, "not responding")
    RespTup = [host, "is not responding. Scan aborted at", dt_string, "\n"]
    RespOut = ' '.join(RespTup)
    xfile.write(RespOut)
    xfile.close()
    exit()
elif (cResult.find("could not find") != -1):
    print("cannot be found")
    RespTup = [host, "cannot be found, Scan aborted at", dt_string, "\n"]
    RespOut = ' '.join(RespTup)
    xfile.write(RespOut)
    xfile.close()
    exit()
elif (cResult.find("Received = 1") != -1):
    print(host, "is responding. Initializing scan.")
    print("Scan began at: ", dt_string)
    RespTup = [host, "is responding. Beginning scanning at", dt_string, "\n"]
    RespOut = ' '.join(RespTup)
    xfile.write(RespOut)
    xfile.close()

else:
    print("Unexpected error. Try again.")
    exit()

print("Scanning .... ")

for x in CheckRange:
    if CheckPort(host, x):
        print("Port ", x, "is open")
        CheckTup = ["Port", str(x), "is open.", "\n"]
        RespOut = ' '.join(CheckTup)
        xfile = open( "C:/Users/majar/Documents/ProjectBResults.txt", "a+")
        xfile.write(RespOut)

    else:
        print("Port", x, "is closed")
        CheckTup = ["Port", str(x), "is closed.", "\n"]
        RespOut = ' '.join(CheckTup)
        xfile = open("C:/Users/majar/Documents/ProjectBResults.txt", "a+")
        xfile.write(RespOut)

# notify user process has finished
end = time.time()
print("Task completed. Port range", MinRange, "-", MaxRange, "has been scanned.")
elapsed = end - start
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("Scan completed at: ", dt_string)
print("Total scan time: ", "%.2f" % elapsed, "seconds.")
FinTup = ["Scan completed at", str(dt_string), "\n"]
FinOut = ''.join(FinTup)
xfile.write(FinOut)
xfile.close()



