import argparse

def search(args):
    args = args.lower()
    arguments = args.split()
    with open('.src/emosnippet', 'r') as f:
        for line in f:
            emoji, name = line.split()[0].lower(), line.split()[1].lower()           
            if name in arguments:
                for word in arguments:
                    if word == name:
                        args = args.replace(word, emoji)
    print(args)

def main():
    parser = argparse.ArgumentParser(description='i will get u  what u want from emojis :) ')
    parser.add_argument('sentence', help='sentence u wanna to translate it to emoji put the sentence between quoets " "', type=str)
    args = parser.parse_args()
    search(args.sentence)

if __name__ == '__main__':
    main()
