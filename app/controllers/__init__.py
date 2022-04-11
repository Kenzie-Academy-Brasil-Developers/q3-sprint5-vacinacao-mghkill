def change_data(data):

    key = data.keys()
    value = data.values()

    key = list(key)[0:4]
    value = list(value)[0:4]

    data = dict(zip(key, value))

    return data