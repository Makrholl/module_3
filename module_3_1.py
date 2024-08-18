calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(data):
    i = []
    i.append(len(data))
    i.append(data.upper())
    i.append(data.lower())
    count_calls()
    return i


def is_contains(s, l):
    s = s.lower()
    for item in l:
        if s == item.lower():
            count_calls()
            return True
    count_calls()
    return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)




