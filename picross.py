from pygame import *
import numpy as np

init()
res=[800,800]
window=display.set_mode(res)
clock = time.Clock()
Font=font.SysFont("Arial",16)
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
grey=(106,106,106)
darkgrey=(50,50,50)


class Game(object):
    def __init__(self):
        file=open("round1.dat")
        line=file.readline()
        line=line.split()
        self.win=False
        self.x=int(line[0])
        self.y=int(line[1])
        self.size=600/max(self.x,self.y)
        self.Font=font.SysFont("Arial",int(self.size)/3)
        self.tab=np.zeros((self.x,self.y))
        self.result=np.zeros((self.x,self.y))
        self.Y=[]            
        for i in range(self.x):
            line=file.readline().split()
            tmp=[]
            for l in line:
                tmp.append(int(l))
            self.Y.append(tmp)

        self.X=[]
        for i in range(self.y):
            line=file.readline().split()
            tmp=[]
            for l in line:
                tmp.append(int(l))
            self.X.append(tmp)
        for i in range(self.x):
            line=file.readline()
            for j in range(self.y):
                self.result[i][j]=int(line[j])
        print self.result


    
    def draw(self):
        window.fill(black)
        for i in range(self.x):
            for j in range(self.y):
                if self.tab[i][j] == 0:
                    draw.rect(window,grey,Rect(200+self.size*i,200+self.size*j,self.size-1,self.size-1),0)
                if self.tab[i][j] == 1:
                    draw.rect(window,blue,Rect(200+self.size*i,200+self.size*j,self.size-1,self.size-1),0)
                if self.tab[i][j] == -1:
                    draw.rect(window,darkgrey,Rect(200+self.size*i,200+self.size*j,self.size-1,self.size-1),0)
        for i in range(len(self.X)):
            for j in range(len(self.X[i])):
                text = self.Font.render(str(self.X[i][j]),True,white)
                window.blit(text,(200+i*self.size+0.4*self.size,200-(len(self.X[i])-j)*self.size/2))        
        for i in range(len(self.Y)):
            for j in range(len(self.Y[i])):
                text = self.Font.render(str(self.Y[i][j]),True,white)
                #window.blit(text,(200+i*self.size+0.4*self.size,200-(len(self.X[i])-j)*self.size/2)) 
                window.blit(text,(200-(len(self.Y[i])-j)*self.size/2,200+i*self.size+0.4*self.size)) 

        if self.win:
            Font2=font.SysFont("Arial",40)
            text = Font2.render("YOU WIN",True,white)  
            window.blit(text,(350,400))                                        

    def check(self):
        res=True
        for i in range(self.x):
            for j in range(self.y):
                if self.tab[i][j] == 1 and self.result[i][j]==0:
                    res=False
                if self.tab[i][j] in [0,-1] and self.result[i][j]==1:
                    res = False
        self.win=res

    def event(self):
        if 200 < mouse.get_pos()[0] < 800 and 200 < mouse.get_pos()[1] < 800:
            pos=[(mouse.get_pos()[0]-200)/self.size,(mouse.get_pos()[1]-200)/self.size]
            if mouse.get_pressed()[0]:
                self.tab[pos[0]][pos[1]] = 1
            if mouse.get_pressed()[2]:
                self.tab[pos[0]][pos[1]] = -1
            if mouse.get_pressed()[1]:
                self.tab[pos[0]][pos[1]] = 0
                      
game=Game()
end=False
while not end:
	for zet in event.get():
		if zet.type ==QUIT:
			end=True
    
	game.draw()
	game.event()
	game.check()
	clock.tick(15)
	display.flip()