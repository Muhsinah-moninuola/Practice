TotalPurchase = int(input('Kindly enter the total amount of your purchase: '))
Discount = 0.1*TotalPurchase
if  1000 < TotalPurchase <5000:
    print('Congratulations, You are eligible to a 10% discount')
    Atp = TotalPurchase - Discount
    print ('The total amount you have to pay for this purchase after discount is: ', Atp)
elif 5000 < TotalPurchase <10000: 
    print('Congratulations, You are eligible to a 50% discount')
    D3 = 0.5 *TotalPurchase  
    Atp3 = TotalPurchase - D3
    print ('The total amount you have to pay for this purchase after discount is: ', Atp3)
elif TotalPurchase >10000:
    print('Congratulations, You are eligible to a 20% discount')
    D2 = 0.2*TotalPurchase
    Atp2 = TotalPurchase - D2
    print ('The total amount you have to pay for this purchase after discount is: ', Atp2)
else: 
    print('You are to eligible to a discount')
    print('Your total is: ', TotalPurchase)
    
