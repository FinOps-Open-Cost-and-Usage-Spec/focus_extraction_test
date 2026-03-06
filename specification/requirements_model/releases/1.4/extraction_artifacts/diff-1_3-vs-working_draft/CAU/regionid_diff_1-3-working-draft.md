## Diff

diff --git a/specification/datasets/cost_and_usage/columns/regionid.md b/specification/datasets/cost_and_usage/columns/regionid.md
index bca40600..0e4df921 100644
--- a/specification/datasets/cost_and_usage/columns/regionid.md
+++ b/specification/datasets/cost_and_usage/columns/regionid.md
@@ -4,12 +4,11 @@ A Region ID is a host-provider-assigned identifier for an isolated geographic ar

## Requirements

RegionId [-adheres-]{+MUST adhere+} to the following requirements:

[-* RegionId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within a region.-]
* RegionId MUST be of type String.
* RegionId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* RegionId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region.
  * RegionId MAY be null when a *resource* or *service* is not operated in or managed from a distinct region.

@@ -27,13 +26,14 @@ Host-provider-assigned identifier for an isolated geographic area where a *resou

## Content constraints

| Constraint      | Value                                                |
[-|-----------------|-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

