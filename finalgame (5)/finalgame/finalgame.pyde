import random
import pickle
gamestate = 0
setupLength = 700
setupWidth = 700
speedincr = 20.0
direction = "forward"
frogx = 200.0
frogy= 400.0
reletivey = 0.0
incr = 0.8
whattoshow = []
roadstartingY =700 
roadlength = 80.0
groundlist = ["road","grass"]
gameround = 0
collided = False
displayYFrog = 0
name = False
pressed = False
moves = ["w","a","w","d", "w","w","w","w", "w", "w", "w"]
scorestate = 0
player1name = ""
turncounter = 0
gameOver = False
showscoreboard = False
delaycount = 120
z = 0
readydelay = 30
error = False
maplength = 200
choice = ""
y = 150
yadder = 0

def setup():
    global movingleftgreen, movingrightgreen, movingbackwardgreen, movingforwardgreen, back, carlist, grass, road, pausebutton, pausebackg,quitbutton,backbutton,scoresbutton,restartbutton, displayfont,namebackground,namefont, greenB,frog1,frog2,frog,scoresB, scoresfont,startscreenB,grassrain,roadrain
    global snowroad, snowgrass,movingbackwardblue,movingrightblue,movingleftblue,movingforwardblue,bluefrogdisplay,greenfrogdisplay, rulesbg, rulesbutton
    size(setupLength,setupWidth)
    rulesbg = loadImage("rules.png")
    bluefrogdisplay = loadImage("bluefrogdisplay.png")
    greenfrogdisplay = loadImage("greenfrogdisplay.png")
    snowroad = loadImage("snowroad.png")
    snowgrass =loadImage("snowgrass.png")
    grassrain = loadImage("grassrain.png")
    roadrain = loadImage("roadrain.png")
    startscreenB = loadImage("startscreenB.png")
    scoresB = loadImage("leaderboard.png")
    greenB = loadImage("background.png")
    namefont = loadFont("Leelawadee-Bold-28.vlw")
    scoresfont = loadFont("AgencyFB-Bold-20.vlw")
    displayfont = loadFont("AgencyFB-Bold-48.vlw")
    pausebackg = loadImage("pausebackground.jpg")
    movingforwardgreen = loadImage("movingforwardleft.png")
    movingleftgreen = loadImage("movingleft.png")
    movingrightgreen = loadImage("movingright.png")
    movingbackwardgreen = loadImage("movingbackward.png")
    movingforwardblue = loadImage("movingforwardleftblue.png")
    movingleftblue = loadImage("movingleftblue.png")
    movingrightblue = loadImage("movingrightblue.png")
    movingbackwardblue = loadImage("movingbackwardblue.png")
    grass = loadImage("grass.png")
    bluecar = loadImage("bluecar.png")
    hatchback = loadImage("hatchback.png")
    orangecar = loadImage("orangecar.png")
    policecar = loadImage("policecar.png")
    redcar = loadImage("redcar.png")
    schoolbus = loadImage("schoolbus.png")
    towtruck = loadImage("towtruck.png")
    yellowcar = loadImage("yellowcar.png")
    road = loadImage("road.png")
    fontforpause= loadFont("ErasITC-Demi-15.vlw")
    carlist = [yellowcar, towtruck, schoolbus, redcar, policecar, orangecar, hatchback, bluecar]
    pausebutton = Button(setupWidth-60,10,50,50,"Pause",255,fontforpause)
    backbutton = Button(150,200,400,50,"Back",255,fontforpause)
    scoresbutton = Button(150,275,400,50,"Scores",255,fontforpause)
    rulesbutton =  Button(150,350,400,50,"Rules",255,fontforpause)
    restartbutton =  Button(150,425,400,50,"Restart",255,fontforpause)
    quitbutton =  Button(150,500,400,50,"Quit",255,fontforpause)
    namebackground =loadImage("namebackground.png")
    frog1 = Player(player1name, 300,400, "forward",choice)
    frog2 = Player("AI", 300,400, "forward",choice)
    frog1.score = -1
    frog2.score = -1
    
def draw():
    global gamestate
    if gamestate == 0:
        homescreen()
    if gamestate ==1:
        namescreen()
    elif gamestate == 2:
        playscreen()
    elif gamestate == 3:
        pauseScreen()
    elif gamestate == 4:
        scoresScreen()
    elif gamestate == 5:
        recursion()
    elif gamestate == 6:
        playerchoice()
    elif gamestate == 7:
        rules()
        
        
def playerchoice():
    background(pausebackg)
    textFont(displayfont)
    fill(0)
    text("Choose your character", 150,200)
    image(greenfrogdisplay, 100, 400, 200,200)
    image(bluefrogdisplay, 400,400,200,200)
def rules():
    background(rulesbg)
    pausebutton.display()
def checkname(name):
    readfile = open("scoresFroger.txt", "rb")     
    scores = pickle.load(readfile)        
    readfile.close()
    for i in range(len(scores)):
        if scores[i][0] == name: 
            return False
    return True
            
def checkOverlap(x1, y1, x2, y2):
    global rectwidth, rectH

    if (x2 >= x1 and x2 <= (x1 + 22)) and (y2 >= y1 and y2 <= (y1 + 23)):
        return True
    elif (x1 >= x2 and x1 <= (x2 + 50)) and (y1 >= y2 and y1 <= (y2 + 20)):
        return True
    elif (x1 >= x2 and x1 <= (x2 + 50)) and (y2 >= y1 and y2 <= (y1 + 20)):
        return True
    elif (x2 >= x1 and x2 <= (x1 + 22)) and (y1 >= y2 and y1 <= (y2 + 23)):
        return True
    return False
def recursion():
    global z, gamestate, readydelay
    if z < 20:
        background(0)
        fill("#39ff14")
        rect(width/2 - z*10, height/2 - 50, z*20, 100)
        z += 1
        delay(100)
    else:
        fill(255)
        textSize(32)
        text("Ready", width/2 -45, height/2 +110) 
        if readydelay == 0:
            gamestate = 6
        else:
            readydelay -= 1
        


def finalY(y):
    global reletivey
    return y-reletivey
class Grass:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
    def display(self):
        displayY = finalY(self.y)
        image(self.img,self.x,displayY)
    def intersection(self):
        pass
class Road:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.cars = []
        self.percentage = random.randint(4,13)
        self.cooldown = 0
        self.roadspeed = random.uniform(1,10.0)
    def display(self):
        global displayY
        displayY = finalY(self.y)
        image(self.img,self.x,displayY)
        
        if self.cooldown == 0:
            if random.randint(0,1000) <= self.percentage:
                self.cars.append(Car(-100, self.roadspeed, carlist[random.randint(0,7)]))
                self.cooldown = 100
        else:
            self.cooldown -= 1
        i = 0
        while i < len(self.cars):
            car = self.cars[i]
            car.display(displayY)
            if car.x>setupWidth:
                self.cars.pop(i)
                i -= 1
            i += 1
            
                    
        
class Player:
    def __init__(self,name, x, y, direction, img):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.score = 0
        self.img = img
    def display(self):
        global displayYFrog
        fill(255)
        textFont(displayfont)
        text("Score: " +str(self.score), 10,40)
        text(self.name + "'s Turn", 10,80)
        displayYFrog = finalY(self.y)
        if self.img == "green":
            if self.direction == "down":
                image(movingbackwardgreen,self.x, displayYFrog)
            elif self.direction == "left":
                image(movingleftgreen,self.x, displayYFrog)
            elif self.direction == "forward":
                image(movingforwardgreen,self.x, displayYFrog)
            elif self.direction == "right":
                image(movingrightgreen,self.x, displayYFrog)
        else:
            if self.direction == "down":
                image(movingbackwardblue,self.x, displayYFrog)
            elif self.direction == "left":
                image(movingleftblue,self.x, displayYFrog)
            elif self.direction == "forward":
                image(movingforwardblue,self.x, displayYFrog)
            elif self.direction == "right":
                image(movingrightblue,self.x, displayYFrog)
class Car:
    def __init__(self,x,speed,img):
        self.x = x
        self.speed = speed
        self.img = img
    def display(self,displayY):
        global collided
        if frog == None:
            pass
        else:
            if checkOverlap(frog.x, displayYFrog, self.x, displayY):
                collided = True
        self.x += self.speed
        image(self.img,self.x,displayY)
   
class Button:
    def __init__(self, x, y, w, h, t, c, font):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.t = t
        self.c = c
        self.font = font
    def display(self):
        if self.hovered():
            fill(150)
        else:
            fill(self.c)
        rect(self.x, self.y, self.w, self.h)
        fill(0)
        textFont(self.font)
        text(self.t, self.x + (self.w/8), self.y + (self.h/2))
    def hovered(self):
        if mouseX >= self.x and mouseX <= self.x + self.w and mouseY >= self.y and mouseY <= self.y + self.h:
            return True
        return False
            
        
        
        
    
    
def homescreen():
    background(startscreenB)
def namescreen():
    global frog,frog1, frog2
    background(namebackground)
    if error == True:
        fill("#FF0000")
        text("Error: Name already exists.", 190,200)
    fill(0)
    textFont(namefont)
    text(player1name, 350, 267)
    frog1 = Player(player1name, 300,400, "forward",choice)
    frog2 = Player("AI", 300,400, "forward",choice)
    frog = None

def playscreen():
    global frog, gameround,  whattoshow, roadstartingY, grass,road, Grass, reletivey, incr, frog, AIcooldown, turncounter, gamestate, showscoreboard,delaycount, maplength
    if reletivey < -400:
        maplength+=1
    if gameround == 0:
        if turncounter<=1:
            turncounter+=1
            AIcooldown = 0
            if frog is None or frog.name == "AI":
                frog = frog1
            else:
                frog = frog2
            for i in range(maplength):
                current_thing = groundlist[random.randint(0,1)]
                roadstartingY -= roadlength
                if i<12:
                    if i<5:
                        current_thing = "grass"
                    if current_thing == "grass":
                        i = Grass(0,roadstartingY, grass)
                        whattoshow.append(i)
                    else:
                        i = Road(0,roadstartingY, road)
                        whattoshow.append(i)
                elif i>=12 and i<24:
                    if current_thing == "grass":
                        i = Grass(0,roadstartingY, grassrain)
                        whattoshow.append(i)
                    else:
                        i = Road(0,roadstartingY, roadrain)
                        whattoshow.append(i)
                elif i >= 24:
                    if current_thing == "grass":
                        i = Grass(0,roadstartingY, snowgrass)
                        whattoshow.append(i)
                    else:
                        i = Road(0,roadstartingY, snowroad)
                        whattoshow.append(i) 
                    
            gameround = 1
    for i in whattoshow:
        i.display()

    if frog.name == "AI" and gameround!= 2:
        move = moves[random.randint(0,10)]
        if AIcooldown == 0:
            if move == "w":
                frog.score +=1
                frog.y -= speedincr
                frog.direction = "forward"
            elif move == "a":
                    frog.x -= speedincr
                    left = True
                    frog.direction = "left"
            elif move == "d":
                frog.x += speedincr
                frog.direction = "right"
            elif move == "s":
                frog.score -= 1
                frog.y += speedincr
                frog.direction = "down"
            AIcooldown = 15
        else:
            AIcooldown -= 1
        
    if collided == True:
        gameround = 2
    if gameround ==2:
        textFont(displayfont)
        fill(255)
        text("Round over, frog did not survive", 80, 220)
        text("score: "+ str(frog.score),230,300)
        text("Click to contine", 200, 380)
        
    if gameround!= 2:
        frog.display()
        reletivey-=incr
    if gameOver == True:
        background(greenB)
        textFont(displayfont)
        if frog1.score > frog2.score:
            text("Game Over!", 200,300)
            text(frog1.name + " wins",200,400)
        elif frog1.score == frog2.score:
            text("Game Over!", 200,300)
            text(frog2.name + " and " + frog1.name + " tied",200,400)
        else:
            text("Game Over!", 200,300)
            text(frog2.name + " wins",200,400)
        showscoreboard = True
    if showscoreboard == True:
        if delaycount == 0:
            gamestate =4
        else:
            delaycount-=1
        
        
    pausebutton.display()
    

    
    
def pauseScreen():
    background(pausebackg)
    backbutton.display()
    quitbutton.display()
    restartbutton.display()
    scoresbutton.display()
    rulesbutton.display()

def scoresScreen():
    global readfile, scores, player1, player2, scorestate, y
    background(scoresB)
    if scorestate == 0:
        scores = []
        readfile = open("scoresFroger.txt", "rb")     
        scores = pickle.load(readfile)        
        readfile.close()
        if frog1.score > 0:
            replaced = False
            for i in range(len(scores)):
                if scores[i][0] == frog1.name: 
                    if scores[i][1] < frog1.score:
                        scores[i][1] = frog1.score
                    replaced = True
            if not replaced:
                scores.append([frog1.name, frog1.score])
                replaced = True
            scores.sort(key=lambda obj: int(obj[1]), reverse = True)
            if len(scores)>13:
                scores.pop(-1)
            writefile = open("scoresFroger.txt", "wb")
    
            pickle.dump(scores, writefile)
            writefile.close()
            scorestate = 1
    y = 150
    fill(255)
    if len(scores) > 0:
        for n in scores:
            y +=30
            fill(255)
            textFont(scoresfont)
            if y+yadder<600 and y+yadder >=150:
                text(str(n[0]) +":", 130, y+yadder)
                text(str(n[1]) , 400,y +yadder)
    else:
        textFont(scoresfont)
        text("scores list is currently empty:(", 150,300)
    pausebutton.display()
def mouseReleased():
    global gamestate, frog, pressed, gamestate, gameround, reletivey, whattoshow, roadstartingy, collided, gameOver, turncounter, frog1, frog2, frog, player1name,error, choice, reletivey, pressed,displayYFrog,z,readydelay, frog1, frog2,showscoreboard, collided,gameOver 

    if gamestate ==1:
        if mouseX >= 137 and mouseX <= 580 and mouseY >= 225 and mouseY <= 290:
            pressed = True
        if mouseX >= 215 and mouseX <= 490 and mouseY >= 360 and mouseY <= 430:
            if checkname(player1name):
                name = True 
                gamestate = 2
                error = False
            else:
                error = True
    if gamestate == 2 or gamestate == 4 :
        if pausebutton.hovered():
            gamestate = 3
    if gamestate == 2 and gameround == 2:
        if turncounter ==2:
            gameOver = True
        else:
            gameround = 0
            reletivey = 0.0
            # whattoshow = []
            roadstartingy = 700
            collided = False
        
    if gamestate == 3:
        if backbutton.hovered():
            gamestate = 2
        elif quitbutton.hovered():
            exit()
        elif scoresbutton.hovered():
            gamestate = 4
        elif restartbutton.hovered():
            gameround = 0
            gamestate = 0
            reletivey = 0.0
            player1name = ""
            frog = frog2
            turncounter = 0
            choice = ""
            pressed = False
            displayYFrog = 0
            z = 0
            frog1 = Player(player1name, 300,400, "forward",choice)
            frog2 = Player("AI", 300,400, "forward",choice)
            frog1.score = -1
            frog2.score = -1
            showscoreboard = False
            readydelay = 30
            collided = False
            gameOver = False
        elif rulesbutton.hovered():
            gamestate = 7
            gameOver = False
    elif gamestate == 6:
        if mouseX >= 100 and mouseX <= 300 and mouseY >= 400 and mouseY <= 600:
            choice = "green"
            gamestate = 1
        if mouseX >= 400 and mouseX <= 600 and mouseY >= 400 and mouseY <= 600:
            choice = "blue"
            gamestate = 1
    elif gamestate == 7:
        if pausebutton.hovered():
            gamestate = 3

            
def keyReleased():
    global frog, speedincr, direction, frogx, frogy, player1name, name1, gamestate
    if gamestate ==0:
        gamestate = 5
    if gamestate == 1 and pressed == True:
            if key != "\n":
                if key == "\b":
                    if (player1name) !="":
                        player1name = player1name[:-1]
                else:
                    if len(str(key)) == 1:
                        player1name += key
        
    elif gamestate ==2 :
        if gameround != 2 and frog.name == player1name:
            if key == "w":
                frog.score +=1
                frog.y -= speedincr
                frog.direction = "forward"
            elif key == "a":
                frog.x -= speedincr
                left = True
                frog.direction = "left"
            elif key == "d":
                frog.x += speedincr
                frog.direction = "right"
            elif key == "s":
                frog.score -= 1
                frog.y += speedincr
                frog.direction = "down"
def mouseWheel(event):
    global yadder
    if gamestate == 4:
        if event.getCount() > 0 and yadder<0: 
            yadder += 5
        elif y >5:
            yadder -= 5

            
                
