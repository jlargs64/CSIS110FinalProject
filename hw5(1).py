#Justin Largo
#12/8/17
#This program creates an animation based on the classic arcade game
#Mortal Kombat with Sub Zero and Scorpion fighting
 
import random
import os
import math
import java.awt.Font as Font
#program 173
def clip(picture, startX, startY, endX, endY):
  width = endX - startX + 1
  height = endY - startY + 1
  resPict = makeEmptyPicture(width, height)
  resX = 0
  for x in range(startX, endX):
   resY = 0
   for y in range(startY, endY):
    origPixel = getPixel(picture,x,y)
    resPixel = getPixel(resPict, resX, resY)
    setColor(resPixel, (getColor(origPixel)))
    resY = resY + 1
   resX = resX + 1
  return resPict
def copy(source, target, targX, targY):
  targetX = targX
  for sourceX in range(0, getWidth(source)):
   targetY = targY
   for sourceY in range(0, getHeight(source)):
    px = getPixel(source, sourceX, sourceY)
    tx = getPixel(target, targetX, targetY)
    setColor(tx, getColor(px))
    targetY = targetY + 1
   targetX = targetX + 1
# from text, Program 175
def writeFrame(num, dir, pict):
  numStr = str(num)
  if num < 10:
    writePictureTo (pict, dir+"\\frame00"+numStr+".jpg")
  if num >= 10 and num < 100:
    writePictureTo (pict, dir+"\\frame0"+numStr+".jpg")
  if num >= 100:
    writePictureTo (pict, dir+"\\frame"+numStr+".jpg")

# create the animation
def flick():
  #Make the os change to desired directory
  os.chdir("C:\\Users\\justi\\Dropbox (Siena College)\\CSIS 110 MM\\HW\\hw5\\frames")
  #Sets the directory to where we just changed it to
  directory = os.getcwd()
  #Prints it to make sure we have the right one
  print (os.getcwd())
  #Creates a loop sorting through the directory for .jpg files
  for file in os.listdir(directory):
    if file.endswith(".jpg"):
      if file < 10:
        #deletes the file at the path
        os.remove(str(file)) 
      elif file >= 10:
        os.remove(str(file)) 
      else:
        os.remove(str(file))
        
  setMediaPath("HW\hw5")
  
  scorpion = makePicture(getMediaPath("scorpion.jpg"))
  subzero = makePicture(getMediaPath("subzero.jpg"))
  scorpionStart = clip(scorpion, 18, 1180, 86, 1280)
  scorpionEnd = clip(scorpion, 243, 1180, 314, 1280)
  subZeroStart = clip(subzero, 1739, 1177, 1790, 1272)
  subZeroEnd = clip(subzero, 1604, 1187, 1674, 1274)
  
  # create the animation
  for frameNum in range (0, 151):
    canvas = makePicture(getMediaPath("background.jpg"))
    positionX1 = getWidth(canvas)/5-50
    positionY1 = getHeight(canvas)/2
    positionX2 = getWidth(canvas)-75
    positionY2 = getHeight(canvas)/2
    #text changing sizes at different frame intervals
    if frameNum < 75:  
      style1 = makeStyle("Comic Sans", Font.BOLD, 34+frameNum/10)
      text = "Finish Him!"    
      addTextWithStyle(canvas, getWidth(canvas)/3, getHeight(canvas)/4, text, style1,red) 
    else:
      style1 = makeStyle("Comic Sans", Font.BOLD, 34-frameNum/10)
      text = "Finish Him!"   
      addTextWithStyle(canvas, getWidth(canvas)/3, getHeight(canvas)/4, text, style1,red)
     #The characters switch positions
    if frameNum<=80:
      if frameNum%25 ==0:
        copy(scorpionStart, canvas, positionX1, positionY1)
        copy(subZeroStart, canvas, positionX2, positionY2)
      else:
        copy(scorpionEnd, canvas, positionX1, positionY1)
        copy(subZeroEnd, canvas, positionX2, positionY2)
    else:
    #Characters move in circles
      copy(scorpionStart, canvas, positionX1 + int(10*sin(frameNum)), positionY1+int(10*cos(frameNum)))
      copy(subZeroStart, canvas, positionX2+int(10*cos(frameNum)), positionY2 - int(30*sin(frameNum)))
    #Fireball moving and changing directions
    if frameNum <=30:  
      addOvalFilled (canvas, (positionX1+30)+frameNum*10, positionY1, 25, 25, red)
    else:
      addOvalFilled (canvas, getWidth(canvas)-(frameNum*10)/2, positionY1, 25, 25, blue)
    
    writeFrame(frameNum,directory,canvas)
  # wrap up
  movie = makeMovieFromInitialFile (directory+"\\frame000.jpg")
  writeQuicktime(movie, getMediaPath("flick.mov"), 30)
  
  return movie
