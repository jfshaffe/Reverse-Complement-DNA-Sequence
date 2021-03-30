def main():   
    k = input("DNA sequence ")
    s = k[::-1]
    b = s.upper()
    l = b.replace('G', 'Z')
    m = l.replace('C', 'G')
    r = m.replace('A', 'Q')
    e = r.replace('T', 'A')
    p = e.replace('Z', 'C')
    u = p.replace('Q', 'T')
    print(u)
main()
