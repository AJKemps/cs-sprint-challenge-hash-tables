#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    tix = {}

    for ticket in tickets:
        if ticket not in tix:
            tix[ticket.source] = ticket.destination

    routes = []

    count = 0
    finished = False

    while not finished:
        for k, v in tix.items():
            print(k, v, count)
            if count < 1:
                if k == 'NONE':
                    routes.append(v)
                    count += 1
            if count > 0:
                if routes[count-1] == k:
                    routes.append(v)
                    count += 1
                if routes[count-1] == 'NONE':
                    finished = True

    return routes
