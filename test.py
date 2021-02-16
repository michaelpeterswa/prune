import prune

infile = prune.load("example.py")
runes_from_py = prune.prune(infile)
prune.save(runes_from_py, "example.prune")

infile = prune.load("example.prune")
py_from_runes = prune.deprune(infile)
prune.save(py_from_runes, "example_deprune.py")

prune.execute("example_deprune.py")