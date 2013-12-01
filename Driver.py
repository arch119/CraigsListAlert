'''
Created on Dec 1, 2013

@author: arch119
'''
from Mail import GMail
from CraigsList import CraigsList
from time import sleep
import sys

def get_url(alias):
    url_map = { 'bose' : '/search/ela?query=bose',
                'air' : '/search/sya?query=air'
               }
    return url_map[alias]
    
def rows_to_str(rows):
    strrep = ""
    for row in rows:
        strrep += row.get_text() + " " + row.get_url() + " [" + row.get_data_pid() + "]\n"
    return strrep

def send_alert(rows):
    email_from = "<temp gmail address>@gmail.com"
    email_to = ["<my junk free mobile email address for realtime notification>@i.softbank.jp"]
    email_subject = "New Updates"
    email_body = rows_to_str(rows)
    
    if len(rows) < 1:
        return
    else:
        g = GMail(email_from,"<password for temp gmail address>")
        g.send_email(email_to,email_subject,email_body)
    
    
def fetch_latest(list_url,last_posting_id):
    c = CraigsList(list_url)
    rows = c.get_rows()
    if rows == None:
        return last_posting_id

    rows_new = []
    max_pid = 0
    for row in rows:
        pid = row.get_data_pid()
        if pid > last_posting_id:
            rows_new.append(row)
        if pid > max_pid:
            max_pid = pid
    if max_pid <= last_posting_id:
        return last_posting_id
    
    print "Sending alert..."
    print rows_to_str(rows_new)
    send_alert(rows_new)
    return max_pid
    
if __name__ == '__main__':
    alias = 'bose'
    if len(sys.argv)> 1:
        alias = sys.argv[1]
        
    list_url = get_url(alias)
    last_posting_id = 0
    if len(sys.argv) > 2 :
        last_posting_id = sys.argv[2]
    
    while True:
        print "Fetching data..."
        last_posting_id = fetch_latest(list_url,last_posting_id)
        sleep(300)
