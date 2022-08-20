"""
Automorphic Number: A number that its powers end with itself
E.G., 376 ** 2 == 141,376
"""
def get_num_of_zeros(num, pow):
    nums = str(num)
    i = len(nums) - (pow + 1)
    zeros = 0
    while nums[i] == "0" and i >= 0:
        zeros += 1
        i -= 1
    return zeros


def kth_automorphic_number(k):
    if k == 1:
        print(0)
    elif k == 2:
        print(1)
    elif k == 3:
        print(5)
    elif k == 4:
        print(6)
    else:
        li =[[0], [1, 5, 6]]
        for i in range(50):
            li.append([])
        found = 4
        pow = 1
        result_ready = False
        while not result_ready:
            ten_pow = 10 ** pow
            ten_pow_next = 10 ** (pow + 1)
            curr = []
            for i in range(1, 10):
                for elem in li[pow]:
                    num = i * ten_pow + elem
                    if (num ** 2) % ten_pow_next == num:
                        num_of_zeros = get_num_of_zeros(num**2, pow + 1)
                        if num_of_zeros > 0:
                            for j in range(1, num_of_zeros + 1):
                                li[pow + 1 + j].append(num)
                        curr.append(num)
                        found += 1
                        if found == k:
                            print(num)
                            result_ready = True
                            break
                if result_ready:
                    break
            pow += 1
            li[pow].extend(curr)


if __name__ == "__main__":
    k = int(input())
    kth_automorphic_number(k)

