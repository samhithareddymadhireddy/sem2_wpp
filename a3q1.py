text="heLlO wORld"
for i in range(0,11,2):
    ch=text[i]
    p=ch.upper()
    print(p)
    if(i<10):
        ch=text[i+1]
        p=ch.lower()
        print(p)

