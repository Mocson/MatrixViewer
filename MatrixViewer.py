import maya.cmds as mc
import maya.api.OpenMaya as om2

### Default Value ###
mata = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
matb = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
matCalc = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
matVal = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]

### Matrix Input A ###

#======================
#	Input MatrixA

def setMatrixA():
	global matrixA

	secA = mc.ls(sl=True)
	sMatA = mc.getAttr("{}.matrix".format(secA[0]))
	matrixA = om2.MMatrix(mc.getAttr("{}.matrix".format(secA[0])))

	for i in range(16):
		mata[i] = sMatA[i]
		mc.floatField("mata{}".format(i+1), e=True, value=mata[i])

def setPMatrixA():

	secA = mc.ls(sl=True)
	sMatA = mc.getAttr("{}.parentMatrix".format(secA[0]))
	matrixA = om2.MMatrix(mc.getAttr("{}.parentMatrix".format(secA[0])))

	for i in range(16):
		mata[i] = sMatA[i]
		mc.floatField("mata{}".format(i+1), e=True, value=mata[i])

def setWMatrixA():

	secA = mc.ls(sl=True)
	sMatA = mc.getAttr("{}.worldMatrix".format(secA[0]))
	matrixA = om2.MMatrix(mc.getAttr("{}.worldMatrix".format(secA[0])))

	for i in range(16):
		mata[i] = sMatA[i]
		mc.floatField("mata{}".format(i+1), e=True, value=mata[i])


#======================
#	Output MatrixA
def outputMatA():
	outA = mc.ls(sl=True)

	mc.xform(outA[0], a=True, os=True, m=mata)


#======================
#	Edit MatrixA
def mAtomB():
	for i in range(16):
		matb[i] = mata[i]
		mc.floatField("matb{}".format(i+1), e=True, value=matb[i])

def clearMatA():
	for i in range(16):
		mata[i] = matVal[i]
		mc.floatField("mata{}".format(i+1), e=True, value=mata[i])


### Matrix Input B ###


#======================
#	Input MatrixB

def setMatrixB():
	global matrixB

	secB = mc.ls(sl=True)
	sMatB = mc.getAttr("{}.matrix".format(secB[0]))
	matrixB = om2.MMatrix(mc.getAttr("{}.matrix".format(secB[0])))

	for i in range(16):
		matb[i] = sMatB[i]
		mc.floatField("matb{}".format(i+1), e=True, value=matb[i])


def setPMatrixB():

	secB = mc.ls(sl=True)
	sMatB = mc.getAttr("{}.parentMatrix".format(secB[0]))
	matrixB = om2.MMatrix(mc.getAttr("{}.parentMatrix".format(secB[0])))

	for i in range(16):
		matb[i] = sMatB[i]
		mc.floatField("matb{}".format(i+1), e=True, value=matb[i])


def setWMatrixB():

	secB = mc.ls(sl=True)
	sMatB = mc.getAttr("{}.worldMatrix".format(secB[0]))
	matrixB = om2.MMatrix(mc.getAttr("{}.worldMatrix".format(secB[0])))

	for i in range(16):
		matb[i] = sMatB[i]
		mc.floatField("matb{}".format(i+1), e=True, value=matb[i])

#======================
#	Output MatrixB

def outputMatB():
	outB = mc.ls(sl=True)

	mc.xform(outB[0], a=True, os=True, m=matb)


#======================
#	Edit MatrixB

def mBtomA():
	for i in range(16):
		mata[i] = matb[i]
		mc.floatField("mata{}".format(i+1), e=True, value=mata[i])

def clearMatB():
	for i in range(16):
		matb[i] = matVal[i]
		mc.floatField("matb{}".format(i+1), e=True, value=matb[i])


### Matrix Calculation ###
def matrixMltAB():
	multiMat = matrixA*matrixB

	for i in range(16):
		matCalc[i] = multiMat[i]
		mc.floatField("ans{}".format(i+1), e=True, value=matCalc[i])

def matrixMltBA():
	multiMat = matrixB*matrixA

	for i in range(16):
		matCalc[i] = multiMat[i]
		mc.floatField("ans{}".format(i+1), e=True, value=matCalc[i])

def matrixPlsAB():
	plusMat = matrixA + matrixB

	for i in range(16):
		matCalc[i] = plusMat[i]
		mc.floatField("ans{}".format(i+1), e=True, value=matCalc[i])

#======================
#	Edit Calc
def toMA():
	for i in range(16):
		mata[i] = matCalc[i]
		mc.floatField("mata{}".format(i+1), e=True, value=mata[i])

def toMB():
	for i in range(16):
		matb[i] = matCalc[i]
		mc.floatField("matb{}".format(i+1), e=True, value=matb[i])

def clearMat():
	for i in range(16):
		matCalc[i] = matVal[i]
		mc.floatField("ans{}".format(i+1), e=True, value=matCalc[i])


#======================
#	Output Calc
def outputMat():
	out = mc.ls(sl=True)

	mc.xform(out[0], a=True, os=True, m=matCalc)

### help ###

#========================
# help & about

def handA():
	if mc.window("about", exists=True):
		mc.deleteUI("about")

	abWin = mc.window("about", t="about", w=100, h=100)
	mc.columnLayout(adj=True)
	mc.text("Coming Soon")
	mc.button(l="Close", c='mc.deleteUI("about")')
	mc.showWindow("about")


### Create Window ###
def matrixViewer():
	if mc.window("matrixViewer", exists=True):
		mc.deleteUI("matrixViewer")

	createWin = mc.window("matrixViewer", t="matrixViewer", w=250, h=300, menuBar=True)

	mc.menu(label='help', to=False)
	mc.menuItem(label='about',c="handA()")
	mc.menuItem(label='help',c="handA()")
	mc.setParent('..')

	## Matrix A ##
	mc.frameLayout(label="Matrix A")
	mc.columnLayout(adj=True)
	mc.menuBarLayout()
	mc.menu( label='Input', to=False)
	mc.menuItem(label='.matrix',c="setMatrixA()")
	mc.menuItem(label='.parentMatrix',c="setPMatrixA()")
	mc.menuItem(label='.worldMatrix',c="setWMatrixA()")
	mc.menu( label='Output', to=False)
	mc.menuItem(label='.matrix',c="outputMatA()")
	mc.menu( label='Edit', to=False)
	mc.menuItem(label='Clear',c="clearMatA()")
	mc.menuItem(label='MatA -> MatB',c='mAtomB()')


	mc.rowLayout(numberOfColumns=4)
	mc.floatField("mata1")
	mc.floatField("mata2")
	mc.floatField("mata3")
	mc.floatField("mata4")
	mc.setParent('..')

	mc.rowLayout(numberOfColumns=4)
	mc.floatField("mata5")
	mc.floatField("mata6")
	mc.floatField("mata7")
	mc.floatField("mata8")
	mc.setParent('..')

	mc.rowLayout(numberOfColumns=4)
	mc.floatField("mata9")
	mc.floatField("mata10")
	mc.floatField("mata11")
	mc.floatField("mata12")
	mc.setParent('..')

	mc.rowLayout(numberOfColumns=4)
	mc.floatField("mata13")
	mc.floatField("mata14")
	mc.floatField("mata15")
	mc.floatField("mata16")
	mc.setParent('..')
	mc.setParent('..')
	mc.setParent('..')

	## Matrix B ##
	mc.frameLayout(label="Matrix B")
	mc.columnLayout(adj=True)
	mc.menuBarLayout()
	mc.menu( label='Input', to=False)
	mc.menuItem(label='.matrix',c="setMatrixB()")
	mc.menuItem(label='.parentMatrix',c="setPMatrixB()")
	mc.menuItem(label='.worldMatrix',c="setWMatrixB()")
	mc.menu( label='Output', to=False)
	mc.menuItem(label='.matrix',c="outputMatB()")
	mc.menu( label='Edit', to=False)
	mc.menuItem(label='Clear',c="clearMatB()")
	mc.menuItem(label='MatB -> MatA',c='mBtomA()')


	mc.rowLayout(numberOfColumns=4)
	mc.floatField("matb1")
	mc.floatField("matb2")
	mc.floatField("matb3")
	mc.floatField("matb4")
	mc.setParent('..')

	mc.rowLayout(numberOfColumns=4)
	mc.floatField("matb5")
	mc.floatField("matb6")
	mc.floatField("matb7")
	mc.floatField("matb8")
	mc.setParent('..')

	mc.rowLayout(numberOfColumns=4)
	mc.floatField("matb9")
	mc.floatField("matb10")
	mc.floatField("matb11")
	mc.floatField("matb12")
	mc.setParent('..')

	mc.rowLayout(numberOfColumns=4)
	mc.floatField("matb13")
	mc.floatField("matb14")
	mc.floatField("matb15")
	mc.floatField("matb16")
	mc.setParent('..')
	mc.setParent('..')
	mc.setParent('..')

	## Matrix Calculation ##
	mc.frameLayout(label="Matrix Calculation")
	mc.columnLayout(adj=True)
	mc.menuBarLayout()
	mc.menu( label='Calc', to=False)
	mc.menuItem(label='MatA*MatB',c="matrixMltAB()")
	mc.menuItem(label='MatB*MatA',c="matrixMltBA()")
	mc.menuItem(label='MatA+MatB',c="matrixPlsAB()")
	mc.menu( label='Output', to=False)
	mc.menuItem(label='.matrix',c="outputMat()")
	mc.menu( label='Edit', to=False)
	mc.menuItem(label='Clear',c="clearMat()")
	mc.menuItem(label='Calc => MatA',c='toMA()')
	mc.menuItem(label='Calc => MatB',c='toMB()')

	mc.rowLayout(numberOfColumns=4)
	mc.floatField("ans1")
	mc.floatField("ans2")
	mc.floatField("ans3")
	mc.floatField("ans4")
	mc.setParent('..')

	mc.rowLayout(numberOfColumns=4)
	mc.floatField("ans5")
	mc.floatField("ans6")
	mc.floatField("ans7")
	mc.floatField("ans8")
	mc.setParent('..')

	mc.rowLayout(numberOfColumns=4)
	mc.floatField("ans9")
	mc.floatField("ans10")
	mc.floatField("ans11")
	mc.floatField("ans12")
	mc.setParent('..')

	mc.rowLayout(numberOfColumns=4)
	mc.floatField("ans13")
	mc.floatField("ans14")
	mc.floatField("ans15")
	mc.floatField("ans16")
	mc.setParent('..')
	mc.setParent('..')
	mc.setParent('..')

	mc.showWindow(createWin)
