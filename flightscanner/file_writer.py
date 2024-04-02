def write_to_file(filename, contents):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(contents)
