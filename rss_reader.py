import argparse
import requests
import html
from bs4 import BeautifulSoup

parser=argparse.ArgumentParser(description='Pure Python command-line RSS reader.')
exclusive=parser.add_mutually_exclusive_group()
parser.add_argument('--json',action='store_true', help='Print result as JSON in stdout')
parser.add_argument('--verbose',action='store_true',help='Outputs verbose status messages')
parser.add_argument('--limit', type=int,action='store',help='Limit news topics if this parameter provided')
exclusive.add_argument('--version',action='store_true',help='Print version info')
exclusive.add_argument('source',nargs='?',help='RSS URL',default=None)
args=parser.parse_args()


version='v1.0'
err={1: 'You don\'t use --version together with other arguments',
    2: 'Source or --version expected',
    3: 'Incorrect limit input'}


class Error(Exception):
    def __init__(self, code):
        self.error=code


class News:
    def __init__(self,wall_of_text):
        self.title=convert_to_readable(wall_of_text,'title',False)
        self.source=convert_to_readable(wall_of_text,'link/',False)
        self.date=convert_to_readable(wall_of_text,'pubdate',False)
        self.content=convert_to_readable(wall_of_text,'description',False)
        self.images=convert_to_readable(wall_of_text,'img src=',True)

    def show_fields(self):
        print('\n\n'+'Title: '+self.title)
        print('Link: '+self.source)
        print('Date: '+self.date)
        print('\n'+self.content)
        print('\nImage: '+self.images)


def verboser(func,action):
    def wrapper(*args, **kwargs):
        print('Started '+action)
        result=func(*args,**kwargs)
        print('Finished '+action)
        return result
    return wrapper

def ultimately_unescape(str):
    while html.unescape(str)!=str:
        str=html.unescape(str)
    return str

def cut_tags(text, cutfrom,tag_name):
    while text[cutfrom]=='<':
        cutfrom=text.find('>',cutfrom)+1
    return cutfrom

def convert_to_readable(text,tag_name,is_in_tag):
    text=ultimately_unescape(str(text))
    cutfrom=text.find(tag_name)+len(tag_name)+1
    cutfrom=cut_tags(text,cutfrom,tag_name)
    if not is_in_tag:
        cutto=text.find('<',cutfrom)
    else:
        cutto=text.find('"',cutfrom)
    return text[cutfrom:cutto] if cutfrom>len(tag_name) else 'None'


def retrieve_news(link, limit):
    soup=requests.get(link).text
    soup=BeautifulSoup(soup,"html5lib")
    title=convert_to_readable(soup,'title',False)
    print('\nSource: '+title)
    content=soup('item')
    news=[]
    for item in (content[:min(limit,len(content))] if limit else content):
        news.append(News(item))
    return news


def make_json(*args):
    pass

def print_news(news):
    for item in news:
        item.show_fields()


if args.version and (args.json or args.limit):
    raise Error(err[1])
if not (args.version or args.source):
    raise Error(err[2])
if args.limit and args.limit<1:
    raise Error(err[3])

if args.version:
    print('Current version of RSS-reader: '+version)
else:
    if args.verbose:
        print_news=verboser(print_news,'printing')
        retrieve_news=verboser(retrieve_news,'retrieving')
        make_json=verboser(make_json,'making JSON')
    news=retrieve_news(args.source,args.limit)
    print_news(news)
    if args.json:
        make_json(news)
