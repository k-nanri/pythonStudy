import click
import time

def progress():

    total_size = 20
    with click.progressbar(fill_char="*",
                           empty_char=" ",
                           bar_template='%(label)s  |%(bar)s|  %(info)s',
                           length=total_size) as bar:
        
        count = 0
        while True:
             bar.update(1)
             count += 1
             time.sleep(0.5)
             if count == total_size:
                 break

if __name__ == '__main__':
    progress()