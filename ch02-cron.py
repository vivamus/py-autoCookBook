import argparse
import sys
from datetime import datetime
import configparser

def main(n1,n2,out):
    print(f'[{datetime.utcnow().isoformat()}] result of {n1} * {n2} is {n1*n2}', file=out)
    