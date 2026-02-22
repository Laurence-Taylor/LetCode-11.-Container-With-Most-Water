class Solution:
    def maxArea(self, height: list[int]) -> int:
        p_begin = 0                 # Pointer Begin
        p_end = len(height)-1       # Pointer End
        max_area = 0
        while p_begin < p_end:
            min_height = min(height[p_begin],height[p_end])
            current_area = min_height * (p_end - p_begin)
            max_area = max(current_area, max_area)
            if height[p_begin] < height[p_end]:
                p_begin += 1
            else:
                p_end -= 1
                
        return max_area 
    
if __name__ == '__main__':
    sol=Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))