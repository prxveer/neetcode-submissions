class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []

        for current in range(len(temperatures)):

            while stack and temperatures[current] > temperatures[stack[-1]]:
                previous = stack.pop()
                answer[previous] = current - previous

            stack.append(current)

        return answer