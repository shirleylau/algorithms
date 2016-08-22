test1 = [[1, 2], 2]
test2 = [[3, 2, 1], 4]
test3 = [[3, 5, 2], 7]

def count_solutions(addends, total):
    solutions = 0
    viable_addends = addends
    for addend in addends:
        multiplier = int(total / addend)
        viable_addends = viable_addends[1:]
        while multiplier > 0:
            remainder = total - (addend * multiplier)
            if not remainder:
                solutions += 1
            else:
                new_viable_addends = [x for x in viable_addends if x <= remainder]
                if len(new_viable_addends) > 0:
                    solutions += count_solutions(new_viable_addends, remainder)
            multiplier -= 1

    return solutions

print count_solutions(test2[0], test2[1])
# print count_solutions(test2[0], test2[1])
# print count_solutions(test3[0], test3[1])
