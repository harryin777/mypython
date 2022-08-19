year = 2016
event = 'Referendum'
# f 相当于让{}内的内容，引用了变量，如果没有 f，直接就是一个字符串
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
# 格式化很神奇，很多道道
print('{:1} YES votes  {:2.2%}'.format(yes_votes, percentage))

