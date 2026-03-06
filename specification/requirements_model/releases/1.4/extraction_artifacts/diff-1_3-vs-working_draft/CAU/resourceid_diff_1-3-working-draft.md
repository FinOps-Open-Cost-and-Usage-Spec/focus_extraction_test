## Diff

diff --git a/specification/datasets/cost_and_usage/columns/resourceid.md b/specification/datasets/cost_and_usage/columns/resourceid.md
index 57a92859..1896ebcf 100644
--- a/specification/datasets/cost_and_usage/columns/resourceid.md
+++ b/specification/datasets/cost_and_usage/columns/resourceid.md
@@ -4,15 +4,14 @@ A Resource ID is an identifier assigned to a [*resource*](#glossary:resource) by

## Requirements

ResourceId [-adheres-]{+MUST adhere+} to the following requirements:

[-* ResourceId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned *resources*.-]
* ResourceId MUST be of type String.
* ResourceId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ResourceId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ResourceId MUST be null when a [*charge*](#glossary:charge) is not related to a *resource*.
  * ResourceId MUST NOT be null when a *charge* is related to a *resource*.
* When ResourceId is not null, ResourceId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ResourceId MUST be a unique identifier within the service provider.
  * ResourceId SHOULD be a fully-qualified identifier.

@@ -30,13 +29,14 @@ Identifier assigned to a *resource* by the service provider.

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

