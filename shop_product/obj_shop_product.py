
class ShopProduct():

    def __init__(self,id,shopId,shopName,productId,productName,totalCommission,guideCommission,driverCommission,companyCommissionWithGuide,operatorCommission,hotelRepCommission,companyCommissionWithHotel,startDate,finishDate):
        self.id = id
        self.shopId = shopId
        self.shopName = shopName
        self.productId = productId
        self.productName = productName
        self.totalCommission = totalCommission
        self.guideCommission = guideCommission
        self.driverCommission = driverCommission
        self.companyCommissionWithGuide = companyCommissionWithGuide
        self.operatorCommission = operatorCommission
        self.hotelRepCommission = hotelRepCommission
        self.companyCommissionWithHotel = companyCommissionWithHotel
        self.startDate = startDate + " 00:01:00"
        self.finishDate = finishDate + " 00:01:00"
        self.status = 1


class ShopProductView():

    def __init__(self,id,productId,productName,totalCommission,guideCommission,driverCommission,companyCommissionWithGuide,operatorCommission,hotelRepCommission,companyCommissionWithHotel):
        self.id = id
        self.productId = productId
        self.productName = productName
        self.totalCommission = totalCommission
        self.guideCommission = guideCommission
        self.driverCommission = driverCommission
        self.companyCommissionWithGuide = companyCommissionWithGuide
        self.operatorCommission = operatorCommission
        self.hotelRepCommission = hotelRepCommission
        self.companyCommissionWithHotel = companyCommissionWithHotel