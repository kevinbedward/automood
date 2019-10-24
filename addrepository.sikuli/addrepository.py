from sikuli import *

#setBundlePath(r"C:\sik\IN11795.sikuli\rep-man-images")
def outputErrorToFile(message):
    my_dir = "c:\\sik\\IN11795.sikuli\\rep-man-images\\ERROR_LOGS\\" 
    el = "\n"
    my_file=file(my_dir + "TEST_ERRORS.txt" , "a")
    my_file.write(message+el)
    my_file.close()
    
    #Test that all 3 tabs exist on repository manager, if not, report it but complete the test
    if exists("repmanfiletab.PNG"):
        click("repmanfiletab.PNG")
    else:
        outputErrorToFile("Repository Manager - File tab missing.")
    
    if exists("repmanrepositoriestab.PNG"):
        click("repmanrepositoriestab.PNG")
    else:
        outputErrorToFile("Repository Manager - Repositories tab missing.")
    
    if exists("repmanservertab.PNG"):
        click("repmanservertab.PNG")
    else:
        outputErrorToFile("Repository Manager - Servers tab missing.")
    click("repmanrepositoriestab.PNG")
    
def addRep():
    if exists("addarepository.PNG"):
        click("addarepository.PNG")
    else:
        outputErrorToFile("Repository Manager - Add Repository button missing.")        
    
    if exists("repositorynamefield.PNG"):
        type("MooD Test")
        type(Key.TAB + Key.TAB + Key.TAB + Key.TAB + Key.TAB + Key.BACKSPACE + Key.BACKSPACE)
        type("sa" + Key.TAB) 
        type("Ts0rg123") 
        click("createbutton.PNG")
        wait(4)
    else:
        popError("Test Failure. Unable to create a new Repository")
        #good point to add the end of test timestamp
        #outputErrorToFile("Repository Manager - Servers tab missing.") 