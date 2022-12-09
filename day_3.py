# https://adventofcode.com/2022/day/3

def day_3():
    data = []
    alpha = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = 0

    for line in open("day_3_data.txt", "r"):
        data.append(line[:-1])

# Part 1
    # for rucksack in data:
    #     half = int(len(rucksack)/2)
    #     pocket1 = rucksack[0:half]
    #     pocket2 = rucksack[half:]
    #     for char in pocket1:
    #         if char in pocket2:
    #             score += alpha.index(char)
    #             break

# Part 2
    for index in range(0, len(data), 3):
        for char in data[index]:
            if char in data[index+1] and char in data[index+2]:
                score += alpha.index(char)
                break

    return score

print(day_3())
