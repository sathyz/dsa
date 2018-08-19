"""Group kids in a birthday party, such that range(age) in each group is < 1year."""
def grouping_kids(kids, L):
    """
    kids => age of each kid in years (sorted ascending).
    L => range(age) to be satisfied in group (in months).
    """
    # print(kids)
    current_index = 1
    group_start = 0
    n = len(kids)
    num_groups = 0

    while current_index < n:
        distance = int((kids[current_index] - kids[group_start]) * 12)
        if distance > L:
            num_groups += 1
            print(num_groups, kids[group_start: current_index])
            group_start = current_index
        current_index += 1
    if group_start < current_index:
        num_groups += 1
        print(num_groups, kids[group_start:])
    return num_groups


if __name__ == '__main__':
    num_groups = grouping_kids([1.2, 1.5, 1.7, 2.2, 2.5, 3, 3.5, 4.5, 5.6], 12)
    print(num_groups)
