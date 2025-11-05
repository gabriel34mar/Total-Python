text = input("Enter a random text: ")
a = input("Enter a random letter: ")
b = input("Enter a random letter: ")
c = input("Enter a random letter: ")
initial=text[0]
final=text[-1]
reverse_words = text.split()[::-1]
text_lower = text.lower()   # Convertimos todo a minúsculas

count_a = text_lower.count(a.lower())
count_b = text_lower.count(b.lower())
count_c = text_lower.count(c.lower())

print(f"The letter '{a}' appears {count_a} times.")
print(f"The letter '{b}' appears {count_b} times.")
print(f"The letter '{c}' appears {count_c} times.")

print(f"The length of the text is {len(text)}")
print(f"The initial letter is {initial}")
print(f"The last letter is{final}")
print(reverse_words)
print(bool('python' in text_lower))