#23456789112345678921234567893123456789412345678951234567896123456789712
import bpy
import math
import os

directory = os.path.dirname(bpy.data.filepath)

def scale_in(value1):
    a = value1/39.37
    
    return a


def place_racks_json(rack):

    vbeam =[]
    for n in range( len(rack['bays']) ):

        # verticle beam
        bpy.ops.wm.obj_import( filepath = os.path.join(directory + \
          "/objects",rack['frame'] ))

        vbeam =bpy.context.active_object

        vbeam.location = (
          scale_in( rack['x'] ), scale_in( rack['y'] + \
            ( rack['bays'][n]['span'] + rack['vbeam_width'] )*n ),0)

        # horizontal beams
        for m in range( len( rack['bays'][n]['levels'] ) ):

            # front and rear beam
            for k in range(2):

                bpy.ops.wm.obj_import( filepath = os.path.join(\
                  directory + "/objects", rack['bays'][n]['beam'] ) )

                beam1 = bpy.context.active_object

                beam1.location= \
                (
                  scale_in( rack['x'] + \
                    math.cos( math.pi*k )*( rack['depth']/2 +.5 ) ), \
                  scale_in( rack['y'] + ( \
                    rack['bays'][n]['span']/2 ) + \
                    rack['notch_bottom'] + \
                    ( rack['bays'][n]['span'] + \
                      rack['vbeam_width']\
                    )*n ), \
                  scale_in( rack['notch_spacing']*rack['bays'][n]\
                    ['levels'][m] + rack['notch_bottom'] )
                )

                beam1.rotation_euler = [math.radians(90),
                  math.radians(0), math.radians(-1*math.cos(math.pi*k)*90)]


    # verticale beam
    bpy.ops.wm.obj_import( filepath = os.path.join(directory + \
      "/objects",  rack['frame'] ) )
    vbeam = bpy.context.active_object
    vbeam.location = \
      (
        scale_in( rack['x'] ),
        scale_in( rack['y'] + ( rack['bays'][n]['span'] + \
          rack['vbeam_width'] )*len(rack['bays']) + 1 ),0)

