#Gideon Quaye
#CS-175L-02
#stocks
Commission_Rate = float(input("Please enter Commission Rate: "))
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75
amountPaidForStock = NUM_SHARES*PURCHASE_PRICE
purchaseCommission = Commission_Rate*amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES*SELLING_PRICE
sellingCommission = Commission_Rate*stockSoldFor
totalRecieved = stockSoldFor - sellingCommission
profitOrLoss = totalRecieved - totalPaid

print(f'Amount paid for stock: ${amountPaidForStock:,.2f}')
print(f'Commission paid on the purchase: ${purchaseCommission:,.2f}')
print(f'Amount the stock sold for: ${stockSoldFor:,.2f}')
print(f'Commission paid on the sale: ${sellingCommission:,.2f}')
print(f'Profit (or loss if negative): ${profitOrLoss:,.2f}')
