# https://adventofcode.com/2022/day/2

def day_2():
    data = []
    score = 0

# 1=rock, 2= paper, 3=scissor, 0 loose, 3 tie, 6 win

    translation = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }

    for line in open("day_2_data.txt", "r"):
        data.append(line[:-1])

    for line in data:
        print(line)
        score += translation[line]

    # Part 1
    # for line in data:
    #     if line[2] == "X":
    #         score += 1
    #     elif line[2] == "Y":
    #         score += 2
    #     elif line[2] == "Z":
    #         score += 3
    #     value =  ord(line[2]) - ord(line[0]) - 23
    #     if value == "0":
    #         score += 3
    #     elif value == 1 or value == -2:
    #         score += 6

    return score

print(day_2())
