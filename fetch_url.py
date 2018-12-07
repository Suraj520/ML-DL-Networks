#
# Complete the 'crawl' function below.
#Reading Input
import sys
import re
import time
from threading import Thread
Input=[]
while True:
    try:
        input_ =input().split()
        if input_ == 'EOF':
            break
        Input.append(input_)
    except EOFError:
        pass
#print(Input)       
# The function is expected to return a LIST
# The function accepts following parameters:
#  1. STRING root_url
#  2. INTEGER n_workers
#  3. FUNCTION get_hyperlinks
global get_hyperlinks,Sections
root_url = str(Input[0])
n_workers = int(Input[1])
get_hyperlinks = Input[2:]
get_hyperlinks="\n".join(get_hyperlinks)
exec(get_hyperlinks)
def UniqueSection(url):
    Sections = get_hyperlinks(url)
    OutputTags=[]
    OutputTags.append(url)
    for i in Sections:
        if i.startswith('https')!=True:
            OutputTags.append(root_url + i)
    return OutputTags
# print(get_hyperlinks)


def crawl(root_url, n_workers, get_hyperlinks):
    ThreadRunner=[]
    for j in range(n_workers):
        for k in Sections:
            ThreadRunner.append(threading.thread(target= UniqueSection, args =(k)))
        ThreadRunner[j].start()
        ThreadRunner[j].join()

print(root_url, n_workers,get_hyperlinks)
        
                                                 
        
#    exec(get_hyperlinks)
#    print(get_hyperlinks(root_url))

#    OutputTags=[]
#    for i in get_hyperlinks(root_url):
#        OutputTags.append(i)
#    return get_hyperlinks(root_url)

#print(crawl(root_url,n_workers, get_hyperlinks))

    # Write your code here
