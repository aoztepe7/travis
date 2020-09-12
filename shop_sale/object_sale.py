class ShopSale():
    def __init__(self, id, guideId, tourName, tourType, hotel, note, operatorId, shopId, shopProductId, totalPax,
                 totalSale, moneyOnGuide, moneyReceived, isForwardedSale
                 , saleDate, forwardDate, shopCurrency, rate,
                 addVip, addLanding, addChief, productName, guideSelection, guideName, operatorName, shopName,
                 guideCommRate, driverCommRate, operatorCommRate, hotelRepCommRate, totalCommRate, compRateGuide,
                 compRateHotel):
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
        self.moneyOnGuide = moneyOnGuide
        self.moneyReceived = moneyReceived
        self.isForwardedSale = isForwardedSale
        self.saleDate = saleDate + " 01:00:00"
        self.forwardDate = forwardDate + " 01:00:00"
        self.shopCurrency = shopCurrency
        self.rate = rate
        self.addVip = addVip
        self.addLanding = addLanding
        self.addChief = addChief
        self.productName = productName
        self.guideSelection = guideSelection
        self.guideName = guideName
        self.operatorName = operatorName
        self.shopName = shopName
        self.guideCommRate = guideCommRate
        self.driverCommRate = driverCommRate
        self.operatorCommRate = operatorCommRate
        self.hotelRepCommRate = hotelRepCommRate
        self.totalCommRate = totalCommRate
        self.compRateGuide = compRateGuide
        self.compRateHotel = compRateHotel
        self.status = 1