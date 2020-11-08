from matplotlib.pylab import *
from matplotlib import cm
from calor_de_hidratacion import Calor_de_hidratacion


# Definiciones geometricas
a = 1.04    #y
b = 0.54    #x
c = 0.50    #z 

Nx = 27    #numero de intervalos en X
Ny = 52    #numero de intervalos en Y
Nz = 25    #numero de intervalos en Z

dx = b/Nx  #discretizacion espacial en x
dy = a/Ny  #discretizacion espacial en y
dz = c/Nz  #discretizacion espacial en y

if dx != dy or dx != dz:
    print("Error dx")
    exit(-1)


#Funciones de conveniencia para calcular las coordenadas del punto(1,j)

coords = lambda i,j,k:(dx*i,dy*j,dz*k)

def imshowbien(u):
    imshow(u.T[Nx::-1,:],cmap=cm.coolwarm, interpolation='bilinear')
    cbar = colorbar(extend='both', cmap=cm.coolwarm)
    ticks = arange(0,35,5)
    ticks_Text=["{}°".format(deg) for deg in ticks]
    cbar.set_ticks(ticks)
    cbar.set_ticklabels(ticks_Text)
    clim(0, 30)
    
    xlabel('b')
    ylabel('a')
    xTicks_N = arange(0, Nx+1, 3)
    yTicks_N = arange(0, Ny+1, 3)
    xTicks =[coords(i,0)[0] for i in xTicks_N]
    yTicks =[coords(0,i)[1] for i in yTicks_N]
    xTicks_Text = ["{0:.2f}".format(tick) for tick in xTicks]
    yTicks_Text = ["{0:.2f}".format(tick) for tick in yTicks]
    xticks(xTicks_N,xTicks_Text, rotation='vertical')
    yticks(yTicks_N,yTicks_Text)
    margins(0.2)
    subplots_adjust(bottom=0.15)
    
    
u_k = zeros((Nx+1,Ny+1,Nz+1),dtype=double)
u_km1 = zeros((Nx+1,Ny+1,Nz+1),dtype=double)

#Condicion de borde inicial
'''DEFINIR CONDICION INICIAL'''
u_k[:,:] = 20. #20 grados inicial en todas partes

#Parametros del problema (hierro)
dt = 0.01   #s
K = 79.5
c = 450.    #
ρ = 7800.
α = K*dt/(c*ρ*dx**2)

#informar cosas interesantes
print(f"dt = {dt}")
print(f"dx = {dx}")
print(f"K = {K}")
print(f"c = {c}")
print(f"ρ = {ρ}")
print(f"α = {α}")

#Loop en el tiempo
minuto = 60.
hora = 3600.
dia = 24.5 * 3600

dt = 1*minuto
dnext_t = 0.5*hora

next_t = 0
framenum = 0

T = 1*dia
Days = 1*T #Cuantos dias quiero simular

#Vectores para acumular la t° en Puntos Interesantes
p_1  = zeros(int32(Days/dt))     
p_2  = zeros(int32(Days/dt))  
p_3  = zeros(int32(Days/dt)) 
p_4  = zeros(int32(Days/dt))     
p_5  = zeros(int32(Days/dt))  
p_6  = zeros(int32(Days/dt)) 
p_7  = zeros(int32(Days/dt))     
p_8  = zeros(int32(Days/dt))  
p_9  = zeros(int32(Days/dt)) 
p_10 = zeros(int32(Days/dt))     
p_11 = zeros(int32(Days/dt))  
p_12 = zeros(int32(Days/dt)) 
p_13 = zeros(int32(Days/dt))     
p_14 = zeros(int32(Days/dt))  
p_15 = zeros(int32(Days/dt)) 

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

#Loop en el tiempo K
for k in range(int32(Days/dt)):
    t = dt*(k+1)
    dias = truncate(t/dia,0)
    horas = truncate((t-dias*dia)/hora,0)
    minutos = truncate((t-dias*dia-horas*hora)/minuto,0)
    titulo = "k = {0:05.0f}".format(k) + " t = {0:02.0f}d {1:02.0f}h {2:02.0f}m ".format(dias, horas, minutos)
    print(titulo)
    
    
    #CB esenciales, se repiten en cada iteración
    
    u_ambiente = 20.+10*sin((2*pi/T)*t)
    
    u_k[ : , : , 0 ] = 0.           #cara inferior xy
    u_k[ : , : ,-1 ] = u_ambiente   #cara superior xy
    u_k[ : ,-1 , : ] = 0.           #cara derecha xz
    u_k[ : , 0 , : ] = 0.           #cara izquierda xz
    u_k[-1 , : , : ] = 0.           #cara frontal yz
    u_k[ 0 , : , : ] = 0.           #cara atras yz
    
    #Escribiendo Puntos Interesantes
    p_1[k]  = u_k[int(Nx/2),int(Ny*765/1040),int(Nz/2)]   #1
    p_2[k]  = u_k[int(Nx/2),int(Ny/2),int(Nz/2)]          #2
    p_6[k]  = u_k[int(Nx*510/540),int(Ny/2),int(Nz/2)]    #3
    p_11[k] = u_k[int(Nx/2),int(Ny/2),int(Nz*470/500)]    #4
    p_1[k]  = u_k[int(Nx/2),int(Ny*30/1040),int(Nz/2)]    #5
    p_6[k]  = u_k[int(Nx*30/540),int(Ny/2),int(Nz/2)]     #6
    p_8[k]  = u_k[int(Nx/2),int(Ny/2),int(Nz*360/500)]    #7
    p_8[k]  = u_k[int(Nx/2),int(Ny/2),int(Nz*140/500)]    #8
    p_9[k]  = u_k[int(Nx*150/540),int(Ny/2),int(Nz/2)]    #9
    p_10[k] = u_k[int(Nx/2),int(Ny*1010/1040),int(Nz/2)]  #10
    p_11[k] = u_k[int(Nx/2),int(Ny/2),int(Nz*30/500)]     #11
    p_1[k]  = u_k[int(Nx/2),int(Ny*275/1040),int(Nz/2)]   #12
    p_13[k] = u_k[int(Nx/2),int(Ny/2),int(Nz)]            #13
    p_9[k]  = u_k[int(Nx*390/540),int(Ny/2),int(Nz/2)]    #14
    p_15[k] = u_k[int(Nx/2),int(Ny),int(Nz/2)]            #15
    
    #Loop en el espacio i = 1 ...... n-1
    for i in range(1,Nx):
        for j in range(1,Ny):
            for k in range(1,Nz):
                #Algoritmo de diferencia finitas 2-D para difusión
                nabla_u_k = u_k[i-1,j,k] + u_k[i+1,j,k] + u_k[i,j-1,k] + u_k[i, j+1,k] + u_k[i, j,k-1] + u_k[i, j,k+1] - 6*u_k[i,j] + Calor_de_hidratacion(t,DC = 360.)
            
            #Forward Euler
            u_km1[i,j] = u_k[i,j] + α*nabla_u_k
    
    #Avanzar la solución a k+1
    u_k = u_km1
    
    #CB denuevo, para asegurar cumpliemiento
    u_k[ : , : , 0 ] = 0.           #cara inferior xy
    u_k[ : , : ,-1 ] = u_ambiente   #cara superior xy
    u_k[ : ,-1 , : ] = 0.           #cara derecha xz
    u_k[ : , 0 , : ] = 0.           #cara izquierda xz
    u_k[-1 , : , : ] = 0.           #cara frontal yz
    u_k[ 0 , : , : ] = 0.           #cara atras yz
    
    if t > next_t:
        figure(1)
        imshowbien(u_k)
        title(titulo)
        savefig("caso_interperie/frame_{0:04.0f}.png".format(framenum))
        framenum += 1
        next_t += dnext_t
        close(1)
        
#Ploteo historia de t° en Puntos Interesantes
Sensores = []
Sensores.append(p_1)
Sensores.append(p_2)
Sensores.append(p_3)
Sensores.append(p_4)
Sensores.append(p_5)
Sensores.append(p_6)
Sensores.append(p_7)
Sensores.append(p_8)
Sensores.append(p_9)
Sensores.append(p_10)
Sensores.append(p_11)
Sensores.append(p_12)
Sensores.append(p_13)
Sensores.append(p_14)
Sensores.append(p_15)

figure(2)
for i,p in enumerate(Sensores):
    plot(range(int32(Days/dt)),p,label=f'Sensor{i+1}')

title("Evolución de temperatura en puntos")
legend()
#savefig(f'caso_1.png')
show()      
        
        