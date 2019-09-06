api_version = 'v2'
account = {
    'client_id': 'amzn1.application-oa2-client.a0d844f974444b90be9d3b0d76f24108',
    'client_secret': 'e47e39ea3ca8e4d5539db798912d5cdcdf538c0f4e5963c05748bda5369880b1',
    'access_token': 'Atza|IwEBIAFblC2ztltnU8hwozAt4sHSF6jtWV8eVhsgTGAs41CqB0BcB-NqDoJCYN4cnRZGuZ8dbWm_cdIexQJ5FNk2haisDP0Jpc92XuR38H6B8Wl0DmJKKLtnm4PvGZD0YRj4MihK0HkLtwIbj3Lkh8Bj9eolQDM6rMv-qYkHBQNmqTT796B22uVtqHjvFPXi5Qaw_99-xe3NdPXmWVbkMsePEtglO1esx61qbYaC_fKMXUf7CdFHFfgLRvqVVBN1e3wst9HZ2Kt2sAja70pQb9eQUGqtHlrpVBBMdOPdkjCVkBGynWiKxsrSijYaHoiTEUeA4E1NCXdEmSQxLBKV3cvagCSsP0luO8IZJitbj9fWHr3_HbWQkx12d99jEtXoDRUV_buUuthzPoOG7XpbvRUWsRdRYrK5o0n3LZXSZIeWnPV8s9DGJYS7RPXfWiB74l1zb16mTaGAa54S0dR9KsMbXamAgUqVAyIpe6d0YZFSGLEj5QQ0dCfqw4eXjwtxl39cte8J5Uy5UI2p1R-6_4x9sO11VMuFkDfLNq1mMC4kHIma662Lq3DYT1VjIGyCah4yrDo9ZBTB5Nk0ExTerB_VcQPUfzY7M5iauX1mPDke57EZVA',
    'refresh_token': 'Atzr|IwEBIMQjfJ-KgsfG5TQxQsu58zujpBezyiO5FdtMhp3w_oGZ6kQlmDlch3l6COw5d0AnTpVGR-Bg3bxtI19Rjt5Pv02UKs0tXMIWtWYxPI7fU-dGXPZtPjEKPQ0LMTqLTl7J5_sw5CvIIaPeSINXhCOnQeef-1NPBBMsk1KdMcvrOYvIj8BJW2WykPx0YuAxiRyBpkgabMKFYcllFf8XS9k1UyD7MJv9i9yJB15edCUcWVZ4W-U9OQCAp5SmZEAMEQEeNrd5HnEo7nf9ttPzbQOBdUig7WfxHQSiEh6vcIaqD5wW6Moo8QgfEsbvQQBZb3PqCzpVBpAtNEHrW8PkYnr_fjpOPZPbODFo8hrMwf-KffdiA1AS6Gc_DWAkBdrIVjLcpYcMDH3USKKE8s3r9hoQdh1_VMQ4J3EXOagulR3CPoDjzi6PNahXo5Sh-afyRbHnrrt_Xn6wskEX3qhFuCjifB7DnarhCpFMXiQFtt5Y0G1xUO14wMC7oHtYkcV2juKJCsQ7FmZIu6OJjYMsZI24OLwCeDONb3cjE59323zU_8Rac4yBLecCPDKs2ymUWTTujgRmNKa3o2gnqhP6Y_Me-5eh',
    'scope': {
        'us': '1223366941512513',
        'ca': '4395156076169305'
    }
}
oauth_url = 'https://api.amazon.com/auth/o2/token'
regions = {
    'sandbox': 'advertising-api-test.amazon.com',
    'na': 'advertising-api.amazon.com',
    'eu': 'advertising-api-eu.amazon.com',
    'fe': 'advertising-api-fe.amazon.com'
}
report_type = {
    'rp_scope': ['US1223366941512513', 'CA4395156076169305'],
    'type': ['sp', 'hsa','asin'],
    'sp_keyword_seg': ['query', 'placement'],
    'sp': ['campaigns', 'adGroups', 'keywords', 'productAds', 'targets'],
    'hsa': ['campaigns', 'adGroups', 'keywords'],
    'asin': ['asins'],
    'campaigns': ['portfolioId', 'portfolioName', 'bidPlus', 'campaignStatus', 'campaignBudget'],
    'adGroups': ['adGroupName', 'adGroupId'],
    'keywords': [ 'keywordId', 'keywordText', 'matchType'],
    'productAds': ['adGroupName', 'adGroupId', 'currency', 'asin', 'sku'],
    'targets': ['targetId', 'targetingExpression', 'targetingText', 'targetingType'],
    'asins': ['adGroupName', 'adGroupId', 'keywordId', 'keywordText', 'asin', 'otherAsin', 'sku', 'currency',
              'matchType'],
    'sp_common': ['campaignId', 'campaignName', 'impressions', 'clicks', 'cost',
                  'attributedConversions1d', 'attributedConversions7d',
                  'attributedConversions14d', 'attributedConversions30d',
                  'attributedConversions1dSameSKU', 'attributedConversions7dSameSKU',
                  'attributedConversions14dSameSKU', 'attributedConversions30dSameSKU',
                  'attributedUnitsOrdered1d', 'attributedUnitsOrdered7d',
                  'attributedUnitsOrdered14d', 'attributedUnitsOrdered30d',
                  'attributedSales1d', 'attributedSales7d', 'attributedSales14d',
                  'attributedSales30d', 'attributedSales1dSameSKU',
                  'attributedSales7dSameSKU', 'attributedSales14dSameSKU',
                  'attributedSales30dSameSKU'],
    'hsa_common': ['campaignId', 'campaignName', 'impressions', 'clicks', 'cost', 'attributedSales14d',
                   'attributedSales14dSameSKU', 'attributedConversions14d',
                   'attributedConversions14dSameSKU', 'attributedOrdersNewToBrand14d',
                   'attributedOrdersNewToBrandPercentage14d', 'attributedOrderRateNewToBrand14d',
                   'attributedSalesNewToBrand14d', 'attributedSalesNewToBrandPercentage14d',
                   'attributedUnitsOrderedNewToBrand14d','attributedUnitsOrderedNewToBrandPercentage14d'],
    'asin_common': ['campaignName', 'campaignId', 'attributedUnitsOrdered1dOtherSKU', 'attributedUnitsOrdered7dOtherSKU',
                    'attributedUnitsOrdered14dOtherSKU', 'attributedUnitsOrdered30dOtherSKU', 'attributedSales1dOtherSKU',
                    'attributedSales7dOtherSKU', 'attributedSales14dOtherSKU', 'attributedSales30dOtherSKU']
}