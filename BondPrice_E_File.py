def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    bondPrice = 0

    for i, y in enumerate(yc):
        t=i+1

        cf=coupon
        if t==m:
            cf=cf+face

        pvm=1/((1+y)**t)
        pvcf=pvm*cf
        
        bondPrice=bondPrice+pvc

    return bondPrice
