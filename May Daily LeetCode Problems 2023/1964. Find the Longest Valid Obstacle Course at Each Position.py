class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        cur = list()
        ans = list()

        for ob in obstacles:
            if not cur:
                cur.append(ob)
                ans.append(1)
            else:
                inserti = bisect.bisect(cur, ob)
                ans.append(inserti + 1)
                if inserti == len(cur):  # at the end of cur
                    cur.append(ob)
                else:  # can replace
                    cur[inserti] = ob
        return ans