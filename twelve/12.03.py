import os
if not os.path.exists('newdir1'):
    os.mkdir('newdir1')

if not os.path.exists('newdir2'):
    os.mkdir('newdir2', 0o377)



try:
    # 删除newdir1目录，如果目录为空，则抛出一个OSError异常
    os.rmdir('newdir1')
except OSError as e:
    print(e)

try:
    os.rmdir('newdir2')
except OSError as e:
    print(e)



