## Diff

diff --git a/specification/datasets/cost_and_usage/columns/skumeter.md b/specification/datasets/cost_and_usage/columns/skumeter.md
index adf12e33..5e4a184f 100644
--- a/specification/datasets/cost_and_usage/columns/skumeter.md
+++ b/specification/datasets/cost_and_usage/columns/skumeter.md
@@ -6,13 +6,12 @@ Service providers often have billing models in which multiple SKUs exist for a g

## Requirements

SkuMeter [-adheres-]{+MUST adhere+} to the following requirements:

[-* SkuMeter MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.-]
* SkuMeter MUST be of type String.
* SkuMeter MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* SkuMeter {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SkuMeter MUST be null when [-[SkuId](#skuid)-]{+[SkuId](#datasets.costandusage.skuid)+} is null.
  * SkuMeter SHOULD NOT be null when SkuId is not null.
* SkuMeter SHOULD remain consistent over time for a given SkuId.

@@ -34,13 +33,14 @@ Describes the functionality being metered or measured by a particular SKU in a *

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

