from addrepository import *

def openNewRep():
    doubleClick("moodtestrepository.PNG")
    click("okbuttonopenba.PNG")
    wait(4)
    if exists("showstatusoflastconnection.PNG"):
        rightClick("processestheme.PNG")
        click("newprocess.PNG")
        type("Test Process" + Key.ENTER + Key.ENTER)

def reduceProcessSymbolSize():
    rightClick("processmodelsymbol.PNG")
    click("formatstyle.PNG")
    click(Region(727,406,35,22))
    doubleClick("processmodelformatstylesizewidth.PNG")
    type("100" + Key.TAB + "100")
    click("formatstyleokbutton.PNG")
    dragDrop(Location(Location(1050, 607)), Location(Location(648, 306)))

def pickAndUseFormattedTextEditorOnModel():
    click("ribbonactionsmenu.PNG")
    click("formattedtexteditor.PNG")
    mouseMove(Location(800, 702))
    mouseDown(Button.LEFT)
    mouseUp(Button.LEFT)
    click("fteditorclicktoselect.PNG")
    click("fields.PNG")
    click("datanavigatorformattedtextfield.PNG")
    click("datanavigatorpurpose.PNG")
    click("fteokbutton.PNG")
    dragDrop(Location(Location(835, 739)), Location(Location(996, 432)))

def openNewProcess():
    rightClick("newtestprocesselement.PNG")
    click("processopen.PNG")
    click(Location(537, 332))
    type("Lorem Ipsum dolor sit amet, consectetur adipiscing elit.")
    click("ribbonfilebutton.PNG")
    click("ribbonsaveall.PNG")
    click("processmodeltab.PNG")
    

def cleanup():
    click("closeba.PNG")
    rightClick("deletethetestrep.PNG")
    click("removetestrep.PNG")
    click("deleterep.PNG")
    popup("Test completed successfully.")

                
                
App.open(r"C:\Program Files (x86)\MooD\16\RepositoryManager.exe")
setBundlePath(r"C:\sik\IN11795.sikuli\rep-man-images")
wait(3)
outputErrorToFile("h")
addRep()
openNewRep()
reduceProcessSymbolSize()
pickAndUseFormattedTextEditorOnModel()
openNewProcess()
cleanup()
