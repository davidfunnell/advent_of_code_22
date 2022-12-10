#https://adventofcode.com/2022/day/5

def day_5():
    data = []
    containers = [[],[],[],[],[],[],[],[],[],[]]
    result = 0

    for line in open("day_5_data.txt", "r"):
        data.append(line[:-1])

    for row in range(0,8):
        counter = 1
        for i in range(1,10):
            if len(data[row]) >=counter and data[row][counter].isalpha():
                containers[i].append(data[row][counter])
            counter += 4

    for row in range(10,len(data)):
        instructions = data[row].split(" ")
        containers[0].append(instructions[1::2])

# Part 1
    # for li in containers[0]:
    #     for moves in range(0,int(li[0])):
    #         f = containers[int(li[1])]
    #         t = containers[int(li[2])]
    #         value = containers[int(li[1])].pop(0)
    #         containers[int(li[2])].insert(0,value)

# Part 2
    for li in containers[0]:
        l = []
        for moves in range(0,int(li[0])):
            f = containers[int(li[1])]
            t = containers[int(li[2])]
            value = containers[int(li[1])].pop(0)
            l.append(value)
        containers[int(li[2])] = l + containers[int(li[2])]

    result = ""
    for index in range(1,10):
        result += containers[int(index)][0]
    return result

print(day_5())
