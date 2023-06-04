def find_pairs(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target or nums[j] + nums[i] == target:
                pairs.append((nums[i], nums[j]))
    return pairs

nums_input = input("Введіть список чисел, розділених пробілом: ")
nums = [int(num) for num in nums_input.split()]

target = int(input("Введіть цільове значення: "))

pairs = find_pairs(nums, target)

print("Знайдені пари, сума яких дорівнює цільовому значенню:")
print(pairs)