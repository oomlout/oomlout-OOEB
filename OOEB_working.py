#import OOEB_library as oe

import OOEB_library as ooeb
import OPSC_insert as opsc

color = "red"

parts = ooeb.baseModule3x2(color)
opsc.saveToFile("parts\\test\\test.scad", parts)