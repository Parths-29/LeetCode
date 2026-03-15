'''
Question: 1622. Fancy Sequence (Hard)
Write an API that generates fancy sequences using the append, addAll, and multAll operations.
Implement the Fancy class:
- Fancy() Initializes the object with an empty sequence.
- void append(val) Appends an integer val to the end of the sequence.
- void addAll(inc) Increments all existing values in the sequence by an integer inc.
- void multAll(m) Multiplies all existing values in the sequence by an integer m.
- int getIndex(idx) Gets the current value at index idx (0-indexed), modulo 10^9 + 7. If the index is greater or equal than the length of the sequence, return -1.

---
My Approach (Linear Transformation + Modular Inverse):
1. Instead of updating the array on every `addAll` or `multAll` (which takes O(N) time), maintain a global multiplier `a` (initialized to 1) and a global adder `b` (initialized to 0).
2. The true value of any element `x` in the array at any time is `(a * x + b) % mod`.
3. When `addAll(inc)` is called, we update the global adder: `b = (b + inc) % mod`.
4. When `multAll(m)` is called, we scale both the multiplier and the adder: `a = (a * m) % mod` and `b = (b * m) % mod`.
5. When `append(val)` is called, we must insert a "base" value `x` that, when transformed by the CURRENT `a` and `b`, equals `val`. We use Fermat's Little Theorem to find the modular inverse of `a` to solve for `x`: `x = ((val - b) * (a^-1)) % mod`.
6. When `getIndex(idx)` is called, simply apply the current global `a` and `b` to the base value stored at `val[idx]`.

Time Complexity: O(1) for all operations (pow with a fixed modulus size is effectively O(1)).
Space Complexity: O(N) where N is the number of appended elements.
'''

import ast

class Fancy:
    def __init__(self):
        self.mod = 10**9 + 7  
        self.val = []  
        self.a = 1  
        self.b = 0  

    def append(self, val: int) -> None:
        # Calculate the base value x that satisfies: (a * x + b) % mod = val
        x = (val - self.b + self.mod) % self.mod
        # Fermat's Little Theorem for modular inverse: a^(mod-2) % mod
        inverse_a = pow(self.a, self.mod - 2, self.mod)
        self.val.append((x * inverse_a) % self.mod)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.mod
        self.b = (self.b * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.val):
            return -1  
        return (self.a * self.val[idx] + self.b) % self.mod

# --- Interactive Driver Code ---
if __name__ == "__main__":
    print("--- 1622. Fancy Sequence Interactive Runner ---")
    try:
        cmds_input = input("Enter commands (e.g., ['Fancy', 'append', 'addAll', 'append', 'multAll', 'getIndex', 'getIndex']): ")
        args_input = input("Enter arguments (e.g., [[], [2], [3], [7], [2], [0], [1]]): ")
        
        commands = ast.literal_eval(cmds_input)
        args = ast.literal_eval(args_input)
        
        if len(commands) != len(args):
            raise ValueError("Commands and arguments lists must be the same length.")
            
        obj = None
        output = []
        
        for cmd, arg in zip(commands, args):
            if cmd == "Fancy":
                obj = Fancy()
                output.append(None)
            elif cmd == "append":
                obj.append(arg[0])
                output.append(None)
            elif cmd == "addAll":
                obj.addAll(arg[0])
                output.append(None)
            elif cmd == "multAll":
                obj.multAll(arg[0])
                output.append(None)
            elif cmd == "getIndex":
                res = obj.getIndex(arg[0])
                output.append(res)
                
        print(f"\nOutput: {output}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")