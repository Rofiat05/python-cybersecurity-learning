routers = []
switches = []

devices = ["RT1", "RT2", "RT3", "SW1", "SW2", "SW3"]
devices = devices + ["RT4", "SW4"]

for i in devices:
    if "R" in i:
        routers.append(i)
    else: 
        switches.append(i)

print("Routers:", routers)
print("Switches:", switches)  

devicenames = ["RT1", "RT2", "SW1", "SW2"]
print(devicenames[-1])

addition = 22 + 10
print(addition)

print([1,2,4,5] + [3,6])

y = 2
y * 3 
'test'*y
print('test'*y) 

devicenames = ["RT1", "RT2", "SW1", "SW2"]
hostnames = devicenames + [" RT3", "SW3"]
del hostnames [3]
print(hostnames)

print = ipAddress = {"R1": "10.1.1.1", "R2": "10.2.2.1", "R3": "10.3.3.1"}

ipaddress = {"R1":" 10.1.1.1", "R2": "10.2.2.1", "R3":" 10.3.1"}
print(ipaddress["R2"])

aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <= 199:
    print("This is an extended IPv4 ACL.")
else:
    print("this is not a standard or extended IPv4 ACL.") 