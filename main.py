len_a = input()
a = set(input().split())

len_b = input()
b = set(input().split())


difference = list(map(int, a.symmetric_difference(b)))

difference.sort()

for i in difference:
    print(i)