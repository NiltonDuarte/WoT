from panda3d.core import *

ambientLight = AmbientLight('ambientLight')
ambientLight.setColor(VBase4(0.4, 0.4, 0.3, 1))
ambientLightNP = render.attachNewNode(ambientLight)
render.setLight(ambientLightNP)

pos = 110
posZ = 100
attenuationA = 0
attenuationB = 0.005
attenuationC = 0
color = [0.3,0.3,0.2,1]

pointLight = PointLight('pointLight1')
pointLight.setColor(VBase4(*color))
pointLight.setAttenuation(Point3(attenuationA, attenuationB, attenuationC))
pointLightNP = render.attachNewNode(pointLight)
pointLightNP.setPos(pos, pos,posZ)
render.setLight(pointLightNP)

pointLight = PointLight('pointLight2')
pointLight.setColor(VBase4(*color))
pointLight.setAttenuation(Point3(attenuationA, attenuationB, attenuationC))
pointLightNP = render.attachNewNode(pointLight)
pointLightNP.setPos(pos, -pos,posZ)
render.setLight(pointLightNP)

pointLight = PointLight('pointLight3')
pointLight.setColor(VBase4(*color))
pointLight.setAttenuation(Point3(attenuationA, attenuationB, attenuationC))
pointLightNP = render.attachNewNode(pointLight)
pointLightNP.setPos(-pos, pos,posZ)
render.setLight(pointLightNP)

pointLight = PointLight('pointLight4')
pointLight.setColor(VBase4(*color))
pointLight.setAttenuation(Point3(attenuationA, attenuationB, attenuationC))
pointLightNP = render.attachNewNode(pointLight)
pointLightNP.setPos(-pos, -pos,posZ)
render.setLight(pointLightNP)

