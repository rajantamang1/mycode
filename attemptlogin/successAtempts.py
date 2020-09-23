#!/urs/bin/python3
loginSuccess =0
failedlogin=0
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

keystone_file_lines = keystone_file.readlines()

for line in keystone_file_lines:
    if not "- - - - -] Authorization failed" in line and not "ERROR" in line:
        loginSuccess += 1 # for counting number of successful attempts
    else:
        failedlogin += 1
print("The number of successful login attemps is: ", loginSuccess)
print("The number of failed login attempt is:", failedlogin, line.split("from")[-1])
keystone_file.close() 
