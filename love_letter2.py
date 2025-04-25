s=input("enter string")

l=len(s)
temp=l

count=0


left=l//2-1
if l%2==0:
    right=l//2
else:
    right=l//2+1

while left>=0 and right<l:
    if s[left]>s[right]:
        count+=ord(s[left]) - ord(s[right])
        left-=1
        right+=1
    
    elif s[left]<s[right]:
        count+=ord(s[right]) - ord(s[left])
        left-=1
        right+=1

    else:
        left-=1
        right+=1

print(count)