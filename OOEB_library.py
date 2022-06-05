from solid.objects import cube, cylinder, difference, translate, union, hull, rotate, linear_extrude, square, offset

import OPSC_dimensions as od
import OPSC_insert as opsc



######  Variables

    ######  OOBB variables
oobbWidth02 = (2 * 15) - 3
oobbWidth03 = (3 * 15) - 3

    ######  OOEB variables
ooebWireExtra = 0.5    


######  Modules Input



def ooebOutpLedsX(color):
    mode = opsc.getMode()
    mainWidth = oobbWidth03
    mainHeight = oobbWidth02
    part = opsc.item()
    part.addPos(insert("OOEB-BASE-3X2",color=color))
    part.addNeg(insert("OOMP-LEDS-10-X-X-01",pos=[0,-5,0],rotZ=45,color=color))
    if(mode == "TRUE"):            
        part.addPos(insert("OOMP-LEDS-10-X-X-01",pos=[0,-5,0],rotZ=45,color=color))
        part.addPos(insert("OOMP-RESE-W04-X-X-01",pos=[-10,-5,0],rotZ=90,color=color))

    part.addNeg(insert("OOMP-RESE-W04-X-X-01",pos=[-10,-5,0],rotZ=90,color=color))
    return part.getPart()

######  Modules Output

######  Module Helpers

def baseModule3x2(color):

    mode = opsc.getMode()

    mainWidth = oobbWidth03
    mainHeight = oobbWidth02
    mainDepth = 12
    holeM6APos = [15,15/2,0]
    holeM6BPos = [0,15/2,0]

    holeM3APos = [-15,15/2,0]
    nutM3APos = [holeM3APos[0],holeM3APos[1],-mainDepth+od.nutM3depth-.01]
    captiveStandoffM3APos = [holeM3APos[0],holeM3APos[1],-3]
    countersunkM3APos = [holeM3APos[0],holeM3APos[1],0+.01]
    
    holeM3BPos = [15,-15/2,0]
    nutM3BPos = [holeM3BPos[0],holeM3BPos[1],-mainDepth+od.nutM3depth-.01]
    captiveStandoffM3BPos = [holeM3BPos[0],holeM3BPos[1],-3]
    countersunkM3BPos = [holeM3BPos[0],holeM3BPos[1],0+.01]

    clearancePos = [-1,-4,-mainDepth+9]
    clearanceSize = [24,13,3]
    
    connectorPos = [-mainWidth/2,-3,-mainDepth+6]
    

    #posParts = opsc.insert("cubeRounded",width=width,height=height,depth=depth,color=color)
    #print("posParts" + str(posParts))
    part = opsc.item()
    part.addPos(insert("cubeRounded",width=mainWidth,height=mainHeight,depth=mainDepth,color=od.colOOEBbase))
        ###### Negative Parts

    if(mode == "LAZE"):    
        part.addNeg(insert("nutM3",pos=captiveStandoffM3APos,depth=6))
        part.addNeg(insert("nutM3",pos=captiveStandoffM3BPos,depth=6))


    else:  
        part.addNeg(insert("nutM3",pos=nutM3APos))
        part.addNeg(insert("nutM3",pos=nutM3BPos))
        part.addNeg(insert("countersunkM3",pos=countersunkM3APos))
        part.addNeg(insert("countersunkM3",pos=countersunkM3BPos))
        x=0          

    

    part.addNeg(insert("holeM6",pos=holeM6APos))
    part.addNeg(insert("holeM6",pos=holeM6BPos))
    part.addNeg(insert("holeM3",pos=holeM3APos))
    part.addNeg(insert("holeM3",pos=holeM3BPos))
    part.addNeg(insert("OOEB-WIRE-BA",pos=connectorPos,rotZ=180))
    part.addNeg(insert("cubeRounded",pos=clearancePos,size=clearanceSize))

    return part.getPart()

######  Wire Parts

def ooebWireBa(color):
    rv = opsc.item()
    depth = 3
    a= []
    #frontBox
    pos = [-1.615,0,0]
    size = [8.73+ooebWireExtra,10.16+ooebWireExtra,depth]    
    rv.addPos(opsc.insert("cube",pos=pos,size=size, color=color))
    #backBox
    pos = [-15.52,1.27,0]
    size = [14 + ooebWireExtra,7.62+ooebWireExtra,depth]
    rv.addPos(opsc.insert("cube",pos=pos,size=size, color=color))
    #wireBox
    pos = [-25.135,1.27,0]
    size = [9.23 + ooebWireExtra,5.62 + ooebWireExtra,depth]
    rv.addPos(opsc.insert("cube",pos=pos,size=size, color=color))
    #keyBox
    pos = [-7.25,0,0]
    size = [2.54 + ooebWireExtra,15.24 + ooebWireExtra,depth]
    rv.addPos(opsc.insert("cube",pos=pos,size=size, color=color))
    #dotBox
    pos = [0,-10,0]
    size = [0,0,depth]
    rad = 1.5
    rv.addPos(opsc.insert("cylinder",pos=pos,size=size,rad=rad, color=color))

    return rv.getPart()

######  OOMP ROUTINES

def oompLeds10XX01(color):
    part = opsc.item()



    posA = [1.27,0,0.1]
    posB = [-posA[0],posA[1],posA[2]]
    size = [od.ooebPinWidth,od.ooebPinWidth,5.1]

    color = od.colWire
    part.addPos(insert("cube",pos=posA,size=size,color=color))
    part.addPos(insert("cube",pos=posB,size=size,color=color))
    color = od.colLEDRed
    part.addPos(insert("cylinder",pos=[0,0,8.5],rad=5,depth=6.5,color=color))
    part.addPos(insert("cylinder",pos=[0,0,2.05],rad=5.5,depth=2,color=color))
    part.addPos(insert("sphere",pos=[0,0,8.5+5],rad=5,color=color))

    return part.getPart()


def oompReseW04XX01(color):
    part = opsc.item()
    
    pinSpacing = 3.81
    resLength = 6.8
    resRad = 2.5/2
    resBandSpacing = 1

    posA = [pinSpacing,0,0+resRad+od.ooebPinWidth/2]
    posB = [-posA[0],posA[1],posA[2]]
    size = [od.ooebPinWidth,od.ooebPinWidth,5+resRad+od.ooebPinWidth/2]

    color = od.colWire
    part.addPos(insert("cube",pos=posA,size=size,color=color))
    part.addPos(insert("cube",pos=posB,size=size,color=color))
    part.addPos(insert("cube",pos=[pinSpacing*2/2,0,resRad],size=[od.ooebPinWidth,od.ooebPinWidth,pinSpacing*2],rot=[0,90,0],color=color))

    color = od.colResistor
    resPos = [resLength/2,0,resRad+0.01]
    part.addPos(insert("cylinder",pos=resPos,depth=resLength,rad=resRad,rot=[90,0,90],color=color))
    
    ####bands
    bandRad=resRad+0.01
    bandDepth = 0.75
    band1Pos=[resPos[0]-1,resPos[1],resPos[2]]    
    band1Color = od.colRes[5]
    part.addPos(insert("cylinder",pos=band1Pos,depth=bandDepth,rad=bandRad,rot=[90,0,90],color=band1Color))
    
    band2Pos=[band1Pos[0]-resBandSpacing,resPos[1],resPos[2]]    
    band2Color = od.colRes[6]
    part.addPos(insert("cylinder",pos=band2Pos,depth=bandDepth,rad=bandRad,rot=[90,0,90],color=band2Color))
    
    band3Pos=[band2Pos[0]-resBandSpacing,resPos[1],resPos[2]]    
    band3Color = od.colRes[1]
    part.addPos(insert("cylinder",pos=band3Pos,depth=bandDepth,rad=bandRad,rot=[90,0,90],color=band3Color))




    return part.getPart()

######  Insert Routines

def insert(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color=od.colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
    returnValue = ""
    if pos[0] != None:
        x=pos[0]
        y=pos[1]
        z=pos[2]
    if rot[0] != None:
        rotX=rot[0]
        rotY=rot[1]
        rotZ=rot[2]
    
    returnValue = translate((x,y,z))(
            rotate((rotX,rotY,rotZ))(
                OOEBInsertIf(item,pos,x,y,z,ex,size,length,rot,rotX,rotY,rotZ,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)
            )
        )
    

    return returnValue

def OOEBInsertIf(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color=od.colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):

    #print("    OOEBInsert item:" + str(item) + " at:[" + str(x) + "," + str(y) + "," + str(z) + "] size: [" + str(width) + "," + str(height) + "," + str(depth) + "]")

    #print(pos)

    if(item=="OOEB-WIRE-BA"):
        returnValue = ooebWireBa(color)
    ######  OOEB-OUTP        
    elif(item=="OOEB-OUTP-LEDS-X"):
        returnValue = ooebOutpLedsX(color)

    ######  OOEB-INPU    
    elif(item=="OOEB-BASE-3X2"):
        returnValue = baseModule3x2(color)
    ######  OOMP ITEMS
    elif(item=="OOMP-LEDS-10-X-X-01"):
        returnValue = oompLeds10XX01(color)
    elif(item=="OOMP-RESE-W04-X-X-01"):
        returnValue = oompReseW04XX01(color)

    else:    
        returnValue = opsc.insert(item,[None,None,None],0,0,0,ex,size,length,[None,None,None],0,0,0,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)
    return returnValue


