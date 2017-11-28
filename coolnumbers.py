ncool = 100001 * [0]
for n in xrange(5, 100001):
    nc = 0
    bn = bin(n)[2:]
    pos = -2
    while True:
        pos = bn.find("101", pos + 2)
        if pos >= 0:
            nc += 1
        else:
            break
    ncool[n] = nc
    

def solve(r,k):
    return sum(1 if ncool[i] >= k else 0 for i in xrange(5,r+1))
    

def main():
    t = input()
    for _ in xrange(t):
        r, k = map(int, raw_input().split())
        print solve(r,k)
        
        
main()