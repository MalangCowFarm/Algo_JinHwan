import sys
sys.stdin = open("input.txt")

T = int(input())
kar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for _ in range(T):
    txt = input().split()
    s = ord(txt[0]) - ord('a')
    e = ord(txt[2]) - ord('a')
    print(s, e)