def filter_file(file, words):
    words_lower = [x.lower() for x in words.copy()]
    while True:
        line = file.readline()
        data = line.strip().split()
        for word in data:
            if word.lower() in words_lower:
                yield line

        if not line:
            break
