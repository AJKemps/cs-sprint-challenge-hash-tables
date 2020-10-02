def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    counts = {}

    for num in a:
        if abs(num) in counts:
            counts[abs(num)] += 1
        if abs(num) not in counts:
            counts[abs(num)] = 1

    result = []

    for k, v in counts.items():
        if v > 1:
            result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
