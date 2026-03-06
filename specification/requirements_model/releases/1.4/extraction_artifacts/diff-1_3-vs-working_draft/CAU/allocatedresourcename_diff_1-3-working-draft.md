## Diff

diff --git a/specification/datasets/cost_and_usage/columns/allocatedresourcename.md b/specification/datasets/cost_and_usage/columns/allocatedresourcename.md
index 2b4aa156..a592cdc4 100644
--- a/specification/datasets/cost_and_usage/columns/allocatedresourcename.md
+++ b/specification/datasets/cost_and_usage/columns/allocatedresourcename.md
@@ -1,16 +1,15 @@
# Allocated Resource Name

The Allocated Resource Name is a display name which cost is being allocated to in a [Data Generator-Calculated Split Cost [-Allocation](#datagenerator-calculatedsplitcostallocationhandling).-]{+Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).+} The Allocated Resource Name is used to understand what the cost is being allocated to in [*charges*](#glossary:charge) where the service provider is allocating costs to something other than the charge's [-[ResourceID](#ResourceId),-]{+[ResourceID](#datasets.costandusage.resourceid),+} as is the case for [allocated charges](#glossary:allocated-charge).

## Requirements

AllocatedResourceName [-adheres-]{+MUST adhere+} to the following requirements:

[-* AllocatedResourceName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports data generator-calculated split cost allocation.-]
* AllocatedResourceName MUST be of type String.
* AllocatedResourceName MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* AllocatedResourceName {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedResourceName MUST be null when [-[AllocatedResourceId](#AllocatedResourceId)-]{+[AllocatedResourceId](#datasets.costandusage.allocatedresourceid)+} is null.
  * AllocatedResourceName MUST NOT be null when AllocatedResourceId is not null.
* AllocatedResourceName MAY duplicate AllocatedResourceId when a separate display name is not applicable.

@@ -28,13 +27,14 @@ The display name of the object to which cost is allocated in data generator-calc

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

