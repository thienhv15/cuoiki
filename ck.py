# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 06:50:50 2024

@author: Admin
"""

'''from typing import Optional
def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    for i in nums:
        a = target - i
        if a in nums and a!=i:
            return i,a
    return None
print(question_21([1,2,3,4,5,6], 10))'''

'''def question_22(nums: list[int]) -> None:
    n = 0
    for i in nums:
        if i !=0:
            nums[n] =i
            n+=1
    for i in range(n,len(nums)):
        nums[i] = 0
    return nums
print(question_22([1,2,0,1,0]))'''

'''def question_23(nums: list[int]) -> bool:
    ds = set()
    for i in nums:
        if i in ds:
          return True
        ds.add(i)
    return False
print(question_23([1,2,4]))'''

'''def question_24(nums: list[int]) -> int:
    nums = sorted(nums)
    return nums[len(nums)//2]
print(question_24([1,21,2,2,2,2,1,3]))'''

'''def question_25(nums: list[int]) -> list[int]:
    ds = []
    for i in nums:
        ds.append(i**2)
    return sorted(ds)
print(question_25([1,2,3,1,2]))'''

'''def question_26(s: str) -> int:
    dem = {}
    for i in s:
        if i in dem:
            dem[i] +=1
        else:
            dem[i] =1
    dodai = 0
    for j in dem.values():
        if j%2 ==0:
            dodai += j
        else:
            dodai = j-1
        if j%2 !=0:
            dodai +=1 
    return dodai
print(question_26('abccccdd'))'''
            
'''def question_27(strs: list[str]) -> str:
    if not strs:
        return ''
    for s in strs[1:]:
        tiento = strs[0]
        i = 0
        while i<len(tiento) and i<len(s) and tiento[i] == s[i]:
            i+=1
        tiento = tiento[:i]
        if not tiento:
            return ''
    return tiento
print(question_27(["dog", "racecar", "car"]))'''

'''from typing import Dict
def question_28(s: str) -> Dict[str, int]:
    dem = {}
    for i in s:
        if i in dem:
            dem[i] +=1
        else:
            dem[i] = 1
    return dem
print(question_28("hello"))'''

'''from typing import Optional,Tuple,List
def question_29(nums: List[int]) -> Optional[Tuple[int, int]]:
    nums = sorted(nums)
    n = len(nums)
    if n%2 ==0:
        return (nums[n//2] + nums[n//2 -1])/2 
    return nums[n//2]
print(question_29([1,2,3,4]))'''

'''from typing import Dict
def question_30(paragraph: str) -> Dict[str, int]:
    dem = {}
    s = paragraph.split()
    for i in s:
        if i in dem:
            dem[i] +=1 
        else:
            dem[i] =1 
    return dem
print(question_30("apple orange apple banana orange"))'''
    
'''from typing import List
def question_31(paragraph: str, n: int) -> List[str]:
     ds = {}
     s = paragraph.lower().split()
     for i in s:
         if i in ds:
             ds[i] +=1
         else:
             ds[i] = 1
     lst = []
     for word,count in ds.items():
         if count/len(s) >0.2:
            lst.append(word)
     return lst[:n]
print(question_31("hello world hello universe hello", 2))'''

'''from typing import Tuple,List
def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
    dschan = []
    dsle = []
    for i in nums:
        if i%2 ==0:
            dschan.append(i)
        else:
            dsle.append(i)
        dsle.sort()
    return sorted(dschan, reverse = True),dsle
print(question_32( [4, 1, 3, 2, 7, 8, 5]))'''

'''def question_33(nums: list[int]) -> tuple[int, int]:
    nums = sorted(nums)
    if len(nums) <5:
        return None
    return nums[-2],nums[4]
print(question_33([1,2,3,4]))'''

'''def question_34(s: str) -> int:
    chuoi = []
    dodaimax = 0
    for i in s:
        while i in chuoi:
            chuoi.pop(0)
        chuoi.append(i)
        dodaimax = max(dodaimax,len(chuoi))
    return dodaimax
print(question_34( "abcabcbb"))'''

'''def question_35(s: str) -> str:
    n = len(s)
    chuoidai = ''
    for i in range(n):
        for j in range(i+1,n):
            chuoi=s[i:j]
            if s.count(chuoi)>1:
                if len(chuoi)>len(chuoidai):
                    chuoidai = chuoi
    return chuoidai
print(question_35("aabcdeaabcd"))'''

'''import itertools
def question_36(nums: list[int]) -> list[list[int]]:
    return [list(i) for i in itertools.permutations(nums)]
print(question_36([1,2,3]))'''

'''def question_37(s: str) -> bool:
    daungoac = {']': '[', ')': '(', '}': '{'}
    ds =[]
    if not s:
        return False
    for i in s:
        if i in daungoac.values():
            ds.append(i)
        elif i in daungoac:
            if ds and ds[-1] == daungoac[i]:
                ds.pop()
            else:
                return False
    return len(ds)==0 

print(question_37("[d({}"))'''

'''def question_38(n: int) -> int:
    if n<=1:
        return 1
    a,b = 1,1
    for i in range(2,n+1):
        c = a+b
        a,b = b,c
    return b
print(question_38(3))'''

'''def question_39(prices: list[int]) -> int:
    if not prices:
        return 0
    giamax = 0
    muamin = prices[0]
    for i in prices[1:]:
        giamax = max(giamax,i-muamin)
        muamin = min(muamin,i)
    return giamax
print(question_39([6, 7, 8, 9, 20, 5]))'''
        
            


            
        
        
    


        


        
        
    

            

    



            
            
            
    
