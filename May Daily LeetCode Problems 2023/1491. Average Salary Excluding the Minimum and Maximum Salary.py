class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        L = len(salary)

        salary.remove(salary[0])
        salary.remove(salary[-1])

        Sum = sum(salary)

        return Sum / (L - 2)




