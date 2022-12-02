from turtle import *
from Vector2 import Vector2
from Vector3 import Vector3
def GetTriangle(triangleIndecies):
	return (verts[triangleIndecies[0]],verts[triangleIndecies[1]],verts[triangleIndecies[2]])
def GetZProjection(vertex):
	return Vector2(vertex.x, vertex.y)
def Get2DArea(tri):
	tri2D = (GetZProjection(tri[0]),GetZProjection(tri[1]),GetZProjection(tri[2]))
	return -(tri2D[0].x * (tri2D[1].y - tri2D[2].y) + tri2D[1].x * (tri2D[2].y - tri2D[0].y) + tri2D[2].x * (tri2D[0].y - tri2D[1].y))/2
def isInsideTriangle2D(tri, point):
	return 0 == Get2DArea(tri) - (Get2DArea((point, tri[0],tri[1])) + Get2DArea((point, tri[1],tri[2])) + Get2DArea((point, tri[2],tri[3])))
trt = Turtle()
tracer(0, 0)
trt.hideturtle()
canvas = getcanvas()

verts = [
	Vector3(1, -2, 2)*100, Vector3(1,2,1)*100, Vector3(1,-1,-1)*100,
	Vector3(-1, -2, 2)*100, Vector3(-1,2,1)*100, Vector3(-1,-1,-1)*100,
]
tris = [(0,1,2),(3,4,5),(0,1,4),(4,5,2)]

trt.fillcolor(0.4, 0.4, 0.4)
while trt:
	trt.clear()
	
	for tri in tris:
		trt.penup()
		trt.goto(verts[tri[0]].x, verts[tri[0]].y)
		trt.begin_fill()
		trt.pendown()
		trt.goto(verts[tri[1]].x, verts[tri[1]].y)
		trt.goto(verts[tri[2]].x, verts[tri[2]].y)
		trt.goto(verts[tri[0]].x, verts[tri[0]].y)
		trt.end_fill()			

	for i in range(len(verts)):
		vert = verts[i]
		planeVert = Vector2(vert.x, vert.z)
		planeVert.RotateByAngle(0.2)
		verts[i] = Vector3(planeVert.x, vert.y, planeVert.y)
		print(verts[i])
	update()
