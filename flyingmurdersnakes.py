import Rasterizer
import bge
	
def loadBlend(status):
	print("Loaded %s" % status.libraryName);
	
def screamHopelesslyUntilGodComesBack():
	Rasterizer.showMouse(1)

	controller = bge.logic.getCurrentController();
	owner = controller.owner;
	scene = bge.logic.getCurrentScene();
	objects = scene.objects;
	
	bge.logic.LibLoad('//bluestar.blend','Scene',async=True).onFinish = loadBlend;
	bge.logic.LibLoad('//blackstar.blend','Scene',async=True).onFinish = loadBlend;
	scene.objects["Camera"].position = [0,0,9];

	import GameLogic as g;
	g.objectSelected = None;
	
def makeSmallStar():
	controller = bge.logic.getCurrentController();
	owner = controller.owner;
	scene = bge.logic.getCurrentScene();
	objects = scene.objects;
	import GameLogic as g;

	sensor = controller.sensors["1"]
	if sensor:
		if sensor.status == 1:
			duh = scene.addObject("Blue star",owner);
			duh.position = [0,0,5];
			g.objectSelected = duh;
			
def makeBigStar():
	controller = bge.logic.getCurrentController();
	owner = controller.owner;
	scene = bge.logic.getCurrentScene();
	objects = scene.objects;
	import GameLogic as g;
		
	sensor = controller.sensors["2"]
	if sensor:
		if sensor.status == 1:
			duh = scene.addObject("Black star",owner);
			duh.position = [0,0,5];
			g.objectSelected = duh;
			
def justAStepToTheRight():
	import GameLogic as g;
	g.objectSelected.position.x += 0.1;