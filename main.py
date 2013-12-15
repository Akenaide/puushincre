"""
Created on 7 août 2013

@author: KMS
"""
from CharPuush import CharPuush
import webbrowser


def mkparser():
    import argparse

    parser = argparse.ArgumentParser(description='Puush increment')
    parser.add_argument('--link', help='beginning of increment')
    parser.add_argument('number', help='number of link', type=int)

    return parser.parse_args()

def main():
    args = mkparser()

    entry = args.link
    # entry = input('lien puush :')
    link = entry[14:]
    link = link.split('.')[0]
    idPuush = list()
    continu = 1

    for charac in link:
        temp = CharPuush(charac)
        idPuush.append(temp)

    while continu == 1:
        #n = int(input("nombre de tour : "))
        number_iteration = args.number
        i = 0
        while i < number_iteration:
            rank = 1

            while idPuush[-rank].incre():
                rank += 1

            temp = "".join(x.get_value() for x in idPuush)
            webbrowser.open_new('http://puu.sh/'+temp)
        continu = int(input("1. pour continuer"))

if __name__ == '__main__':
    main()