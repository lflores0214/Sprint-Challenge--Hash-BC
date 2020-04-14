#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # iterate through the list
    for i in range(length):
        # find the difference between the limit and each weight
        difference = limit - weights[i]

        # grab the weights that hit the limit
        target = hash_table_retrieve(ht, difference)

        # check the hashtable for None then insert the key: value pair
        if target is None:
            hash_table_insert(ht, weights[i], i)
        else:
                return(i, target)
        # hash_table_insert(ht, weights[i], i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
