#coding=utf8

import nltk
#http://www.2cto.com/kf/201403/287479.html
sent='消息/n 源/g 新浪/nz 财经/n 称/v ，/w 针对/p 今日/t 有/v 媒体/n 平台/n 报道/v 央行/n 已经/d 发文/v 暂停/v 比特/q 币/g 交易/n 的/u 消息/n ，/w 接近/v 监管/vn 层/qv 人士/n 对/p 新浪/nz 财经/n 表示/v ，/w 央行/n 确实/ad 下发/v 文件/n ，/w 但/c 并非/v 叫/v 停/v 比特/q 币/g ，/w 而是/c 加强/v 比特/q 币/g 的/u 监管/vn 。/w ';
sTuple=[nltk.tag.str2tuple(t) for t in sent.split()]  #根据文本中的空格进行切分，切分后每一项再转为tuple元组，结构为: ('消息', 'N')
wordsCount=len(sTuple)  #统计词个数
print('总词数：',wordsCount) 
plt=nltk.FreqDist(sTuple) #获取统计结果，结果的结构为：<freqdist: ('，',="" 'w'):="" 5,="" ('币',="" 'g'):="" 3,....="">  每一项后面的数字是该字与其词性组合的出现次数，除了第一项的FreqDist外，后面的结构正好符合字典类型
print('各词性标注统计结果：')
d=dict(plt)  #把统计结果转为字典型，它会删掉不符合字典结构的第一项FreqDist，把后面的结果转存为字典型
for key in d.keys():  #遍历字典，每一类词性的总次数一目了然
    print(key,d[key])