def palindrome(s):
	for i in range(len(s)//2):
		if s[i] != s[-(i+1)]:
			return False
	return True

nums = [x for x in range(1000000) if palindrome(str(x))]
nums = [x for x in nums if palindrome(str(bin(x))[2:])]
print(sum(nums))