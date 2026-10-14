from functions.get_file_content import get_file_content

content: str = get_file_content("calculator", "lorem.txt")

print(f"lorem.txt length: {len(content)}")
print(f"lorem.txt truncated: {'truncated' in content}")
test1: str = get_file_content("calculator", "main.py")
test2: str = get_file_content("calculator", "pkg/calculator.py")
test3: str = get_file_content("calculator", "/bin/cat")
test4: str = get_file_content("calculator", "pkg/does_not_exist.py")

print(test1)
print(test2)
print(test3)
print(test4)
