fileout=open("output.txt",'w')
dic1={"0":"a","11":"b","101":"c","100":"d"}
#dic1={"a":"0","b":"11","c":"101","d":"100"}
#dic2={v:k for k,v in dic1.items()}
result=""
dec="0111011000"
p=""
for i in range(len(dec)):
    p+=dec[i]
    if p in dic1:
        result+=dic1[p]
        p=""
fileout.write(result)