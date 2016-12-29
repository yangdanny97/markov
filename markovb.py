import random

def createDictionary(filename,y):
    '''creates a dictionary with an input text file,
    y specifies the number of words to use per key'''
    file=open(filename)
    string=file.read()
    string=string.replace('"','')
    lst=string.split()
    file.close()

    d={}

    counter=y
    while counter<len(lst):
        x=' '.join(lst[counter-y:counter])
        if x not in d:
            d[x]=[lst[counter]]

        else:
            d[x].append(lst[counter])
        counter+=1

    return d



def generateText(txt,n,y):
    '''generates markov text from a text file,
    n specifies number of words to generate, y specifies number of words to use in each key'''
    counter=y
    d=createDictionary(txt,y)
    a=random.choice(d.keys())
    gen=a.split()
    while counter<n:
        b=' '.join(gen[counter-y:counter])
        if b in d:
            gen.append(random.choice(d[b]))
        else:
            break
            print('wot')
        counter+=1
    print ' '.join(gen)

#sample function call here
generateText('holmes.txt',100,5)
