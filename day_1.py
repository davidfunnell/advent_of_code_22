# https://adventofcode.com/2022/day/1


def day_1():
    l = []
    elfs = []
    elf = []
    max_cal_list = []

    for line in open("day_1_data.txt", "r"):
        l.append(line[:-1])

    for line in l:
        if line == "":
            elfs.append(elf)
            elf = []
        else:
            elf.append(line)
    elfs.append(elf)
    print(elfs)

    for t in elfs:
        elf_cal = 0
        for items in t:
            elf_cal += int(items)
        max_cal_list.append(elf_cal)

    max_cal_list.sort(reverse=True)

    # return sum(max_cal_list[0:3])
    return max_cal_list[0]

print(day_1())
