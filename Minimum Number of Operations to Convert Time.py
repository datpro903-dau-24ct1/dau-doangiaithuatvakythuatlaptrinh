class Solution(object):
    def convertTime(self, current, correct):
        cur_h, cur_m = map(int, current.split(":"))
        cor_h, cor_m = map(int, correct.split(":"))
        current_minutes = cur_h * 60 + cur_m
        correct_minutes = cor_h * 60 + cor_m
        diff = correct_minutes - current_minutes
        operations = 0
        for step in [60, 15, 5, 1]:
            operations += diff // step
            diff %= step
        return operations