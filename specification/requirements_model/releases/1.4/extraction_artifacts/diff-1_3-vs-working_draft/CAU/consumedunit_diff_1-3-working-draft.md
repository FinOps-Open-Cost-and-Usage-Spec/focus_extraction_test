## Diff

diff --git a/specification/datasets/cost_and_usage/columns/consumedunit.md b/specification/datasets/cost_and_usage/columns/consumedunit.md
index 6b00d524..61c6c7c0 100644
--- a/specification/datasets/cost_and_usage/columns/consumedunit.md
+++ b/specification/datasets/cost_and_usage/columns/consumedunit.md
@@ -1,16 +1,15 @@
# Consumed Unit

The Consumed Unit represents a service-provider-specified measurement unit indicating how a service provider measures usage of a metered SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service). Consumed Unit complements the [Consumed [-Quantity](#consumedquantity)-]{+Quantity](#datasets.costandusage.consumedquantity)+} metric. It is often listed at a finer granularity or over a different time interval when compared to [Pricing [-Unit](#pricingunit)-]{+Unit](#datasets.costandusage.pricingunit)+} (complementary to [Pricing [-Quantity](#pricingquantity)),-]{+Quantity](#datasets.costandusage.pricingquantity)),+} and focuses on *resource* and *service* consumption, not pricing and cost.

## Requirements

ConsumedUnit [-adheres-]{+MUST adhere+} to the following requirements:

[-* ConsumedUnit MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports the measurement of usage.-]
* ConsumedUnit MUST be of type String.
* ConsumedUnit MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ConsumedUnit SHOULD conform to [-[UnitFormat](#unitformat)-]{+[UnitFormat](#attributes.unitformat)+} requirements.
* ConsumedUnit {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ConsumedUnit MUST be null when ConsumedQuantity is null.
  * ConsumedUnit MUST NOT be null when ConsumedQuantity is not null.

@@ -28,13 +27,14 @@ Service-provider-specified measurement unit indicating how a service provider me

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | [Unit [-Format](#unitformat)-]{+Format](#attributes.unitformat)+} recommended    |

## Introduced (version)

