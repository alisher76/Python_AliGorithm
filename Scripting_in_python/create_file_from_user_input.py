"""
Write a script that prompts the user for:

    A file_name where it should write the content.
    The content that should go in the file. 
    The script should keep accepting lines of 
    text until the user enters an empty line.

"""

def get_file_name(reprompt=False):
    if reprompt:
        print("Please enter a file name.")

    file_name = input("Destination file name: ").strip()
    return file_name or get_file_name(True)

file_name = get_file_name()

print("Please enter your content. Entering an empty line will write the content to {}".format(file_name))

with open(file_name, 'w+') as f:
    eof = False
    lines = []

    while not eof:
        line = input()
        if line.strip():
            lines.append("{}\n".format(line))
        else:
            eof = True

    f.writelines(lines)
    print("Lines written to {file_name}")