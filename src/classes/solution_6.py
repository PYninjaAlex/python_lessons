def reverse(string: str) -> str:
    list_string = string.split()
    output = ''
    for i in range(len(list_string)-1, -1, -1):
        output += f"{list_string[i]} "
    return output

print(reverse("The quick brown fox jumps over the lazy dog"))