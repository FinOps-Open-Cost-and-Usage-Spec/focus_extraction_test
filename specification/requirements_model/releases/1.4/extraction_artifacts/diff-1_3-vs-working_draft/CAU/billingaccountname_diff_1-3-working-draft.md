## Diff

diff --git a/specification/datasets/cost_and_usage/columns/billingaccountname.md b/specification/datasets/cost_and_usage/columns/billingaccountname.md
index 19817c76..b717f89f 100644
--- a/specification/datasets/cost_and_usage/columns/billingaccountname.md
+++ b/specification/datasets/cost_and_usage/columns/billingaccountname.md
@@ -4,14 +4,13 @@ A Billing Account Name is a display name assigned to a [*billing account*](#glos

## Requirements

BillingAccountName [-adheres-]{+MUST adhere+} to the following requirements:

[-* BillingAccountName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* BillingAccountName MUST be of type String.
* BillingAccountName MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* BillingAccountName MUST NOT be null when the invoice issuer supports assigning a display name for the *billing account*.

See [Appendix: Grouping constructs for resources or [-services](#groupingconstructsforresourcesorservices)-]{+services](#appendix.groupingconstructsforresourcesorservices)+} for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

@@ -27,13 +26,14 @@ The display name assigned to a *billing account*.

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

