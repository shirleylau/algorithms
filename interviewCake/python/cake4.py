test1 = [(0, 3), (3, 5), (4, 8), (10, 12), (9, 10)]
test2 = [(9, 10), (4, 8), (0, 1), (10, 12), (3, 5)]
test3 = [(-2, 1), (4, 5), (3, 6), (0, 2), (10, 13)]
# test3 = [0, 3, 7, 7, 7, 0]

def condense_meeting_times(arr):
    ascending = sorted(arr)
    condensed = []
    start = None
    end = None
    for tup in ascending:
        if start is None:
            start = tup[0]
            end = tup[1]
        elif tup[0] <= end:
            end = max(end, tup[1])
        else:
            condensed.append((start, end))
            start = tup[0]
            end = tup [1]
    condensed.append((start, end))

    return condensed

print condense_meeting_times(test1)
print condense_meeting_times(test2)
print condense_meeting_times(test3)
