Python 3.7.0a2 (v3.7.0a2:f7ac4fe, Oct 17 2017, 17:06:29) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> anagram=['cat','dog','fired','god','pat','tap','fried','tac']
>>> grouped_anagram={}
>>> for string in anagrams:
	sorted_string=str(sorted(string))
	if sorted_string in grouped_anagrams:
		grouped_anagrams[sorted_string].append(string)
		else:
			
SyntaxError: invalid syntax
>>> grouped_anagrams[sorted_string]=[string]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    grouped_anagrams[sorted_string]=[string]
NameError: name 'string' is not defined
>>> strings = ["apple", "orange", "grapes", "pear", "peach"]
anagrams = {}
for string in strings:
   key = "".join(sorted(string))
      if string in anagrams.keys():
         anagrams[key].append(string)
      else:
         anagrams[key] = []
         anagrams[key].append(string)
result = ""
for key, value in anagrams.items():
   result += "".join(value) + " "
print(result)
SyntaxError: multiple statements found while compiling a single statement
>>> 
