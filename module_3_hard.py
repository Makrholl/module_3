def cal(data):
    sum = 0

    if isinstance(data, int):
        sum += data
    elif isinstance(data, str):
        sum += len(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            sum += cal(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            sum += cal(key)
            sum += cal(value)

    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = cal(data_structure)
print(result)

