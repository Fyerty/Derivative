from string import digits

"-5x^4 - 5 x ^ 2 - 4"
"5  *x^3 - 3 x ^ 2+1"
"-5x - 5 x ^ 2 - 4"
"-5x - 5x^2 - 4x^0.5"


def preparation(exp: str) -> list:
    exp = exp.replace(" ", "").replace("-", "+-")

    for dig in digits:
        exp = exp.replace(f"{dig}x", f"{dig}*x")

    # exp = exp.split("+")

    return exp


def flint(a: float|int|str):
    if type(a) == float:
        if float(int(a)) - float(a) == 0.0:
            return int(a)
        return a

    elif type(a) == int:
        return a

    return flint(float(a))

def deriv_polynomial(polynom: str) -> str:
    monoms = polynom.split("+")
    deriv = ""

    for monom in monoms:
        try:
            u = monom.split("*")
            v = u[1].split("^")
            if len(v) == 1: v += [1]
            deriv += f"+{flint(float(u[0]) * float(v[1]))}x^{flint(v[1]) - 1}"
        except IndexError:  ...

    deriv = deriv.replace("+-", "-").replace("^1", "").replace("x^0", "")

    return deriv if deriv[0] == "-" else deriv.replace("+-", "-")[1:]


print("Производная: " + deriv_polynomial(preparation(input("Введите выражение: "))))