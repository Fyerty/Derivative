from string import digits

"-5x^4 - 5 x ^ 2 - 4"
"5  *x^3 - 3 x ^ 2+1"
"-5x - 5 x ^ 2 - 4"


def deriv_polynomial(polynom: str) -> str:
    monoms = polynom.split("+")
    deriv = ""

    for monom in monoms:
        try:
            u = monom.split("*")
            v = u[1].split("^")
            if len(v) == 1: v += [1]
            deriv += f"+{str(int(u[0]) * int(v[1]))}x^{int(v[1]) - 1}"
        except IndexError:  ...

    deriv = deriv.replace("+-", "-").replace("^1", "").replace("x^0", "")

    return deriv if deriv[0] == "-" else deriv.replace("+-", "-")[1:]


exp = input("Введите многочлен: ").replace(" ", "").replace("-", "+-")

for dig in digits:
    exp = exp.replace(f"{dig}x", f"{dig}*x")

print("Производная: " + deriv_polynomial(exp))
