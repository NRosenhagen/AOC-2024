def parse_input(data):
    with open(data) as f:
        cols=[[int(y) for y in x.split("   ")] for  x in f.read().split('\n')]
        left_col=[]
        right_col=[]
        for col in cols:
            left_col.append(col[0])
            right_col.append(col[1])

        left_col.sort()
        right_col.sort()
        return left_col,right_col
    
def solution_part_1(data):
    left_col,right_col=parse_input(data)
    sub_list = [abs(y-x) for x,y in zip(left_col,right_col)]

    return sum(sub_list)

def solution_part_2(data):
    left_col,right_col=parse_input(data)
    total = 0

    for vals in left_col:
        total+=vals*right_col.count(vals)
    return total

print(solution_part_1('Day_1_input.txt'))
print(solution_part_2('Day_1_input.txt'))
