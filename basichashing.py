# Number Hashing Using array
def numhash():
    a = list(map(int, input("Enter elements with space as seperator(each upto 100): ").split(' ')))
    n = len(a)

    hash = [0]*101

    for i in range(n):
        hash[a[i]] += 1
# Char Hashing using array
def strHash():
    s = input("Enter the string(lowercase): ")
    strhash = [0]*26
    n = len(s)
    for i in range(n):
        strhash[ord(s[i]) - ord('a')] +=1
    print(strhash)

def maxFrequency(self, nums: list[int], k: int) -> int:
        answer = 1
        n = len(nums)
        l = 0
        for r in range(n):
            target = nums[r]
            cost = target*(r-l+1) - sum(nums[l:r+1])
            while cost>k:
                l+=1
                cost = target*(r-l+1) - sum(nums[l:r+1])
            if cost<=k:
                answer = max(answer, r-l+1)
        return answer
