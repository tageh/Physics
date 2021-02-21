import numpy as np
import matplotlib.pyplot as plt


x = 0
y = 0
th0 = 45*np.pi/180
th0l = 44*np.pi/180
v0 = 73 #hastighet
ax = 0 #akselasjon i x
ay = -9.81 #akslerasjon i y
Yground = 0 #høyde over bakken
tSteg = 0.001 #tid mellom hvert steg
tidsrom = 15 #tiden vi følger kastet
totSteg = int(tidsrom/tSteg)
m = 2.0
D = 1.4*10**-3


# In[448]:


vx = v0*np.cos(th0)
vy = v0*np.sin(th0)

vxl = v0*np.cos(th0l)
vyl = v0*np.sin(th0l)

axl = (-D * (vx2**2 + vy2**2)*np.cos(th0)) / m
ayl = -9.81 + (-D * (vx2**2 + vy2**2)*np.sin(th0)) / m

print("Utgangshastighet i x retning: {} m/s".format(vx))
print("Utgangshastighet i y retning: {} m/s".format(vy))

xPos = np.zeros(totSteg)
yPos = np.zeros(totSteg)

xlPos = np.zeros(totSteg)
ylPos = np.zeros(totSteg)


xPos[0] = x
yPos[0] = y

xlPos[0] = x
ylPos[0] = y

for i in range(1,totSteg):

    vxl = vxl + axl*tSteg
    vyl = vyl + ayl*tSteg
    xlPos[i] = xlPos[i-1] + vxl*tSteg
    ylPos[i] = ylPos[i-1] + vyl*tSteg

    vx = vx + ax*tSteg
    vy = vy + ay*tSteg
    xPos[i] = xPos[i-1] + vx*tSteg
    yPos[i] = yPos[i-1] + vy*tSteg


plt.plot(xPos,yPos, label="uten luftmotstand")
plt.plot(xlPos, ylPos, label="med luftmotstand")

plt.grid()
plt.title("time: {} s".format(tidsrom))
plt.ylabel("y [m]")
plt.xlabel("x [m]")
plt.ylim(0,250)
plt.legend()
plt.show()

print("Maksimal oppnådd høyde: {} m".format(max(yPos)))

diffy = np.abs(yPos - Yground)
diffyl = np.abs(ylPos - Yground)

landingindex = np.where(diffy == min(diffy[2:]))
landingindexl = np.where(diffyl == min(diffyl[2:]))

MaksAvstand = xPos[landingindex]
MaksAvstandl = xlPos[landingindexl]

print("Maksimal avstand før den treffer bakken: {} m".format(MaksAvstand))
print("Maksimal avstand før den treffer bakken med luftmotstand: {} m".format(MaksAvstandl))
print("Vinkel luftmotstand: {}".format(th0l*180/np.pi))