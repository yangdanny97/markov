import random

def createDictionary(filename):
  """imports a txt file and creates a dictionary of word associations for use with the markov text generator
  this dictionary lists the words that can be used to start a sentence under the key '$'
  """
  file=open(filename)
  string=file.read()
  lst=string.split()
  file.close()
  
  d={}
  d['$']=[lst[0]]

  counter=1
  while counter<len(lst):
    if lst[counter-1][-1] or lst[counter-1][-2]=='.' or '?' or '!':
      d['$'].append(lst[counter])
    
    elif lst[counter-1] not in d:
      d[lst[counter-1]]=[lst[counter]]
    
    else:
      d[lst[counter-1]].append(lst[counter])
    counter+=1
  
  return d



def generateText(d,n):
"""inputs: 
      d- a text dictionary generated using createDictionary
      n- an integer representing the number of words to generate
  outputs: prints a string of the generated text """

  counter=1
  gen=[random.choice(d['$'])+' ']
  while counter<n:
    if gen[counter-1][-1] or gen[counter-1][-2]=='.' or '?' or '!':
      gen.append(random.choice(d['$'])+' ')
    else:
      gen.append(random.choice(d[str(gen[counter-1])])+' ')
    counter+=1
  print ''.join(gen)

#sample function call, generate 5000 words based on the provided oscarwilde.txt (the preface to Picture of Dorian Gray)
generateText(createDictionary('oscarwilde.txt'),5000)