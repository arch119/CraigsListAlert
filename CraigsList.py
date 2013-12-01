'''
Created on Dec 1, 2013

@author: arch119
'''
from pyquery import PyQuery as pq


class CraigsListRow(object):
    def __init__(self,baseurl,elem):
        self.base_url = baseurl
        self.elem = elem
    
    def get_text(self):
        return self.elem.text()
    
    def get_url(self,relative=False):
        a = self.elem.children("a")
        if relative:
            return a.attr("href")
        else:
            return self.base_url+a.attr("href")
    
    def get_data_pid(self):
        return self.elem.attr("data-pid")
    
class CraigsList(object):
    '''
    classdocs
    '''
    base_url = "http://tokyo.craigslist.jp"

    def __init__(self,rel_url):
        '''
        Constructor
        '''
        self.url = CraigsList.base_url + rel_url
        self.html = None
        
    def get_html(self,force=False):
        if force:
            self.html = None
            
        if self.html != None:
            return self.html
        
        try:
            self.html = pq(url=self.url)
        except:
            self.html = None
        return self.html
    
    def get_rows(self):
        html = self.get_html()
        if html == None:
            return None
        rows = []
        for row in html(".row").items():
            rows.append(CraigsListRow(CraigsList.base_url,row))
        return rows
    
    def print_rows(self):
        rows = self.get_rows()
        if rows.__class__ == list:
            for row in rows:
                print row.get_text() + " " + row.get_url() + "[" + row.get_data_pid() + "]"

class CraigsListPosting(CraigsList):
    def __init__(self,rel_url):
        CraigsList.__init__(self,rel_url)
        
    def get_posting_title(self):
        html = self.get_html()
        if html == None:
            return None
        return html(".postingtitle").text()
    
    def get_reply_to(self):
        html = self.get_html()
        if html == None:
            return None
        a = html(".dateReplyBar").children("a")
        return a.text()
    
    