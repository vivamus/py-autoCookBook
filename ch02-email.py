import argparse 
import configparser
import smtplib #sic!
from email.message import EmailMessage

def main(email_to,server,port,email_from,passwd):
    print(f"send email from '{email_from}' to '{email_to}'")
    subject = 'my subject'
    text = '''my text'''
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = email_from    
    msg['To'] = email_to

    server = smtplib.SMTP_SSL(server,port)
    server.login(email_from,passwd)
    server.set_msg(msg)
    server.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email', type=str, help='destination email') # to args.email
    parser.add_argument('-c', dest='config', type=argparse.FileType('r'),help='config file', default=None)
    args = parser.parse_args()
    if not args.config:
        print('Error, a config file is required')
        parser.print_help()
        exit(1)
    config = configparser.ConfigParser()
    config.read_file(args.config)
    main(args.email,
        server=config['DEFAULT']['server'],
        port=config['DEFAULT']['port'],
        email_from=config['DEFAULT']['email'],
        password=config['DEFAULT']['password'])