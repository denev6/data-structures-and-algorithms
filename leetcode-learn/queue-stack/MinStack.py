class MinStack:
    # You must implement a solution with O(1) time complexity for each function.

    def __init__(self):
        self.stack = list()
        # When pushing a value, find a min value. And record the min value in "min_vals".
        # When popping a value, the new min value is just the min value of the previous step (t-1).
        # In other words, "min_vals" is a stack that records the min values in order of time steps.
        self.min_vals = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_vals:
            min_val = min(val, self.min_vals[-1])
        else:
            min_val = val
        self.min_vals.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_vals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]
