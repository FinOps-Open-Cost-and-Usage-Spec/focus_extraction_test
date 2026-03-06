## Diff

diff --git a/specification/datasets/cost_and_usage/columns/chargeperiodend.md b/specification/datasets/cost_and_usage/columns/chargeperiodend.md
index 54da95d7..849e62b6 100644
--- a/specification/datasets/cost_and_usage/columns/chargeperiodend.md
+++ b/specification/datasets/cost_and_usage/columns/chargeperiodend.md
@@ -1,14 +1,13 @@
# Charge Period End

Charge Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound) of a [*charge period*](#glossary:chargeperiod). For example, a time period where [Charge Period [-Start](#chargeperiodstart)-]{+Start](#datasets.costandusage.chargeperiodstart)+} is '2024-01-01T00:00:00Z' and Charge Period End is '2024-01-02T00:00:00Z' includes [*charges*](#glossary:charge) for January 1 since Charge Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound), but does not include *charges* for January 2 since Charge Period End represents the *exclusive end bound*.

## Requirements

ChargePeriodEnd [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargePeriodEnd MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ChargePeriodEnd MUST be of type Date/Time.
* ChargePeriodEnd MUST conform to [-[DateTimeFormat](#date/timeformat)-]{+[DateTimeFormat](#attributes.date/timeformat)+} requirements.
* ChargePeriodEnd MUST NOT be null.
* ChargePeriodEnd MUST be the *exclusive end bound* of the effective period of the *charge*.

@@ -26,13 +25,14 @@ The *exclusive end bound* of a *charge period*.

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-------------------------------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Date/Time                                            |
| Value format    | [Date/Time [-Format](#date/timeformat)-]{+Format](#attributes.date/timeformat)+}      |

## Introduced (version)

