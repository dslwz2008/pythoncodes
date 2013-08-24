#codeing:utf-8

import cocos
from cocos import tiles, layer, actions

class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        self.back_layer = tiles.load('test.tmx')['Background']
        scroller = layer.ScrollingManager()
        scroller.add(self.back_layer)
        

if __name__ == '__main__':
    # director init takes the same arguments as pyglet.window
    cocos.director.director.init()

    # We create a new layer, an instance of HelloWorld
    #hello_layer = HelloWorld ()
    tilemap = tiles.load('test.tmx')
    back_layer = tilemap['Background']
    objects = tilemap['Objects']
    start = objects['SpawnPoint']
    scroller = layer.ScrollingManager()
    scroller.add(back_layer)

    # A scene that contains the layer hello_layer
    main_scene = cocos.scene.Scene (scroller)

    # And now, start the application, starting with main_scene
    cocos.director.director.run (main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( HelloWorld() ) )
