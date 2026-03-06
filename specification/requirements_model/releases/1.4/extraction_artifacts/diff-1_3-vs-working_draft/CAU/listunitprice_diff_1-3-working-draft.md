## Diff

diff --git a/specification/datasets/cost_and_usage/columns/listunitprice.md b/specification/datasets/cost_and_usage/columns/listunitprice.md
index 1de50c0f..ae602ea6 100644
--- a/specification/datasets/cost_and_usage/columns/listunitprice.md
+++ b/specification/datasets/cost_and_usage/columns/listunitprice.md
@@ -1,24 +1,23 @@
# List Unit Price

The List Unit Price represents the suggested service-provider-published unit price for a single [Pricing [-Unit](#pricingunit)-]{+Unit](#datasets.costandusage.pricingunit)+} of the associated SKU, exclusive of any discounts. This price is denominated in the [Billing [-Currency](#billingcurrency).-]{+Currency](#datasets.costandusage.billingcurrency).+} The List Unit Price is commonly used for calculating savings based on various rate optimization activities.

## Requirements

ListUnitPrice [-adheres-]{+MUST adhere+} to the following requirements:

[-* ListUnitPrice MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider publishes unit prices exclusive of discounts.-]
* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* ListUnitPrice {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ListUnitPrice MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * ListUnitPrice MUST be null when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Tax".
  * ListUnitPrice MUST NOT be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is not null.
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
* [-[ListCost](#listcost)-]{+[ListCost](#datasets.costandusage.listcost)+} MUST equal the product of ListUnitPrice and [-[PricingQuantity](#pricingquantity)-]{+[PricingQuantity](#datasets.costandusage.pricingquantity)+} when ListUnitPrice is not null and PricingQuantity is not null.

## Column ID

@@ -38,14 +37,15 @@ The suggested service-provider-published unit price for a single Pricing Unit of

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

