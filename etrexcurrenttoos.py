import xml.etree.ElementTree as ET
import sys

args = sys.argv
if len(args) != 2:
    print("Must have one argument - the base name of the file", file=sys.stderr)
    sys.exit(1)
print (args)

ns = {'GPX':"http://www.topografix.com/GPX/1/1"}
xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gpx version="1.1" creator="OS Maps - Web" xmlns="http://www.topografix.com/GPX/1/1"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"
xmlns:gs="http://www.topografix.com/GPX/gpx_style/0/2"
xmlns:gh="https://graphhopper.com/public/schema/gpx/1.1"
xmlns:os="https://ordnancesurvey.co.uk/public/schema/route/0.1">"""

tree = ET.parse(args[1] + ".gpx")
root = tree.getroot()

trk = root.find("GPX:trk",ns)
name = trk.find("GPX:name",ns).text

xml = xml + "<metadata><name>" + name + "</name></metadata>\n"

n = 0
for trk in root.findall("GPX:trk",ns):
    print("Track", trk.find("GPX:name",ns).text)
    for trkseg in trk.findall("GPX:trkseg",ns):
        for trkpt in trkseg.findall("GPX:trkpt",ns):
            n+= 1
            xml = xml + '<wpt lat="' + trkpt.attrib["lat"] + '" lon="' +  trkpt.attrib["lon"] + '"></wpt>\n'

    
xml = xml + "</gpx>"
with open(args[1] + "-os.gpx", "w") as f:
    f.write(xml)
print ("Route with", n, "points converted")
    
