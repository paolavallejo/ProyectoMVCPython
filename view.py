from model import Person

def showAllView(list):
    print('In our db we have %i users. Here they are:' % len(list))
    for item in list:
        print( item.name())
        
def startView():
    print( 'MVC - the simplest example')
    print( 'Do you want to see everyone in my db?[y/n]')

def endView():
    print( 'Goodbye!')
    
    
    
    
 #Fuente: https://www.it-swarm-es.com/es/python/mvc-el-ejemplo-mas-simple/825830948/