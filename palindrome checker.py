word = input("Enter a word to know if it is a palindrome: ").strip().lower()
palindrome_checker = []

# Reverse the word and store each character in the list
for i in word[::-1]:
    palindrome_checker.append(i)

reversed_string = ''.join(palindrome_checker)

# Check if the original word matches the reversed word
if word == reversed_string:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
