def is_palindrome(string: str) -> bool:
    if string == string[::-1]:
        return True
    return False

input_string = "cbbd"

longest_palindromic_substring = ""

for i in range(len(input_string)):
    for j in range(i+1, len(input_string)+1):
        current_substring = input_string[i:j]
        if not is_palindrome(current_substring):
            continue
        if j - 1 - i > len(longest_palindromic_substring):
            longest_palindromic_substring = current_substring

print(longest_palindromic_substring)

