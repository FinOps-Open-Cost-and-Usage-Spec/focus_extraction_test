## Diff

diff --git a/specification/datasets/cost_and_usage/columns/allocatedmethodid.md b/specification/datasets/cost_and_usage/columns/allocatedmethodid.md
index a758081e..c10131e7 100644
--- a/specification/datasets/cost_and_usage/columns/allocatedmethodid.md
+++ b/specification/datasets/cost_and_usage/columns/allocatedmethodid.md
@@ -1,15 +1,14 @@
# Allocated Method ID

Allocated Method ID is the unique identifier for the [allocated method](#glossary:allocated-method) defined by the service provider which was used for the [Data Generator-Calculated Split Cost [-Allocation](#datagenerator-calculatedsplitcostallocationhandling).-]{+Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).+} This unique identifier can be used to find how the [allocated charge](#glossary:allocated-charge) was calculated in the provider's documentation.

## Requirements

AllocatedMethodId [-adheres-]{+MUST adhere+} to the following requirements:

[-* AllocatedMethodId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the data generator supports data generator-calculated split cost allocation.-]
* AllocatedMethodId MUST be of type String.
* AllocatedMethodId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* AllocatedMethodId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedMethodId MUST be null when a [*charge*](#glossary:charge) is not related to a data generator-calculated split cost allocation.
  * AllocatedMethodId MUST NOT be null when a *charge* is related to a data generator-calculated split cost allocation.
* Data generator documentation of a split cost allocation method MUST make reference to a single AllocatedMethodId value.
@@ -28,13 +27,14 @@ A unique identifier defining the method of data generator-calculated split cost

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

