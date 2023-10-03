s0='aAbBaAb'
for i in range(9):
    s0=s0.replace('A','121')
    s0=s0.replace('B','AbA')
    s0=s0.replace('121','BaB')
print(s0[1027])