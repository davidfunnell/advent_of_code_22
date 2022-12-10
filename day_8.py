#https://adventofcode.com/2022/day/8

def day_8():
    data = []
    result = 0
    scores = []
    myset = set()

    for line in open("day_8_data.txt", "r"):
        value = [int(char) for char in line[:-1]]
        data.append(value)

# Part 1
# # east
#     for row in range(len(data)):
#         height = -1
#         for col in range(0,len(data[0])):
#             if data[row][col] > height:
#                 print(data[row][col])
#                 myset.add(f'{row}.{col}')
#                 height = data[row][col]
# # west
#     for row in range(len(data)):
#         height = -1
#         for col in range(len(data[0])-1,-1,-1):
#             if data[row][col] > height:
#                 myset.add(f'{row}.{col}')
#                 height = data[row][col]
# # north
#     for col in range(len(data[0])):
#         height = -1
#         for row in range(len(data)):
#             if data[row][col] > height:
#                 myset.add(f'{row}.{col}')
#                 height = data[row][col]
# # south
#     for col in range(len(data[0])):
#         height = -1
#         for row in range(len(data)-1,-1,-1):
#             if data[row][col] > height:
#                 print(data[row][col], row, col)
#                 myset.add(f'{row}.{col}')
#                 height = data[row][col]
#     print(len(myset))


#Part 2
    for row in range(len(data)):
        for col in range(0,len(data[0])):
            height = data[row][col]

            # right
            right_score = 0
            for right in range(col+1,len(data[0])):
                right_score += 1
                if data[row][right] >= height:
                    break
            # left
            left_score = 0
            for left in range(col-1,-1,-1):
                left_score += 1
                if data[row][left] >= height:
                    break
            # up
            up_score = 0
            for up in range(row-1,-1,-1):
                up_score += 1
                if data[up][col] >= height:
                    break
            # down
            down_score = 0
            for down in range(row+1,len(data)):
                down_score += 1
                if data[down][col] >= height:
                    break

            scores.append(right_score*left_score*up_score*down_score)

    return max(scores)

print(day_8())
