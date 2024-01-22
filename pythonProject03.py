text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
import re

# Split the text into lines
lines = re.split('\n|\xa0 ', text)


capitalized_sentences = []
for line in lines:
  # Split the lines into sentences
  splits = line.split('. ')

  # Capitalize each sentence
  capitalized_split = [split.capitalize() for split in splits]

  #Add each capitalized split list into the main list
  capitalized_sentences.append(capitalized_split)

#Join each sentence in a line then join each line into the full text
capitalized_result = '\n'.join(['. '.join(sentence) for sentence in capitalized_sentences])

# Print the result
print(capitalized_result)
##################################################################
#create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
#split the text based on '.'
lines = capitalized_result.split('.')

for line in lines:
  # Split the lines into words.
  splits = line.split(' ')

  #Add each last word into the main text
  capitalized_result = capitalized_result + splits[-1] + ' '


print(capitalized_result)
##################################################################
#It iz misspelling here. Fix“iz” with correct “is”, but only when it iz a mistake.
import re

# Define a regular expression pattern to find 'iz'
pattern = r' iz '

# Replace all 'iz' in the text with 'is'
fixed_result = re.sub(pattern, ' is ', capitalized_result)

# Print the result
print(fixed_result)
#####################################################################
#  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.

# Define a regular expression pattern to find whitespace characters
pattern = r'[ \t\r\f\v\n]'

# Use re.findall() to find all matches of the pattern in the text
whitespace_occurrences = re.findall(pattern, fixed_result)

# Count the number of occurrences
count_of_whitespace = len(whitespace_occurrences)

# Print the result
print(f"Number of whitespace occurrences: {count_of_whitespace}")
