import re
def averages(threshold=0.05):
    filename = "C:\\Users\\Robert\\Desktop\\guesses.txt"
    AVG_TRESH = threshold
    rex = re.compile(r"[\d\,]{3,5}")
    xago = re.compile(r"\d\d?[dhs] ago")
    numbers = []
    pages = 1
    line_i = 0
    line_last = 0
    total = 0
    total_100 = 0
    for line in open(filename):
        r = rex.search(line)
        if r:
            n = re.sub(",", "", r.group())
            n = int(n)
            numbers.append(n)
            total += n
            avg = total / len(numbers)
            if n > avg - (avg * AVG_TRESH) and n < avg + (avg * AVG_TRESH):
                print("*** close ***", line.strip(), " avg:", avg, " line:", line_i)
            total_100 += n
            if len(numbers) % 100 == 0:
                print("i:", len(numbers), " avg:", avg, " avg 100:", total_100 / 100)
                total_100 = 0
        if len(line.strip()) == 0:
            pages += 1
            line_last = line_i
        elif line_last == line_i-1:
            if xago.search(line):
                print("line: ", line_i, " missing top page:", pages)
        line_i += 1
    print("pages:", pages)
    
    print("avg:", (sum(numbers) / len(numbers)), " of:", len(numbers))
    return numbers

