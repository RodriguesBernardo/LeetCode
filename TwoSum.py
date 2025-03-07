def twoSum(target, list):
    map = {}
    
    for i, num in enumerate(list):
        complemento = target - num
        if complemento in map:
            return [map[complemento], i]
        map[num] = i
    return []
        
print(twoSum(9, [2, 7, 11, 15])) # [0, 1]