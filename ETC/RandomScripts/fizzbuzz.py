limit = 100

for i in range(1,limit):
    d = {
    3:"fizz",
    5:"buzz",
    }
    string = ""
    for key in d:
        if i % key == 0:
            string += d[key]

    if string == "":
        string += str(i)
    print(string)