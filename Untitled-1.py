from tkinter import *

window = Tk()

window.title('owned by tg:@h1katsuka')
c = Canvas(window,width=720,height=480,bg='white')

# sky
c.create_rectangle(0, 0, 720, 3000, fill='#6b5ba6', outline='#6b5ba6')    

######################################################################################

# stars_on_left_side
c.create_oval(31, 41, 38, 48, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(91, 111, 98, 118, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(161, 56, 168, 63, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(121, 26, 128, 33, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(41, 141, 48, 148, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')


# stars_on_right_side
c.create_oval(541, 41, 548, 48, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(441, 61, 448, 68, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(401, 161, 408, 168, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(466, 121, 473, 128, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(546, 135, 553, 142, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(586, 88, 593, 95, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(646, 28, 653, 35, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(666, 168, 673, 175, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(696, 68, 703, 75, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')                   

# moon
c.create_oval(286, 40, 390, 160, 
            width=0, fill='#ffdfb9', outline='#ffdfb9')
c.create_oval(313, 24, 420, 132, 
            width=0, fill='#6b5ba6', outline='#ffdfb9')
######################################################################################
#####################################__layer-01__#####################################

# big_back_hill
c.create_polygon((204, 90), (-50, 380), (460, 380), fill='#693c91')
c.create_polygon((-50, 380), (70, 200), (300, 200), (400 ,380), fill='#693c91')
c.create_polygon((-50, 380), (5, 270), (300,270), (400, 380), fill='#693c91')

# center_back_hills
c.create_polygon((356, 220), (240,380), (486, 380), fill='#693c91')
c.create_polygon((398, 230), (266,380), (566, 380), fill='#693c91')

# friendly_back_hills
c.create_polygon((486, 135), (334, 380), (640, 380), fill='#693c91')
c.create_polygon((610, 180), (440, 380), (750, 380), fill='#693c91')

# tree
c.create_polygon((230, 75), (210, 170), (250, 170), fill='#693c91')
c.create_polygon((250, 95), (230, 170), (270, 170), fill='#693c91')
c.create_polygon((120, 115), (100, 200), (140, 200), fill='#693c91')
c.create_polygon((139, 120), (116, 200), (160, 200), fill='#693c91')
c.create_polygon((44, 195), (24, 300), (64, 300), fill='#693c91')
c.create_polygon((44, 195), (24, 300), (64, 300), fill='#693c91')
c.create_polygon((28, 225), (13, 300), (43, 300), fill='#693c91')
c.create_polygon((450, 155), (417, 260), (480, 240), fill='#693c91')
c.create_polygon((425, 196), (396, 275), (450, 275), fill='#693c91')
c.create_polygon((645, 196), (627, 260), (657, 260), fill='#693c91')
######################################################################################
#####################################__layer-02__#####################################

# right_hill
c.create_polygon((486, 198), (385, 380), (593, 380),
            fill='#66327c')
c.create_rectangle(520, 286, 720, 380,
            fill='#66327c', outline='#66327c')

# left_hill
c.create_polygon((340, 262), (260, 380), (444, 380), fill='#66327c')
c.create_polygon((260, 232), (168, 380), (386, 380), fill='#66327c')
c.create_polygon((180, 282), (108, 380), (286, 380), fill='#66327c')
c.create_polygon((50, 380), (95, 320), (300,320), (400, 380), fill='#66327c', outline='#66327c')

# tree
c.create_polygon((60, 263), (37, 350), (83, 350), fill='#66327c')
c.create_polygon((30, 293), (12, 350), (57, 350), fill='#66327c')
c.create_polygon((143, 235), (123,330), (163, 330), fill='#66327c')
c.create_polygon((116, 275), (103,330), (133, 330), fill='#66327c')
c.create_polygon((212, 205), (193,330), (243, 330), fill='#66327c')
c.create_polygon((312, 230), (289,330), (340, 330), fill='#66327c')
c.create_polygon((583, 235), (558,330), (613, 330), fill='#66327c')
c.create_polygon((603, 215), (578,330), (633, 330), fill='#66327c')
c.create_polygon((623, 248), (608,340), (648, 340), fill='#66327c')
c.create_polygon((506, 200), (480, 320), (525, 320), fill='#66327c')

# mini_ground
c.create_rectangle(0, 334, 720, 380, fill='#66327c', outline='#66327c')
######################################################################################
#####################################__layer-03__#####################################

c.create_polygon((720, 230),(540, 380),(720, 380), fill='#5c2b6c')
c.create_rectangle(600, 360, 470, 380, fill='#5c2b6c', outline='#5c2b6c')
c.create_polygon((420,290), (320, 380), (530, 380), fill='#5c2b6c')

# tree
c.create_polygon((696, 200), (680, 270), (720, 270), fill='#5c2b6c')
c.create_polygon((670, 230), (650, 300), (690, 270), fill='#5c2b6c')
c.create_polygon((486, 234), (438, 380), (534, 380), fill='#5c2b6c')
c.create_polygon((518, 276), (486, 380), (550, 380), fill='#5c2b6c')
######################################################################################
#######################################__home__#######################################

c.create_polygon((421, 288), (421, 240), (441, 240), (441,300), fill='#481a48')     #дымоход
c.create_polygon((417, 245), (417, 238), (446, 238), (446, 245), fill='#481a48')

c.create_polygon((298, 380),
                 (298, 340), (283, 340), (283, 346), (298, 346),                    # штука какая-то
                 (298, 320), (282, 320),                                            # треугольник
                 (298, 310), (368, 310),                                            # крыша
                 (368, 220), (515, 355), (515, 360),                                # большой треугольник 
                 (510, 360), (510, 380),                                            
                fill='#512151')

## light
c.create_polygon((308, 328), (308, 323), (340, 323), (340, 328), fill='#ffdfb9')
c.create_polygon((308, 331), (308, 336), (328, 336), (328, 331), fill='#ffdfb9') 
c.create_polygon((331, 331), (331, 336), (340, 336), (340, 331), fill='#ffdfb9') 
c.create_polygon((349, 328), (349, 323), (365, 323), (365, 328), fill='#ffdfb9')
c.create_polygon((349, 331), (349, 336), (365, 336), (365, 331), fill='#ffdfb9')

c.create_polygon((325, 368), (325, 355), (340, 355), (340, 368), fill='#ffdfb9')
c.create_polygon((349, 368), (349, 355), (353, 355), (353, 368), fill='#ffdfb9')
c.create_polygon((356, 368), (356, 355), (365, 355), (365, 368), fill='#ffdfb9')

c.create_polygon((378, 368), (378, 283), (430, 283), (430 ,368), fill='#ffdfb9')
c.create_polygon((389, 368), (389, 283), (395, 283), (395, 368), fill='#512151')
c.create_polygon((444, 368), (444, 351), (490, 351), (490, 368), fill='#ffdfb9')
c.create_polygon((458, 368), (458, 351), (462, 351), (462, 368), fill='#512151')
c.create_polygon((477, 368), (477, 351), (473, 351), (473, 368), fill='#512151')
c.create_polygon((407, 368), (407, 283), (412, 283), (412, 368), fill='#512151')
c.create_polygon((425, 368), (425, 283), (430, 283), (430, 368), fill='#512151')
c.create_polygon((378, 351), (378, 327), (430, 327), (430, 351), fill='#512151')
############

# lantern
c.create_polygon((530, 380), (530, 342), (535, 342), (535, 380), fill='#522254')
c.create_oval(523, 340, 541, 322, fill='#ffdfb9', outline='#ffdfb9')

# main_ground

c.create_polygon((250, 340), (242, 380), (258, 380), fill='#481a48')
c.create_polygon((230, 326), (220, 380), (240, 380), fill='#481a48')

c.create_rectangle(0, 560, 720, 380, fill='#481a48', outline='#481a48')
c.pack() 
window.mainloop() 