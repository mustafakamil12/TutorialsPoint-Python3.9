#www.facebook.com/CSxFunda
#Extract weights without using regular expressions

#read the text file having weights
fp=open('weights.txt','r')
text=fp.read()

#extract the weights without using regular expressions
#lengthy and complex code
weights=[]
for i in range(len(text)-1):
    sub=text[i:i+2]
    if sub.isdecimal():
        weights.append(sub)
		
#display the weights       
print(weights)
        
