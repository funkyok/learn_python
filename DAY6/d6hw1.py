num = 1
score = []
while num < 11:
    judge = input('请评委'+ str(num) + '输入您要打的分数:(大于等于5且小于等于10的数字)')
    if 5 <= float(judge) <= 10: 
        score.append(float(judge))
        num += 1
    else:
        print('输入错误，请重新输入：')
# nscore = 0
# for i in score:
#     nscore += score[i]
# final_score = nscore / len(score)
final_score = sum(score) / len(score)

print('参赛选手的平均分为:' + str(final_score))