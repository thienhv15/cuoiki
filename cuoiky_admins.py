# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:55:22 2024

@author: MINH NHUT
"""
import random #question_2, question_7, question_12, question_17
def question_1(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def question_2(n: int) -> (int, float):
    danh_sach = []
    for i in range(n):
        x = random.randint(1, 100)
        danh_sach.append(x)
    tong = sum(danh_sach)
    trung_binh = tong / n
    return (tong, trung_binh)

def question_3(s: str) -> (int, int):
    hoa = 0
    thuong = 0
    for i in s:
        if i.isupper():
            hoa += 1
        elif i.islower():
            thuong += 1
    return (hoa, thuong)

def question_4(n: int) -> bool:
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        return False
    
def question_5(lst: list, x: int) -> int or None:
    try:
        return lst.index(x)
    except ValueError:
        return None
    
def question_6(n: int) -> int:
    ket_qua = 1
    for i in range(1, n+1):
        ket_qua *= i
    return ket_qua

def question_7(n: int) -> (float, float):
    danh_sach = []
    for i in range(n):
        x = random.uniform(0, 1)
        danh_sach.append(x)
    lon_nhat = max(danh_sach)
    nho_nhat = min(danh_sach)
    return (lon_nhat, nho_nhat)

def question_8() -> str:
    s = input("Nhập vào chuỗi: ")
    dao_chuoi = s[::-1]
    return dao_chuoi

def question_9(s: str) -> bool:
    chuoi_s = ''.join(i.lower() for i in s if i.isalnum())
    chuoi_s_dao = chuoi_s[::-1]
    return chuoi_s == chuoi_s_dao
  
def question_10() -> None:
    ds = input("Nhập vào danh sách số nguyên: ")
    if not ds:
        return None
    ds_so_nguyen = [int(i) for i in ds.split()]
    return ds_so_nguyen

def question_11(n: int) -> int:
    

def question_12() -> bool:
    n = random.randint(1, 1000)
    print(f"Số ngẫu nhiên: {n}")
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def question_13(s: str) -> int:
    cac_tu = s.split()
    return len(cac_tu)

def question_14(s: str) -> bool:
    if s.isdigit():
        return True
    return False

def question_15(value) -> bool:
    if not value:
        return True
    return False

def question_16(*agr) -> float:
    if not agr:
        return None
    trung_binh = sum(agr) / len(agr)
    return trung_binh

def question_17(n: int) -> list:
    danh_sach = []
    for i in range(n):
        x = random.randint(1, 100)
        danh_sach.append(x)
    danh_sach.sort(reverse= True)
    return danh_sach

def question_18(s: str) -> str:
    s = s.strip()
    s = " ".join(s.split())
    return s

def question_19(x: int, n: int) -> bool:
    if x > n:
        return True
    return False

from typing import Optional
def question_20() -> Optional[str]:
    s = input("Nhập giá trị từ bán phím: ")
    if s:
        return s
    else:
        return None

from typing import Optional
def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    lis = [] 
    for i in nums:
        so_t2 = target - i
        if so_t2 in lis:    
            return (so_t2, i)
        lis.append(i)
    return None

def question_22(nums: list[int]) -> None:
    so_0 = nums.count(0)
    nums_moi = [i for i in nums if i != 0]
    nums_moi.extend([0]*so_0)
    return nums_moi

def question_23(nums: list[int]) -> bool:
    lis = []
    for i in nums:
        if i in lis:
            return True
        lis.append(i)
    return False

def question_24(nums: list[int]) -> int:
    phan_tu = None
    dem = 0
    for i in nums:
        if dem == 0:
            phan_tu = i
        dem += (1 if i == phan_tu else -1)
    return phan_tu

def question_24_c2(nums: list[int]) -> int:
    n = len(nums)
    nums.sort()
    return nums[n//2]

import collections
def question_24_c3(nums: list[int]) -> int:
    n = len(nums)
    dic_phantu_soluong = collections.Counter(nums)
    for phantu, soluong in dic_phantu_soluong.items():
        if soluong > n//2:
            return phantu

    
def question_25(nums: list[int]) -> list[int]:
    nums_new = sorted([i**2 for i in nums])
    return nums_new

def question_26(s: str) -> int:
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    do_dai = 0
    ky_tu_giua = False
    for i in dic.values():
        if i % 2 == 0:
            do_dai += i
        else:
            do_dai += i - 1
            ky_tu_giua = True
    if ky_tu_giua:
        do_dai += 1
    return do_dai

import collections
def question_26_c2(s: str) -> int:
    dic_tu_so = collections.Counter(s)
    do_dai = 0
    co_so_le = False
    for so in dic_tu_so.values():
        do_dai += so // 2 * 2    
        if so % 2 == 1:
            co_so_le = True
    if co_so_le:
        do_dai += 1
    return do_dai

def question_27(strs: list[str]) -> str:
    tien_to = strs[0]
    for i in strs[1:]:
        while not i.startswith(tien_to):
            tien_to = tien_to[:-1]
            if not tien_to:
                return ""
    return tien_to

import collections
def question_28(s: str) -> dict[str, int]:
    dic_ky_tu = dict(collections.Counter(s))
    return dic_ky_tu
    
def question29(nums: list[int]) -> float:
    nums.sort()
    so_pt = len(nums)
    if so_pt % 2 != 0:
        return nums[(so_pt - 1) // 2]
    else:
        so_giua_1 = nums[(so_pt // 2) -1]
        so_giua_2 = nums[so_pt // 2]
        so_trung_vi = (so_giua_1 + so_giua_2) / 2
        return so_trung_vi

def question_30(paragraph: str) -> dict[str, int]:
    dic = {}
    cac_tu = paragraph.split()
    for tu in cac_tu:
        if tu in dic:
            dic[tu] += 1
        else:
            dic[tu] = 1
    return dic

import collections
def question_30_c2(paragraph: str) -> dict[str, int]:
    cac_tu = paragraph.split()
    dic_tu = dict(collections.Counter(cac_tu))
    return dic_tu

import collections
def question_31(paragraph: str, n: int) -> list[str]:
    cac_tu = paragraph.split()
    dic_tu = dict(collections.Counter(cac_tu))
    so_tu = len(dic_tu)
    tu_nhieu = [tu for tu, so in dic_tu.items() if so / so_tu > 0.2 ]
    sap_xep_tu = sorted(tu_nhieu, key=lambda tu: dic_tu[tu], reverse= True)
    return sap_xep_tu[:n]
    
def  question_32(nums: list[int]) -> tuple[list[int], list[int]]:
    ds_chan_giam = sorted([i for i in nums if i % 2 == 0], reverse= True)
    ds_le_tang = sorted([ i for i in nums if i % 2 != 0])
    Tuple = (ds_chan_giam, ds_le_tang)
    return Tuple

def question_33(nums: list[int]) -> tuple[int, int]:
    if len(nums) >= 5:
        giam_dan = sorted(nums, reverse= True)
        pt_lon_2 = giam_dan[1]
        tang_dan = sorted(nums)
        pt_nho_5 = tang_dan[4]
        return (pt_lon_2, pt_nho_5)
    else:
        return None
    
def question_34(s: str) -> int:
    danh_sach = []
    do_dai_max = 0
    for i in s:
        while i in danh_sach:
            danh_sach.pop(0)
        danh_sach.append(i)
        do_dai_max = max(do_dai_max, len(danh_sach))
    return do_dai_max
            
def question_35(s: str) -> str:
    n = len(s)
    chuoi_dai = ""
    for i in range(n):
        for j in range(i+1, n):
            chuoi = s[i:j]
            if s.count(chuoi) > 1:
                if len(chuoi) > len(chuoi_dai):
                    chuoi_dai = chuoi
    return chuoi_dai

import itertools
def question_36(nums: list[int]) -> list[list[int]]:
    return [list(i) for i in itertools.permutations(nums)]

def question_36_c2(nums: list[int]) -> list[list[int]]:
    if len(nums) <= 1:
        return [nums]
    ket_qua = []
    for i in range(len(nums)):
        so_hien_tai = nums[i]
        so_con_lai = nums[:i] + nums[i+1:]
        for j in question_36_c2(so_con_lai):
            ket_qua.append([so_hien_tai] + j)
    return ket_qua
    
def question_37(s: str) -> bool:
    dic_ky_tu = {')':'(', '}':'{', ']':'['}
    ds_ngoac_mo = []
    for i in s:
        if i in dic_ky_tu.values():
            ds_ngoac_mo.append(i)
        elif i in dic_ky_tu:
            if ds_ngoac_mo and ds_ngoac_mo[-1] == dic_ky_tu[i]:
                ds_ngoac_mo.pop()
            else:
                return False
    return True if not ds_ngoac_mo else False
     
def question_38(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
# dóng dóng fibonancy

def question_39(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    gia_max = 0
    mua_min = prices[0]
    for i in prices[1:]:
        gia_max = max(gia_max, i - mua_min)
        mua_min = min(mua_min, i)
    return gia_max

if __name__ == "__main__":
    print(question_1(11))
    print(question_2(5))
    print(question_3("Hello World"))
    print(question_3("Python Programming"))
    print(question_4(4))
    print(question_4(7))
    print(question_5([1, 2, 3, 4, 5], 3))
    print(question_5([10, 20, 30, 40], 25))
    print(question_6(5))
    print(question_6(7))
    print(question_7(5))
    print(question_7(10))
    #print(question_8())
    print(question_9("A man, a plan, a canal: Panama"))
    print(question_9("race a car"))
    #print(question_10())
    print(question_11(10))
    print(question_12())
    print(question_13("    this is a test.   "))
    print(question_14("12345"))
    print(question_15(None))
    print(question_16(10, 20))
    print(question_17(5))
    print(question_18("   Hello    world!   "))
    print(question_19(15, 10))
    #print(question_20())
    print(question_21([2,7,11,15], 9))
    print(question_22([0,1,0,3,12]))
    print(question_23([1,2,3,1]))
    print(question_24([2,2,1,1,1,2,2]))
    print(question_24_c2([2,2,1,1,1,2,2]))
    print(question_24_c3([2,2,1,1,1,2,2]))
    print(question_25([-7,-3,2,3,11]))
    print(question_26('abccccdd'))
    print(question_26_c2('abccccdd'))
    print(question_27(["flower", "flow", "flight"]))
    print(question_28('hello'))
    print(question29([1,3,4,2,5]))
    print(question29([1,2,3,4]))
    print(question_30("apple orange apple banana orange"))
    print(question_30_c2("hello world hello"))
    print(question_31("apple apple banana orange orange apple", 2))
    print(question_31("hello world hello universe hello", 1))
    print(question_32([4,1,3,2,7,8,5]))
    print(question_33([3,1,4,5,9,2,6,8,7]))
    print(question_33([1,3,2,5]))
    print(question_34("abcabcbb"))
    print(question_34("pwwkew"))
    print(question_35("aabcdeaabcd"))
    print(question_36([1,2,3]))
    print(question_36_c2([1,2,3]))
    print(question_37("()[]{}"))
    print(question_37("([)]"))
    print(question_38(3))
    print(question_39([6,7,8,9,20,5]))
    print(question_39([7,1,5,3,6,4]))