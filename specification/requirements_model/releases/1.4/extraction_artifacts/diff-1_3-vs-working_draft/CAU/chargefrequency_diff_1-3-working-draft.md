## Diff

diff --git a/specification/datasets/cost_and_usage/columns/chargefrequency.md b/specification/datasets/cost_and_usage/columns/chargefrequency.md
index 70b5833c..c9451a56 100644
--- a/specification/datasets/cost_and_usage/columns/chargefrequency.md
+++ b/specification/datasets/cost_and_usage/columns/chargefrequency.md
@@ -4,13 +4,12 @@ Charge Frequency indicates how often a [*charge*](#glossary:charge) will occur.

## Requirements

ChargeFrequency [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargeFrequency is RECOMMENDED to be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ChargeFrequency MUST be of type String.
* ChargeFrequency MUST NOT be null.
* ChargeFrequency MUST be one of the allowed values.
* ChargeFrequency MUST NOT be "Usage-Based" when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Purchase".

## Column ID

@@ -26,13 +25,14 @@ Indicates how often a *charge* will occur.

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:---------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Recommended                                          |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

Allowed values:

