class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    #sort array
    nums.sort()
    # N = length of numbers array
    # result = []
    N, result = len(nums), []
    #for number[all but last index]
    for i in range(N):
      # if index > 0 and number[index] = number[index-1]
      if i > 0 and nums[i] == nums[i-1]: 
        continue
      # target = -(number[index])
      target = nums[i] * -1
      # start pointer = [1], end pointer = [last index] 
      s, e = i + 1, N - 1
      # while start < end
      while s < e:
        # if number[start] + number[end] = targer
        if nums[s] + nums[e] == target:
          # add number[i], number[s], number[e] to results[]  
          result.append([nums[i], nums[s], nums[e]])
          # start index + 1
          s = s + 1
          # check start and end pointers
          # check start number is not same as last  
          while s < e and nums[s] == nums[s - 1]:
            # start index +1
            s = s + 1
        # if start number + end number < target
        elif nums[s] + nums[e] < target:
          # start index +1
          s = s + 1
        # otherwise    
        else:
          # end index -1
          e = e-1 
    return result

#if __name__ == '__main__':
#  thing = Solution()
#  print(thing.threeSum([-1,0,1,2,-1,-4]))
