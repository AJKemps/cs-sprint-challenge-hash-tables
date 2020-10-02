def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    store = {}

    for i in range(len(weights)):
        if weights[i] not in store:
            store[weights[i]] = i

    for k, v in store.items():

    return None
