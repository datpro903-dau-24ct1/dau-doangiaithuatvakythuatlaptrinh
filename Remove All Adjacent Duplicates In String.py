class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()   # xóa cặp trùng
            else:
                stack.append(ch)
        
        return "".join(stack)