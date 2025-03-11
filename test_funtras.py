import pregunta1 as P

Relleno_raiz = P.cos_t(3 * P.div_t(7)) + P.ln_t(2) #cos(3/7) + ln(2)
Numerador = P.root_t(Relleno_raiz, 3) #3√(cos(3/7) + ln(2))

Denominador = P.sinh_t(P.sqrt_t(2)) #sinh(√2)

division = Numerador * P.div_t(Denominador) #3√(cos(3/7) + ln(2)) / sinh(√2)

sumando = P.atan_t(P.exp_t(-1)) #arctan(e^-1)

Resultado = division + sumando #3√(cos(3/7) + ln(2)) / sinh(√2) + arctan(e^-1)

print("Resultado")
print(Resultado)
