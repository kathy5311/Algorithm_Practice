import sys

cash = int(sys.stdin.readline())

chart = list(map(int,(sys.stdin.readline().split())))
stock = 0

#Jun
stock_j = stock
cash_j = cash
for i in range(len(chart)):
    if cash_j >= chart[i]:
        stock_j+=cash_j//chart[i]
        cash_j -= stock_j*chart[i]
jun=stock_j*chart[-1]+cash_j
    
#Sung
stock_s = stock
cash_s = cash
checkpoint=0
for i in range(len(chart)-4):
    if (chart[i] < chart[i+1]< chart[i+2]<chart[i+3]):
        cash_s += stock_s*chart[i+3]
        stock_s = 0

    elif (chart[i]>chart[i+1]>chart[i+2]>chart[i+3]):

        stock_quan = cash_s//chart[i+3]
        stock_s += stock_quan
        cash_s = cash_s - (stock_quan*chart[i+3])
sung=(stock_s*chart[-1]+cash_s)

if jun > sung:
    print("BNP")
elif jun < sung:
    print("TIMING")
else:
    print("SAMESAME")

