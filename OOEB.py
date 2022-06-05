from solid.objects import cube, cylinder, difference, translate, union, hull, rotate, linear_extrude, square, offset

import OPSC as opsc
import OOMPscad as oomp



######  Variables

    ######  OOBB variables
oobbWidth02 = (2 * 15) - 3
oobbWidth03 = (3 * 15) - 3

    ######  OOEB variables
ooebWireExtra = 0.5    

######  Modules Brains
def ooebObbbProjArdcStan01(color):
    return  cube([10,10,10])

######  Modules Input

def ooebInpuButaX(color):
    mode = opsc.getMode()
    mainWidth = oobbWidth03
    mainHeight = oobbWidth02

    but06Pos = [0,-5,0]
    but12Pos = but06Pos
    resPos=[-10,-5,0]

    part = opsc.item()
    part.addPos(insert("OOEB-BASE-3X2",color=color))
    part.addNeg(oomp.insert("OOMP-BUTA-06-X-X-01",pos=but06Pos,color=color))
    part.addNeg(oomp.insert("OOMP-BUTA-12-X-X-01",pos=but12Pos,color=color))
    if(mode == "TRUE"):            
        part.addPos(oomp.insert("OOMP-BUTA-06-X-X-01",pos=but06Pos,rotZ=0,color=color))
        part.addPos(oomp.insert("OOMP-BUTA-12-X-X-01",pos=but12Pos,rotZ=0,color=color))
        part.addPos(oomp.insert("OOMP-RESE-W04-X-O561-01",pos=resPos,rotZ=90,color=color))

    part.addNeg(oomp.insert("OOMP-RESE-W04-X-O561-01",pos=resPos,rotZ=90,color=color))
    return part.getPart()

def ooebInpuPoteX(color):
    return cube([10,10,10])

######  Modules Output
def ooebOutpLedsX(color):
    mode = opsc.getMode()
    mainWidth = oobbWidth03
    mainHeight = oobbWidth02
    part = opsc.item()
    part.addPos(insert("OOEB-BASE-3X2",color=color))
    part.addNeg(oomp.insert("OOMP-LEDS-10-X-X-01",pos=[0,-5,0],rotZ=45,color=color))
    if(mode == "TRUE"):            
        part.addPos(oomp.insert("OOMP-LEDS-10-X-X-01",pos=[0,-5,0],rotZ=45,color=color))
        part.addPos(oomp.insert("OOMP-RESE-W04-X-O561-01",pos=[-10,-5,0],rotZ=90,color=color))

    part.addNeg(oomp.insert("OOMP-RESE-W04-X-O561-01",pos=[-10,-5,0],rotZ=90,color=color))
    return part.getPart()





######  Module Helpers

def baseModule3x2(color):

    mode = opsc.getMode()

    mainWidth = oobbWidth03
    mainHeight = oobbWidth02
    mainDepth = 12
    holeM6APos = [15,15/2,0]
    holeM6BPos = [0,15/2,0]

    holeM3APos = [-15,15/2,0]
    nutM3APos = [holeM3APos[0],holeM3APos[1],-mainDepth+opsc.nutM3depth-.01]
    captiveStandoffM3APos = [holeM3APos[0],holeM3APos[1],-3]
    countersunkM3APos = [holeM3APos[0],holeM3APos[1],0+.01]
    
    holeM3BPos = [15,-15/2,0]
    nutM3BPos = [holeM3BPos[0],holeM3BPos[1],-mainDepth+opsc.nutM3depth-.01]
    captiveStandoffM3BPos = [holeM3BPos[0],holeM3BPos[1],-3]
    countersunkM3BPos = [holeM3BPos[0],holeM3BPos[1],0+.01]

    clearancePos = [-1,-4,-mainDepth+9]
    clearanceSize = [24,13,3]
    
    connectorPos = [-mainWidth/2,-3,-mainDepth+6]
    

    #posParts = opsc.insert("cubeRounded",width=width,height=height,depth=depth,color=color)
    #print("posParts" + str(posParts))
    part = opsc.item()
    part.addPos(insert("cubeRounded",width=mainWidth,height=mainHeight,depth=mainDepth,color=opsc.colOOEBbase))
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



######  Insert Routines

def insert(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color=opsc.colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
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

def OOEBInsertIf(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color=opsc.colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):

    #print("    OOEBInsert item:" + str(item) + " at:[" + str(x) + "," + str(y) + "," + str(z) + "] size: [" + str(width) + "," + str(height) + "," + str(depth) + "]")

    #print(pos)

    if(x=="22222222"):
        x=0
    ######  OOEB-WIRE        
    elif(item=="OOEB-WIRE-BA"):
        returnValue = ooebWireBa(color)
    ######  OOEB-OBBB    
    elif(item=="OOEB-OBBB-PROJ-ARDC-SHEN-STAN-01"):
        returnValue = ooebObbbProjArdcStan01(color)
    ######  OOEB-INPU
    elif(item=="OOEB-INPU-BUTA-X"):
        returnValue = ooebInpuButaX(color)
    elif(item=="OOEB-INPU-POTE-X"):
        returnValue = ooebInpuPoteX(color)
    ######  OOEB-OUTP        
    elif(item=="OOEB-OUTP-LEDS-X"):
        returnValue = ooebOutpLedsX(color)

    ######  OOEB-BASE    
    elif(item=="OOEB-BASE-3X2"):
        returnValue = baseModule3x2(color)

    else:    
        returnValue = opsc.insert(item,[None,None,None],0,0,0,ex,size,length,[None,None,None],0,0,0,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)
    return returnValue


