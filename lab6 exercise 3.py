class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = 250
        self.g = 255
        self.b = 102
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)

    
    def isMouseOn(self):
        mouseX , mouseY=pg.mouse.get_pos()
        if mouseX >= self.x and mouseX <= self.x+self.w and mouseY >= self.y and mouseY <= self.y + self.h:
            return True
        else:
            return False
btn = Button(500,200,100,100) # สร้าง Object จากคลาส Button ขึ้นมา   

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
class  Age:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isnumeric():
                        self.text += event.unicode
                    else:
                        return False
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


    
import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))  

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32) # สร้าง InputBox2
input_box3 = Age(100, 300, 140, 32) # สร้าง InputBox2
input_boxes = [input_box1, input_box2 , input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
font1 = pg.font.Font('freesansbold.ttf', 25) # font and fontsize
font2 = pg.font.Font('freesansbold.ttf', 20) # font and fontsize
font1 = pg.font.Font('freesansbold.ttf', 25) # font and fontsize
text = font.render('First Name',True,(0,128,255),(255,255,255)) # (text,is smooth?,letter color,background color)
text2 = font.render('Last Name',True,(0,128,255),(255,255,255))
text3 = font.render('Age',True,(0,128,255),(255,255,255))
text4 = font1.render('submit',True,(0,0,0))
textRect = text.get_rect() # text size
textRect2 = text.get_rect() # text size
textRect3 = text.get_rect() # text size
textRect4 = text.get_rect() # text size
textRect5 = text.get_rect() # text size
textRect.center = (160,65)
textRect2.center = (160,165)
textRect3.center = (160,265)
textRect4.center = (600,300)
textRect5.center = (440,220)
btn = Button(400,100,120,75) # สร้าง Objct จากคลาส Button ขึ้นมา
btn.draw(screen)
Click = False

while run:
    screen.fill((255, 255, 255))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        btn.draw(screen)
        screen.blit(text, (100,68))
        screen.blit(text2, (100,168))
        screen.blit(text3, (100,260))
        screen.blit(text4, (415,127))


    if btn.isMouseOn():
        if pg.mouse.get_pressed() == (1,0,0):
            Click = True
            btn.r,btn.g,btn.b = (51,255,153)
        else:
            btn.r,btn.g,btn.b = (153,255,255)
    if Click == True:
        text5 = font2.render('hello '+str(input_box1.text)+' '+str(input_box2.text)+'! You are '+str(input_box3.text)+' years old.',True,(153,76,0),(255,204,229))
        screen.blit(text5,textRect5)

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    pg.time.delay(1)
    pg.display.update()