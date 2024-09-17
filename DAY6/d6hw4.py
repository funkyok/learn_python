cars = ['鲁A32444','鲁B12333','京B8989M','黑C49678','黑C46555','沪B25041']
locals = {'沪':'上海','黑':'黑龙江','鲁':'山东','鄂':'湖北','湘':'湖南','京':'北京'}

result = {}
lis = []
for i in cars:
    lis.append(i[0])
for i in lis:
    if result.get(locals.get(i)) == None:
        result.setdefault(locals.get(i),1)
    else:
        result[locals.get(i)] += 1
print(result)