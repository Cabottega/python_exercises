sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper()


print(sentence)
print(sentence_two)

sentence_three = 'The quick brown fox jumped'.title()

print(sentence_three)

# instructor notes
# uppercase. Note that s.upper().isupper() might be False > if s contains uncased characters or if the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. > “Lt” (Letter, titlecase).

# str.capitalize()
# Return a copy of the string with its first character capitalized and the rest lowercased.

# str.lower()
# Return a copy of the string with all the cased characters [4] converted to lowercase.
# """
