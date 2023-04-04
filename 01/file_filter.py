def filter_file(file, words):
    fopen_flag = False

    if isinstance(file, str):
        file = open(file, "r")
        fopen_flag = True

    words_lower = [x.lower() for x in words]
    while True:
        line = file.readline()
        if not line:
            break
        data = line.strip().split()
        for word in data:
            if word.lower() in words_lower:
                yield line
                break

    if fopen_flag:
        file.close()
