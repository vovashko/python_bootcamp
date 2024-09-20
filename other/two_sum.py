import ast


def get_indexes(nums, target):
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if (nums[i] + nums[j]) == int(target):
                indexes = [i, j]
                return (indexes)
            else:
                j += 1
        else:
            i += 1
    indexes = [i, j]
    return (indexes)

def main():
   input_str = input()
   nums_str, target_str = input_str.split(', ')
   num_def, nums_before_convertion = nums_str.split(' = ')
   nums = eval(nums_before_convertion)
   target_def, target = target_str.split(' = ')
   indexes = get_indexes(nums, target)
   print(indexes)
   return(indexes)

main()
    
