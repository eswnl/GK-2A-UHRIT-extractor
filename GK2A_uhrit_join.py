#!/usr/bin/env python

# GK-2A UHRIT
# Join images

from gimpfu import *

def GK2A_uhrit_join_2km(image,drawable):
    # function code goes here...
	#image.add_layer(layer)
	#go to the top layer
	#pdb.gimp_image_set_active_layer(image, image.layers[0])
	
	
	
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,-125)
	
    pdb.gimp_image_set_active_layer(image, image.layers[1])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,125)	
	
    pdb.gimp_image_set_active_layer(image, image.layers[2])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,375)
	
    pdb.gimp_image_set_active_layer(image, image.layers[3])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,625)  
	
    pdb.gimp_image_set_active_layer(image, image.layers[4])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,875)

    pdb.gimp_image_set_active_layer(image, image.layers[5])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,1125)	
	
    pdb.gimp_image_set_active_layer(image, image.layers[6])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,1375)
	
    pdb.gimp_image_set_active_layer(image, image.layers[7])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,1625)

    pdb.gimp_image_set_active_layer(image, image.layers[8])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,1875)	
	
    pdb.gimp_image_set_active_layer(image, image.layers[9])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,2125)
	
    pdb.gimp_image_set_active_layer(image, image.layers[10])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,2375)
	
    pdb.gimp_image_set_active_layer(image, image.layers[11])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,2625)
	
    pdb.gimp_image_set_active_layer(image, image.layers[12])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,2875)
	
    pdb.gimp_image_set_active_layer(image, image.layers[13])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,3125)
	
    pdb.gimp_image_set_active_layer(image, image.layers[14])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,3375)
	
    pdb.gimp_image_set_active_layer(image, image.layers[15])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,3625)
	
    pdb.gimp_image_set_active_layer(image, image.layers[16])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,3875)
	
    pdb.gimp_image_set_active_layer(image, image.layers[17])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,4125)
	
    pdb.gimp_image_set_active_layer(image, image.layers[18])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,4375)
	
    pdb.gimp_image_set_active_layer(image, image.layers[19])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,4625)
	
    pdb.gimp_image_set_active_layer(image, image.layers[20])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,4875)
	
    pdb.gimp_image_set_active_layer(image, image.layers[21])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,5125)
	
    pdb.gimp_image_set_active_layer(image, image.layers[22])
    layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_offsets(layer , 0,5375)
	
	#path_name = pdb.gimp_image_get_filename(image)[:-36]
	#pdb.gimp_message("Searching "+path_name+ "for enhancement overlays")
	#for i in range(len(image.layers)):
	     
		#extend the canvas
		#pdb.gimp_layer_set_offsets(image, 100,200)
		#pdb.gimp_image_set_active_layer(image, image.layers[i+1])
		#pdb.gimp_layer_set_offsets(image, 0,500)
		#image.add_layer(pdb.gimp_layer_new(image, 2200, 2400, 0, ImageName, 100, 0))
		#pdb.gimp_image_raise_item(image,image.layers[i+1])
		#pdb.gimp_image_set_active_layer(image, image.layers[i])
		
		
		#layer = pdb.gimp_file_load_layer(image, path_name+(pdb.gimp_item_get_name(pdb.gimp_image_get_active_layer(image))[:-4]+"_ENHANCED.png"))
		#image.add_layer(layer)
		
		
		
		
		#pdb.gimp_image_set_active_layer(image, image.layers[i])
		#layer = pdb.gimp_image_merge_down(image, image.layers[i], 0)
		#layer = pdb.gimp_image_merge_down(image, image.layers[i], 0)
		
		
		
		#if(i < len(image.layers)-1):
			#pdb.gimp_image_set_active_layer(image, image.layers[i+1])
	
register(
    "GK2A_uhrit_join_2km",
    "Joins images",
    "file",
    "John Bell", "John Bell", "2024",
    "GK-2A UHRIT join images (2km)",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
    ],
    [],
    GK2A_uhrit_join_2km, menu="<Image>/Layer/GK-2A..")  # second item is menu location

main()