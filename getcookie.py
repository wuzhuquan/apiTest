import http.cookiejar, urllib.request
from urllib.parse import urlencode


def getcookie():
    #生成cookie
    cookiejar = http.cookiejar.CookieJar()
    urlOpener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
    values = {
        'JSESSIONID': '977CC810042581C21FF48F86C27BF742'
    }
    cookiedata = urlencode(values)
    return cookiedata
