## Diff

diff --git a/specification/datasets/cost_and_usage/columns/billingperiodend.md b/specification/datasets/cost_and_usage/columns/billingperiodend.md
index fef90c9d..99b19324 100644
--- a/specification/datasets/cost_and_usage/columns/billingperiodend.md
+++ b/specification/datasets/cost_and_usage/columns/billingperiodend.md
@@ -1,14 +1,13 @@
# Billing Period End

Billing Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound) of a [*billing period*](#glossary:billing-period). For example, a time period where [Billing Period [-Start](#billingperiodstart)-]{+Start](#datasets.costandusage.billingperiodstart)+} is '2024-01-01T00:00:00Z' and Billing Period End is '2024-02-01T00:00:00Z' includes [*charges*](#glossary:charge) for January since Billing Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound), but does not include *charges* for February since Billing Period End represents the *exclusive end bound*.

## Requirements

BillingPeriodEnd [-adheres-]{+MUST adhere+} to the following requirements:

[-* BillingPeriodEnd MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* BillingPeriodEnd MUST be of type Date/Time.
* BillingPeriodEnd MUST conform to [-[DateTimeFormat](#date/timeformat)-]{+[DateTimeFormat](#attributes.date/timeformat)+} requirements.
* BillingPeriodEnd MUST NOT be null.
* BillingPeriodEnd MUST be the *exclusive end bound* of the *billing period*.

@@ -26,13 +25,14 @@ The *exclusive end bound* of a *billing period*.

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:-------------------------------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Date/Time                                            |
| Value format    | [Date/Time [-Format](#date/timeformat)-]{+Format](#attributes.date/timeformat)+}      |

## Introduced (version)

