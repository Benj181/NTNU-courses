import pulp as p

model = p.LpProblem('HammersAndNails', p.LpMaximize)

x = p.LpVariable("x", lowBound=0 ,upBound=40)
y = p.LpVariable("y", lowBound=0)

model += 3000*x + 1000*y

model += (2*x + y <= 100), "NailConstraint"
model += (x + 2*y <= 80), "HammerConstraint"
model += (x <= 40), "MaxHammerConstraint"

print(model)
status = model.solve()
print("x =", p.value(x))
print("y =", p.value(y))
print("Objective =", p.value(model.objective))