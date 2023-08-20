> Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. <br> If target is not found in the array, return [-1, -1].
<br> You must write an algorithm with O(log n) runtime complexity.

> Example 1: <br> Input: nums = [5,7,7,8,8,10], target = 8 <br> Output: [3,4]

> Example 1: <br> Input: nums = [5,7,7,8,8,10], target = 6 <br> Output: [-1,-1]

> Example 3: <br> Input: nums = [], target = 0 <br> Output: [-1,-1]

***
***
**<font color = red> False Code</font>**
```python
class Solution(object):
    def searchRange(self, nums, target):
        left, right = 0, len(nums)-1
        pivot = 0   #pivot the first-found-target
        while(left <= right):
            middle =  left + ((right - left) // 2)
            if nums[middle] == target:
                pivot = middle
                break
            elif nums[middle] < target:
                left = middle + 1
            else: right = middle - 1
        
        if pivot == 0:   #target not found
            return [-1, -1]
        else:   #Check the left-and-right-side of the pivot
            resLeft = pivot
            resRight = pivot
            for i in range(0, right-pivot+1):   #check the right side
                if nums[pivot+i] == target:
                    resRight = pivot + i
                    i += 1
                else: continue
                
                if nums[pivot -i] == target:   #check the left side
                    resLeft = pivot - i
                    i -= 1
            return [resLeft,resRight]
```
**<font color = red> Failed Case Example </font>**

```
nums = [1]
target = 1
Output: [-1,-1]
Expected Output: [0,0]
```


**<font color = red> False Code Analysis </font>**

*pivot* was initialized to 0 outside of the loop, which is not necessary. *pivot* should be set only when we find a match for the target value. 
<br> Moreover, this implementation is not optimal. The second loop can take O(n) time in the worst case scenario. We can improve the efficiency by using two seperate binary searches to find the left and right bounds of the range. This will ensure a more efficient solution. 

***
***
**<font color = red> Corrected <br> Time complexity O(n) </font>**
```python
class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        pivot = -1
        
        while left <= right:
            middle = middle =  left + ((right - left) // 2)
            if nums[middle] == target:
                pivot = middle
                break
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        if pivot == -1:
            return [-1, -1]
        
        resLeft = pivot
        resRight = pivot
        
        for i in range(0, right - pivot + 1):
            if pivot + i <= len(nums)-1 and nums[pivot + i] == target:
                resRight = pivot + i
                
            if pivot - i >= 0 and nums[pivot - i] == target:
                resLeft = pivot - i
                
        return [resLeft, resRight]
```


**<font color = red> Corrected <br> Time complexity O(log(n)) </font>**
```python
class Solution(object):
    def searchRange(self, nums, target):
        
        #To find the right bound
        left, right = 0, len(nums)-1
        resLeft, resRight = -1, -1
        while left <= right: 
            middle =  left + ((right - left) // 2)
            if nums[middle] == target:    #One 'target' is found 
                resRight = middle   
                #check the right side of 'target' 
                left = middle + 1        
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        # To find the left bound (similar logic)
        # DO NOT forget to reset the left and right pointer index
        left, right = 0, len(nums)-1
        while left <= right:  
            middle = (left + right) // 2
            if nums[middle] == target:
                resLeft = middle
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return [resLeft, resRight]
```
