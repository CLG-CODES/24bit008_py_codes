#CODE 1: Count how many vowels are there in string. Accept the string from the user
s1=input("");
s=s1.lower()
i=0
count=0;
for i in range (0,len(s)):
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        count=count+1;
print(count)
    
