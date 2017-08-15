def matched(str):
    count = 0
    for i in str:
    	print i
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    if count < 0 or count == 0:
            print 'all matched'
    else:
    	print 'Something fishy'


string = '(abc)'
matched(string)