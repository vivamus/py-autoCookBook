import argparse
import sys
import logging
LOG_FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
LOG_LEVEL = logging.DEBUG

def main(n1,n2,out):
    print(f'{n1} / {n2} = {n1/n2}',file=out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1',type=int,default=1,help='numerator')
    parser.add_argument('-n2',type=int,default=1,help='denom')
    parser.add_argument('-o',dest='out',type=argparse.FileType('a'),default=sys.stdout,help='out')
    parser.add_argument('-l',type=str,dest='log',help='logfile')
    args = parser.parse_args()
    if args.log:
        logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL, filename=args.log)
    else:
        logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

    try: 
        main(args.n1,args.n2,args.out)
    except Exception as exc:   # Pokemon exception -- catch them all
        logging.exception("Error running task")
        print('There has been an error. Check the logs.')
        exit(1)





