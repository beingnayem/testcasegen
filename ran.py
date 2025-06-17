def liza_chocolates(n, k, m, people):
    given = [0] * n
    l = [p[2] for p in people]
    r = [p[3] for p in people]

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

# Read from input.txt and solve
with open("input.txt", "r") as f:
    n, k, m = map(int, f.readline().split())
    people = [tuple(map(int, f.readline().split())) for _ in range(n)]

result = liza_chocolates(n, k, m, people)

# Write output to output.txt
with open("output.txt", "w") as f:
    f.write(str(result) + "\n")
