def get_middle(left_n: int, right_n: int) -> int:
    size = right_n - left_n + 1
    dist_to_middle = size//2
    new_middle = left_n + dist_to_middle
    return (new_middle)

def get_sublength(left_n: int, right_n: int) -> int:
    new_length = right_n - left_n + 1
    return(new_length)

class BinarySearch:
  
  def search(self, nums: List[int], target: int) -> int:
      length = len(nums)
      left = 0
      right = len(nums) - 1
      middle = get_middle(left,right)
      sublength = length
      solvable = True

      #first pass on edge numbers and if length is too small
      if nums[left] == target: return(left);
      if nums[right] == target: return(right);
      if length < 3: return -1 

      #binary search
      while (solvable == True):
        sublength = get_sublength(left,right)
        if sublength == 3:
          print ("checking final numbers")
          if target == nums[left]: 
            return left
          if target == nums[right]: 
            return right
          if target == nums[left+1]: 
            return (left+1)
          else: 
            solvable == False
            print('Not solvable')
            return (-1)
            break;

        if target > nums[middle]:
          left = middle 
        if target < nums[middle]:
          right = middle
        elif target == nums[middle]:
          return middle
        middle = get_middle(left,right)

        
          

        


          
            
          
        
