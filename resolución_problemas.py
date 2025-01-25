def subarray_sum(nums, k):
    count = 0
    sum_dict = {0 : 1}
    current_sum = 0
    
    for num in nums:
        current_sum += num
        if current_sum - k in sum_dict:
            count += sum_dict[current_sum - k]
        if current_sum in sum_dict:
            sum_dict[subarray_sum] += 1
        else:
            sum_dict[current_sum] = 1
            
    return count

# Ejemplo de uso
nums = [1, 1, 1]
k = 2

print(subarray_sum(nums, k)) # Output : 2