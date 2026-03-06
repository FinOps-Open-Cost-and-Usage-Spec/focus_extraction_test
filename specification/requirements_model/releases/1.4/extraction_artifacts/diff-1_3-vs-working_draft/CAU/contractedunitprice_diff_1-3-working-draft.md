## Diff

diff --git a/specification/datasets/cost_and_usage/columns/contractedunitprice.md b/specification/datasets/cost_and_usage/columns/contractedunitprice.md
index 5fe71ccc..a4fbcdd4 100644
--- a/specification/datasets/cost_and_usage/columns/contractedunitprice.md
+++ b/specification/datasets/cost_and_usage/columns/contractedunitprice.md
@@ -1,25 +1,23 @@
# Contracted Unit Price

The Contracted Unit Price represents the agreed-upon unit price for a single [Pricing [-Unit](#pricingunit)-]{+Unit](#datasets.costandusage.pricingunit)+} of the associated SKU, inclusive of [*negotiated discounts*](#glossary:negotiated-discount), if present, while excluding negotiated [*commitment discounts*](#glossary:commitment-discount) or any other discounts. This price is denominated in the [Billing [-Currency](#billingcurrency).-]{+Currency](#datasets.costandusage.billingcurrency).+} The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. If negotiated discounts are not applicable, the Contracted Unit Price defaults to the [List Unit [-Price](#listunitprice).-]{+Price](#datasets.costandusage.listunitprice).+}

## Requirements

ContractedUnitPrice [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractedUnitPrice MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports negotiated pricing concepts.-]
[-* ContractedUnitPrice adheres to the following additional requirements:-]
* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* ContractedUnitPrice {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ContractedUnitPrice MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * ContractedUnitPrice MUST be null when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Tax".
  * ContractedUnitPrice MUST NOT be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is not null.
  * ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
  * ContractedUnitPrice MAY be null in all other cases.
* When ContractedUnitPrice is not null, ContractedUnitPrice [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ContractedUnitPrice MUST be a non-negative decimal value.
  * ContractedUnitPrice MUST be denominated in the BillingCurrency.
* [-[ContractedCost](#contractedcost)-]{+[ContractedCost](#datasets.costandusage.contractedcost)+} MUST equal the product of ContractedUnitPrice and [-[PricingQuantity](#pricingquantity)-]{+[PricingQuantity](#datasets.costandusage.pricingquantity)+} when ContractedUnitPrice is not null and PricingQuantity is not null.

## Column ID

@@ -39,14 +37,15 @@ The agreed-upon unit price for a single Pricing Unit of the associated SKU, incl

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

