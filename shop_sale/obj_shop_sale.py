class ShopSale():

    def __init__(self,id,guideId,tourName,tourType,hotel,note,operatorId,shopId,shopProductId,totalPax,totalSale,totalCommissionAmount,guideCommissionAmount,
                 operatorCommissionAmount,driverCommissionAmount,chiefCommissionAmount,totalLandingFeeAmount,totalVipCommissionAmount,moneyOnGuide,moneyReceived,isForwardedSale
                 ,saleDate,forwardDate,shopCurrency,convertCurrency,rate,convertedTotalSale,convertedTotalCommissionAmount,convertedGuideCommissionAmount,convertedOperatorCommissionAmount,
                 convertedDriverCommissionAmount,convertedChiefCommissionAmount,convertedTotalLandingFeeAmount,convertedTotalVipCommissionAmount,totalCompanyIncome,convertedCompanyIncome,
                 addVip,addLanding,addChief,productName,guideSelection,vipCommissionAmountRep,convertedVipCommissionAmountRep,guideName,operatorName,shopName):
        self.id = id
        self.guideId = guideId
        self.tourName = tourName
        self.tourType = tourType
        self.hotel = hotel
        self.note = note
        self.operatorId = operatorId
        self.shopId = shopId
        self.shopProductId = shopProductId
        self.totalPax = totalPax
        self.totalSale = totalSale
        self.totalCommissionAmount = totalCommissionAmount
        self.guideCommissionAmount = guideCommissionAmount
        self.operatorCommissionAmount = operatorCommissionAmount
        self.driverCommissionAmount = driverCommissionAmount
        self.chiefCommissionAmount = chiefCommissionAmount
        self.totalLandingFeeAmount = totalLandingFeeAmount
        self.totalVipCommissionAmount = totalVipCommissionAmount
        self.moneyOnGuide = moneyOnGuide
        self.moneyReceived = moneyReceived
        self.isForwardedSale = isForwardedSale
        self.saleDate = saleDate + " 01:00:00"
        self.forwardDate = forwardDate + " 01:00:00"
        self.shopCurrency = shopCurrency
        self.convertCurrency = convertCurrency
        self.rate = rate
        self.convertedTotalSale = convertedTotalSale
        self.convertedTotalCommissionAmount = convertedTotalCommissionAmount
        self.convertedGuideCommissionAmount = convertedGuideCommissionAmount
        self.convertedOperatorCommissionAmount = convertedOperatorCommissionAmount
        self.convertedDriverCommissionAmount = convertedDriverCommissionAmount
        self.convertedChiefCommissionAmount = convertedChiefCommissionAmount
        self.convertedTotalLandingFeeAmount = convertedTotalLandingFeeAmount
        self.convertedTotalVipCommissionAmount = convertedTotalVipCommissionAmount
        self.totalCompanyIncome = totalCompanyIncome
        self.convertedCompanyIncome = convertedCompanyIncome
        self.addVip = addVip
        self.addLanding = addLanding
        self.addChief = addChief
        self.productName = productName
        self.guideSelection = guideSelection
        self.vipCommissionAmountRep = vipCommissionAmountRep
        self.convertedVipCommissionAmountRep = convertedVipCommissionAmountRep
        self.guideName = guideName
        self.operatorName = operatorName
        self.shopName = shopName
        self.status = 1