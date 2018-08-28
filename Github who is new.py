import urllib.request as urlR
import time, re

###  Searching for new users  ###
def check( ):
    f_Old = open("old", 'r+');
    f_New = open("new", 'r');
    nowe = [];
    stare = [];
    test = [];

    ###  Add new and old users to arrays  ###
    for lineO in f_Old:
        stare.append(lineO)
    for lineN in f_New:
        nowe.append(lineN)

    '''  If in 'old' array element != 'new' array element pushing
        this new user to 'test' array  '''
    for i in range(0,len(nowe)):
        if nowe[i] not in stare:
            test.append(nowe[i])

    ###  Writing new users to 'old' file  ###
    for i in range(0,len(test)):
        f_Old.write(test[i]);

    ###  Showing new users  ###
    for i in range(0,len(test)):
        print(test[i])

    ###  Closing all files  ###
    f_New.close();
    f_Old.close();

def __main__():
    ###  Opening all needed files  ###
    urlString = open('source.txt','r')
    time.sleep(1);
    f_New = open("new", 'w+');
    

    ###  Reading a page  ###
    data = urlR.urlopen(urlString.read());
    nicks = re.findall(r'<a href="/+\w*', str(data.read()));
    i=0;
    for nick in nicks:
        if(i%2==0):
            f_New.write(nick[10:]+"\n");
        i=i+1;     
    
    ###  Closing all files  ###
    f_New.close();

    check()

__main__();


