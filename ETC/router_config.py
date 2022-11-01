vlans = [111,112,121,122,211,212,221,222,150,170,180,250,270,280,300,400]
virtual_ips = ["0.1","0.65","0.129","0.193","1.1","1.65","1.129","1.193","2.17","2.33","2.49","2.65","2.81","2.97","2.1","2.113"]
int1_ips = ["0.2","0.66","0.130","0.194","1.2","1.66","1.130","1.194","2.18","2.34","2.50","2.66","2.82","2.98","2.2","2.114"]
int2_ips = ["0.3","0.67","0.131","0.195","1.3","1.67","1.131","1.195","2.19","2.35","2.51","2.67","2.83","2.99","2.3","2.115"]

snm = ["192","192","192","192","192","192","192","192","240","240","240","240","240","240","240","248"]

print("________Router1 CONFIG__________")
print("en")
print("conf t")
print("int gi0/0")
print("no sh")
for i,(vlan,ip) in enumerate(zip(vlans,virtual_ips)): 
	a = f"int gi0/0.{vlan}"
	b = f"en do {vlan}"
	c = f"ip add 172.17.{int1_ips[i]} 255.255.255.{snm[i]}"
	c1 = f"standby {vlan} ip 172.17.{ip}"
	c2 = f"standby {vlan} priority 250"
	c3 = f"standby {vlan} preempt"
	d = "ip helper-address 172.17.2.116"
	e = "no sh"
	print(a)
	print(b)
	print(c)
	print(c1)
	print(c2)
	print(c3)
	print(d)
	print(e)

print("________Router2 CONFIG__________")
print("en")
print("conf t")
print("int gi0/0")
print("no sh")
for i,(vlan,ip) in enumerate(zip(vlans,virtual_ips)): 
	a = f"int gi0/0.{vlan}"
	b = f"en do {vlan}"
	c = f"ip add 172.17.{int2_ips[i]} 255.255.255.{snm[i]}"
	c1 = f"standby {vlan} ip 172.17.{ip}"
	d = "ip helper-address 172.17.2.116"
	e = "no sh"
	print(a)
	print(b)
	print(c)
	print(c1)
	print(d)
	print(e)