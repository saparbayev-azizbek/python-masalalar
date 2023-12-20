vec = [2,3,5,7]
a = [2,3,5,7]
s = ''
for q in a:
    for w in a:
        s = s + str(q) + str(w)
        vec.append(s)
        for e in a:
            s = s + str(q) + str(w) + str(e)
            vec.append(s)
            for r in a:
                s = s + str(q) + str(w) + str(e) + str(r)
                vec.append(s)
                for t in a:
                    s = s + str(q) + str(w) + str(e) + str(r) + str(t)
                    vec.append(s)
                    for y in a:
                        s = s + str(q) + str(w) + str(e) + str(r) + str(t) + str(y)
                        vec.append(s)
                        for u in a:
                            s = s + str(q) + str(w) + str(e) + str(r) + str(t) + str(y) + str(u)
                            vec.append(s)
                            for i in a:
                                s = s + str(q) + str(w) + str(e) + str(r) + str(t) + str(y) + str(u) + str(i)
                                vec.append(s)
                                for o in a:
                                    s = s + str(q) + str(w) + str(e) + str(r) + str(t) + str(y) + str(u) + str(i) + str(o)
                                    vec.append(s)
vec.sort()
print(vec, end=" ")