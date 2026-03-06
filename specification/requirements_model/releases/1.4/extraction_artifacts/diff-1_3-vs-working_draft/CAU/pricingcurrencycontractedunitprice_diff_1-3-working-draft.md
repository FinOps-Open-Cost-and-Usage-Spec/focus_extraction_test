## Diff

diff --git a/specification/datasets/cost_and_usage/columns/pricingcurrencycontractedunitprice.md b/specification/datasets/cost_and_usage/columns/pricingcurrencycontractedunitprice.md
index ceb0db82..b2245403 100644
--- a/specification/datasets/cost_and_usage/columns/pricingcurrencycontractedunitprice.md
+++ b/specification/datasets/cost_and_usage/columns/pricingcurrencycontractedunitprice.md
@@ -1,24 +1,23 @@
# Pricing Currency Contracted Unit Price

The Pricing Currency Contracted Unit Price represents the agreed-upon unit price for a single [Pricing [-Unit](#pricingunit)-]{+Unit](#datasets.costandusage.pricingunit)+} of the associated [*SKU*](#glossary:sku), inclusive of [*negotiated discounts*](#glossary:negotiated-discount), if present, while excluding negotiated [*commitment discounts*](#glossary:commitment-discount) or any other discounts. This price is denominated in the [Pricing [-Currency](#pricingcurrency).-]{+Currency](#datasets.costandusage.pricingcurrency).+} When negotiated discounts do not apply to unit prices and instead are applied to exchange rates, the Pricing Currency Contracted Unit Price defaults to the [Pricing Currency List Unit [-Price](#pricingcurrencylistunitprice).-]{+Price](#datasets.costandusage.pricingcurrencylistunitprice).+} The Pricing Currency Contracted Unit Price is commonly used to calculate savings based on negotiation activities.

## Requirements

PricingCurrencyContractedUnitPrice [-adheres-]{+MUST adhere+} to the following requirements:

* PricingCurrencyContractedUnitPrice presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset)[-is defined as follows:-]
[-  * PricingCurrencyContractedUnitPrice-] MUST [-be present in a Cost and Usage *FOCUS dataset* when-]{+adhere to+} the [-service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.-]{+following presence requirements:+}
  * PricingCurrencyContractedUnitPrice [-is RECOMMENDED to-]{+SHOULD+} be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyContractedUnitPrice MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
* PricingCurrencyContractedUnitPrice MUST be of type Decimal.
* PricingCurrencyContractedUnitPrice MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* PricingCurrencyContractedUnitPrice {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * PricingCurrencyContractedUnitPrice MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * PricingCurrencyContractedUnitPrice MUST be null when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Tax".
  * PricingCurrencyContractedUnitPrice MUST NOT be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is not null.
  * PricingCurrencyContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
  * PricingCurrencyContractedUnitPrice MAY be null in all other cases.
* When PricingCurrencyContractedUnitPrice is not null, PricingCurrencyContractedUnitPrice [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * PricingCurrencyContractedUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyContractedUnitPrice MUST be denominated in the PricingCurrency.

@@ -40,14 +39,15 @@ The agreed-upon unit price for a single Pricing Unit of the associated SKU, incl

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

