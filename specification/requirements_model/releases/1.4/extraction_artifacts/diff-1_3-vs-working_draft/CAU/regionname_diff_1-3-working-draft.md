## Diff

diff --git a/specification/datasets/cost_and_usage/columns/regionname.md b/specification/datasets/cost_and_usage/columns/regionname.md
index 06333c9d..c93053fb 100644
--- a/specification/datasets/cost_and_usage/columns/regionname.md
+++ b/specification/datasets/cost_and_usage/columns/regionname.md
@@ -4,13 +4,12 @@ Region Name is a host-provider-assigned display name for an isolated geographic

## Requirements

RegionName [-adheres-]{+MUST adhere+} to the following requirements:

[-* RegionName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within a region.-]
* RegionName MUST be of type String.
* RegionName MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* RegionName {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * RegionName MUST be null when [-[RegionId](#regionid)-]{+[RegionId](#datasets.costandusage.regionid)+} is null.
  * RegionName MUST NOT be null when RegionId is not null.

## Column ID
@@ -27,13 +26,14 @@ The name of an isolated geographic area where a *resource* is provisioned or a *

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

