zhubo = {'卢本伟':'222000','冯提莫':'189999','金老板':'99999','吴老板':'250000','alex':'126'}

#计算主播平均收益值
lis = []
for i in zhubo.values():
    lis.append(int(i))
print('主播们的平均收益是：' + str(sum(lis) / len(lis)) + '元')

#干掉小于平均值的主播
lis2 = []
for k, i in zhubo.items():
    if int(i) <= sum(lis) / len(lis):
        print(str(k) + '收益' + str(i) + '元，小于平均值，干掉')
        lis2.append(k)
for i in lis2:
    zhubo.pop(i)                
print(zhubo)

#干掉卢本伟
zhubo.pop('卢本伟')
print('干掉卢本伟')
print(zhubo)
        