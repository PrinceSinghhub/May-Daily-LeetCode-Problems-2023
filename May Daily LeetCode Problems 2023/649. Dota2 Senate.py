class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # round-based procedure
        # until last one win

        ban = defaultdict(int)
        nxt = deque()
        cur = deque(senate)
        exists = {}
        while cur:
            while cur:
                party = cur.popleft()
                if party == "R" and ban["R"] > 0:
                    ban["R"] -= 1
                elif party == "D" and ban["D"] > 0:
                    ban["D"] -= 1
                else:
                    if party == "R":
                        ban["D"] += 1
                    else:
                        ban["R"] += 1

                    nxt.append(party)
                    exists[party] = True
            if len(exists) == 1:
                return "Radiant" if "R" in exists else "Dire"
            cur, nxt = nxt, deque()
            exists = {}