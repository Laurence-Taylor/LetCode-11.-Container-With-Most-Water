class Solution:
    def maxArea(self, height: List[int]) -> int:
        p_begin = 0                 # Pointer Begin
        p_end = len(height)-1       # Pointer End
        max_area = 0                # Define MAx area = 0
        # while the pointers cannot reach each others
        while p_begin < p_end:
            # find minimum height
            min_height = min(height[p_begin],height[p_end])
            # calculate area of minimum height
            current_area = min_height * (p_end - p_begin)
            # find maximum area and update it
            max_area = max(current_area, max_area)
            # change pointer of the minimum height
            if height[p_begin] < height[p_end]:
                p_begin += 1
            else:
                p_end -= 1
                
        return max_area 
    
if __name__ == '__main__':
    sol=Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))