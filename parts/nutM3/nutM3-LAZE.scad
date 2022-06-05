// Generated by SolidPython 1.1.3 on 2022-06-04 18:09:17
$fn = 48;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 0]) {
						difference() {
							translate(v = [0, 0, -1.2500000000]) {
								cube(center = true, size = [11.0000000000, 11.0000000000, 2.5000000000]);
							}
							difference() {
								union() {
									translate(v = [8.2500000000, 0, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, -1.2500000000]) {
												cube(center = true, size = [11.0000000000, 11.0000000000, 2.5000000000]);
											}
										}
									}
									translate(v = [-8.2500000000, 0, 0]) {
										rotate(a = [0, 0, 0]) {
											translate(v = [0, 0, -1.2500000000]) {
												cube(center = true, size = [11.0000000000, 11.0000000000, 2.5000000000]);
											}
										}
									}
								}
								union();
							}
							rotate(a = [0, 0, 60]) {
								difference() {
									union() {
										translate(v = [8.2500000000, 0, 0]) {
											rotate(a = [0, 0, 0]) {
												translate(v = [0, 0, -1.2500000000]) {
													cube(center = true, size = [11.0000000000, 11.0000000000, 2.5000000000]);
												}
											}
										}
										translate(v = [-8.2500000000, 0, 0]) {
											rotate(a = [0, 0, 0]) {
												translate(v = [0, 0, -1.2500000000]) {
													cube(center = true, size = [11.0000000000, 11.0000000000, 2.5000000000]);
												}
											}
										}
									}
									union();
								}
							}
							rotate(a = [0, 0, -60]) {
								difference() {
									union() {
										translate(v = [8.2500000000, 0, 0]) {
											rotate(a = [0, 0, 0]) {
												translate(v = [0, 0, -1.2500000000]) {
													cube(center = true, size = [11.0000000000, 11.0000000000, 2.5000000000]);
												}
											}
										}
										translate(v = [-8.2500000000, 0, 0]) {
											rotate(a = [0, 0, 0]) {
												translate(v = [0, 0, -1.2500000000]) {
													cube(center = true, size = [11.0000000000, 11.0000000000, 2.5000000000]);
												}
											}
										}
									}
									union();
								}
							}
						}
					}
				}
			}
		}
	}
	union();
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
import OPSC_dimensions as od
from solid.objects import cube, cylinder, difference, translate, union, hull, rotate, linear_extrude, square, offset, projection, intersection
from solid import scad_render_to_file


def setMode(mode="3DPR"):
    od.changeMode(mode)

def getMode():
    return od.mode

def saveToScad(fileName, parts):
    file_out = scad_render_to_file(parts, fileName, file_header=f'$fn = 48;')


def insert(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color="gray",alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
    return OPSCInsert(item,pos,x,y,z,ex,size,length,rot,rotX,rotY,rotZ,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)


def OPSCInsert(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color="gray",alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
    
    """
        color(color,alpha){
            translate([x,y,z]){
                    rotate([rotX,rotY,rotZ]){
    """
    returnValue = ""

    print(pos)

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
                OPSCInsertIf(item,pos,x,y,z,ex,size,length,rot,rotX,rotY,rotZ,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)
            )
        )
    

    return returnValue

def OPSCInsertIf(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color="gray",alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
    returnValue = cube([10,10,10])

    if size[0] != None:
        width=size[0]
        height=size[1]
        depth=size[2]

    print("    OPSCInsert item:" + str(item) + " at:[" + str(x) + "," + str(y) + "," + str(z) + "] size: [" + str(width) + "," + str(height) + "," + str(depth) + "]")

    if(item=="cube"):
        returnValue =  translate([0,0,-depth/2])(cube([width,height,depth],center=True))
    elif(item=="cylinder"):        
        returnValue = translate([0,0,-depth/2])(cylinder(r=rad,h=depth,center=True))
    elif(item=="plane"):
        returnValue = insert("cube",size=[1000,1000,0.1],color=color)    
    elif(item=="cubeRounded"):
        if(rad == 0):
                            rad = 5
        returnValue =  translate([0,0,-depth])(
                        linear_extrude(height=depth)(                        
                            offset(r=rad)(
                                square((width-rad*2+.01,height-rad*2+.01),center=True)
                                )
                            )
        )

    ######  Holes    
    elif(item == "holeM1"):
        returnValue = OSPCgetHole(rad=1)
    elif(item == "holeM2"):
        returnValue = OSPCgetHole(rad=2)
    elif(item == "holeM3"):
        returnValue = OSPCgetHole(rad=3)
    elif(item == "holeM4"):
        returnValue = OSPCgetHole(rad=4)
    elif(item == "holeM5"):
        returnValue = OSPCgetHole(rad=5)
    elif(item == "holeM6"):
        returnValue = OSPCgetHole(rad=6)
    elif(item == "hole"):
        returnValue = OSPCgetHole(rad=rad)

    ######  Nuts
    elif(item == "nutM1"):
        returnValue = OSPCgetNut(rad=1,depth=depth)
    elif(item == "nutM2"):
        returnValue = OSPCgetNut(rad=2,depth=depth)
    elif(item == "nutM3"):
        returnValue = OSPCgetNut(rad=3,depth=depth)
    elif(item == "nutM4"):
        returnValue = OSPCgetNut(rad=4,depth=depth)
    elif(item == "nutM5"):
        returnValue = OSPCgetNut(rad=5,depth=depth)
    elif(item == "nutM6"):
        returnValue = OSPCgetNut(rad=6,depth=depth)
    elif(item == "nut"):
        returnValue = OSPCgetNut(rad=rad,depth=depth)
    return returnValue

                

def OSPCgetHole(rad):
    return translate([0,0,-250])(cylinder(r=od.holeM[rad-1],h=500))

def OSPCgetNut(rad,depth):
    print(depth)
    print(od.nutM)
    depth = od.nutM[rad-1][od.NUTDEPTH] if depth==100 else depth
    returnValue = OPSChexagon(od.nutM[rad-1][od.NUTWIDTH],depth=depth)
    return returnValue

def OPSChexagon(width,depth):
    cutter = item()
    wid=width*2
    cutter.addPos(insert("cube",pos=[wid/2+width/2,0,0],size=[wid,wid,depth]))
    cutter.addPos(insert("cube",pos=[-wid/2-width/2,0,0],size=[wid,wid,depth]))

    cut = cutter.getPart()
    print(depth)
    returnValue = difference()(
        translate([0,0,-depth/2])(cube([wid,wid,depth],center=True)),
        cut,
        rotate([0,0,60])(cut),
        rotate([0,0,-60])(cut)
    )

    return returnValue




class item:

    def __init__(self):
        self.posItems=list()
        self.negItems=list()


    def addPos(self,part):
        self.posItems.append(part)
    def addNeg(self,part):
        self.negItems.append(part)

    def getPart(self):
        returnValue = difference()(
            union()(self.posItems),
            union()(self.negItems)
        )
        return returnValue

    def getLaser(self,start=0,layers=1,thickness=-3,tileDif=200):
        rv= []

        for x in range(layers):
            rv.append(translate([0,x*tileDif,0])(
                    projection()(
                        intersection()(
                            insert("plane",z=start+x*thickness),
                            self.getPart()
                        )
                    )
            )
            )
        return union()(rv)
 
 
************************************************/
