## Diff

diff --git a/specification/datasets/cost_and_usage/columns/consumedquantity.md b/specification/datasets/cost_and_usage/columns/consumedquantity.md
index f0f1e07b..24c8a3f4 100644
--- a/specification/datasets/cost_and_usage/columns/consumedquantity.md
+++ b/specification/datasets/cost_and_usage/columns/consumedquantity.md
@@ -1,19 +1,18 @@
# Consumed Quantity

The Consumed Quantity represents the volume of a metered SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used, based on the [Consumed [-Unit](#consumedunit).-]{+Unit](#datasets.costandusage.consumedunit).+} Consumed Quantity is often derived at a finer granularity or over a different time interval when compared to the [Pricing [-Quantity](#pricingquantity)-]{+Quantity](#datasets.costandusage.pricingquantity)+} (complementary to [Pricing [-Unit](#pricingunit))-]{+Unit](#datasets.costandusage.pricingunit))+} and focuses on *resource* and *service* consumption, not pricing and cost.

## Requirements

ConsumedQuantity [-adheres-]{+MUST adhere+} to the following requirements:

[-* ConsumedQuantity MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports the measurement of usage.-]
* ConsumedQuantity MUST be of type Decimal.
* ConsumedQuantity MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* ConsumedQuantity {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ConsumedQuantity MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * ConsumedQuantity MUST be null when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is not "Usage", or when ChargeCategory is "Usage" and [-[CommitmentDiscountStatus](#commitmentdiscountstatus)-]{+[CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus)+} is "Unused".
  * When ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedQuantity [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
    * ConsumedQuantity MUST NOT be null when [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
    * ConsumedQuantity MAY be null when ChargeClass is "Correction".
* ConsumedQuantity MUST be a valid decimal value when not null.

@@ -31,14 +30,15 @@ The volume of a metered SKU associated with a *resource* or *service* used, base

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:--------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric [-Format](#numericformat)-]{+Format](#attributes.numericformat)+}          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

