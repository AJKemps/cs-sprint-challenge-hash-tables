def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    store = {}

    for i in range(len(weights)):
        if weights[i] in store:
            store[weights[i]] = [*store[weights[i]], i]
        if weights[i] not in store:
            store[weights[i]] = [i]

    print(store)
    results = []

    for k, v in store.items():
        if limit - k in store:
            for i in range(len(store[limit-k])):
                results.append(v[i])

    results.sort(reverse=True)

    if results == []:
        results = None

    print(results)
    return results
