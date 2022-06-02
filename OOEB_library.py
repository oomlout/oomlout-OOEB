from solid.objects import cube, cylinder, difference, translate, union, hull, rotate, linear_extrude, square, offset

import OPSC_dimensions
import OPSC_insert as opsc


ooebWireExtra = 0.5

def baseModule3x2(color):
    mainWidth = (3 * 15) - 3
    mainHeight = (2 * 15) - 3
    mainDepth = 12
    holeM6APos = [15,15/2,0]
    holeM6BPos = [0,15/2,0]
    holeM3APos = [-15,15/2,0]
    holeM3BPos = [15,-15/2,0]
    
    connectorPos = [-mainWidth/2,-3,-mainDepth + 6]

    #posParts = opsc.insert("cubeRounded",width=width,height=height,depth=depth,color=color)
    #print("posParts" + str(posParts))
    parts =  difference()(
        ###### Positive Parts
        union()(
            opsc.insert("cubeRounded",width=mainWidth,height=mainHeight,depth=mainDepth,color=color)
        ###### Negative Parts
        ),union()( 
            opsc.insert("holeM6",pos=holeM6APos),
            opsc.insert("holeM6",pos=holeM6BPos),
            opsc.insert("holeM3",pos=holeM3APos),
            opsc.insert("holeM3",pos=holeM3BPos),
            insert("OOEB-WIRE-BA",pos=connectorPos,rotZ=180)                        
         )
    )

    return parts


def ooebWireBa(color):
    returnValue = ""
    print("Making a OOEB-WIRE-BA")
    depth = 3
    a= []
    #frontBox
    pos = [-1.615,0,0]
    size = [8.73+ooebWireExtra,10.16+ooebWireExtra,depth]    
    a.append(opsc.insert("cube",pos=pos,size=size, color=color))
    #backBox
    pos = [-15.52,1.27,0]
    size = [14 + ooebWireExtra,7.62+ooebWireExtra,depth]
    a.append(opsc.insert("cube",pos=pos,size=size, color=color))
    #wireBox
    pos = [-25.135,1.27,0]
    size = [9.23 + ooebWireExtra,5.62 + ooebWireExtra,depth]
    a.append(opsc.insert("cube",pos=pos,size=size, color=color))
    #keyBox
    pos = [-7.25,0,0]
    size = [2.54 + ooebWireExtra,15.24 + ooebWireExtra,depth]
    a.append(opsc.insert("cube",pos=pos,size=size, color=color))
    #dotBox
    pos = [0,-10,0]
    size = [0,0,depth]
    rad = 1.5
    a.append(opsc.insert("cylinder",pos=pos,size=size,rad=rad, color=color))

    return union()(a)


def insert(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color="gray",alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
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

def OOEBInsertIf(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color="gray",alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):

    print("    OOEBInsert item:" + str(item) + " at:[" + str(x) + "," + str(y) + "," + str(z) + "]")


    if(item=="OOEB-WIRE-BA"):
        returnValue = ooebWireBa(color)

    return returnValue


