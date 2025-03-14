function matriz_penta()
  clc; clear;

  m = 2500;

  a=zeros(m,1);
  b=zeros(m-1,1);
  c=zeros(m-1,1);
  d=zeros(m-2,1);
  e=zeros(m-2,1);
  h=zeros(m,1);

  for i=1:m
    a(i)=2i;
    h(i)=2i-5;
  endfor

  for i=1:m-1
    b(i)= -(i+1)/3;
    c(i)= i/3;
  endfor

  for i=1:m-2
    d(i)= -(i+2)/2;
    e(i)= i/2;
  endfor

   A=pentadiagonal(m,a,b,c,d,e);

   x=mldivide(A,h);

   error=norm((A*x)-h)

end


function A=pentadiagonal(m,a,b,c,d,e)
  A=zeros(m);

  for i=1:m
    A(i,i)=a(i);
  endfor

  for i=1:m-1
    A(i+1,i)=b(i);
    A(i,i+1)=c(i);
  endfor

  for i=1:m-2
    A(i+2,i)=d(i);
    A(i,i+2)=e(i);
  endfor

end







