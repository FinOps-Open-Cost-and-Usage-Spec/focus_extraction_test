## Diff

diff --git a/specification/datasets/cost_and_usage/columns/subaccountname.md b/specification/datasets/cost_and_usage/columns/subaccountname.md
index ffbfd6a1..bf145266 100644
--- a/specification/datasets/cost_and_usage/columns/subaccountname.md
+++ b/specification/datasets/cost_and_usage/columns/subaccountname.md
@@ -1,42 +1,42 @@
# Sub Account Name

A Sub Account Name is a display name assigned to a [*sub account*](#glossary:sub-account). Sub account Name is commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies.

## Requirements

SubAccountName [-adheres-]{+MUST adhere+} to the following requirements:

* SubAccountName MUST be[-present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports a *sub account* construct.-]
[-* SubAccountName MUST be-] of type String.
* SubAccountName MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* SubAccountName {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SubAccountName MUST be null when [-[SubAccountId](#subaccountid)-]{+[SubAccountId](#datasets.costandusage.subaccountid)+} is null.
  * SubAccountName MUST NOT be null when SubAccountId is not null.

See [Appendix: Grouping constructs for resources or [-services](#groupingconstructsforresourcesorservices)-]{+services](#appendix.groupingconstructsforresourcesorservices)+} for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

SubAccountName

## Display Name

Sub Account Name

## Description

A name assigned to a grouping of [*resources*](#glossary:resource) or [*services*](#glossary:service), often used to manage access and/or cost.

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

0.5
