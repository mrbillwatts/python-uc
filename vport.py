'''for i in range(72):
    print(f"dial-peer voice 3{i:02} pots")
    print("service stcapp")
    print(f"port 3/0/{i}")
    print("shutdown")

for i in range(73,145,1):
    print(f"no dial-peer voice {i}")

for i in range(56,72,1):
    print(f"dial-peer voice 99930{i} pots")
    print("shutdown")
'''
for i in range(56,72,1):
    with open("dpshut.txt","a") as file:
        file.write(f"dial-peer voice 99930{i} pots\n")
        file.write("shutdown\n")
    
