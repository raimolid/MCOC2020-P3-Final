# MCOC2020-P3-Entrega 7

# Predicción de resultados con curva de hidratación de la tesis de Contreras

* Con los datos y experimentos realizados, se obtienen las curvas de hidratación experimentales:

![Alt Text](https://github.com/raimolid/MCOC2020-P3-Final/blob/main/caso_1_camara_de_curado.png)


![Alt Text](https://github.com/raimolid/MCOC2020-P3-Final/blob/main/caso_2_intemperie.png)

* Para predecir aquellos resultados, se implementa un modelo 3D del bloque de hormigón, que lleve a producir la curva de hidratación para el problema:

Primero, para el caso del bloque en la cámara de curado, se intenta llegar a un modelo 3D modificando el caso 2D, anteriormente implementado.
Se modifica el doble ciclo for hacia un triple ciclo for, agregando la componente en z y los indices correspondientes para el algoritmo de diferencias finitas que nos permitirá calcular el laplaciano


```
#Loop en el espacio i = 1 ...... n-1
    for i in range(1,Nx):
        for j in range(1,Ny):
            for k in range(1,Nz):
                #Algoritmo de diferencia finitas 2-D para difusión
                nabla_u_k = u_k[i-1,j,k] + u_k[i+1,j,k] + u_k[i,j-1,k] + u_k[i, j+1,k] + u_k[i, j,k-1] + u_k[i, j,k+1] - 6*u_k[i,j] + Calor_de_hidratacion(t,DC = 360.)

```

Luego, ocupando las condiciones de borde descritas en el enunciado (gradiente cero para los lados del bloque lados izquierdo, derecho, adelante, atrás y abajo del bloque), que se traducen a 3D de la siguiente manera:

```
u_k[ : , : , 0 ] = u_k[ : , : , 1 ]-0*dx   #cara inferior xy
u_k[ : , : ,-1 ] = u_ambiente              #cara superior xy
u_k[ : ,-1 , : ] = u_k[ : ,-2 , : ]-0*dx   #cara derecha xz
u_k[ : , 0 , : ] = u_k[ : , 1 , : ]-0*dx   #cara izquierda xz
u_k[-1 , : , : ] = u_k[-2 , : , : ]-0*dx   #cara frontal yz
u_k[ 0 , : , : ] = u_k[ 1 , : , : ]-0*dx   #cara atras yz

```
Se obtiene el siguiente gráfico que no predice de buena manera los resultados obtenidos, pero que da una forma más o menos para donde puede llevar el código implementado, que mejorandole algunos parámetros podría replicar los resultados correctos

![Alt Text](https://github.com/raimolid/MCOC2020-P3-Final/blob/main/caso_1.png)
