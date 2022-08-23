# command to find any word from multiple of line

a = "hello ali! how are you?"
print(len(a))
if "ali" in a:
    starting_index = 6 - len(a)
    ending_index = starting_index + 3

    print(a[starting_index:ending_index])
