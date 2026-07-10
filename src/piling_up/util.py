def check_stackability(blocks):
    left = 0
    right = len(blocks) - 1
    top_cube = float('inf')
    
    while left <= right:
        left_val = blocks[left]
        right_val = blocks[right]
        
        if left_val >= right_val:
            if left_val <= top_cube:
                top_cube = left_val
                left += 1
            elif right_val <= top_cube:
                top_cube = right_val
                right -= 1
            else:
                return "No"
        else:
            if right_val <= top_cube:
                top_cube = right_val
                right -= 1
            elif left_val <= top_cube:
                top_cube = left_val
                left += 1
            else:
                return "No"
                
    return "Yes"