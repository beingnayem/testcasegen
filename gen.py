import random
import os

# Config
TEST_CASES = 15
MAX_N = 100    # Reduce for better control
MAX_K = 20
MAX_M = 100
MAX_HEIGHT = 10**4
MAX_DAYS = 50  # Keep short but flexible

# Output folder
os.makedirs("liza_test_cases", exist_ok=True)

# Smart Serve Logic
def serve_liza(n, k, m, people):
    day = 1
    max_day = max(r for _, _, l, r in people)

    while day <= max_day:
        today = []
        for i in range(n):
            h, b, l, r = people[i]
            if l <= day <= r and b > 0:
                today.append((h, i))

        today.sort()
        served = 0
        last_height = -1
        for h, i in today:
            if served == k:
                break
            if people[i][1] > 0 and h > last_height:
                give = min(m, people[i][1])
                people[i][1] -= give
                served += 1
                last_height = h

        if all(b == 0 for _, b, _, _ in people):
            return day
        day += 1

    return -1

# Generate Test Case
def generate_test_case(idx):
    n = random.randint(5, MAX_N)
    k = random.randint(2, MAX_K)
    m = random.randint(1, MAX_M)

    people = []
    for _ in range(n):
        h = random.randint(1, MAX_HEIGHT)
        l = random.randint(1, MAX_DAYS - 10)
        r = random.randint(l + 2, l + 10)  # Ensure decent serving window
        max_possible_days = r - l + 1
        b = random.randint(1, max_possible_days * m)
        people.append([h, b, l, r])

    # Write input
    with open(f"liza_test_cases/input{idx}.txt", "w") as f:
        f.write(f"{n} {k} {m}\n")
        for person in people:
            f.write(" ".join(map(str, person)) + "\n")

    # Write output
    res = serve_liza(n, k, m, [p.copy() for p in people])
    with open(f"liza_test_cases/output{idx}.txt", "w") as f:
        f.write(str(res) + "\n")

# Generate 10 test cases
for i in range(1, TEST_CASES + 1):
    generate_test_case(i)
