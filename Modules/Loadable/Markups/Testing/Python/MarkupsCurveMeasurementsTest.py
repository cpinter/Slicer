from __future__ import print_function
from slicer.util import TESTING_DATA_URL
import os

#
# Test curvature computation for curve markups
#

# Download test scene
curveMeasurementsTestDir = slicer.app.temporaryPath + '/curveMeasurementsTest'
print('Test directory: ', curveMeasurementsTestDir)
if not os.access(curveMeasurementsTestDir, os.F_OK):
  os.mkdir(curveMeasurementsTestDir)

testSceneFilePath = curveMeasurementsTestDir + '/MarkupsCurvatureTestScene.mrb'

slicer.util.downloadFile(
  TESTING_DATA_URL + 'SHA256/5b1f39e28ad8611790152fdc092ec9b3ee14254aad4897377db9576139c88e32',
  testSceneFilePath,
  checksum='SHA256:5b1f39e28ad8611790152fdc092ec9b3ee14254aad4897377db9576139c88e32')

# Import test scene
slicer.util.loadScene(testSceneFilePath)
curveNode = slicer.util.getNode('C')

# Check number of arrays in the curve node
curvePolyData = curveNode.GetCurveWorld()
curvePointData = curvePolyData.GetPointData()
if curvePointData.GetNumberOfArrays() != 1:
  exceptionMessage = "Unexpected number of data arrays in curve: " + str(curvePointData.GetNumberOfArrays())
  raise Exception(exceptionMessage)

# Turn on curvature calculation in curve node
curveNode.SetCalculateCurvature(True)

# Check curvature computation result
if curvePointData.GetNumberOfArrays() != 2:
  exceptionMessage = "Unexpected number of data arrays in curve: " + str(curvePointData.GetNumberOfArrays())
  raise Exception(exceptionMessage)

if curvePointData.GetArrayName(1) != 'Curvature':
  exceptionMessage = "Unexpected data array name in curve: " + str(curvePointData.GetArrayName(1))
  raise Exception(exceptionMessage)

curvatureArray = curvePointData.GetArray(1)
if curvatureArray.GetMaxId() != curvePointData.GetNumberOfTuples()-1:
  exceptionMessage = "Unexpected number of values in curvature data array: %d (expected %d)" % (curvatureArray.GetMaxId(), curvePointData.GetNumberOfTuples()-1)
  raise Exception(exceptionMessage)

if abs(curvatureArray.GetRange()[0] - 0.0) > 0.0001:
  exceptionMessage = "Unexpected minimum in curvature data array: " + str(curvatureArray.GetRange()[0])
  raise Exception(exceptionMessage)
if abs(curvatureArray.GetRange()[1] - 0.9816015970208652) > 0.0001:
  exceptionMessage = "Unexpected maximum in curvature data array: " + str(curvatureArray.GetRange()[1])
  raise Exception(exceptionMessage)

# Turn off curvature computation
curveNode.SetCalculateCurvature(False)
if curvePointData.GetNumberOfArrays() != 1:
  exceptionMessage = "Unexpected number of data arrays in curve: " + str(curvePointData.GetNumberOfArrays())
  raise Exception(exceptionMessage)

print('Open curve curvature test finished successfully')

#
# Test closed curve curvature computation
#
closedCurveNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsClosedCurveNode')
pos = [0]*3
for i in range(curveNode.GetNumberOfControlPoints()):
  curveNode.GetNthControlPointPosition(i, pos)
  posVector = vtk.vtkVector3d()
  posVector.Set(pos[0], pos[1], pos[2])
  closedCurveNode.AddControlPoint(posVector)

closedCurveNode.SetCalculateCurvature(True)

curvePolyData = closedCurveNode.GetCurveWorld()
curvePointData = curvePolyData.GetPointData()
if curvePointData.GetNumberOfArrays() != 2:
  exceptionMessage = "Unexpected number of data arrays in curve: " + str(curvePointData.GetNumberOfArrays())
  raise Exception(exceptionMessage)

if curvePointData.GetArrayName(1) != 'Curvature':
  exceptionMessage = "Unexpected data array name in curve: " + str(curvePointData.GetArrayName(1))
  raise Exception(exceptionMessage)

curvatureArray = curvePointData.GetArray(1)
if curvatureArray.GetMaxId() != curvePointData.GetNumberOfTuples()-1:
  exceptionMessage = "Unexpected number of values in curvature data array: %d (expected %d)" % (curvatureArray.GetMaxId(), curvePointData.GetNumberOfTuples()-1)
  raise Exception(exceptionMessage)

if abs(curvatureArray.GetRange()[0] - 0.0) > 0.0001:
  exceptionMessage = "Unexpected minimum in curvature data array: " + str(curvatureArray.GetRange()[0])
  raise Exception(exceptionMessage)
if abs(curvatureArray.GetRange()[1] - 0.26402460470400924) > 0.0001:
  exceptionMessage = "Unexpected maximum in curvature data array: " + str(curvatureArray.GetRange()[1])
  raise Exception(exceptionMessage)

print('Closed curve curvature test finished successfully')
