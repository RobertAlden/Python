student_vlan = 222
printer_vlan = 250
faculty_vlan = 270
voip_vlan = 280
security_vlan = 300


a = ["en","conf t","int ra fa0/1-24",f"sw acc vlan {student_vlan}","int ra gi0/1-2", "sw mo tr",""]
print("_____First Switch:_______")
for i in a:
	print(i)
	
print("int ra fa0/1-24")
print("sw port mac sticky")
print("sw port voil shutdown")

b = ["en","conf t","int ra fa0/1-8",f"sw acc vlan {student_vlan}","int fa0/9",f"sw acc vlan {faculty_vlan}","int fa0/10",f"sw acc vlan {printer_vlan}","int fa0/11",f"sw acc vlan {voip_vlan}","int ra gi0/1-2", "sw mo tr",""]
print("_____Second Switch:_______")
for i in b:
	print(i)

print("int ra fa0/1-24")
print("sw port mac sticky")
print("sw port voil shutdown")