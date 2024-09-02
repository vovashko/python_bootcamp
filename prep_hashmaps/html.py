def tagvalidator(str1):
    if not str1 or '<' not in str1:
        return False

    stack = []
    i = 0
    while i < len(str1):
        if str1[i] == '<' and str1[i + 1] != '/':
            j = i + 1
            while j < len(str1) and str1[j] != '>':
                j += 1
            if j < len(str1):
                tag = str1[i:j + 1] #Performing slicing operation
                if tag[-2] != '/':
                    stack.append(tag)
                i = j
        elif str1[i] == '<' and str1[i + 1] == '/':
            j = i + 2
            while j < len(str1) and str1[j] != '>':
                j += 1
            if j < len(str1):
                end = str1[i:j + 1]
                if not stack or stack[-1][1:] != end[2:]:
                    return False
                stack.pop()
                i = j
        i += 1
    
    return len(stack) == 0

str1 = "<html><body><div></div><h1></h1></body></html>"
print(tagvalidator(str1))