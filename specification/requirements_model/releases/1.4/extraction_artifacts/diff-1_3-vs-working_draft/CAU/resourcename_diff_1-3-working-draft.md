## Diff

diff --git a/specification/datasets/cost_and_usage/columns/resourcename.md b/specification/datasets/cost_and_usage/columns/resourcename.md
index a1a31ec4..767e2d6b 100644
--- a/specification/datasets/cost_and_usage/columns/resourcename.md
+++ b/specification/datasets/cost_and_usage/columns/resourcename.md
@@ -4,13 +4,12 @@ The Resource Name is a display name assigned to a [*resource*](#glossary:resourc

## Requirements

ResourceName [-adheres-]{+MUST adhere+} to the following requirements:

[-* ResourceName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned resources.-]
* ResourceName MUST be of type String.
* ResourceName MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ResourceName {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ResourceName MUST be null when [-[ResourceId](#resourceid)-]{+[ResourceId](#datasets.costandusage.resourceid)+} is null or when the *resource* does not have an assigned display name.
  * ResourceName MUST NOT be null when ResourceId is not null and the *resource* has an assigned display name.
* ResourceName MUST NOT duplicate ResourceId when the *resource* is not provisioned interactively or only has a system-generated ResourceId.

@@ -28,13 +27,14 @@ Display name assigned to a *resource*.

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

