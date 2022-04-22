from AVLTreeList import AVLTreeList
import random
import math

for i in range(1,11):
    n = 1000 * i
    print("n = " + str(n) + " i = " + str(i))
    lst1 = AVLTreeList()

    sum_of_balances = 0
    sum_of_depth = 0

    for j in range(n):
        num_of_rebalances, depth = lst1.insert(0,"a")
        sum_of_balances += num_of_rebalances
        sum_of_depth += depth

    avg_balance = sum_of_balances/n
    avg_depth = sum_of_depth/n

    print("insert in the begining: the average num of balances is " + str(avg_balance) + " the average depth is " + str(avg_depth) )

    lst3 = AVLTreeList()

    sum_of_balances3 = 0
    sum_of_depth3 = 0

    num_of_circles = int(math.log(n, 2))

    for circle in range(num_of_circles):
        for index in range(0, 2 ** (circle + 1), 2):
            num_of_balances3, depth3 = lst3.insert(index, "a")
            sum_of_balances3 += num_of_balances3
            sum_of_depth3 += depth3

            avg_balance3 = sum_of_balances3 / n
            avg_depth3 = sum_of_depth3 / n

    print("insert in balanced order: the average num of balances is " + str(
        avg_balance3) + " the average depth is " + str(avg_depth3))

    lst2 = AVLTreeList()

    sum_of_balances2 = 0
    sum_of_depth2 = 0

    # Insert n items in random order
    for curr_size in range(n):
        random_index = random.randint(0, curr_size)

        num_of_rebalances2, depth2 = lst2.insert(random_index, "a")
        sum_of_balances2 += num_of_rebalances2
        sum_of_depth2 += depth2

    avg_balance2 = sum_of_balances2 / n
    avg_depth2 = sum_of_depth2 / n

    print("insert in random index: the average num of balances is " + str(avg_balance2) + " the average depth is " + str(avg_depth2))



