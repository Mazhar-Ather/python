# in this program we use break and continue statement
# break mean loop ko chor kr nikal jao
for i in range(12):
    if i==10:
        break
    print(f"5 * {i+1} = {5*(i+1)}")
print("loop se bahir agya")

# continue statement mean k ilteration ko chor KR niKal jao
for i in range(15):
    if i==10:
        continue
    print(f"5 * {i+1} = {5*(i+1)}")
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)