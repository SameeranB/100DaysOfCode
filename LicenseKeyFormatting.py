# Day 9 - 21st August 2020
# This question was solved on leetcode

# Important Takeaway - Try to avoid looping if working with strings. String manipulation can be very powerful.


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = list(S)
        currentpos = len(S)-1
        partLength = 0
        output = []
        
        while currentpos>=0:
            
#             If it's a -, skip it and keep skipping if you keep getting -
            while S[currentpos] == '-':
                if not currentpos<0:
                    currentpos-=1
                else:
                    break
            
            if not currentpos<0:
                
                if S[currentpos].isalpha():
                    S[currentpos] = S[currentpos].upper()
                
                output.insert(0, S[currentpos])
                partLength+=1
                
                if partLength==K and currentpos>0:
                    output.insert(0, '-')
                    partLength=0
                
                currentpos-=1
                
                
            else:
                break
            
            
        pos = 0
        while len(output)>0 and not output[pos].isalnum():
            output = output[pos+1:]
            pos+=1
        
        return ''.join(output)
        
