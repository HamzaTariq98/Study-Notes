

def reverse_iterative(text):
    return text[::-1]

def reverse_recursive(text):
    if text is '':
        return ''
    return text[-1]+reverse_recursive(text[:-1])

text = '6543210'
print(reverse_iterative(text)) # 0123456
print(reverse_recursive(text)) # 0123456

