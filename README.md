My markov text generator in python.

Edit: there are two versions, markov and markovb

Version 1:
This is pretty basic, it takes a txt file as input and creates a dictionary.
For each different word in the input file, the dictionary makes a list of the words that follow that word.
In addition, there is a list of words that can be used to start sentences.
The generate function takes two inputs, the dictionary (which must be generated separately), and the number of words to generate.

Version 2:
This version allows the user to determine how long the keys in the dictionary are. For example, you can have an entry of {'there is':'one'} in the dictionary (key length=2) which will generate 'one' if 'there is' were the last two words that were generated.

This needs to be run in console, a sample function call is provided in the code.
