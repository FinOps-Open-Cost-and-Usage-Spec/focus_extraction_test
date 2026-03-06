## Diff

diff --git a/specification/datasets/cost_and_usage/columns/subaccountid.md b/specification/datasets/cost_and_usage/columns/subaccountid.md
index c66aed3c..66f9b123 100644
--- a/specification/datasets/cost_and_usage/columns/subaccountid.md
+++ b/specification/datasets/cost_and_usage/columns/subaccountid.md
@@ -4,16 +4,15 @@ A Sub Account ID is a service-provider-assigned identifier assigned to a [*sub a

## Requirements

SubAccountId [-adheres-]{+MUST adhere+} to the following requirements:

[-* SubAccountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports a *sub account* construct.-]
* SubAccountId MUST be of type String.
* SubAccountId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* SubAccountId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SubAccountId MUST be null when a [*charge*](#glossary:charge) is not related to a *sub account*.
  * SubAccountId MUST NOT be null when a *charge* is related to a *sub account*.

See [Appendix: Grouping constructs for resources or [-services](#groupingconstructsforresourcesorservices)-]{+services](#appendix.groupingconstructsforresourcesorservices)+} for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

@@ -29,13 +28,14 @@ An ID assigned to a grouping of [*resources*](#glossary:resource) or [*services*

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

