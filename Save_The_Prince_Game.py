#Final Project- Save The Prince Game
#Diego Daboub, Christopher Lovejoy, Michael Marcoux
#Credit to Issac Sheets for helping with object instantiation

    #Version 10.0.1
    #Added some comments explaining how code works
    #Image citation
    
#princess image - https://www.pngguru.com/free-transparent-background-png-clipart-kupxn/download
#prince image - https://www.pngguru.com/free-transparent-background-png-clipart-vzgnr/download
#background image - https://www.flickr.com/photos/84568447@N00/4854195954
  #all images were labeled for noncommercial reuse

import gui
import timer
from time import sleep

#Creates Princess class 
#includes start coordinates, shape attributes and directional functions for the key press

#create class life that records 3 lives at beginning
class Life:
  lives = 3
  winGame = false

#check to update a label and lives when princess dies
  def updateLives(self):
    global livesLabel
    self.lives -= 1
    livesLabel.setText("Lives: " + str(self.lives))
    self.checkLose()

#function to display information when lives run out 
#will also stop the main song from playing    
  def checkLose(self):
    if self.lives == 0:
      showInformation("You died! Try again?")
      stopPlaying(theme)
      
#upon win, prince and princess objects are removed, win sound plays  
#information letting player know they've won          
  def winGame(self):
    global gameWorld, prince
    gameWorld.remove(prince.shape)
    gameWorld.remove(princess.shape)
    winSound = makeSound("C:\Users\Christopher Lovejoy\Desktop\Code 1300 Final Project\Sound\winTrack.wav")
    stopPlaying(theme)
    play(winSound)
    sleep(3)
    stopPlaying(winSound)
    showInformation("You win! :)")
    

myLives = Life()  

#moves class that prompts a label when moves reach 0      
class Moves:
  moves = 250
  youLose = false
  loseLabel = gui.Label("You're out of moves! YOU LOSE.")
  loseLabel.setForeground(gui.Color.WHITE)
 
#function that decreases moves amount by one
#will run every time a key is pressed   
  def updateMoves(self):
    global movesLabel
    self.moves -=1
    movesLabel.setText("Moves: " + str(self.moves))

#function to detect when moves = 0, and will lose the game and remove sprites    
  def checkNoMoves(self):
    global handleKeyPress
    if self.moves == 0:
      self.youLose = true
      gameWorld.add(Moves.loseLabel, 125, 300)
      gameWorld.remove(movesLabel)
      
myMoves = Moves()
  
#princess class that creates and removes princess based on win/lose
class Princess():
  
  def makePrincess(self, panel):
    
    princess = gui.Icon("C:\Users\Christopher Lovejoy\Desktop\Code 1300 Final Project\Images\princess.png",20,20)
       
    panel.add(princess, 580, 580)
    self.shape = princess
    
  def killPrincess(self, panel):
    panel.remove(princess)
    
#check to see if princess object interacts (touches) a border or the prince
#if prince is intersected, the game will prompt a win      
  def touchCheck(self):
    global bList, myLives, prince
    
    if prince.shape.intersects(self.shape) == true:
      myLives.winGame()
      
    for border in bList:
      if border.intersects(self.shape) == true:
        myLives.updateLives()
        self.shape.setPosition(580,580)
        
   
        
#functions to move princess in certain directions depending on key press    
  def moveLeft(self):
    pos = self.shape.getPosition()
    self.shape.setPosition(pos[0] - 6, pos[1] +0)
  def moveRight(self):
    pos = self.shape.getPosition()
    self.shape.setPosition(pos[0] + 6, pos[1] +0)
  def moveUp(self):
    pos = self.shape.getPosition()
    self.shape.setPosition(pos[0] +0, pos[1] -6)
  def moveDown(self):
    pos = self.shape.getPosition()
    self.shape.setPosition(pos[0] +0, pos[1] +6)
  def moveDownRight(self):
    pos = self.shape.getPosition()
    self.shape.setPosition(pos[0] +6, pos[1] +6)
  def moveDownLeft(self):
    pos = self.shape.getPosition()
    self.shape.setPosition(pos[0] -6, pos[1] +6)
  def moveUpRight(self):
    pos = self.shape.getPosition()
    self.shape.setPosition(pos[0] +6, pos[1] -6)
  def moveUpLeft(self):
    pos = self.shape.getPosition()
    self.shape.setPosition(pos[0] -6, pos[1] -6)

#prince object to create a prince in top right corner of panel     
class Prince():
  
  def makePrince(self,panel):
  
    prince = gui.Icon("C:\Users\Christopher Lovejoy\Desktop\Code 1300 Final Project\Images\prince.png",80,80)
    panel.add(prince, 550, 40)
    
    self.shape = prince
  
#Border class for maze barriers
class Border():

  def createBorder(self,x,y,w,h):
    border = gui.Rectangle(x,y,w,h,gui.Color(255,0,127),true)
    gameWorld.add(border)   
    
    global bList
    bList.append(border)
                                    
#creates function to add the princess, prince and border objects in the game                                                    
def runProgram():
  global lives, livesLabel, movesLabel, prince
  princess = Princess()
  princess.makePrincess(gameWorld)
  
  prince = Prince()
  prince.makePrince(gameWorld)
  
  border = Border()
  border.createBorder(0,275,275,300)
  border.createBorder(300,275,600,300)
  border.createBorder(0,450,450,475)
  border.createBorder(475,450,600,475)
  border.createBorder(0,150,150,175)
  border.createBorder(175,150,600,175)  
  
  livesLabel = gui.Label("Lives: " + str(myLives.lives)) 
  gameWorld.add(livesLabel)
  livesLabel.setForeground(gui.Color.WHITE)
  
  movesLabel = gui.Label("Moves: " + str(myMoves.moves) + "   ")
  gameWorld.add(movesLabel, 0,30)
  movesLabel.setForeground(gui.Color.WHITE)
  
  showInformation("Rescue the prince! Use the arrow keys to move the princess")
    
  return princess
  

#Links arrow keys to the desired directional movement
def handleKeyPress(key):
  global princess
  global myMoves
  global myLives
  if key == 37:
    princess.moveLeft()
  if key == 39:
    princess.moveRight()
  if key == 38:
    princess.moveUp()
  if key == 40:
    princess.moveDown()
  if key == 40 and 39:
    princess.moveDownRight()
  if key == 38 and 39:
    princess.moveUpRight()
  if key == 40 and 37:
    princess.moveDownLeft()
  if key == 38 and 37:
    princess.moveUpLeft()
    
  princess.touchCheck()
  myMoves.updateMoves()
  myLives.checkLose()
  myMoves.checkNoMoves()
    
theme = makeSound(r"C:\Users\Christopher Lovejoy\Desktop\Code 1300 Final Project\Sound\theme.wav")
play(theme)
  
  #displays game world
gameWorld = gui.Display('Save the Prince!', 600, 600,0,0,white)
background = gui.Icon("C:\Users\Christopher Lovejoy\Desktop\Code 1300 Final Project\Images\Background.jpg",1500,1500)
gameWorld.add(background)
#create list for borders
bList = []

prince = "placeholder for instance"
#calls function for key press
gameWorld.onKeyDown(handleKeyPress)  

#calls function to start the game
princess = runProgram()


                                                                                                                                                                                                                                        