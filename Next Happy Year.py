year = int(input())
year += 1
while True:
    y = str(year)
    if (y[0] not in y[1:] and
        y[1] not in y[2:] and
        y[2] != y[3] and
        y[0] != y[2] and
        y[0] != y[3] and
        y[1] != y[3]):
        print(f"{year}")
        break
    year += 1

