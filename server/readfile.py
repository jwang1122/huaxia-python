def filereader(filename):
    with open(filename) as f:
        text = f.read()
    return text

content = filereader("./src/assets/grade1-3.html")
print(content)