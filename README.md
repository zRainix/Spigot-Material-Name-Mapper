# Spigot-Material-Name-Mapper

A material name mapper working for the latest Minecraft versions.

These scripts should work for versions 1.13 and above.

Scripts for 1.12 and under might follow soon.

How to use the material name mapper (materialMapper.py):

This material mapper is based on the official Minecraft lang files. To get this file you need to launch the Minecraft version that your server is running on. When this is done, you can close your Minecraft application and open your ".minecraft" folder. To do that, press Win + R and type in "%appdata%" and press enter. In your file explorer, open the ".minecraft" folder. Then navigate to "versions" and open the folder with the version you just started. In this folder should be a ".jar" file, which you need to open with WinRar or any other programme that can open archived files. Now navigate to "assets" -> "minecraft" -> "lang". There you should find a ".json" language file. Note: If this is a ".lang" file, this script won't work. Also make sure that the item and block names start with "(item/block).minecraft.". If this is all done, move the ".json" file into a folder with the python script. Execute the python script and you should have an "ItemMapper.java" file that can be imported into your Minecraft plugin.

How to use the enhanced material name mapper (enhancedMaterialMapper.py):

This mapper can now also get the name mappings of other languages besides us_en. To use this script you need to launch the Minecraft version that your server is running on. When this is done, you can close your Minecraft application and open your ".minecraft" folder. To do that, press Win + R and type in "%appdata%" and press enter. In your file explorer, open the ".minecraft" folder. Now in that folder, create a new folder (the name doesn't matter) and copy the "enhancedMaterialMapper.py" script into it. Now you can edit your file and put your desired version and languageCode. For the newer versions, the version should be just '1.xx' and not '1.xx.y'. In this example, it is 1.19. languageCode is 'de_de', which can be any language supported by Minecraft. Now you only have to run the script and an "ItemMapper.java" file should appear in your folder that can be imported into your Minecraft plugin.

These scripts were tested on version 1.19.3.

