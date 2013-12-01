'''
Created on Dec 1, 2013

@author: arch119
'''
import smtplib

class GMail(object):
    '''
    classdocs
    '''
    gmail_smtp_server = "smtp.gmail.com"
    gmail_smtp_port = 587
    
    def __init__(self,email,pwd):
        '''
        Constructor
        '''
        self.gmail_user = email
        self.gmail_pwd = pwd
        
    def send_email(self,recepients,subject,content):
        gmail_user = self.gmail_user
        gmail_pwd = self.gmail_pwd
        FROM = gmail_user
        TO = recepients #must be a list
        SUBJECT = subject
        TEXT = content

        # Prepare actual message
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP(GMail.gmail_smtp_server, GMail.gmail_smtp_port) #or port 465 doesn't seem to work!
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print 'successfully sent the mail'
        except:
            print "failed to send mail"