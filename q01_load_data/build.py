

path = 'data/episource.txt'


def q01_load_data(path):
    "write your solution here"
    file = open(path, 'r')
    data = file.read()

    return data, len(data.split(" "))

