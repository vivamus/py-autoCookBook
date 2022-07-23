import argparse
import sys
from datetime import datetime
import configparser

def main(n1,n2,out):
    print(f'[{datetime.utcnow().isoformat()}] result of {n1} * {n2} is {n1*n2}', file=out)

if __name__ == '__main__':
    # ArgumentDefaultsHelpFormatter -- gives defaults with -h
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config', type=argparse.FileType('r'), help='config file',default='/etc/automate.ini')
    parser.add_argument('-o',help='output', default=sys.stdout, dest='output', 
          type=argparse.FileType('a'))
    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        # Transforming values into integers
        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])
    main(args.n1, args.n2, args.output)