with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("Файлдағы мәтін:")
print(content)

upper_content = content.upper()

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(upper_content)