import argparse

def search(args):
    args = args.split()
    with open('.src/emoji.txt', 'r') as f:
        for line in f:
            emoji = line.split()[0]
            if emoji in args:
                print(emoji)

def main():
    parser = argparse.ArgumentParser(description='i will get u  what u want from emojis :) ')
    parser.add_argument('sentence', help='sentence u wanna to translate it to emoji put the sentence between quoets " "', type=str)
    args = parser.parse_args()
    search(args.srentence)

if __name__ == '__main__':
    main()
