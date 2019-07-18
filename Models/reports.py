# coding: utf-8
from Config import db
from sqlalchemy import Column, String, Integer, Float, DECIMAL, Boolean, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DBConnection = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=%s' % \
               (db.User, db.Passwd, db.Host, db.Port, db.DB, db.CharSet)
engine = create_engine(DBConnection)
DBSession = sessionmaker(bind=engine)

class ModelSpReports:
    ID = Column(Integer, primary_key=True)
    SnapDate = Column(DateTime)
    Country = Column(String(10))
    CampaignId = Column(Integer)
    CampaignName = Column(String(400))
    Impressions = Column(Integer)
    Clicks = Column(Integer)
    Cost = Column(DECIMAL(10, 2))
    DayUnits = Column(Integer)
    Day7Units = Column(Integer)
    Day14Units = Column(Integer)
    Day30Units = Column(Integer)
    TotalDayOrders = Column(Integer)
    DayOrders = Column(Integer)
    TotalDay7Orders = Column(Integer)
    Day7Orders = Column(Integer)
    TotalDay14Orders = Column(Integer)
    Day14Orders = Column(Integer)
    TotalDay30Orders = Column(Integer)
    Day30Orders = Column(Integer)
    TotalDayRev = Column(DECIMAL(10, 2))
    DayRev = Column(DECIMAL(10, 2))
    TotalDay7Rev = Column(DECIMAL(10, 2))
    Day7Rev = Column(DECIMAL(10, 2))
    TotalDay14Rev = Column(DECIMAL(10, 2))
    Day14Rev = Column(DECIMAL(10, 2))
    TotalDay30Rev = Column(DECIMAL(10, 2))
    Day30Rev = Column(DECIMAL(10, 2))

    def __init__(self, SnapDate, Country, json_report):
        self.SnapDate = SnapDate
        self.Country = Country
        self.CampaignId = json_report.get('campaignId', 0)
        self.CampaignName = json_report.get('campaignName', '')
        self.Impressions = json_report.get('impressions', 0)
        self.Clicks = json_report.get('clicks', 0)
        self.Cost = json_report.get('cost', 0.0)
        self.DayUnits = json_report.get('attributedUnitsOrdered1d', 0)
        self.Day7Units = json_report.get('attributedUnitsOrdered7d', 0)
        self.Day14Units = json_report.get('attributedUnitsOrdered14d', 0)
        self.Day30Units = json_report.get('attributedUnitsOrdered30d', 0)
        self.TotalDayOrders = json_report.get('attributedConversions1d', 0)
        self.DayOrders = json_report.get('attributedConversions1dSameSKU', 0)
        self.TotalDay7Orders = json_report.get('attributedConversions7d', 0)
        self.Day7Orders = json_report.get('attributedConversions7dSameSKU', 0)
        self.TotalDay14Orders = json_report.get('attributedConversions14d', 0)
        self.Day14Orders = json_report.get('attributedConversions14dSameSKU', 0)
        self.TotalDay30Orders = json_report.get('attributedConversions30d', 0)
        self.Day30Orders = json_report.get('attributedConversions30dSameSKU', 0)
        self.TotalDayRev = json_report.get('attributedSales1d', 0.0)
        self.DayRev = json_report.get('attributedSales1dSameSKU', 0.0)
        self.TotalDay7Rev = json_report.get('attributedSales7d', 0.0)
        self.Day7Rev = json_report.get('attributedSales7dSameSKU', 0.0)
        self.TotalDay14Rev = json_report.get('attributedSales14d', 0.0)
        self.Day14Rev = json_report.get('attributedSales14dSameSKU', 0.0)
        self.TotalDay30Rev = json_report.get('attributedSales30d', 0.0)
        self.Day30Rev = json_report.get('attributedSales30dSameSKU', 0.0)

class ModelHsaReports:
    ID = Column(Integer, primary_key=True)
    SnapDate = Column(DateTime)
    Country = Column(String(10))
    CampaignId = Column(Integer)
    CampaignName = Column(String(400))
    Impressions = Column(Integer)
    Clicks = Column(Integer)
    Cost = Column(Float(6, 2))
    TotalOrders = Column(Integer)
    Orders = Column(Integer)
    TotalRev = Column(Float(6, 2))
    Rev = Column(Float(6, 2))
    CR = Column(Float(6, 2))
    NewOrders = Column(Integer)
    NewOrdersRate = Column(Float(6, 2))
    NewUnits = Column(Integer)
    NewUnitsRate = Column(Float(6, 2))
    NewRev = Column(Float(6, 2))
    NewRevRate = Column(Float(6, 2))


    def __init__(self, SnapDate, Country, json_report):
        self.SnapDate = SnapDate
        self.Country = Country
        self.CampaignId = json_report.get('campaignId', 0)
        self.CampaignName = json_report.get('campaignName', '')
        self.Impressions = json_report.get('impressions', 0)
        self.Clicks = json_report.get('clicks', 0)
        self.Cost = json_report.get('cost', 0)
        self.TotalOrders = json_report.get('attributedConversions14d', 0)
        self.Orders = json_report.get('attributedConversions14dSameSKU', 0)
        self.TotalRev = json_report.get('attributedSales14d', 0.0)
        self.Rev = json_report.get('attributedSales14dSameSKU', 0.0)
        self.CR = json_report.get('attributedOrderRateNewToBrand14d')
        self.NewOrders = json_report.get('attributedOrdersNewToBrand14d')
        self.NewOrdersRate = json_report.get('attributedOrdersNewToBrandPercentage14d')
        self.NewUnits = json_report.get('attributedUnitsOrderedNewToBrand14d')
        self.NewUnitsRate = json_report.get('attributedUnitsOrderedNewToBrandPercentage14d')
        self.NewRev = json_report.get('attributedSalesNewToBrand14d')
        self.NewRevRate = json_report.get('attributedSalesNewToBrandPercentage14d')

SpBase = declarative_base(cls=ModelSpReports)
class AprSpCampaigns(SpBase):

    __tablename__ = 'Apr_Sp_Campaigns'

    PortfolioId = Column(Integer)
    PortfolioName = Column(String(200))
    Status = Column(String(20))
    Budget = Column(DECIMAL(10, 2))
    BidPlus = Column(Boolean)

    def __init__(self, SnapDate, Country, json_report):
        ModelSpReports.__init__(self, SnapDate, Country, json_report)
        self.PortfolioId = json_report.get('portfolioId')
        self.PortfolioName = json_report.get('portfolioName')
        self.Status = json_report.get('campaignStatus', '')
        self.Budget = json_report.get('campaignBudget', 0.0)
        self.BidPlus = json_report.get('bidPlus', 0)

class AprSpAdGroups(SpBase):

    __tablename__ = 'Apr_Sp_AdGroups'

    AdGroupId = Column(Integer)
    AdGroupName = Column(String(400))

    def __init__(self, SnapDate, Country, json_report):
        ModelSpReports.__init__(self, SnapDate, Country, json_report)
        self.AdGroupId = json_report.get('adGroupId', 0)
        self.AdGroupName = json_report.get('adGroupName', '')

class AprSpKeywords(SpBase):

    __tablename__ = 'Apr_Sp_Keywords'

    KeywordId = Column(Integer)
    Keyword = Column(String(400))
    MatchType = Column(String(20))
    Query = Column(String(400))

    def __init__(self, SnapDate, Country, json_report):
        ModelSpReports.__init__(self, SnapDate, Country, json_report)
        self.KeywordId = json_report.get('keywordId', 0)
        self.Keyword = json_report.get('keywordText', '')
        self.MatchType = json_report.get('matchType', '')
        self.Query = json_report.get('query', '')

class AprSpProductAds(SpBase):

    __tablename__ = 'Apr_Sp_ProductAds'

    AdGroupId = Column(Integer)
    AdGroupName = Column(String(400))
    AdId = Column(Integer)
    Asin = Column(String(20))
    Sku = Column(String(50))
    Currency = Column(String(10))

    def __init__(self, SnapDate, Country, json_report):
        ModelSpReports.__init__(self, SnapDate, Country, json_report)
        self.AdGroupId = json_report.get('adGroupId', 0)
        self.AdGroupName = json_report.get('adGroupName', '')
        self.AdId = json_report.get('adId', 0)
        self.Asin = json_report.get('asin', '')
        self.Sku = json_report.get('sku', '')
        self.Currency = json_report.get('currency', '')

class AprSpTargets(SpBase):

    __tablename__ = 'Apr_Sp_Targets'

    TargetId = Column(Integer)
    TargetingText = Column(String(400))
    TargetingType = Column(String(100))
    TargetingExpression = Column(String(400))
    Query = Column(String(400))

    def __init__(self, SnapDate, Country, json_report):
        ModelSpReports.__init__(self, SnapDate, Country, json_report)
        self.TargetId = json_report.get('targetId', 0)
        self.TargetingText = json_report.get('targetingText', '')
        self.TargetingType = json_report.get('targetingType', '')
        self.TargetingExpression = json_report.get('targetingExpression', '')
        self.Query = json_report.get('query', '')

HsaBase = declarative_base(cls=ModelHsaReports)
class AprHsaCampaigns(HsaBase):

    __tablename__ = 'Apr_Hsa_Campaigns'

    Status = Column(String(20))
    Budget = Column(Float(6, 2))

    def __init__(self, SnapDate, Country, json_report):
        ModelHsaReports.__init__(self, SnapDate, Country, json_report)
        self.Status = json_report.get('campaignStatus', '')
        self.Budget = json_report.get('campaignBudget', 0.0)

class AprHsaAdGroups(HsaBase):

    __tablename__ = 'Apr_Hsa_AdGroups'

    AdGroupId = Column(Integer)
    AdGroupName = Column(String(400))

    def __init__(self, SnapDate, Country, json_report):
        ModelHsaReports.__init__(self, SnapDate, Country, json_report)
        self.AdGroupId = json_report.get('adGroupId', 0)
        self.AdGroupName = json_report.get('adGroupName', '')

class AprHsaKeywords(HsaBase):

    __tablename__ = 'Apr_Hsa_Keywords'

    KeywordId = Column(Integer)
    KeywordText = Column(String(400))
    MatchType = Column(String(20))
    Query = Column(String(400))

    def __init__(self, SnapDate, Country, json_report):
        ModelHsaReports.__init__(self, SnapDate, Country, json_report)
        self.KeywordId = json_report.get('keywordId', 0)
        self.KeywordText = json_report.get('keywordText', '')
        self.MatchType = json_report.get('matchType', '')
        self.Query = json_report.get('query', '')



