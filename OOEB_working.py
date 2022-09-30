#import OOEB_library as oe

import OOEB as ooeb
import OPSC as opsc

color = "red"

def makePart(part):
    print("Making: " + part)
    opsc.setMode("3DPR")
    item = opsc.item()
    item.addPos(ooeb.insert(part))
    file = "parts\\" + part + "\\" + part 
    opsc.saveToScad(file + "-3DPR.scad", item.getPart())
    opsc.saveToScad(file +"-3dprint.scad", item.getSplit(start=0,depth=4,tileDif=45))

    opsc.setMode("LAZE")
    item = opsc.item()
    item.addPos(ooeb.insert(part))    
    opsc.saveToScad(file +"-LAZE.scad", item.getPart())
    opsc.saveToScad(file +"-laser.scad", item.getLaser(layers=2,tileDif=45,thickness=-6))

    opsc.setMode("TRUE")
    item = opsc.item()
    item.addPos(ooeb.insert(part))    
    opsc.saveToScad(file +"-TRUE.scad", item.getPart())
    
 

def makeFiles(part):
    file = "parts\\" + part + "\\" + part 

    opsc.saveToStl(file + "-3dprint.scad")
    opsc.saveToPng(file + "-3dprint.scad")
        
    opsc.saveToStl(file + "-3DPR.scad")
    opsc.saveToPng(file + "-3DPR.scad")

    opsc.saveToStl(file + "-TRUE.scad")
    opsc.saveToPng(file + "-TRUE.scad")
    opsc.saveToPng(file + "-TRUE.scad",extra="--preview")

    opsc.saveToStl(file + "-LAZE.scad")
    opsc.saveToPng(file + "-LAZE.scad")
    
    opsc.saveToStl(file + "-laser.scad")
    opsc.saveToPng(file + "-laser.scad")
    opsc.saveToDxf(file + "-laser.scad")


    
#parts = ["nutM3"]
from solid.objects import *

def makeParts():
    parts = [
            "OOEB-INPU-BUTA-X",
            "OOEB-INPU-POTE-X",
            "OOEB-OBBB-PROJ-ARDC-SHEN-STAN-01",
            "OOEB-OUTP-LEDS-X",
            "OOEB-BASE-3X2-PCB",
            "OOEB-OBBB-BASE-4X3"            
            ]
    for part in parts:
        makePart(part)    
    for part in parts:
        makeFiles(part) 
        x=0

######  Test
#parts = color(c="red")(cube(size=[10,20,30]))
#opsc.saveToScad("parts/test/test.scad",parts)

#makeParts()        

#part = "OOEB-BASE-3X2-PCB" 
part = "OOEB-OBBB-PROJ-ARDC-SHEN-STAN-01-TOP"
#part = "OOEB-INPU-BUTA-X" 
makePart(part)
makeFiles(part)