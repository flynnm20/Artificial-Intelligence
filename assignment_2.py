fit = 0
unfit = 1
dead = 2
exercise = 1
relax = 0

exercise_table = [[[.891, .009, .1], [8, 8, 0]], [
    [.18, .72, .1], [0, 0, 0]], [[0, 0, 1], [0, 0, 0]]]
relax_table = [[[.693, .297, .01], [10, 10, 0]], [
    [0, .99, .01], [5, 5, 0]],  [[0, 0, 1], [0, 0, 0]]]

# q0(s, a) := p(s, a, fit)r(s, a, fit) + p(s, a, unfit)r(s, a, unfit)
# Vn(s) := max(qn(s, exercise), qn(s,relax))
# qn+1(s, a) := q0(s, a) + γp(s, a, fit)Vn(fit) + p(s, a, unfit)Vn(unfit)).


def show(n, s, gamma):
    if n < 0:
        return "Constraint: n must be a positive integer"
    if s != fit and s != unfit and s != dead:
        return "Constraint: state must be either Fit, Unfit, or Dead"
    if gamma >= 1 or gamma <= 0:
        return "Constraint: 0 < g < 1"
    global g
    g = gamma
    for i in range(0, n+1):
        print('n=%d exer: %f relax: %f' %
              (i, q(s, exercise, i), q(s, relax, i)))

# q


def q(s, a, n):
    if s == dead:
        return 0
    # q0
    q0 = (p(s, a, fit) * r(s, a, fit)) + (p(s, a, unfit) * r(s, a, unfit))
    if n == 0:
        return q0
    # qn+1
    else:
        return q0 + (g * ((p(s, a, fit) * vn(fit, n-1)) + (p(s, a, unfit) * vn(unfit, n-1))))

# Vn(s)


def vn(s, n):
    return max(q(s, exercise, n), q(s, relax, n))

# Get probability from probability table


def p(s, a, result):
    if a == exercise:
        return exercise_table[s][0][result]
    else:
        return relax_table[s][0][result]

# Get result from result table


def r(s, a, result):
    if a == exercise:
        return exercise_table[s][1][result]
    else:
        return relax_table[s][1][result]


show(10, fit, 0.5)
print()
show(8, unfit, 0.8)
print()
show(10, dead, 0.99)
