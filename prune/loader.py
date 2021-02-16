def load(filename):
    full_file = []
    with open(filename, "r") as f:
        for line in f:
            full_file.append(line.rstrip("\n"))

    return full_file
