from solid.objects import cube, cylinder, difference, translate, union, hull, rotate, linear_extrude, square, offset

import OPSC as opsc
import OOMPscad as oomp



######  Variables

    ######  OOBB variables
oobbWidth02 = (2 * 15) - 3
oobbWidth03 = (3 * 15) - 3
oobbWidth04 = (4 * 15) - 3

    ######  OOEB variables
ooebWireExtra = 0.5    

######  Modules Brains
def ooebObbbProjArdcStan01(color):
    part = opsc.item()

    part.addPos(insert("OOEB-OBBB-PROJ-ARDC-SHEN-STAN-01-BOTTOM",pos=[0,0,0],color=color))
    pcbThickness = 1.6
    topThickness = 6
    z = pcbThickness + topThickness   
    part.addPos(insert("OOEB-OBBB-PROJ-ARDC-SHEN-STAN-01-TOP",pos=[0,0,z],color=color))

    return part.getPart()

def ooebObbbProjArdcStan01Top(color):
    depthTotal=8
    part = opsc.item()
    part.addPos(base4x3(color,depth=depthTotal,nuts=False))

    #D1
    z=0.0
    depth=6.1
    pins = []
    shenShift = 7
    ####  Bottom Side
    x= shenShift - 2.54*7
    y= -3 * 2.54
    rot=-90
    pins.append(["D0",[x,y,z],rot,"ooebWiVert"])
    x = x+2.54
    pins.append(["D1",[x,y,z],rot,"ooebWiVert"])
    x = x+2.54
    y = y-2.54
    pins.append(["D3",[x,y,z],rot,"ooebWiVert"])
    x = x+2.54
    pins.append(["D4",[x,y,z],rot,"ooebWiVert"])
    y = y+2.54    
    x = x+ 2.54
    pins.append(["D2",[x,y,z],rot,"ooebWiVert"])
    x = x+ 2.54
    y = y - 2.54    
    pins.append(["D3Blank",[x,y,z],rot,"oompHead02"])
    x = x+ 2.54
    pins.append(["D4Blank",[x,y,z],rot,"oompHead02"])
    x = x+ 2.54
    pins.append(["D5Blank",[x,y,z],rot,"oompHead02"])
    y = y + 2.54    
    x = x+ 2.54
    pins.append(["D6",[x,y,z],rot,"ooebWiVert"])    
    x = x+ 2.54
    pins.append(["D7",[x,y,z],rot,"ooebWiVert"])
    x = x+ 2.54
    pins.append(["D8",[x,y,z],rot,"ooebWiVert"])
    x = x+ 2.54
    pins.append(["D9",[x,y,z],rot,"ooebWiVert"])
    x = x+ 2.54
    pins.append(["D10",[x,y,z],rot,"ooebWiVert"])
    x = x+ 2.54
    pins.append(["D11",[x,y,z],rot,"ooebWiVert"])
    x = x+ 2.54
    pins.append(["D12",[x,y,z],rot,"ooebWiVert"])

    ####  Top Side
    rot=90
    x=x
    y=-y
    pins.append(["D13",[x,y,z],rot,"ooebWiVert"])
    x=x-3*2.54
    pins.append(["A0",[x,y,z],rot,"ooebWiVert"])
    x=x-2.54
    pins.append(["A1",[x,y,z],rot,"ooebWiVert"])
    x=x-2.54
    pins.append(["A2",[x,y,z],rot,"ooebWiVert"])
    x=x-2.54
    pins.append(["A3",[x,y,z],rot,"ooebWiVert"])
    x=x-2.54
    y = y + 2.54    
    pins.append(["A4Blank",[x,y,z],rot,"oompHead02"])
    x=x-2.54
    pins.append(["A5Blank",[x,y,z],rot,"oompHead02"])
    x=x-2.54
    pins.append(["A6Blank",[x,y,z],rot,"oompHead02"])
    x=x-2.54
    y = y - 2.54    
    pins.append(["A7",[x,y,z],rot,"ooebWiVert"])
    x=x-2.54
    y = y + 2.54    
    pins.append(["5V",[x,y,z],rot,"oompHead02"])
    x=x-2*2.54
    pins.append(["GND",[x,y,z],rot,"oompHead02"])
    zs = [0,-2,-4,-6,-8]
    for z in zs:
        for pin in pins:
            if pin[3] == "oompHead02":
                part.addNeg(oomp.insert("OOMP-HEAD-I01-X-PI02-01-topClearance",x=pin[1][0],y=pin[1][1],z=pin[1][2]+z,rotZ=pin[2],color=color))
            else:
                part.addNeg(insert("OOEB-WIRE-BA-VERT",x=pin[1][0],y=pin[1][1],z=pin[1][2]+z,rotZ=pin[2],color=color))    
    
    ######  I2C

    zs = [0,-2,-4,-6,-8]
    for z2 in zs:
        x=-19.67
        y=-4.62
        z=0.0
        rot=180
        part.addNeg(insert("OOEB-WIRE-BA-VERT",pos=[x,y,z+z2],rotZ=rot,color=color))    
        y=y +2.54
        part.addNeg(insert("OOEB-WIRE-BA-VERT",pos=[x,y,z+z2],rotZ=rot,color=color))    
        y=y + 2 * 2.54
        part.addNeg(insert("OOEB-WIRE-BA-VERT",pos=[x,y,z+z2],rotZ=rot,color=color))     
        y=y +2.54
        part.addNeg(insert("OOEB-WIRE-BA-VERT",pos=[x,y,z+z2],rotZ=rot,color=color))   
        ######  SHennie Clearance
        part.addNeg(oomp.insert("OOMP-PROJ-ARDC-SHEN-STAN-01-topClearance",pos=[7,0,-depthTotal+4-.01],rotZ=-90,depth=4,color=color))   

    ######  Test Pin    
    #part.addNeg(insert("cube",pos=[-10.78,-2.54,10],size=[2.54,2.54,100],color=color))


    return part.getPart()

def ooebObbbProjArdcStan01Bottom(color):
    part = opsc.item()
    part.addPos(base4x3(color,depth=4.5))
        ######  Clearance
    depth = 3.1
    z = 0.1
        # Main ARDC clearance
    part.addNeg(insert("cube",pos=[7,0,z],size=[43.18,22.86,depth]))    
        # Bottom wing
    part.addNeg(insert("cube",pos=[17.16,0,z],size=[17.78,27.94,depth]))   
        # Top wing
    part.addNeg(insert("cube",pos=[-6.97,0,z],size=[15.24,27.94,depth]))    
        # i2C Clearince
    part.addNeg(insert("cube",pos=[-22.21,0,z],size=[10.16,15.24,depth]))   
        # Resistors
    part.addNeg(insert("cube",pos=[-10.5,16.5,z],size=[10,6,depth]))  
    #d3andd4 clearance    
    part.addNeg(insert("cube",pos=[-4.43,-13.97,z],size=[5.08,5.08,depth]))
    return part.getPart()

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


def baseModule3x2PCB(color):
    part = opsc.item()
    part.addPos(base3X2(color,mode=opsc.getMode(),depth=4.5))
    clear = 0.5
    z=0.1
    depth=3.1
    #header plastic clearance
    part.addNeg(insert("cube",pos=[-13.73,-4.27,z],size=[2.54+clear,7.62+clear,depth]))
    #plug clearance
    part.addNeg(insert("cube",pos=[-18,-3,z],size=[6+clear,10.16+clear,depth]))
    #big clearance
    part.addNeg(insert("cube",pos=[-1.417,-4,z],size=[22.805+clear,13+clear,depth]))
    #littleClearance    
    part.addNeg(insert("cube",pos=[13.813,-0.726,z],size=[8.375+clear,4.452+clear,depth]))
    #extraClearance    
    part.addNeg(insert("cube",pos=[0,-11.25,z],size=[10,1.5,2]))



    return part.getPart()



######  Module Helpers


def base4x3(color,depth=6,nuts=True):
    mode = opsc.getMode()

    mainWidth = oobbWidth04
    mainHeight = oobbWidth03
    mainDepth = depth
    holeM6APos = [-22.5,15,0]
    holeM6BPos = [-22.5,-15,0]

    holeM3APos = [4.5,-15,0]
    nutM3APos = [holeM3APos[0],holeM3APos[1],-mainDepth+opsc.nutM3depth-.01]
    captiveStandoffM3APos = [holeM3APos[0],holeM3APos[1],-3]
    
    holeM3BPos = [4.5,15,0]
    nutM3BPos = [holeM3BPos[0],holeM3BPos[1],-mainDepth+opsc.nutM3depth-.01]
    captiveStandoffM3BPos = [holeM3BPos[0],holeM3BPos[1],-3]



    part = opsc.item()
    part.addPos(insert("cubeRounded",width=mainWidth,height=mainHeight,depth=mainDepth,color=opsc.colOOEBbase))
        ###### Negative Parts
    ######  Holes
    if nuts:
        part.addNeg(insert("nutM3",pos=nutM3APos))
        part.addNeg(insert("nutM3",pos=nutM3BPos))
    part.addNeg(insert("holeM6",pos=holeM6APos))
    part.addNeg(insert("holeM6",pos=holeM6BPos))
    part.addNeg(insert("holeM3",pos=holeM3APos))
    part.addNeg(insert("holeM3",pos=holeM3BPos))
  

    return part.getPart()


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

def base3X2(color,mode,depth):

    mode = opsc.getMode()

    mainWidth = oobbWidth03
    mainHeight = oobbWidth02
    mainDepth = 12
    holeM6APos = [15,15/2,0]
    holeM6BPos = [0,15/2,0]

    holeM3APos = [-15,15/2,0]
    nutM3APos = [holeM3APos[0],holeM3APos[1],-depth+opsc.nutM3depth-.01]
    captiveStandoffM3APos = [holeM3APos[0],holeM3APos[1],-3]
    countersunkM3APos = [holeM3APos[0],holeM3APos[1],0+.01]
    
    holeM3BPos = [15,-15/2,0]
    nutM3BPos = [holeM3BPos[0],holeM3BPos[1],-depth+opsc.nutM3depth-.01]
    captiveStandoffM3BPos = [holeM3BPos[0],holeM3BPos[1],-3]
    countersunkM3BPos = [holeM3BPos[0],holeM3BPos[1],0+.01]

    clearancePos = [-1,-4,-mainDepth+9]
    clearanceSize = [24,13,3]
    
    connectorPos = [-mainWidth/2,-3,-mainDepth+6]
    

    #posParts = opsc.insert("cubeRounded",width=width,height=height,depth=depth,color=color)
    #print("posParts" + str(posParts))
    part = opsc.item()
    part.addPos(insert("cubeRounded",width=mainWidth,height=mainHeight,depth=depth,color=opsc.colOOEBbase))
        ###### Negative Parts

    if(mode == "LAZE"):    
        #part.addNeg(insert("nutM3",pos=captiveStandoffM3APos,depth=6))
        #part.addNeg(insert("nutM3",pos=captiveStandoffM3BPos,depth=6))
        c=0


    else:  
        part.addNeg(insert("nutM3",pos=nutM3APos))
        part.addNeg(insert("nutM3",pos=nutM3BPos))
        #part.addNeg(insert("countersunkM3",pos=countersunkM3APos))
        #part.addNeg(insert("countersunkM3",pos=countersunkM3BPos))
        x=0          

    

    part.addNeg(insert("holeM6",pos=holeM6APos))
    part.addNeg(insert("holeM6",pos=holeM6BPos))
    part.addNeg(insert("holeM3",pos=holeM3APos))
    part.addNeg(insert("holeM3",pos=holeM3BPos))
    #part.addNeg(insert("OOEB-WIRE-BA",pos=connectorPos,rotZ=180))
    #part.addNeg(insert("cubeRounded",pos=clearancePos,size=clearanceSize))

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

def ooebWireBaVert(color, depth=6):
    rv = opsc.item()
    a= []
    clear = 0.5
    #full height piece
    pos = [1.27,0,0.1]
    size = [10.16+clear,2.54+clear,depth+0.2]    
    rv.addPos(opsc.insert("cube",pos=pos,size=size, color=color))
    #extraClearance
    topThickness = 4
    pos = [1.27,0,-topThickness-0.1]
    size = [12+clear,4+clear,depth-topThickness+0.1]    
    rv.addPos(opsc.insert("cube",pos=pos,size=size, color=color))

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
    elif(item=="OOEB-WIRE-BA-VERT"):
        returnValue = ooebWireBaVert(color)
    ######  OOEB-OBBB    
    elif(item=="OOEB-OBBB-PROJ-ARDC-SHEN-STAN-01"):
        returnValue = ooebObbbProjArdcStan01(color)
    elif(item=="OOEB-OBBB-PROJ-ARDC-SHEN-STAN-01-BOTTOM"):
        returnValue = ooebObbbProjArdcStan01Bottom(color)
    elif(item=="OOEB-OBBB-PROJ-ARDC-SHEN-STAN-01-TOP"):
        returnValue = ooebObbbProjArdcStan01Top(color)
    ######  OOEB-INPU
    elif(item=="OOEB-INPU-BUTA-X"):
        returnValue = ooebInpuButaX(color)
    elif(item=="OOEB-INPU-POTE-X"):
        returnValue = ooebInpuPoteX(color)
    ######  OOEB-OUTP        
    elif(item=="OOEB-OUTP-LEDS-X"):
        returnValue = ooebOutpLedsX(color)

    ######  OOEB-OBBBB-BASE-4X3    
    elif(item=="OOEB-BASE-3X2"):
        returnValue = baseModule3x2(color)
    ######  OOEB-BASE    
    elif(item=="OOEB-BASE-3X2"):
        returnValue = baseModule3x2(color)
    ######  OOEB-BASE    
    elif(item=="OOEB-BASE-3X2-PCB"):
        returnValue = baseModule3x2PCB(color)

    else:    
        returnValue = opsc.insert(item,[None,None,None],0,0,0,ex,size,length,[None,None,None],0,0,0,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)
    return returnValue


