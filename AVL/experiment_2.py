from AVLTreeList import AVLTreeList
import random

for i in range(1,11):
    n = 1000 * 2**i
    print("n = " + str(n))
    lst1 = AVLTreeList()
    lst2 = AVLTreeList()

    # Insert n items in random order
    for curr_size in range(n):
        random_index = random.randint(0, curr_size)

        lst1.insert(random_index, "a")
        lst2.insert(random_index, "a")

    # Split by random index
    random_index = random.randint(0, n-1)
    join_costs = lst1.split(random_index)[1]

    average = sum(join_costs) / len(join_costs)
    maximum = max(join_costs)

    print("for random index avarage cost = " + str(average) + " and the maximum cost = " + str(maximum))

    # Split by maximum from left tree index
    max_from_left_tree = lst2.getRoot().getLeft().getSize() - 1;
    join_costs = lst2.split(max_from_left_tree)[1]

    average2 = sum(join_costs) / len(join_costs)
    maximum2 = max(join_costs)

    print("for maximum from left tree index avarage cost = " + str(average2) + " and the maximum cost = " + str(maximum2))

