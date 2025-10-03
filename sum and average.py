L = [4, 5, 6, 7, 9, 1, 3, 2, 8, 10]
print("original list:", L)
count = 0
for i in L:
    count += i
avg = count/len(L)
print("ssssssssum:", count)
print("average:", avg)
L.sort()
print("sssssssssssmallesssssssssst element issssss:", L[0])
print("largessst element issss:", L[-1])