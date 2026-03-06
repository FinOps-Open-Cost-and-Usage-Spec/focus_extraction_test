## Diff

diff --git a/specification/datasets/cost_and_usage/columns/billingperiodstart.md b/specification/datasets/cost_and_usage/columns/billingperiodstart.md
index 68fabd7a..c8b8cef9 100644
--- a/specification/datasets/cost_and_usage/columns/billingperiodstart.md
+++ b/specification/datasets/cost_and_usage/columns/billingperiodstart.md
@@ -1,14 +1,13 @@
# Billing Period Start

Billing Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound) of a [*billing period*](#glossary:billing-period). For example, a time period where Billing Period Start is '2024-01-01T00:00:00Z' and [Billing Period [-End](#billingperiodend)-]{+End](#datasets.costandusage.billingperiodend)+} is '2024-02-01T00:00:00Z' includes [*charges*](#glossary:charge) for January since Billing Period Start represents the *inclusive start bound*, but does not include *charges* for February since BillingPeriodEnd represents the [*exclusive end bound*](#glossary:exclusiveendbound).

## Requirements

BillingPeriodStart [-adheres-]{+MUST adhere+} to the following requirements:

[-* BillingPeriodStart MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* BillingPeriodStart MUST be of type Date/Time.
* BillingPeriodStart MUST conform to [-[DateTimeFormat](#date/timeformat)-]{+[DateTimeFormat](#attributes.date/timeformat)+} requirements.
* BillingPeriodStart MUST NOT be null.
* BillingPeriodStart MUST be the *inclusive start bound* of the *billing period*.

@@ -26,13 +25,14 @@ The *inclusive start bound* of a *billing period*.

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

