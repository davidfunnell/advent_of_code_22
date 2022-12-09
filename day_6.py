#https://adventofcode.com/2022/day/4

def day_6():
    data = []
    containers = [[],[],[],[],[],[],[],[],[],[]]
    result = 0

    for line in open("day_6_data.txt", "r"):
        string = line

# PART 1
#     for i in range(0,len(string)-4):
#         set_of_4 = {string[i], string[i+1], string[i+2], string[i+3]}
#         if len(set_of_4) == 4:
#             return i+4

    for i in range(0,len(string)-14):
        set_of_4 = {string[i], string[i+1], string[i+2], string[i+3], string[i+4], string[i+5], string[i+6], string[i+7], string[i+8], string[i+9], string[i+10], string[i+11], string[i+12], string[i+13]}
        if len(set_of_4) == 14:
            return i+14

print(day_6())
