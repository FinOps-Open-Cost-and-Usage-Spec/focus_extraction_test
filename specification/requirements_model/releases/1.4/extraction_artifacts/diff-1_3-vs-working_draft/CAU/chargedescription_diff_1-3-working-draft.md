## Diff

diff --git a/specification/datasets/cost_and_usage/columns/chargedescription.md b/specification/datasets/cost_and_usage/columns/chargedescription.md
index d8e0ffd6..cfcfde69 100644
--- a/specification/datasets/cost_and_usage/columns/chargedescription.md
+++ b/specification/datasets/cost_and_usage/columns/chargedescription.md
@@ -4,11 +4,10 @@ A Charge Description provides a high-level context of a [*row*](#glossary:row) w

## Requirements

ChargeDescription [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargeDescription MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ChargeDescription MUST be of type String.
* ChargeDescription MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ChargeDescription SHOULD NOT be null.
* ChargeDescription maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

@@ -26,13 +25,14 @@ Self-contained summary of the *charge's* purpose and price.

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

