class Solution(object):
    def minCostClimbingStairs(self, cost):
        for step in range(2,len(cost)):
            cost[step]+=min(cost[step-1],cost[step-2])
        return min(cost[-1],cost[-2])
        