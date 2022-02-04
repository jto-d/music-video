li = [1,2,3,4,5,6,7,2,4,9,10]
signal = False
for index in range(len(li)):
    if index == 2:
        li.remove(index)
        index -= 1
        if signal:
            signal = False
        else:
            signal = True
    elif signal:
        li.remove(index)
        index -= 1

print(li)

