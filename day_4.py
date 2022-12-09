#https://adventofcode.com/2022/day/4

def day_4():
    data = []
    pairs_list = []

    result = 0

    for line in open("day_4_data.txt", "r"):
        data.append(line[:-1])

    for pair in data:
        individual = pair.split(",")
        for l in individual:
            low_high = l.split("-")
            pairs_list.append(low_high)

    length = int(len(pairs_list))

# part 1
    # for index in range(0, length, 2):
    #     if int(pairs_list[index][0]) <= int(pairs_list[index+1][0]) and int(pairs_list[index][1]) >= int(pairs_list[index+1][1]):
    #         result += 1
    #     elif int(pairs_list[index][0]) >= int(pairs_list[index+1][0]) and int(pairs_list[index][1]) <= int(pairs_list[index+1][1]):
    #         result += 1

    for index in range(0, length, 2):
        if int(pairs_list[index][1]) < int(pairs_list[index+1][0]) or int(pairs_list[index][0]) > int(pairs_list[index+1][1]):
            pass
        else:
            result += 1


    return result

print(day_4())
