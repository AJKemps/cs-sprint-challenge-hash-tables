# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    chopped = {}

    for i in range(len(files)):
        folders = files[i].split('/')
        if folders[-1] in chopped:
            chopped[folders[-1]] = [*chopped[folders[-1]], i]
        if folders[-1] not in chopped:
            chopped[folders[-1]] = [i]

    results = []

    for query in queries:
        if query in chopped:
            for i in range(len(chopped[query])):
                print(chopped[query])
                results.append(files[chopped[query][i]])

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
