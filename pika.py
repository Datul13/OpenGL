from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def pikachu() :
    gluOrtho2D(-4.0, 4.0, -4.0, 4.0)
    glBegin(GL_TRIANGLE_STRIP)
    
    glColor3f(0., 0., 0.)
    glVertex2f(-2.5, 3.25)
    glVertex2f(-1.5, 1)
    glVertex2f(-0.5, 1.5)
    
    glColor3f(0., 0., 0.)
    glVertex2f(-0.5, 1.5)
    
    glColor3f(1., 1., 0.)
    glVertex2f(-0.3, 1)
    
    glColor3f(0., 0., 0.)
    glVertex2f(-1.5, 1)
    
    glColor3f(1, 1, 0.)
    glVertex2f(-1.5, 1)
    glVertex2f(1.5, 1)
    
    glColor3f(1, 1, 0.)
    glVertex2f(0, -0.5) 
    
    glColor3f(1, 1, 0.)
    glVertex2f(0, -0.5)
    glVertex2f(-1.5, 1)
    glVertex2f(-1.75, -0.5)  
    
    glColor3f(1, 1, 0.)
    glVertex2f(0, -0.5)
    glVertex2f(-1.75, -0.5)
    glVertex2f(-1., -1.5) 
    
    glColor3f(1, 1, 0.)
    glVertex2f(0, -0.5)
    glVertex2f(-1., -1.5) 
    glVertex2f(1, -1.5) 
    
    glColor3f(1, 1, 0.)
    glVertex2f(0, -0.5)
    glVertex2f(1., -1.5) 
    glVertex2f(1.75, -0.5)
    
    glColor3f(1, 1, 0.)
    glVertex2f(0, -0.5)
    glVertex2f(1.75, -0.5)
    glVertex2f(1.5, 1)  
    
    glColor3f(1., 1., 0.)
    glVertex2f(1.5, 1)
    
    glColor3f(1., 1., 0.)
    glVertex2f(0.5, 1.5)
    
    glColor3f(1., 1., 0.)
    glVertex2f(0.3, 1)
    
    glColor3f(0., 0., 0.)
    glVertex2f(0.5, 1.5)
    glVertex2f(1.5, 1)
    glVertex2f(2.5, 3.25)
    
    glEnd()
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("Kelompok 3")
glClearColor(1.0, 0.0, 0.0, 0.0)
glClear(GL_COLOR_BUFFER_BIT)
glutDisplayFunc(pikachu)
glutMainLoop()
# End of program
