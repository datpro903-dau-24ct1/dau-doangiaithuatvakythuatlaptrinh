class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        total = 0
        for i in range(len(tickets)):
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)
        return total