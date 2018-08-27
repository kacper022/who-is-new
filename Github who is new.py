import urllib.request as urlR
import time, re

def __main__():
    ###  Opening all needed files  ###
    urlString = open('source.txt','r')
    time.sleep(1);
    f_Old = open("old", 'r');
    f_New = open("new", 'r+');
    testFile = open("testFile", 'w');
    

    ###  Reading a page  ###
    data = urlR.urlopen(urlString.read());
    nicks = re.findall(r'<a href="/+\w*', str(data.read()));
    for nick in nicks:
        
        ###  Showing all users in fork  ###
        print(nick[10:]);
        


    ###  Closing all files  ###
    urlString.close()
    f_Old.close();
    f_New.close()

__main__();


