from OpenGL.GL import glBegin, glColor3f, glEnd, glEndList, glLineWidth, glNewList, glNormal3f, glVertex3f, \
                      GL_COMPILE, GL_LINES, GL_QUADS, GL_TRIANGLES
from OpenGL.GLU import gluDeleteQuadric, gluNewQuadric, gluSphere
import numpy as np
from ObjLoader.LoadObj import *
G_OBJ_PLANE = 1
G_OBJ_SPHERE = 2
G_OBJ_CUBE = 3
G_OBJ_MESH = 4
G_OBJ_MAN = 5

def make_plane():
    glNewList(G_OBJ_PLANE, GL_COMPILE)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    for i in range(41):
        glVertex3f(-10.0 + 0.5 * i, 0, -10)
        glVertex3f(-10.0 + 0.5 * i, 0, 10)
        glVertex3f(-10.0, 0, -10 + 0.5 * i)
        glVertex3f(10.0, 0, -10 + 0.5 * i)

    # Axes
    glEnd()
    glLineWidth(5)

    glBegin(GL_LINES)
    glColor3f(0.5, 0.7, 0.5)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(5, 0.0, 0.0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.5, 0.7, 0.5)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 5, 0.0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.5, 0.7, 0.5)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 5)
    glEnd()

    # Draw the Y.
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)
    glVertex3f(0.0, 5.5, 0.0)
    glVertex3f(0.0, 5.5, 0.0)
    glVertex3f(-0.5, 6.0, 0.0)
    glVertex3f(0.0, 5.5, 0.0)
    glVertex3f(0.5, 6.0, 0.0)

    # Draw the Z.
    glVertex3f(-0.5, 0.0, 5.0)
    glVertex3f(0.5, 0.0, 5.0)
    glVertex3f(0.5, 0.0, 5.0)
    glVertex3f(-0.5, 0.0, 6.0)
    glVertex3f(-0.5, 0.0, 6.0)
    glVertex3f(0.5, 0.0, 6.0)

    # Draw the X.
    glVertex3f(5.0, 0.0, 0.5)
    glVertex3f(6.0, 0.0, -0.5)
    glVertex3f(5.0, 0.0, -0.5)
    glVertex3f(6.0, 0.0, 0.5)

    glEnd()
    glLineWidth(1)
    glEndList()


def make_sphere():
    glNewList(G_OBJ_SPHERE, GL_COMPILE)
    quad = gluNewQuadric()
    gluSphere(quad, 0.5, 30, 30)
    gluDeleteQuadric(quad)
    glEndList()


def make_cube():
    glNewList(G_OBJ_CUBE, GL_COMPILE)
    vertices = [((-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5)),
                ((-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5)),
                ((0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5)),
                ((-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)),
                ((-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5)),
                ((-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5))]
    normals = [(-1.0, 0.0, 0.0), (0.0, 0.0, -1.0), (1.0, 0.0, 0.0), (0.0, 0.0, 1.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0)]

    glBegin(GL_QUADS)
    for i in range(6):
        glNormal3f(normals[i][0], normals[i][1], normals[i][2])
        for j in range(4):
            glVertex3f(vertices[i][j][0], vertices[i][j][1], vertices[i][j][2])
    glEnd()
    glEndList()


def make_mesh():
    glNewList(G_OBJ_MESH,GL_COMPILE)
    vertices=[[1.0,0.0,1.0],[0.0,0.0,-1.0],[-1.0,0.0,1.0],[0.0,1.0,0.0]]
    face=[[1,4,3],[1,2,4],[2,3,4],[1,3,2]]
    for i in range(len(face)):
        glColor3f(216/255,186/255,160/255)
        point0=np.array(vertices[face[i][0]-1])
        point1 = np.array(vertices[face[i][1]-1])
        point2 =np.array(vertices[face[i][2]-1])
        A=point1-point0
        B=point0-point2
        C = np.cross(B, A)
        N = C/np.linalg.norm(C)
        glBegin(GL_TRIANGLES)
        glNormal3f(N[0],N[1],N[2])
        for j in range(3):
            glVertex3f(vertices[face[i][j]-1][0],vertices[face[i][j]-1][1],vertices[face[i][j]-1][2])
        glEnd()
    glEndList()
def make_man(path):
    glNewList(G_OBJ_MAN, GL_COMPILE)
    obj=OBJ(path)
    vertices=obj.vertices
    face=obj.faces
    for i in range(len(face)):
        glColor3f(216 / 255, 186 / 255, 160 / 255)
        glBegin(GL_TRIANGLES)
        glNormal3f(face[i][1][0],face[i][1][1],face[i][1][2])
        for j in range(3):
            glVertex3f(vertices[face[i][0][j]-1][0],vertices[face[i][0][j]-1][1],vertices[face[i][0][j]-1][2])
        glEnd()
    glEndList()
#def make_triangle():
   # glNewList(G_OBJ_TRIANGLE, GL_COMPILE)


def init_primitives():
    make_plane()
    #make_sphere()
    #make_cube()
    #make_mesh()
    #make_man()