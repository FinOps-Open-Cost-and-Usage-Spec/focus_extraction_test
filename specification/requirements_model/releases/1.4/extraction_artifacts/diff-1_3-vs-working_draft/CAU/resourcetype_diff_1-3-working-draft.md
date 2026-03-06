## Diff

diff --git a/specification/datasets/cost_and_usage/columns/resourcetype.md b/specification/datasets/cost_and_usage/columns/resourcetype.md
index c6569578..a60d4f29 100644
--- a/specification/datasets/cost_and_usage/columns/resourcetype.md
+++ b/specification/datasets/cost_and_usage/columns/resourcetype.md
@@ -4,13 +4,12 @@ Resource Type describes the kind of [*resource*](#glossary:resource) the [*charg

## Requirements

ResourceType [-adheres-]{+MUST adhere+} to the following requirements:

[-* ResourceType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned *resources* and supports assigning types to *resources*.-]
* ResourceType MUST be of type String.
* ResourceType MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ResourceType {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ResourceType MUST be null when [-[ResourceId](#resourceid)-]{+[ResourceId](#datasets.costandusage.resourceid)+} is null.
  * ResourceType MUST NOT be null when ResourceId is not null.

## Column ID
@@ -27,13 +26,14 @@ The kind of *resource* the *charge* applies to.

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

