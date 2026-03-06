## Diff

diff --git a/specification/datasets/cost_and_usage/columns/chargecategory.md b/specification/datasets/cost_and_usage/columns/chargecategory.md
index df004ec4..7c89747f 100644
--- a/specification/datasets/cost_and_usage/columns/chargecategory.md
+++ b/specification/datasets/cost_and_usage/columns/chargecategory.md
@@ -4,9 +4,8 @@ Charge Category represents the highest-level classification of a [*charge*](#glo

## Requirements

ChargeCategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargeCategory MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ChargeCategory MUST be of type String.
* ChargeCategory MUST NOT be null.
* ChargeCategory MUST be one of the allowed values.
@@ -25,13 +24,14 @@ Represents the highest-level classification of a *charge* based on the nature of

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | [-:--------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

Allowed values:

