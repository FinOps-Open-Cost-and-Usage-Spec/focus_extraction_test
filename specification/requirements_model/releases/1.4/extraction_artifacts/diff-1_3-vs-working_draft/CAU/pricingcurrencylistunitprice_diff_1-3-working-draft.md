## Diff

diff --git a/specification/datasets/cost_and_usage/columns/pricingcurrencylistunitprice.md b/specification/datasets/cost_and_usage/columns/pricingcurrencylistunitprice.md
index 51d5aa6f..cbdf9f2d 100644
--- a/specification/datasets/cost_and_usage/columns/pricingcurrencylistunitprice.md
+++ b/specification/datasets/cost_and_usage/columns/pricingcurrencylistunitprice.md
@@ -1,24 +1,23 @@
# Pricing Currency List Unit Price

The Pricing Currency List Unit Price represents the suggested service-provider-published unit price for a single [Pricing [-Unit](#pricingunit)-]{+Unit](#datasets.costandusage.pricingunit)+} of the associated [*SKU*](#glossary:sku), exclusive of any discounts. This price is denominated in the [Pricing [-Currency](#pricingcurrency).-]{+Currency](#datasets.costandusage.pricingcurrency).+} The Pricing Currency List Unit Price is commonly used for calculating savings based on various rate optimization activities.

## Requirements

PricingCurrencyListUnitPrice [-adheres-]{+MUST adhere+} to the following requirements:

* PricingCurrencyListUnitPrice presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset)[-is defined as follows:-]
[-  * PricingCurrencyListUnitPrice-] MUST [-be present in a Cost and Usage *FOCUS dataset* when-]{+adhere to+} the [-service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.-]{+following presence requirements:+}
  * PricingCurrencyListUnitPrice [-is RECOMMENDED to-]{+SHOULD+} be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyListUnitPrice MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
* PricingCurrencyListUnitPrice MUST be of type Decimal.
* PricingCurrencyListUnitPrice MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* PricingCurrencyListUnitPrice {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * PricingCurrencyListUnitPrice MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * PricingCurrencyListUnitPrice MUST be null when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Tax".
  * PricingCurrencyListUnitPrice MUST NOT be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is not null.
  * PricingCurrencyListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
  * PricingCurrencyListUnitPrice MAY be null in all other cases.
* When PricingCurrencyListUnitPrice is not null, PricingCurrencyListUnitPrice [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * PricingCurrencyListUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyListUnitPrice MUST be denominated in the PricingCurrency.

@@ -40,14 +39,15 @@ The suggested service-provider-published unit price for a single Pricing Unit of

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:-------------------------------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric [-Format](#numericformat)-]{+Format](#attributes.numericformat)+}          |
| Number range    | Any valid non-negative decimal value                 |

## Introduced (version)

