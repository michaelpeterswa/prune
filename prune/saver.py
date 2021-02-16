def save(output, outfile):
    with open(outfile, "w") as f:
        for line in output:
            f.write(line + "\n")