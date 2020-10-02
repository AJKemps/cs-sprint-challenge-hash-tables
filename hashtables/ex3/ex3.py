def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    num_arr = len(arrays)

    common = {}

    for arr in arrays:
        for num in arr:
            if num not in common:
                common[num] = 1
            if num in common:
                common[num] += 1

    result = []

    for k, v in common.items():
        if v > 2:
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
