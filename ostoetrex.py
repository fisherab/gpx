import xml.etree.ElementTree as ET
import sys

args = sys.argv
if len(args) != 2:
    print("Must have one argument - the base name of the file", file=sys.stderr)
    sys.exit(1)
print (args)

ns = {'GPX':"http://www.topografix.com/GPX/1/1"}
xml = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>Garmin International</text></link><time>2021-12-10T23:29:43Z</time></metadata>'
tree = ET.parse(args[1] + ".gpx")
root = tree.getroot()

name = root.find("GPX:metadata",ns).find("GPX:name",ns).text

xml = xml + "<rte>"
xml = xml + "<name>" + name + "</name>"

wpnum = 0
for wpt in root.findall("GPX:wpt",ns):
    xml = xml + '<rtept lat="' + wpt.attrib["lat"] + '" lon="' +  wpt.attrib["lon"] + '"><name>' + str(wpnum) + "</name></rtept>"
    wpnum += 1
    
xml = xml + "</rte></gpx>"
with open(args[1] + "-etrex.gpx", "w") as f:
    f.write(xml)  
    