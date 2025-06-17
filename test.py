def liza(n, k, m, people):
    given = [0] * n

    l = [person[2] for person in people]
    r = [person[3] for person in people]

    day = 1
    max_day = max(r)

    while day <= max_day:
        eligible = []
        for i in range(n):
            if l[i] <= day <= r[i] and given[i] < people[i][1]:
                eligible.append((people[i][0], i))

        eligible.sort()

        selected = []
        last_height = -1
        for height, idx in eligible:
            if len(selected) == k:
                break
            if height > last_height:
                selected.append(idx)
                last_height = height

        for idx in selected:
            given[idx] += m
            if given[idx] > people[idx][1]:
                given[idx] = people[idx][1]

        if all(given[i] >= people[i][1] for i in range(n)):
            return day

        for i in range(n):
            if day > r[i] and given[i] < people[i][1]:
                return -1

        day += 1

    return -1

n, k, m = map(int, input().split())
people = []
for _ in range(n):
    a, b, l, r = map(int, input().split())
    people.append((a, b, l, r))
print(liza(n, k, m, people))
