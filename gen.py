import os, random, string
from sol import Solution

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)


def generate_input(n):
    numList = []
    for i in range(n):
        temp = random.randint(1, 1000000)
        numList.append(str(temp))
    return " ".join(numList)


def generate_output(n, days):
    n = int(n)
    days = list(map(int, days.split()))
    return Solution.solve(n, days)

random.seed()

for tc in range(1, 16):
    input_path = f"input/in{tc}.txt"
    output_path = f"output/out{tc}.txt"

    n = random.randint(2, 1000)

    with open(input_path, 'w') as infile, open(output_path, 'w') as outfile:
        infile.write(str(n) + "\n")
        inp = generate_input(n)
        infile.write(inp + "\n")
        output_line = generate_output(n, inp)
        outfile.write(output_line + "\n")
        
