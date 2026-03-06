## Diff

diff --git a/specification/datasets/cost_and_usage/columns/pricingunit.md b/specification/datasets/cost_and_usage/columns/pricingunit.md
index 3bc0f81e..7a6b7fc5 100644
--- a/specification/datasets/cost_and_usage/columns/pricingunit.md
+++ b/specification/datasets/cost_and_usage/columns/pricingunit.md
@@ -1,19 +1,18 @@
# Pricing Unit

The Pricing Unit represents a service-provider-specified measurement unit for determining unit prices, indicating how the service provider rates measured usage and purchase quantities after applying pricing rules like [*block pricing*](#glossary:block-pricing). Common examples include the number of hours for compute appliance runtime (e.g., `Hours`), gigabyte-hours for a storage appliance (e.g., `GB-Hours`), or an accumulated count of requests for a network appliance or API service (e.g., `1000 Requests`). Pricing Unit complements the [Pricing [-Quantity](#pricingquantity)-]{+Quantity](#datasets.costandusage.pricingquantity)+} metric. Distinct from the [Consumed [-Unit](#consumedunit),-]{+Unit](#datasets.costandusage.consumedunit),+} it focuses on pricing and cost, not [*resource*](#glossary:resource) and [*service*](#glossary:service) consumption, often at a coarser granularity.

## Requirements

PricingUnit [-adheres-]{+MUST adhere+} to the following requirements:

[-* PricingUnit MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* PricingUnit MUST be of type String.
* PricingUnit MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* PricingUnit SHOULD conform to [-[UnitFormat](#unitformat)-]{+[UnitFormat](#attributes.unitformat)+} requirements.
* PricingUnit {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * PricingUnit MUST be null when PricingQuantity is null.
  * PricingUnit MUST NOT be null when PricingQuantity is not null.
* When PricingUnit is not null, PricingUnit [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in service-provider-published [*price list*](#glossary:price-list).
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in invoice, when the invoice includes a pricing measurement unit.

@@ -31,13 +30,14 @@ Service-provider-specified measurement unit for determining unit prices, indicat

## Content constraints

| Constraint      | Value                                                |
[-|-----------------|-------------------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | [Unit [-Format](#unitformat)-]{+Format](#attributes.unitformat)+}                |

## Introduced (version)

