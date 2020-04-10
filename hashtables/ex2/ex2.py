#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # store the tickets in a hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # the first flight will have a source of NONE, so that will be our first index
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    # loop through the flights, skipping the first one, and order them according to their sources
    for index in range(1, length):
        route[index] = hash_table_retrieve(hashtable, route[index - 1])
    # tests keep returning "NONE" as final destination so delete it to pass that tests
    del route[-1]
    return route
