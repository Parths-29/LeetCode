def multiply(num1, num2):
    '''
    Approach:

    1️⃣ Create an array of size n + m.
    2️⃣ Multiply digits from right to left.
    3️⃣ Place result at positions i+j and i+j+1.
    4️⃣ Handle carry.
    5️⃣ Convert array to string and remove leading zeros.
    '''

    if num1 == "0" or num2 == "0":
        return "0"

    n, m = len(num1), len(num2)
    result = [0] * (n + m)

    # Multiply from right to left
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])

            # Positions in result array
            p1 = i + j
            p2 = i + j + 1

            total = mul + result[p2]

            result[p2] = total % 10
            result[p1] += total // 10

    # Convert to string
    result_str = ''.join(map(str, result)).lstrip('0')

    return result_str


# ====== INPUT / OUTPUT ======
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
print("Product:", multiply(num1, num2))
