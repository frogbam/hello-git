def calculate(a,b):
    if b==0:
        return a
    return calculate(b,a%b)

nums = list(map(int, input().split(" ")))
nums.sort()
gcd = calculate(nums[1], nums[0])
lcm = int(nums[1]*nums[0]/gcd)
print(gcd)
print(lcm)