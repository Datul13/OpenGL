from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

def kotak() :
    gluOrtho2D(0.0, 1.5, 0.0, 1.5)
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1.,0.,1.)
    glVertex2f(0.5,0.5)
    glColor3f(1.,1.,0.)
    glVertex2f(0.5,1.25)
    glColor3f(0.,1.,1.)
    glVertex2f(1.25,0.5)
    glColor3f(1.,0.,0.)
    glVertex2f(1.25,1.25)
    glEnd()
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Kotak Aja")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(kotak)
glutMainLoop()
#End of program
