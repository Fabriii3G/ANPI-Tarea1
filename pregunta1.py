Pi = 3.1415926535897932
iterMax = 2500
tol = 1e-8

"""
Funcion: x!
Dominio: Reales positivos
"""
def factorial(x):
    result = 1
    if x == 0 or x == 1:
        return 1
    elif x < 0:
        return "No se puede calcular el factorial de un numero negativo"
    else:
        for k in range(2, x + 1):
            result *= k
        return result

"""
Funcion: 1/x
Dominio: Reales expecto el 0
"""
def div_t(x):
    eps = 2.2204e-16
    if x == 0:
        return "No se puede dividir entre 0"
    elif factorial(80) < x < factorial(100):
        x0 = eps**15
    elif factorial(60) < x <= factorial(80):
        x0 = eps**11
    elif factorial(10) < x <= factorial(60):
        x0 = eps**8
    elif factorial(20) < x <= factorial(40):
        x0 = eps**4
    else:
        x0 = eps**2
    for k in range(1, iterMax + 1):
        xk = x0 * (2 - x * x0)
        if abs(xk - x0) < tol * abs(xk):
            break
        x0 = xk
    return xk

"""
Funcion: e^x
Dominio: Todos los reales
"""
def exp_t(x):
    Sk_v = 1
    term = 1  # Se inicializa con 1/0! = 1

    for k in range(1, iterMax + 1):
        term *= div_t(k)  # Se calcula 1 / k! de manera incremental, ya que al usar factorial presentaba errores
        Sk = Sk_v + x ** k * term
        er = abs(Sk - Sk_v)
        if er < tol:
            break
        Sk_v = Sk

    return Sk

"""
Funcion: sin(x)
Dominio: Reales
"""
def sin_t(x):
    Sk_v = 0

    for k in range(0, iterMax):
        Sk = ((-1) ** k) * (x ** (2 * k + 1)) * div_t(factorial(2 * k + 1))
        Sk_v_prev = Sk_v
        Sk_v += Sk
        er = abs(Sk_v - Sk_v_prev)
        if er < tol:
            break
    return Sk_v

"""
Funcion: cos(x)
Dominio: Reales
"""
def cos_t(x):
    Sk_v = 0

    for k in range(iterMax):
        Sk = ((-1) ** k) * (x ** (2 * k)) * div_t(factorial(2 * k))
        Sk_v_prev = Sk_v
        Sk_v += Sk
        er = abs(Sk_v - Sk_v_prev)
        if er < tol:
            break
    return Sk_v

"""
Funcion: tan(x)
Dominio: Reales excepto los valores dados por Pi/2 + kPi, donde k pertenece a los enteros
"""
def tan_t(x):
    if x == Pi:
        return 0
    elif -tol < (x - Pi / 2) % Pi < tol:
        return "La tangente no está definida para x = Pi/2 + kPi."
    else:
        return sin_t(x) * div_t(cos_t(x))

"""
Funcion: ln(x)
Dominio: Reales positivos
"""
def ln_t(x):
    if x <= 0:
        return "ln no esta definido para reales negativos"
    c = (x - 1) * div_t(x + 1)
    Sk_v = 0
    for k in range(0, iterMax):
        Sk = div_t(2 * k + 1) * (c ** (2 * k))
        Sk_v_prev = Sk_v
        Sk_v += Sk
        er = abs(2 * c * Sk_v - 2 * c * Sk_v_prev)
        if er < tol:
            break
    return 2 * c * Sk_v

"""
Funcion: log_y(x)
Dominio: Reales positivos
"""
def log_t(x, y):
    if x <= 0 or y <= 0:
        return "la base o el argumento no pueden ser negativos"
    else:
        return ln_t(x) * div_t(ln_t(y))

"""
Funcion: x^y
Dominio: Reales
"""
def power_t(x, y):
    c = x ** abs(y)
    if y == 0:
        return 1
    elif y > 0:
        return c
    else:
        return div_t(c)

"""
Funcion: sinh(x)
Dominio: Reales
"""
def sinh_t(x):
    Sk_v = 0

    for k in range(0, iterMax):
        Sk = (x ** (2 * k + 1)) * div_t(factorial(2 * k + 1))
        Sk_v_prev = Sk_v
        Sk_v += Sk
        er = abs(Sk_v - Sk_v_prev)
        if er < tol:
            break
    return Sk_v

"""
Funcion: cosh(x)
Dominio: Reales
"""
def cosh_t(x):
    Sk_v = 0

    for k in range(iterMax):
        Sk = (x ** (2 * k)) * div_t(factorial(2 * k))
        Sk_v_prev = Sk_v
        Sk_v += Sk
        er = abs(Sk_v - Sk_v_prev)
        if er < tol:
            break
    return Sk_v

"""
Funcion: tanh(x)
Dominio: Reales
"""
def tanh_t(x):
    return sinh_t(x) * div_t(cosh_t(x))

"""
Funcion: √x
Dominio: Reales positivos
"""
def sqrt_t(x):
    if x <= 0:
        return "El valor debe ser positivo"
    else:
        return x ** div_t(2)

"""
Funcion: n√x
Dominio: Reales positvos
"""
def root_t(x, y):
    x0 = x * div_t(2)
    if y == 0:
        return "Ingrese un valor para la raiz mayor a 0"

    elif isinstance(y, int) and y > 0:
        for k in range(0, iterMax):
            x1 = x0 - (x0 ** y - x) * div_t(y * x0 ** (y - 1))
            er = abs(x - x0)
            if er < tol * abs(x):
                break
            x0 = x1

    return x1

"""
Funcion: arcsin(x)
Dominio: [-1, 1]
"""
def asin_t(x):
    Sk_v = 0

    if -1 <= x <=1:
        for k in range(0, iterMax):
            numerador = factorial(2 * k)
            denominador = (4 ** k * factorial(k) ** 2 * (2 * k + 1))
            Sk = (numerador * div_t(denominador)) * (x ** (2 * k + 1))
            Sk_v_prev = Sk_v
            Sk_v += Sk
            er = abs(Sk_v - Sk_v_prev)
            if er < tol:
                break
    else:
        return "El valor del argumento debe estar entre [-1, 1]"

    return Sk_v

"""
Funcion: arccos(x)
Dominio: [-1, 1]
"""
def acos_t(x):
    if -1 <= x <=1:
        return Pi * div_t(2) - asin_t(x)
    else:
        return "El valor del argumento debe estar entre [-1, 1]"

"""
Funcion: arctan(x)
Dominio: Reales
"""
def atan_t(x):
    Sk_v = 0
    if -1 <= x <= 1:
        for k in range (0, iterMax):
            signo = (-1) ** k
            numerador = x ** (2 * k + 1)
            denominador = 2 * k + 1
            Sk = signo * numerador * div_t(denominador)
            Sk_v_prev = Sk_v
            Sk_v += Sk
            er = abs(Sk_v - Sk_v_prev)
            if er < tol:
                break
        return Sk_v
    elif x > 1:
        for k in range(0, iterMax):
            signo = (-1) ** k
            c = (2 * k + 1) * x ** (2 * k +1)
            denominador = 1/c
            Sk = signo * (denominador)
            Sk_v_prev = Sk_v
            Sk_v += Sk
            er = abs((Pi * div_t(2) - Sk_v) - (Pi * div_t(2) - Sk_v_prev))
            if er < tol:
                break
        return Pi * div_t(2) - Sk_v
    else:
        for k in range(0, iterMax):
            signo = (-1) ** k
            c = (2 * k + 1) * x ** (2 * k +1)
            denominador = 1/c
            Sk = signo * (denominador)
            Sk_v_prev = Sk_v
            Sk_v += Sk
            er = abs((-Pi * div_t(2) - Sk_v) - (-Pi * div_t(2) - Sk_v_prev))
            if er < tol:
                break
        return -Pi * div_t(2) - Sk_v

"""
Funcion: sec(x)
Dominio: Reales excepto los valores dados por Pi/2 + kPi donde k pertece a los enteros
"""
def sec_t(x):
    if -tol < (x - Pi / 2) % Pi < tol:
        return "La secante no está definida para x = Pi/2 + kPi."
    else:
        return div_t(cos_t(x))

"""
Funcion: cot(x)
Dominio: Reales excepto los valores dados por kPi donde k pertece a los enteros
"""
def cot_t(x):
    if -tol < x % Pi < tol:
        return "La cotangente no está definida para x = kPi"
    else:
        return div_t(tan_t(x))

"""
Funcion: csc(x)
Dominio: Reales excepto los valores dados por kPi donde k pertece a los enteros
"""
def csc_t(x):
    if -tol < x % Pi < tol:
        return "La cosecante no está definida para x = kPi"
    else:
        return div_t(sin_t(x))