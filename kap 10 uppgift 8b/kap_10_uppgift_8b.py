tal1=1
tal2=1
tal=1
for a in range(20):
    print(tal, ":", tal1, ":", tal2/tal1)
    tal+=1
    print(tal, ":", tal2, ":", tal2/tal1)
    tal+=1
    tal1+=tal2
    tal2+=tal1
