heros =["蜘蛛侠","绿巨人","黑寡妇","鹰眼","灭霸","雷神"]
##heros[4]="钢铁侠"
##heros[3: ]=["武松","林冲","李逵"]
##print(heros)

nums=[3,1,9,6,8,3,5,3]
##nums.sort()
##print(nums)
##nums.reverse()
##print(nums)
nums.sort(reverse=True)
print(nums)

heros.index("绿巨人")
heros[heros.index("绿巨人")] ="神奇女侠"
print(heros)

nums_copy1=nums.copy()
nums_copy2=nums[:]
print(nums_copy1,nums_copy2)
