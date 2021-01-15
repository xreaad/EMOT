import argparse

def search(arg):
    arg = arg.lower()
    arguments = arg.split()
    with open('.src/emosnippet', 'r') as f:
        for line in f:
            line = line.lower()
            emoji, name = line.split()[0].lower(), line.split()[1]
            if name in arguments:
                for word in arguments:
                    if word == name:
                        arg = arg.replace(word, emoji)
    print(arg)

def translate_file():
    pass

def main():
    parser = argparse.ArgumentParser(description='i will get u  what u want from emojis :) ')
    parser.add_argument('s', help='sentence u wanna to translate it to emoji put the sentence between quoets " "', type=str)
    parser.add_argument('-f', '--file', help='translate a file to emoji', action='store_true')
    parser.add_argument('-t', help='file to translate, take the full file path ', type=str)
    parser.add_argument('-o', '--output', help='output file after translate', type=str)
    args = parser.parse_args()
    search(args.s)


if __name__ == '__main__':
    main()
