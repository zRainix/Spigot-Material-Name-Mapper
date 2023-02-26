# Spigot-Material-Name-Mapper

An material name mapper working for the latest Minecraft versions.

This script should work for versions 1.13 and above.

A script for 1.12 and under might follow soon.

How to use the material name mapper:

This material mapper is based on the offical Minecraft lang files. To get this file you need to launch the Minecraft version that your server is running on. When this is done, you can close your Minecraft application and open your ".minecraft" folder. To do that press Win + R and type in "%appdata%" and press enter. In your file explorer open the ".minecraft" folder. Then navigate to "versions" and open the folder with the version you just started. In this folder should be a ".jar" file, which you need to open with WinRar or any other programm that can open archived files. Now navigate to "assets" -> "minecraft" -> "lang". In there you should find a ".json" language file. Note: If this is a ".lang" file, this script won't work. Also make sure that the item- and blocknames start with "(item/block).minecraft.". If this is all done move the ".json" file in a folder with the python script. Execute the python script and you should have a "ItemMapper.java" file that can be imported into your Minecraft plugin.

This script was tested on version 1.19.3.
