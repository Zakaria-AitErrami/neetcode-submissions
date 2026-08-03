class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        prevTimeToTarget = (target - pair[0][0]) / pair[0][1]
        fleet = 1 # first cars always forms a fleet
        for i in range(1, len(pair)):
            curTimeTotarget = (target - pair[i][0]) / pair[i][1]
            if curTimeTotarget > prevTimeToTarget:
                # can't catch up form a fleet
                fleet+=1
                prevTimeToTarget = curTimeTotarget
        return fleet
