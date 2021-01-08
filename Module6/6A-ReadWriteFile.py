def main():
    # opens a file for reading only...
    file = open('colors.txt', 'r')

    # a list to hold the colors...
    colors = []

    # read each line and add it to the list...
    for line in file:
        colors.append(line)

    # don't forget to close the file...
    file.close()

    # opens a file for writing, beware: if the file already exists,
    # its contents will be emptied...
    file = open('colors2.txt', 'w')
    for color in colors:
        file.write(color.upper())
    file.close()

    # opens a file for appending...
    file = open('colors2.txt', 'a')
    file.write('\nGREEN')
    file.close()

main()

    