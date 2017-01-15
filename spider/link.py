#!/usr/bin/env python
# coding=utf-8

import re

def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
    # filter for links matching our regular expression
    for link in get_links(html):
        if re.match(link_regex, link):
            crawl_queue.append(link)
def get_links(html):

