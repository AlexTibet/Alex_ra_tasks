from math import sqrt


def ra_sq_eq_sol(a, b, c):
    if a == 0:
        print('When a = 0, the equation is not square.')
        return
    if b == 0 and c == 0:
        print("For an incomplete square equation where 'b' and 'c' are equal to zero"
              "\nthere is only one root: x = 0.")
        return
    D = (b ** 2) - (4 * a * c)
    if D < 0:
        print('This square equation has no actual roots.')
    elif D == 0:
        x = -b / (2 * a)
        print('The only root of this equation: x =', x)
    else:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print('The roots of the square equation:'
              '\nx1 =', x1,
              '\nx2 =', x2)


if __name__ == '__main__':
    print('Starts the function for solving square equations:')
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    c = int(input("Enter c = "))
    ra_sq_eq_sol(a, b, c)


