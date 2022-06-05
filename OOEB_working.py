#import OOEB_library as oe

import OOEB_library as ooeb
import OPSC_insert as opsc

color = "red"

def makePart(part):
    opsc.setMode("3DPR")
    item = opsc.item()
    item.addPos(ooeb.insert(part))
    file = "parts\\" + part + "\\" + part 
    opsc.saveToScad(file + "-3DPR.scad", item.getPart())
    opsc.saveToScad(file +"-3dprint.scad", item.getSplit(start=0,depth=6,tileDif=30))

    opsc.setMode("LAZE")
    item = opsc.item()
    item.addPos(ooeb.insert(part))    
    opsc.saveToScad(file +"-LAZE.scad", item.getPart())
    opsc.saveToScad(file +"-laser.scad", item.getLaser(layers=4,tileDif=30))

    opsc.setMode("TRUE")
    item = opsc.item()
    item.addPos(ooeb.insert(part))    
    opsc.saveToScad(file +"-TRUE.scad", item.getPart())
    

    

def makeFiles(part):
    file = "parts\\" + part + "\\" + part 
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

    opsc.saveToStl(file + "-3dprint.scad")
    opsc.saveToPng(file + "-3dprint.scad")

    
#parts = ["nutM3"]
from solid.objects import *

def makeParts():
    parts = [
            "OOEB-OUTP-LEDS-X",
            "OOEB-BASE-3X2"
            
            ]
    for part in parts:
        makePart(part)    
    for part in parts:
        makeFiles(part) 
        x=0

parts = color(c="red")(cube(size=[10,20,30]))

opsc.saveToScad("parts/test/test.scad",parts)

makeParts()        