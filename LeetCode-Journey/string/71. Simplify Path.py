def simplifyPath(path):
    '''
    Approach:

    1️⃣ Split the path by '/'.
    2️⃣ Use a stack to process directories.
    3️⃣ If part is:
         - "" or "." → ignore
         - ".." → pop from stack if possible
         - otherwise → push to stack
    4️⃣ Join stack with '/' and prefix with '/'.
    '''

    stack = []
    parts = path.split('/')

    for part in parts:
        if part == "" or part == ".":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)


# ====== INPUT / OUTPUT ======
path = input("Enter absolute path: ")
print("Simplified path:", simplifyPath(path))
