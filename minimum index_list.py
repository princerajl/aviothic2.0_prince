list=eval(input("[enter number]"))
print(list)
mine=list[0]
mini=0
length=len(list)
for i in range(length):
    if list[i]<mine:
        mine =list[i]
        mini=i
print(f"minimum value: {mine}, index: {mini}")              