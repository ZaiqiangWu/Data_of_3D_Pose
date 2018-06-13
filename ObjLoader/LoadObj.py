import os.path
from OpenGL.GL import glCallList, glColor3f, glMaterialfv, glMultMatrixf, glPopMatrix, glPushMatrix, \
                      GL_EMISSION, GL_FRONT
from OpenGL.GL import glBegin, glColor3f, glEnd, glEndList, glLineWidth, glNewList, glNormal3f, glVertex3f, \
                      GL_COMPILE, GL_LINES, GL_QUADS, GL_TRIANGLES
import numpy as np
class OBJ:
    # Load .obj file
    def __init__(self, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.faces = []
        for line in open(filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = list(map(float, values[1:4]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    #w = v.split(' ')
                    face.append(int(v))
                point0=np.array(self.vertices[face[0]-1])
                point1 = np.array(self.vertices[face[1]-1])
                point2 = np.array(self.vertices[face[2]-1])
                A=point1-point0
                B=point0-point2
                C=np.cross(B,A)
                norms=C/np.linalg.norm(C)
                # This stores all properties of a face into faces.
                self.faces.append((face, norms))
    def print(self):
        print(self.vertices)
        print(self.faces)


if __name__ == "__main__":
    file="./OBJ/smpl_np.obj"
    obj=OBJ(file)
    obj.print()