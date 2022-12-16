def parser(s):
    l = []
    c = ""
    for i in range(len(s)):
        print(s[i], end = "")
        if s[i]!=" " and s[i]!="\n" and i!=len(s)-1:
            c += s[i]
        elif i==len(s)-1:
            c+=s[i]
            l.append(c)
            c=""
        else:
            l.append(c)
            c=""
    return l

print(parser("je fais des tests"))