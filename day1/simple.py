#simple.py
languages= ['python','perl','c','java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%4s need compiler" % lang)
    else:
        print("should not reach here")