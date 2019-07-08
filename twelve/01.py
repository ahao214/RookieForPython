# sys模块

import sys
sys.path.append('/test')

print(sys.platform)

print(sys.argv[0])


if len(sys.argv) == 2:
    print(sys.argv[1])

s = sys.stdin.read(6)
print(s)



