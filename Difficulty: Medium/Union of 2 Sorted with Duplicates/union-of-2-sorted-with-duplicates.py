#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        len1,len2=len(a),len(b)
        left,right=0,0
        result=[]
        
        while left<len1 and right<len2:
            if a[left]==b[right]:
                if not result or result[-1]!=a[left]:
                    result.append(a[left])
                left+=1
                right+=1
                
            elif a[left]<b[right]:
                if not result or result[-1]!=a[left]:
                    result.append(a[left])
                left+=1
                
            else:
                if not result or result[-1]!=b[right]:
                    result.append(b[right])
                right+=1
                
        while left<len1:
            if not result or result[-1]!=a[left]:
                result.append(a[left])
            left+=1
            
        while right<len2:
            if not result or result[-1]!=b[right]:
                result.append(b[right])
            right+=1
            
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")

# } Driver Code Ends