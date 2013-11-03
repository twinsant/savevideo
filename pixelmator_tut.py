# Download Pixelmator tutorial videos from vimeo.
# by twinsant
import requests
from pyquery import PyQuery

from savevideo import get_download_links
from savevideo import download_video

if __name__ == '__main__':
    # Get all vimeo urls in tutorial page
    session = requests.Session()
    r = session.get('http://www.pixelmator.com/tutorials/')
    d = PyQuery(r.text.encode('utf8'))
    hrefs = d('a')
    urls = set()
    for href in hrefs:
        a = PyQuery(href).attr.href
        if a.startswith('https://vimeo.com'):
            urls.add(a)
    for url in sorted(list(urls)):
        print 'Get video links for %s' % url
        # With help of savevideo.me
        links = get_download_links(url)
        for link in links:
            video_url, profile = link
            # Exclude HD and Mobile versions
            if profile.find('(MP4 format)')!=-1:
                download_video(video_url)
