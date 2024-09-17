lst = ['金瓶梅','解救吾先生','美国往事','西西里的美丽传说']
dic = {}

for i in lst:
    score = input('请输入您对电影' + str(i) + '的评分：（1-100分）')
    dic.setdefault(i,score)
print(dic)
