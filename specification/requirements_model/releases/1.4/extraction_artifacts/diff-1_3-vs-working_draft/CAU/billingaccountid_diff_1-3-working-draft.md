## Diff

diff --git a/specification/datasets/cost_and_usage/columns/billingaccountid.md b/specification/datasets/cost_and_usage/columns/billingaccountid.md
index 49aeb597..2e596556 100644
--- a/specification/datasets/cost_and_usage/columns/billingaccountid.md
+++ b/specification/datasets/cost_and_usage/columns/billingaccountid.md
@@ -4,16 +4,15 @@ A Billing Account ID is an invoice-issuer-assigned identifier for a [*billing ac

## Requirements

BillingAccountId [-adheres-]{+MUST adhere+} to the following requirements:

[-* BillingAccountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* BillingAccountId MUST be of type String.
* BillingAccountId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* BillingAccountId MUST NOT be null.
* BillingAccountId MUST be a unique identifier within an invoice issuer.
* BillingAccountId SHOULD be a fully-qualified identifier.

See [Appendix: Grouping constructs for resources or [-services](#groupingconstructsforresourcesorservices)-]{+services](#appendix.groupingconstructsforresourcesorservices)+} for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

@@ -29,13 +28,14 @@ The identifier assigned to a *billing account* by the invoice issuer.

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

