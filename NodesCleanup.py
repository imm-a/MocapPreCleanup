from pyfbsdk import *
from pyfbsdk_additions import *

gToolName = "NodesCleanup"

def BuildUI(mainLyt):
    '''Creating Buttons and Layout '''
    x = FBAddRegionParam(100,FBAttachType.kFBAttachCenter,"")
    y = FBAddRegionParam(100,FBAttachType.kFBAttachCenter,"")
    w = FBAddRegionParam(200,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(50,FBAttachType.kFBAttachNone,"")
    mainLyt.AddRegion("button","button", x, y, w, h)

    x = FBAddRegionParam(100,FBAttachType.kFBAttachCenter,"")
    y = FBAddRegionParam(175,FBAttachType.kFBAttachCenter,"")
    w = FBAddRegionParam(200,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(50,FBAttachType.kFBAttachNone,"")
    mainLyt.AddRegion("button1","button1", x, y, w, h)    
    
    lSaveButton = FBButton()
    lSaveButton.Caption = "Clean Nodes"
    lSaveButton.Hint = "Deletes cameras and markers. Keeps just bones."
    lSaveButton.Justify = FBTextJustify.kFBTextJustifyCenter
    mainLyt.SetControl("button",lSaveButton)
    lSaveButton.OnClick.Add(DeleteMarkersCallback)

    lbutton1 = FBButton()
    lbutton1.Caption = "Zero Rotations"
    lbutton1.Hint = "Inputs 0 on XYZ rotations for all joints and faces subject(s) in positive Z axis."
    lbutton1.Justify = FBTextJustify.kFBTextJustifyCenter
    mainLyt.SetControl("button1",lbutton1)
    lbutton1.OnClick.Add(ZeroRotsCallback)

def ZeroRotsCallback (control,event):
    '''Zeroes out rotations on bones'''
    list_of_bones = []
    for lComponent in FBSystem().Scene.Components:
        if lComponent and lComponent.ClassName() == 'FBModelSkeleton':
            list_of_bones.append(lComponent)
        
    for bone in list_of_bones:
        rot = bone.Rotation
        rot.Key()
        rot.Data = FBVector3d(0,0,0)
        rot.Key()
        if bone.Name == 'Hips':
            rot = bone.Rotation
            rot.Key()
            rot.Data = FBVector3d(0,0,180)
            rot.Key()          


def DeleteMarkersCallback (control, event):
    markers = []
    system_components = []
    for lComponent in FBSystem().Scene.Components:
        if lComponent and lComponent.ClassName() == "FBModelMarker":                
            markers.append(lComponent)
        if lComponent and (lComponent.ClassName() == 'FBCamera' or (lComponent.ClassName() == 'FBModelNull' and lComponent.Name == 'System') ):
            system_components.append(lComponent)
        
    while(len(markers)!=0):
        markers[-1].FBDelete()
        markers.remove(markers[-1])
        
    while(len(system_components)!=0):
        system_components[-1].FBDelete()
        system_components.remove(system_components[-1])       
        


def CreateTool():
    # Tool creation will serve as the hub for all other controls
    t = FBCreateUniqueTool("Mocap Pre-Cleanup")
    t.StartSizeX = 400
    t.StartSizeY = 400
    BuildUI(t)
    return t
    
gDEVELOPMENT = False

if gDEVELOPMENT:
    FBDestroyToolByName(gToolName)

if gToolName in FBToolList:
    tool = FBToolList[gToolName]
    ShowTool(tool)
else:
    tool=CreateTool()
    if gDEVELOPMENT:
       ShowTool(tool)
