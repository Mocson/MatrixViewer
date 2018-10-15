import maya.cmds as mc
import maya.api.OpenMaya as om2

### Default Value ###
mata = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
matb = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]


def setMatrixA():
	global matrixA

	secA = mc.ls(sl=True)
	sMatA = mc.getAttr("{}.matrix".format(secA[0]))
	matrixA = om2.MMatrix(mc.getAttr("{}.matrix".format(secA[0])))


	for i in range(16):
		mata[i] = sMatA[i]
		mc.floatField("mata{}".format(i+1), e=True, value=mata[i])


def setMatrixB():
	global matrixB

	secB = mc.ls(sl=True)
	sMatB = mc.getAttr("{}.matrix".format(secB[0]))
	matrixB = om2.MMatrix(mc.getAttr("{}.matrix".format(secB[0])))

	for i in range(16):
		matb[i] = sMatB[i]
		mc.floatField("matb{}".format(i+1), e=True, value=matb[i])




def matrixDiv():
	divMat = matrixA*matrixB

	
	print divMat



### Create Window ###
if mc.window("matrixViewer", exists=True):
	mc.deleteUI("matrixViewer")

createWin = mc.window("matrixViewer", t="matrixViewer", w=250, h=300)

## Matrix A ##
mc.columnLayout(adj=True)
mc.button(l="Set Matrix A", w=150, h=50, c="setMatrixA()" )
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

## Matrix B ##
mc.columnLayout(adj=True)
mc.button(l="Set Matrix B", w=150, h=50, c="setMatrixB()" )
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

mc.columnLayout(adj=True)
mc.button(l="MatrixA * MatrixB", w=150, h=50, c="matrixDiv()" )

mc.showWindow(createWin)

# secObj = mc.ls(sl=True)

# def matIn1():
# 	secObj = mc.ls(sl=True)
# 	matListA = mc.getAttr( "{}.matrix".format(secObj[0]) )

# 	mc.floatField('mat')
	
# matVal1 = om2.MMatrix(mc.getAttr( "{}.matrix".format(secObj[0]) ) )
# matTest = mc.getAttr( "{}.matrix".format(secObj[0]) )
# print matVal1[1]
# print matTest[1]