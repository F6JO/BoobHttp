#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: zhzyker
from color import color
import random

banner_1 = color.yellow(r""" 
   ___                _              _    _          
  / __\  ___    ___  | |__    /\  /\| |_ | |_  _ __  
 /__\// / _ \  / _ \ | '_ \  / /_/ /| __|| __|| '_ \ 
/ \/  \| (_) || (_) || |_) |/ __  / | |_ | |_ | |_) |
\_____/ \___/  \___/ |_.__/ \/ /_/   \__| \__|| .__/ 
                                              |_|    
                                        
""")

banner_2 = color.cyan_fine(r'''
 ______     ______     ______     ______     __  __     ______   ______   ______  
/\  == \   /\  __ \   /\  __ \   /\  == \   /\ \_\ \   /\__  _\ /\__  _\ /\  == \ 
\ \  __<   \ \ \/\ \  \ \ \/\ \  \ \  __<   \ \  __ \  \/_/\ \/ \/_/\ \/ \ \  _-/ 
 \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\    \ \_\    \ \_\  \ \_\   
  \/_____/   \/_____/   \/_____/   \/_____/   \/_/\/_/     \/_/     \/_/   \/_/   
                                                                                  
''')


banner_3 = color.red(r'''
  ____                    _       _   _   _     _           
 | __ )    ___     ___   | |__   | | | | | |_  | |_   _ __  
 |  _ \   / _ \   / _ \  | '_ \  | |_| | | __| | __| | '_ \ 
 | |_) | | (_) | | (_) | | |_) | |  _  | | |_  | |_  | |_) |
 |____/   \___/   \___/  |_.__/  |_| |_|  \__|  \__| | .__/ 
                                                     |_|    
''')



banner_4 = color.green(r'''
 ______                       __         ____  ____    _      _              
|_   _ \                     [  |       |_   ||   _|  / |_   / |_            
  | |_) |    .--.     .--.    | |.--.     | |__| |   `| |-' `| |-'  _ .--.   
  |  __'.  / .'`\ \ / .'`\ \  | '/'`\ \   |  __  |    | |    | |   [ '/'`\ \ 
 _| |__) | | \__. | | \__. |  |  \__/ |  _| |  | |_   | |,   | |,   | \__/ | 
|_______/   '.__.'   '.__.'  [__;.__.'  |____||____|  \__/   \__/   | ;.__/  
                                                                   [__|      

''')


banner_5 = color.magenta(r'''
oooooooooo.                       .o8       ooooo   ooooo     .       .              
`888'   `Y8b                     "888       `888'   `888'   .o8     .o8              
 888     888  .ooooo.   .ooooo.   888oooo.   888     888  .o888oo .o888oo oo.ooooo.  
 888oooo888' d88' `88b d88' `88b  d88' `88b  888ooooo888    888     888    888' `88b 
 888    `88b 888   888 888   888  888   888  888     888    888     888    888   888 
 888    .88P 888   888 888   888  888   888  888     888    888 .   888 .  888   888 
o888bood8P'  `Y8bod8P' `Y8bod8P'  `Y8bod8P' o888o   o888o   "888"   "888"  888bod8P' 
                                                                           888       
                                                                          o888o      
                                                                                     
''')



def banner():
    o_o = random.choice(range(5))
    if o_o == 0:
        return banner_1
    elif o_o == 1:
        return banner_2
    elif o_o == 2:
        return banner_3
    elif o_o == 3:
        return banner_4
    elif o_o == 4:
        return banner_5