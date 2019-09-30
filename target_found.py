import numpy
from PIL import Image
from PIL import ImageGrab
import pyautogui

def image_compare(imageX, imageY, height, width, target, image):
	picker = image[imageY : imageY+height, imageX : imageX+width];
	return numpy.array_equal(target, picker);

def screenprint2png(pngName):
	im = ImageGrab.grab();
	im.save(pngName + '.png');
	
target = Image.open(r"target.png");
image  = Image.open(r"fishing.png");

targetArr = numpy.asarray(target);
imageArr  = numpy.asarray(image);

targetHeight, targetWidth = targetArr.shape[:2];
imageHeight,  imageWidth  = imageArr.shape[:2];

stopX = imageWidth  - targetWidth;
stopY = imageHeight - targetHeight;

screenprint2png('fishing');	
for x in range(0, stopX):
	for y in range(0, stopY):
		if(image_compare(x, y, targetHeight, targetWidth, targetArr, imageArr)):
			print(x, y);
			pyautogui.moveTo(x, y);
			pyautogui.click(x, y);
			pyautogui.typewrite('hello world');
			exit();

#pyautogui.moveTo(100, 150)
#pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
#pyautogui.dragTo(100, 150)
#pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down
#pyautogui.click(100, 100)
