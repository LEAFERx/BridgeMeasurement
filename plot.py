import matplotlib.pyplot as plt
import json

f = open('./data/eth/deposit.json')
deposit = json.load(f)
f.close()

f = open('./data/eth/exit.json')
exit = json.load(f)
f.close()

base = min(deposit[0]['block'], exit[0]['block'])

lastD = 0
lastE = 0
depositB = []
depositV = []
exitB = []
exitV = []

for d in deposit:
    depositB.append(d['block'] - base)
    depositV.append(d['amount'] + lastD)
    lastD = d['amount'] + lastD
for d in exit:
    exitB.append(d['block'] - base)
    exitV.append(d['amount'] + lastE)
    lastE = lastE + d['amount']

plt.scatter(depositB, depositV, marker='.',alpha=0.5, label='deposit')
plt.scatter(exitB, exitV, c='orange', marker='.',alpha=0.5, label='exit')
plt.legend()
plt.show()



# f = open('./data/eth/userexit.json')
# exit = json.load(f)
# f.close()

# f = open('./data/eth/userdeposit.json')
# deposit = json.load(f)
# f.close()

# countE = []
# valueE = []

# for d in exit:
#     countE.append(d['count'])
#     valueE.append(d['sum'])

# countD = []
# valueD = []

# for d in deposit:
#     countD.append(d['count'])
#     valueD.append(d['sum'])

# plt.xlabel("Deposit/Exit Times")
# plt.ylabel("Deposit/Exit Amount")
# plt.scatter(countD, valueD, marker='.', alpha=0.5, label='depoist')
# plt.scatter(countE, valueE, marker='.', alpha=0.5,  c='orange', label='exit')
# plt.legend()
# plt.show()