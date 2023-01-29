s = "1my-first2_name = Mario"
print (s)
t =''.join([i for i in s if not i.isdigit()])
z = t.replace ('-','' '')
y = z.replace('_', '')
print(y)