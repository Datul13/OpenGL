from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def star() :
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glBegin(GL_TRIANGLE_STRIP)

    glColor3f(0., 1., 0.)
    glVertex2f(-0.5, -0.5)
    glColor3f(1., 0., 0.)
    glVertex2f(0.5, 0.5)
    glColor3f(0., 0., 1.)
    glVertex2f(-0.5, 3.25)

    glColor3f(1., 1., 0.)
    glVertex2f(-0.5, -0.5)
    glColor3f(1., 0., 1.)
    glVertex2f(0.5, 0.5)
    glColor3f(0., 1., 1.)
    glVertex2f(3.5, 0.5)

    glColor3f(0., 1., 0.)
    glVertex2f(-0.5, -0.5)
    glColor3f(0., 0., 1.)
    glVertex2f(1., -1.)
    glColor3f(1., 0., 0.)
    glVertex2f(3.5, 0.5)
    
    glColor3f(0., 1., 1.)
    glVertex2f(-0.5, -0.5)
    glColor3f(1., 0., 1.)
    glVertex2f(1., -1.)
    glColor3f(1., 1., 0.)
    glVertex2f(1.75, -3.5)

    glColor3f(0., 0., 1.)
    glVertex2f(-0.5, -0.5)
    glColor3f(0., 1., 0.)
    glVertex2f(-0.5, -1.75)
    glColor3f(1., 0., 0.)
    glVertex2f(1.75, -3.5)

    glColor3f(1., 0., 1.)
    glVertex2f(-0.5, -0.5)
    glColor3f(1., 1., 0.)
    glVertex2f(-0.5, -1.75)
    glColor3f(0., 1., 1.)
    glVertex2f(-2.75, -3.5)

    glColor3f(1., 0., 0.)
    glVertex2f(-0.5, -0.5)
    glColor3f(0., 1., 0.)
    glVertex2f(-2., -1.)
    glColor3f(0., 0., 1.)
    glVertex2f(-2.75, -3.5)

    glColor3f(1., 1., 0.)
    glVertex2f(-0.5, -0.5)
    glColor3f(1., 0., 1.)
    glVertex2f(-2., -1.)
    glColor3f(0., 1., 1.)
    glVertex2f(-4.5, 0.5)

    glColor3f(0., 0., 1.)
    glVertex2f(-0.5, -0.5)
    glColor3f(0., 1., 0.)
    glVertex2f(-0.5, 0.5)
    glColor3f(1., 0., 0.)
    glVertex2f(-4.5, 0.5)

    glColor3f(1., 0., 1.)
    glVertex2f(-0.5, -0.5)
    glColor3f(0., 1., 1.)
    glVertex2f(-1.5, 0.5)
    glColor3f(1., 1., 0.)
    glVertex2f(-0.5, 3.25)

    glEnd()
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Star Program")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(star)
glutMainLoop()
# End of program
