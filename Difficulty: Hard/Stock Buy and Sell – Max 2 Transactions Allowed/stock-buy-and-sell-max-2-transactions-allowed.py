class Solution:
    def maxProfit(self, prices):
        firstBuy=float('-inf')
        firstSell=0
        secondBuy=float('-inf')
        secondSell=0
        
        for i in range(len(prices)):
            firstBuy=max(firstBuy,-prices[i])
            firstSell=max(firstSell,firstBuy+prices[i])
            secondBuy=max(secondBuy,firstSell-prices[i])
            secondSell=max(secondSell,secondBuy+prices[i])
        
        return secondSell

#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends