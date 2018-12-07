import re
import time
def get_hyperlinks(url):
    web = {'https://www.wolfram.com': ['https://community.wolfram.com', 'https://www.wolfram.com/contact-us', 'https://www.wolfram.com', 'https://www.wolfram.com/about', 'https://www.wolfram.com/education'], \
           'https://www.wolfram.com/education': ['/pro', '/web-apps', '/pro/pricing', '/pro/pricing'], \
           'https://www.wolfram.com/about': ['https://community.wolfram.com', 'https://www.wolfram.com/contact-us', 'https://www.wolfram.com', 'https://www.wolfram.com/about', 'https://www.wolfram.com/education'], \
           'https://www.wolfram.com/pro': ['/web-apps', '/pro/pricing', '/pro/pricing'], \
           'https://www.wolfram.com/examples/pro-features/image-input/index.html': ['/examples/mathematics/index.html', '/examples/society-and-culture/points-of-interest/index.html', '/examples/science-and-technology/materials/index.html', '/examples/science-and-technology/physics/index.html'], \
           'https://www.wolfram.com/examples/science-and-technology/engineering/index.html': ['/examples/mathematics/index.html', '/examples/society-and-culture/points-of-interest/index.html', '/input', '/examples/science-and-technology/materials/index.html']}
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    assert re.match(regex, url) is not None, "%s is invalid url. Failing." % url
    time.sleep(0.02)
    return web.get(url, [])

url = 'https://www.wolfram.com'

def ParseUrl(Url):
    FetchedTags =[]
    for i in get_hyperlinks(Url):
        FetchedTags.append(i)
    return sorted(FetchedTags)



print(ParseUrl(url))
