nums = [0, 1, 3]
target = 4


for num in range(0, len(nums)):


    if num == 0:
        num_anterior = None
    else:
        num_anterior = nums[num - 1]


    num_atual = nums[num]
    if num_anterior is not None:
        print(num_anterior) 
        if num_atual + num_anterior == target:
            break
    

print(nums.index(num_atual))
print(nums.index(num_anterior))
    