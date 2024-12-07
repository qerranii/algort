import random
import string


def process(N, arr, Q, qq):
    res = []

    for query in qq:
        if query[0] == 1:
            K = query[1]
            result = []
            for row in arr:
                result.append(row[:K])
            res.append("".join(result))

        elif query[0] == 2:
            L, R = query[1], query[2]
            result = []
            for row in arr:
                result.append(row[L - 1:R])
            res.append("".join(result))

    return res


def generate_test(N, sizee, Q):
    arr = []
    for _ in range(N):
        length = random.randint(1, sizee)
        row = ''.join(random.choices(string.ascii_lowercase, k=length))
        arr.append(row)

    qq = []
    for _ in range(Q):
        meeeow = random.choice([1, 2])
        if meeeow == 1:
            K = random.randint(1, sizee)
            qq.append((1, K))
        else:
            L = random.randint(1, sizee)
            R = random.randint(L, sizee)
            qq.append((2, L, R))

    return N, arr, Q, qq


N = random.randint(1, 100)
sizee = random.randint(1, 100)
Q = random.randint(1, 100)

N, arr, Q, qq = generate_test(N, sizee, Q)

print("Тест:")
print(N)
for row in arr:
    print(row)
print(Q)
for query in qq:
    print(" ".join(map(str, query)))

print("\nОтвет:")
resu= process(N, arr, Q, qq)
for res in resu:
    print(res)
