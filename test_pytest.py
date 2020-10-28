import pytest
import logging
import solution as SolutionClass


# test to see if it returns a correct threesum
def test_correct_solution(duration=0.000001):
  thing = SolutionClass.Solution()
  assert(thing.threeSum([-1,0,1,2,-1,-4]) == [[-1, -1, 2], [-1, 0, 1]])
  

# test an empty list parameter
def test_empty_list():
  thing = SolutionClass.Solution()
  assert(thing.threeSum([]) == [])
  

# single item list
def test_single_item_list():
  thing = SolutionClass.Solution()
  assert(thing.threeSum([0]) == [])
  

# two item list
def test_two_item_list():
  thing = SolutionClass.Solution()
  assert(thing.threeSum([0,1]) == [])
  

# there's no threesum
def test_no_valid_threesum():
  thing = SolutionClass.Solution()
  assert(thing.threeSum([-1, 0, 2]) == [])
  

# unique solution
def test_returns_unique_solution():
  thing = SolutionClass.Solution()
  assert(thing.threeSum([-1, -1, 0, 1, 1]) == [[-1, 0, 1]])
  


