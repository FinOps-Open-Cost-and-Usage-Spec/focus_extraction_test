## Diff

diff --git a/specification/datasets/cost_and_usage/columns/billingaccounttype.md b/specification/datasets/cost_and_usage/columns/billingaccounttype.md
index 05676cda..d2f09bfa 100644
--- a/specification/datasets/cost_and_usage/columns/billingaccounttype.md
+++ b/specification/datasets/cost_and_usage/columns/billingaccounttype.md
@@ -4,13 +4,12 @@ Billing Account Type is an invoice-issuer-assigned name to identify the type of

## Requirements

BillingAccountType [-adheres-]{+MUST adhere+} to the following requirements:

[-* BillingAccountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the invoice issuer supports more than one possible BillingAccountType value.-]
* BillingAccountType MUST be of type String.
* BillingAccountType MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* BillingAccountType {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * BillingAccountType MUST be null when [-[BillingAccountId](#billingaccountid)-]{+[BillingAccountId](#datasets.costandusage.billingaccountid)+} is null.
  * BillingAccountType MUST NOT be null when BillingAccountId is not null.
* BillingAccountType MUST be a consistent, readable display value.

@@ -28,13 +27,14 @@ An invoice-issuer-assigned name to identify the type of *billing account*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | [-:----------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

