> Given an array of integers **nums** which is sorted in ascending order, and an integer **target**, write a function to search **target** in **nums**. If **target** exists, then return its index. Otherwise, return **-1**. 

>You must write an algorithm with **O(log n)** runtime  complexity. 

>Input: nums = [-1,0,3,5,9,12], target = 9
<br>Output: 4
<br>Explanation: 9 exists in nums and its index is 4 
<br><br> Input: nums = [-1,0,3,5,9,12], target = 2
<br>Output: -1
<br>Explanation: 2 does not exist in nums so return -1

***
***
**<font color = red> False Code</font>**

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        for i in range(0, length//2):
            if nums[i] == target:
                return i
            elif nums[length-i-1] == target:
                    return length-i-1
        return -1            
```

**<font color = red> Failed Case Example </font>**

```
nums = [5]
target = 5
Output: -1
Expected Output: 0
```


**<font color = red> False Code Analysis </font>**

The false code is trying to check the elements of the list from both ends moving toward the center. It is not a binary search but rather a two-pointers approach.  

For the input **nums = [5]**, **length** is 1, the loop range in the false code example is **range(0, length//2)**, because **1//2** is **0**, the loop does not run even once. As a result, no number is checked, and the function returns **-1**.

To fix the issue for this specific case, we can modify the loop range to **range(0, length+1)//2**. This ensures that for a length of 1, the loop runs once.

However, this is still not a binary search. It's a two-pointers approach that starts from both ends and meets in the middle. 


***
***
## Binary Search
 A true binary search algorithm works by dividing **the sorted list** into half repeatedly until the desired element is found or until the entire list is exausted. 

Binary search involves many boundary conditions, the logic behind it is simple but rather sophisticated. For example, whether to use **while (left < right)** or **while (left <= right)**, **right == middle**, or **right == midddle -1**? The key to these confusions is <font color = red> the definition of the interval </font>.

There are two different ways to define the interval.
<br> Taking for example we are going to search **2** in an Arrary of  **1,2,3,4,7,9,10**.

#### I. We define the *target* to be in a left-closed and right-closed interval, i.e. <font color = red> [left, right]</font>.
   
|index:    | 0   | 1   | 2   | 3   | 4   | 5   |  6  | 
|  :--:    | :--:| :--:| :--:| :--:| :--:| :--:| :--:| 
|elements: | 1   | 2   | 3   | 4   | 7   |  9  |  10 |
|          |L = 0|      |     | M = 3    |     |     | R = 6|

&ensp;&ensp; (i) We need to use <font color = red> while (left <= right)</font>. <br>&ensp;&ensp; (ii) If nums[middle] > target, assign **right** as **middle - 1** because *nums[middle]* is definitely not the target, and the ending index of the next search left interval will be **middle - 1**.
| index:    | 0   | 1   | 2   |
|  :--:     | :--:| :--: | :--:|
|elements:  | 1   | 2    | 3   |
|           |L = 0| M = 1 | R = 2|

```python
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while (left <= right):
            # To avoid overflow, do not use (left + right) // 2
            middle =  left + ((right - left) // 2)   
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle -1
            else: left = middle + 1
        return -1
```
#### II. We define the *target* to be in a left-closed and right-open interval, i.e. <font color = red> [left, right)</font>.

|index:    | 0   | 1   | 2   | 3   | 4   | 5   |  6  |  7  |
|  :--:    | :--:| :--:| :--:| :--:| :--:| :--:| :--:| :--:|
|elements: | 1   | 2   | 3   | 4   | 7   |  9  |  10 |     |
|          |L = 0|      |    | M = 3|    |     |      | R = 7|

&ensp;&ensp; (i) Use <font color = red> while (left < right)</font> <br> &ensp;&ensp; (ii) If nums[middle] > target, assign **right** as **middle** because **nums[middle]** is not equal to the target, we need to continue searching in the left interval, and since the search interval is left-closed and right-open, update **right** to **middle**.

| index:    | 0   | 1   | 2   | 3    |
|  :--:     | :--:| :--: | :--:| :--:|
|elements:  | 1   | 2    | 3   |  4  |
|           |L = 0| M = 1|     | R = 3

```python
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)
        while (left < right): 
            # To avoid overflow, do not use (left + right) // 2
            middle =  left + ((right - left) // 2)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle 
            else: left = middle + 1
        return -1
```

***
***
## Variant
#### [35_E]Search Insert Position

>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
<br> You must write an algorithm with O(log n) runtime complexity.

>Example 1: <br> Input: nums = [1,3,5,6], target = 5 <br> Output: 2

>Example 2: <br> Input: nums = [1,3,5,6], target = 2 <br> Output: 1

>Example 3: <br> Input: nums = [1,3,5,6], target = 7 <br>Output: 4

Analysis: The only modification is in the return value. Instead of returning -1 when the target is not found, we return the value of ***left***, which is the index where the target should be inserted to maintain the sorted order of the array. 

***
***
## Variant
#### [34_M]Find First and Last Position of Element in Sorted Array
#### [69_E]Sqrt(x)

