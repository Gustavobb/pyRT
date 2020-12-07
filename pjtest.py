from pyrt.math import Vec3
from pyrt.scene import Scene
from pyrt.light import PointLight
from pyrt.geometry import Triangle, Sphere, Vertex
from pyrt.material import PhongMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT
from PIL import Image

# Specify width/height 
# width = 320
# height = 240

width = 1280
height = 720

# now create a camera and a view :
camera = PerspectiveCamera(width, height, 90)
camera.setView(Vec3(0.,-10.,10.), Vec3(0.,0.,0.), Vec3(0.,0.,1.))

# Create a scene
scene = Scene()

# Add a light to the scene
scene.addLight(PointLight(Vec3(0,0,15)))

# create some materials:
floormaterial = PhongMaterial(color=Vec3(0.5,0.5,0.5))
sphere0material = PhongMaterial(color=Vec3(1.,0.,0.))
sphere1material = PhongMaterial(color=Vec3(0.,1.,0.))
sphere2material = PhongMaterial(color=Vec3(0.,0.,1.))
sphere3material = PhongMaterial(color=Vec3(1.,1.,0.))

# Add "floor"

A = Vertex(position=(-20.0, -70.0, 0.0))
B = Vertex(position=( 20.0, -70.0, 0.0))
C = Vertex(position=( 20.0,  10.0, 0.0))
D = Vertex(position=(-20.0,  10.0, 0.0))

scene.add(Triangle(A,B,C, material=floormaterial))
scene.add(Triangle(A,C,D, material=floormaterial))

# Add some spheres

scene.add(Sphere(center=Vec3(-2.5,-8.0,1.75), radius=1.75, material=sphere0material))
scene.add(Sphere(center=Vec3( 2.5,-8.0,1.75), radius=1.75, material=sphere1material))
scene.add(Sphere(center=Vec3( 2.5, 5.0,1.75), radius=1.75, material=sphere2material))
scene.add(Sphere(center=Vec3(-2.5,-3.5,1.75), radius=1.75, material=sphere3material))
scene.add(Sphere(center=Vec3(10.0,10.0,5.0), radius=1.75, material=PhongMaterial(color=Vec3(1.,0.,0.))))
scene.add(Sphere(center=Vec3(-10.0,5.0,5.0), radius=3., material=PhongMaterial(color=Vec3(1.,.5,0.))))

# Now tell the scene which camera we use
scene.setCamera(camera)

# Create a raytracer using "SimpleRT"
engine = SimpleRT(shadow=True)

# Render the scene:
image = engine.render(scene)

# Save the resulting image using pillow
image.save("render2.png")
