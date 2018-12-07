#
# Complete the 'crawl' function below.
#Reading Input
import sys
import re
import time
import threading
Input=[]
while True:
    input_ =input()
    if input_ == 'EOF':
        break
    Input.append(input_)
#print(Input)       
# The function is expected to return a LIST
# The function accepts following parameters:
#  1. STRING root_url
#  2. INTEGER n_workers
#  3. FUNCTION get_hyperlinks

root_url = str(Input[0])
n_workers = int(Input[1])
get_hyperlinks = Input[2:]
get_hyperlinks="\n".join(get_hyperlinks)
exec(get_hyperlinks)
global Sections
Sections = get_hyperlinks(root_url)


# print(get_hyperlinks)



def crawl(root_url, n_workers, get_hyperlinks):
    OutputTags=[]
    for i in Sections:
        OutputTags.append(i)
    
        
#    exec(get_hyperlinks)
#    print(get_hyperlinks(root_url))

#    OutputTags=[]
#    for i in get_hyperlinks(root_url):
#        OutputTags.append(i)
#    return get_hyperlinks(root_url)

print(crawl(root_url,n_workers, get_hyperlinks))

    # Write your code here
