import argparse
import sys
import configparser

def main(n1,n2,output):
    print(f'result of {n1}*{n2} is {n1*n2}', file=output) # f-string with defined vars

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='num 1', default=1)    
    parser.add_argument('-n2', type=int, help='num 2', default=1)
    parser.add_argument('-c', '--config', type=argparse.FileType('r'), help='config file')
    parser.add_argument('-o', dest='output',type=argparse.FileType('w'),
        default=sys.stdout,help='output file')
    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])
    main(args.n1, args.n2, args.output)