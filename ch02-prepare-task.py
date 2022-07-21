import argparse

def main(n1,n2):
    result = n1 * n2
    print(f'result of {n1}*{n2} is {result}') # f-string with defined vars

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='num 1', default=1)    
    parser.add_argument('-n2', type=int, help='num 2', default=1)
    args = parser.parse_args()
    main(args.n1, args.n2)