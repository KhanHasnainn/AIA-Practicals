from simpleai.search import CspProblem, backtrack
def different(names, values):
    return values[0] != values[1]


names = ('WA', 'NT', 'SA', 'QL', 'Vict', 'Tasmania')
colors = {s: ['red', 'green', 'blue'] for s in names}


constraints = [
    (('WA', 'NT'), different),
    (('WA', 'SA'), different),
    (('NT', 'SA'), different),
    (('NT', 'QL'), different),
    (('SA', 'QL'), different),
    (('SA', 'Vict'), different),
    (('QL', 'Vict'), different)
]


problem = CspProblem(names, colors, constraints)
result = backtrack(problem)


for s, c in result.items():
    print(s, "=", c)
