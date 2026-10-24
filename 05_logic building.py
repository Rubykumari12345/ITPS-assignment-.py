# 5. check karo ki string palindrome hai ya nahi:
s = input("String: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")