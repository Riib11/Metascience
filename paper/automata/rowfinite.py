import random

N = 20 # cells in state
G = 20 # generations to simulate

# a rule is an 8-array of boolean values

def index_to_rule(i):
    rule = []
    bin_str = bin(i)[2:]
    for j in range(len(bin_str)):
        b = int(bin_str[j])
        rule.append(int(b))
    for j in range(8 - len(bin_str)):
        rule.append(0)
    return rule

rule = index_to_rule(70)

def local_update(a, b, c):
    return rule[sum([
        1 if a else 0,
        2 if b else 0,
        4 if c else 0])]

def update(row):
    row_new = [0] * N
    for i in range(N):
        if i == 0:
            row_new[i] = local_update(False, row[i], row[i+1])
        elif i == N-1:
            row_new[i] = local_update(row[i-1], row[i], False)
        else:
            row_new[i] = local_update(row[i-1], row[i], row[i+1])
    return row_new

def simulate(row):
    history = [row]
    for _ in range(G):
        row = update(row)
        history.append(row)
    return history

def write_history(history):
    with open("rowfinite_output.txt", "w+") as file:
        file.write(str(history)\
            .replace("[", "{")\
            .replace("]", "}"))

def main():
    # row_start = [random.randint(0,1) for _ in range(N)]
    row_start = [0] * N
    row_start[len(row_start)//2] = 1
    history = simulate(row_start)
    write_history(history)

main()
