a="a:b:c:d"

b=a.split(":")
c='#'.join(b)

print(c)

c=a.replace(':','#')
print(c)