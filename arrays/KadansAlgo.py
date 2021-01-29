def maxSubArraySum(a,size):
    ##Your code here
    start=0
    currSum=0
    maxSum=0
    while start<size:
        currSum= max(a[start],currSum+a[start])
        maxSum= max(currSum,maxSum)
        start+=1
    return maxSum