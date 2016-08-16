from __future__ import division

test1 = {
    'left_x': 3,
    'bottom_y': 4,
    'width': 8,
    'height': 4,
}
test2 = {
    'left_x': 8,
    'bottom_y': 5,
    'width': 5,
    'height': 7,
}
test3 = {
    'left_x': 8,
    'bottom_y': 5,
    'width': 4,
    'height': 7,
}

def find_intersection(r1, r2):
    compatability = 0
    left_most = sorted([r1, r2], key = lambda k: k['left_x'])
    overlap = {
        'left_x': None,
        'bottom_y': None,
        'width': None,
        'height': None,
    }
    overlap['left_x'], overlap['width'] = check_overlap(r1, r2, 'left_x', 'width')
    overlap['bottom_y'], overlap['height'] = check_overlap(r1, r2, 'bottom_y','height')

    if overlap['left_x'] is not None and overlap['bottom_y'] is not None:
        compatability = int((overlap['width'] * overlap['height']) / (((r1['width'] * r1['height']) + (r2['width'] * r2['height'])) / 2) * 100)

    return compatability

def check_overlap(obj1, obj2, low_bound_key, distance_key):
    highest_low = max(obj1[low_bound_key], obj2[low_bound_key])
    lowest_high = min(obj1[low_bound_key] + obj1[distance_key], obj2[low_bound_key] + obj2[distance_key])

    return (highest_low, lowest_high - highest_low) if highest_low < lowest_high else (None, None)


print find_intersection(test1, test2)
print find_intersection(test2, test3)
# print find_intersection(test3)
