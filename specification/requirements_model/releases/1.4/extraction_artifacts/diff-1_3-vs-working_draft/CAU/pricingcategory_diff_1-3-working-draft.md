## Diff

diff --git a/specification/datasets/cost_and_usage/columns/pricingcategory.md b/specification/datasets/cost_and_usage/columns/pricingcategory.md
index 05580461..81170fd0 100644
--- a/specification/datasets/cost_and_usage/columns/pricingcategory.md
+++ b/specification/datasets/cost_and_usage/columns/pricingcategory.md
@@ -4,16 +4,15 @@ Pricing Category describes the pricing model used for a [*charge*](#glossary:cha

## Requirements

PricingCategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* PricingCategory MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports more than one pricing category across all [*SKUs*](#glossary:sku).-]
* PricingCategory MUST be of type String.
* PricingCategory {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * PricingCategory MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * PricingCategory MUST be null when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Tax".
  * PricingCategory MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
  * PricingCategory MAY be null in all other cases.
* When PricingCategory is not null, PricingCategory [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * PricingCategory MUST be one of the allowed values.
  * PricingCategory MUST be "Standard" when pricing is predetermined at the agreed upon rate for the [billing account](#glossary:billing-account).
  * PricingCategory MUST be "Committed" when the *charge* is subject to an existing *commitment discount* and is not the purchase of the *commitment discount*.
@@ -34,13 +33,14 @@ Describes the pricing model used for a *charge* at the time of use or purchase.

## Content constraints

| Constraint      | Value                                                |
| :-------------- | [-:--------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

Allowed values:

