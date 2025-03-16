function matriz_penta()

  %Limpiar la terminal cada vez que se compila
  clc; clear;

  %Valor inicial de m
  m = 2500;

  %Inicialización de vectores según lo establecido
  a=zeros(m,1);
  b=zeros(m-1,1);
  c=zeros(m-1,1);
  d=zeros(m-2,1);
  e=zeros(m-2,1);
  h=zeros(m,1);

  %Cálculo de cada uno de los valores de los vectores a y h
  %Tamaño m x 1
  for i=1:m
    a(i)=2i;
    h(i)=2i-5;
  endfor

  %Cálculo de cada uno de los valores de los vectores b y c
  %Tamaño m-1 x 1
  for i=1:m-1
    b(i)= -(i+1)/3;
    c(i)= i/3;
  endfor

  %Cálculo de cada uno de los valores de los vectores d y e
  %Tamaño m-2 x 1
  for i=1:m-2
    d(i)= -(i+2)/2;
    e(i)= i/2;
  endfor

   %Se llama a la función para generar la matriz pentadiagonal con cada uno de sus valores necesarios
   A=pentadiagonal(m,a,b,c,d,e);

   %Se calcula el sistema de ecuaciones Ax = h
   x=mldivide(A,h);

   %Se calcula el error con la ecuacion ||Ax-h||
   error=norm((A*x)-h)

end

%Funcion para generar matriz pentadiagonal
function A=pentadiagonal(m,a,b,c,d,e)

  %Inicialización de matriz
  A=zeros(m);

  %Introducción de los datos de los valores de a (diagonal central)
  for i=1:m
    A(i,i)=a(i);
  endfor

  %Introducción de los datos de los valores de b y c (diagonales adyacentes a la central m-1 x 1)
  for i=1:m-1
    A(i+1,i)=b(i);
    A(i,i+1)=c(i);
  endfor

  %Introducción de los datos de los valores de d y e (diagonales adyacentes a b y c m-2 x 1)
  for i=1:m-2
    A(i+2,i)=d(i);
    A(i,i+2)=e(i);
  endfor

end







