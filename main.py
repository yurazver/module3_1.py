calls = 0
def count_calls():
    global calls
    calls = 4
    print(calls)

def string_info(string):
    return  len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    string = string.lower()
    is_cont = False
    j = len(list_to_search)
    i = 0
    while i in range(j):
        list_to_search[i] = list_to_search[i].lower()
        if list_to_search[i] == string:
            is_cont = True
            i += 1
            break
        else:
            is_cont = False
            i += 1
            continue
    return is_cont




print(string_info("Capybara"))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
count_calls()
