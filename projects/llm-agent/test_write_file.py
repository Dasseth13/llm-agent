from functions.write_file import write_file

test1: str = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(test1)
test2: str = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(test2)
test3: str = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
