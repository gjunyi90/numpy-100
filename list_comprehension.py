# ls = list()
#
# for element in range(10):
#     if not(element % 2):
#         ls.append(element)
# ls = list(filter(lambda element: not(element % 2),range(10)))



# ls = [element for element in range(10) if not (element % 2)]
#
# print(ls)


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
# for word in words:
#       if word != "the":
#           word_lengths.append(len(word))
# print(words)

word_lengths = [len(word) for word in words if not word == 'the']
print(word_lengths)


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
print(newlist)

newlist = [int(number) for number in numbers if number > 0]
print(newlist)

results = [number for number in range(1000) if number % 7 == 0]
print(results)

results = [number for number in range(1000) if str(number).find('3')>0]
print(results)

teststring = 'Find all of the words in a string that are less than 4 letters'
results = [word for word in teststring.split(' ') if len(word)<4]
print(results)

#Remove all of the vowels in a string [make a list of the non-vowels]
teststring = 'Find all of the words in a string that are less than 4 letters'
vowels = ['a','e','i','o','u',' ']
nonvowels = [letter for letter in teststring if letter not in vowels]
print(nonvowels)

sentence = 'Use a dictionary comprehension to count the length of each word in a sentence'
results = {word:len(word) for word in sentence.split()}
print(results)


results = [number for number in range(1001) if True in [True for divisor in range(8,9) if number % divisor == 0]]
print(results)