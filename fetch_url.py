#
# Complete the 'crawl' function below.
#Reading Input
import sys
import re
import time
from threading import Thread
Input=[]



def crawl(root_url, n_workers, get_hyperlinks):
    
    def UniqueSection(url):
        Sections = get_hyperlinks(url)
        OutputTags=[]
        OutputTags.append(url)
        for i in Sections:
            if i.startswith('https')!=True:
                OutputTags.append(root_url + i)
        return OutputTags

    # print(UniqueSection('https://www.openai.com'))
    uricollec=[]
    def recur(url):
        for i in get_hyperlinks(url):
            uricollec.append(i)
            get_hyperlinks(i)
    recur(root_url)
    return uricollec
