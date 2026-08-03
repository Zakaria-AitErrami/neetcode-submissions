class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p,s in pair:
            time_arrival = (target - p) / s
            stack.append(time_arrival)
            if len(stack) >=2 and time_arrival <= stack[-2]:
                stack.pop()
        return len(stack)

