## Diff

diff --git a/specification/datasets/cost_and_usage/columns/chargeclass.md b/specification/datasets/cost_and_usage/columns/chargeclass.md
index cdaec2b5..de2bdbaf 100644
--- a/specification/datasets/cost_and_usage/columns/chargeclass.md
+++ b/specification/datasets/cost_and_usage/columns/chargeclass.md
@@ -4,11 +4,10 @@ Charge Class indicates whether the [*row*](#glossary:row) represents a correctio

## Requirements

ChargeClass [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargeClass MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ChargeClass MUST be of type String.
* ChargeClass {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ChargeClass MUST be null when the *row* does not represent a correction or when it represents a correction within the current *billing period*.
  * ChargeClass MUST NOT be null when the *row* represents a correction to a previously invoiced *billing period*.
* ChargeClass MUST be "Correction" when ChargeClass is not null.
@@ -27,13 +26,14 @@ Indicates whether the *row* represents a correction to a previously invoiced *bi

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | [-:--------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

Allowed values:

@@ -44,4 +44,3 @@ Allowed values:
## Introduced (version)

1.0
[--]
