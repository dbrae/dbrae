randomList = ['apples', 'bananas', 'oranges', 'grapes', 'pears']

def format_list(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    else:
        return ", ".join(items[:-1]) + " and " + items[-1]

formatted_string = format_list(randomList)
print(formatted_string)
