def lon(nums):
    if not nums:
        return 0
    lis=[1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                lis[i]=max(lis[i],lis[j]+1)
    return max(lis)
print(lon([1,2,3,3,2,1,56,90,80]))
