import os
import shutil

def createDirectory(urlName):
    try:
        os.mkdir(urlName)
        
    except FileExistsError:
        ""
        
        
def moveFiles(file, dirName):
    x = os.getcwd()
    
    try:
    
        shutil.move(f"{x}\\{file}", f"{x}\{dirName}")
        
    except shutil.Error:
        ""
        
        
def directoryName(urlName):
    if urlName.startswith("https://"):
        urlName = urlName.replace("https://", "")
        
    elif urlName.startswith("http://"):
        urlName = urlName.replace("http://", "")
        
    urlName = urlName[0: urlName.index(".")]
    
    return urlName



        
        

        

    
    
            
    
    
    
        
        

        
        
        
        
        






































































