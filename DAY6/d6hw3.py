dic = {
    '-' : 'fu',
    '0' : 'ling',
    '1' : 'yi',
    '2' : 'er',
    '3' : 'san',
    '4' : 'si',
    '5' : 'wu',
    '6' : 'liu',
    '7' : 'qi',
    '8' : 'ba',
    '9' : 'jiu',
    '.' : 'dian',
}
target = str(input('请输入一个数字：'))
lis = list(target)
result_target = []
for i in lis:
    print(dic.get(i), end = ' ')
