## Diff

diff --git a/specification/datasets/cost_and_usage/columns/subaccounttype.md b/specification/datasets/cost_and_usage/columns/subaccounttype.md
index 73139339..40117b9a 100644
--- a/specification/datasets/cost_and_usage/columns/subaccounttype.md
+++ b/specification/datasets/cost_and_usage/columns/subaccounttype.md
@@ -4,13 +4,12 @@ Sub Account Type is a service-provider-assigned name to identify the type of [*s

## Requirements

SubAccountType [-adheres-]{+MUST adhere+} to the following requirements:

[-* SubAccountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports more than one possible SubAccountType value.-]
* SubAccountType MUST be of type String.
* SubAccountType MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* SubAccountType {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SubAccountType MUST be null when [-[SubAccountId](#subaccountid)-]{+[SubAccountId](#datasets.costandusage.subaccountid)+} is null.
  * SubAccountType MUST NOT be null when SubAccountId is not null.
* SubAccountType MUST be a consistent, readable display value.

@@ -28,13 +27,14 @@ A service-provider-assigned name to identify the type of *sub account*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | [-:----------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

