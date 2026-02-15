def addBinary(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    carry = 0
    result = []

    # Sum using XOR logic
    def sum_bit(x, y, c):
        return (x ^ y) ^ c

    # Carry using AND/OR logic
    def carry_bit(x, y, c):
        return (x & y) | ((x ^ y) & c)

    for i in range(max_len):
        # Get bits from right side
        bit_a = int(a[-1 - i]) if i < len(a) else 0
        bit_b = int(b[-1 - i]) if i < len(b) else 0

        # Append sum bit
        result.append(str(sum_bit(bit_a, bit_b, carry)))

        # Update carry
        carry = carry_bit(bit_a, bit_b, carry)

    # If carry remains, append it
    if carry:
        result.append("1")

    # Reverse because we built from LSB to MSB
    return "".join(reversed(result))


# ====== INPUT / OUTPUT ======
a = input("Enter binary string a: ")
b = input("Enter binary string b: ")

print("Binary sum:", addBinary(a, b))
