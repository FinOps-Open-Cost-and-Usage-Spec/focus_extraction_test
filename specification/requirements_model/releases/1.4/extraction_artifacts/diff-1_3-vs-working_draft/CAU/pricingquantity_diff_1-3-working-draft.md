## Diff

diff --git a/specification/datasets/cost_and_usage/columns/pricingquantity.md b/specification/datasets/cost_and_usage/columns/pricingquantity.md
index 60156ec3..6f24e1ab 100644
--- a/specification/datasets/cost_and_usage/columns/pricingquantity.md
+++ b/specification/datasets/cost_and_usage/columns/pricingquantity.md
@@ -1,21 +1,20 @@
# Pricing Quantity

The Pricing Quantity represents the volume of a given [*SKU*](#glossary:sku) associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing [-Unit](#pricingunit).-]{+Unit](#datasets.costandusage.pricingunit).+} Distinct from [Consumed [-Quantity](#consumedquantity)-]{+Quantity](#datasets.costandusage.consumedquantity)+} (complementary to [Consumed [-Unit](#consumedunit)),-]{+Unit](#datasets.costandusage.consumedunit)),+} it focuses on pricing and cost, not *resource* and *service* consumption.

## Requirements

PricingQuantity [-adheres-]{+MUST adhere+} to the following requirements:

[-* PricingQuantity MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* PricingQuantity {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * PricingQuantity MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * PricingQuantity MUST be null when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Tax".
  * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
  * PricingQuantity MAY be null in all other cases.
* PricingQuantity MUST be a valid decimal value when not null.
* Cost metric (e.g., [-[ContractedCost](#contractedcost))-]{+[ContractedCost](#datasets.costandusage.contractedcost))+} MUST equal the product of the corresponding unit price (e.g., [-[ContractedUnitPrice](#contractedunitprice))-]{+[ContractedUnitPrice](#datasets.costandusage.contractedunitprice))+} and PricingQuantity when the unit price is not null and PricingQuantity is not null.

## Column ID

@@ -35,14 +34,15 @@ The volume of a given *SKU* associated with a *resource* or *service* used or pu

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:--------------------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric [-Format](#numericformat)-]{+Format](#attributes.numericformat)+}          |
| Number Range    | Any valid decimal value                              |

## Introduced (version)

