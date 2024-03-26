import math
import time
start = time.time()
q = 332900
b = 2 ** 5
for i in range(q):
    for j in range(b):
        m0 = round(2/q * (j * q / 32) - 2/q * 0 * i) % 2
        m1 = round(2/q * (j * q / 32) - 2/q * 1 * i) % 2
        m2 = round(2/q * (j * q / 32) - 2/q * 2 * i) % 2
        m_1 = round(2/q * (j * q / 32) - 2/q * -1 * i) % 2
        m_2 = round(2/q * (j * q / 32) - 2/q * -2 * i) % 2
        if m0 == 0 and m2 == 0 and m_2 == 0 and m1 == 1 and m_1 == 1:
            print(i, j)
            end = time.time()
            cost = end - start
            print("average: {}".format(cost))
            exit(0)
        if m0 == 1 and m2 == 1 and m_2 == 1 and m1 == 0 and m_1 == 0:
            print(i, j)
            end = time.time()
            cost = end - start
            print("average: {}".format(cost))
            exit(0)
