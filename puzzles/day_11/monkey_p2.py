monkey0 = [72, 64, 51, 57, 93, 97, 68]
monkey1 = [62]
monkey2 = [57, 94, 69, 79, 72]
monkey3 = [80, 64, 92, 93, 64, 56]
monkey4 = [70, 88, 95, 99, 78, 72, 65, 94]
monkey5 = [57, 95, 81, 61]
monkey6 = [79, 99]
monkey7 = [68, 98, 62]

inspections = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10000):
    for item in monkey0:
        inspections[0] += 1
        new_item = (item * 19)%9699690
        if new_item % 17 == 0:
            monkey4.append(new_item)
        else:
            monkey7.append(new_item)
    monkey0 = []

    for item in monkey1:
        inspections[1] += 1
        new_item = (item * 11)%9699690
        if new_item % 3 == 0:
            monkey3.append(new_item)
        else:
            monkey2.append(new_item)
    monkey1 = []

    for item in monkey2:
        inspections[2] += 1
        new_item = (item + 6)%9699690
        if new_item % 19 == 0:
            monkey0.append(new_item)
        else:
            monkey4.append(new_item)
    monkey2 = []

    for item in monkey3:
        inspections[3] += 1
        new_item = (item + 5)%9699690
        if new_item % 7 == 0:
            monkey2.append(new_item)
        else:
            monkey0.append(new_item)
    monkey3 = []

    for item in monkey4:
        inspections[4] += 1
        new_item = (item + 7)%9699690
        if new_item % 2 == 0:
            monkey7.append(new_item)
        else:
            monkey5.append(new_item)
    monkey4 = []

    for item in monkey5:
        inspections[5] += 1
        new_item = (item * item)%9699690
        if new_item % 5 == 0:
            monkey1.append(new_item)
        else:
            monkey6.append(new_item)
    monkey5 = []

    for item in monkey6:
        inspections[6] += 1
        new_item = (item + 2)%9699690
        if new_item % 11 == 0:
            monkey3.append(new_item)
        else:
            monkey1.append(new_item)
    monkey6 = []

    for item in monkey7:
        inspections[7] += 1
        new_item = (item + 3)%9699690
        if new_item % 13 == 0:
            monkey5.append(new_item)
        else:
            monkey6.append(new_item)
    monkey7 = []

print(inspections)
inspections = sorted(inspections)
print(inspections[-1] * inspections[-2])