## Diff

diff --git a/specification/datasets/cost_and_usage/columns/allocatedtags.md b/specification/datasets/cost_and_usage/columns/allocatedtags.md
index 11a4e015..f1d74070 100644
--- a/specification/datasets/cost_and_usage/columns/allocatedtags.md
+++ b/specification/datasets/cost_and_usage/columns/allocatedtags.md
@@ -4,22 +4,21 @@ The Allocated Tags column represents the set of [*tags*](#glossary:tag) assigned

## Requirements

AllocatedTags [-adheres-]{+MUST adhere+} to the following requirements:

* AllocatedTags MUST[-be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).-]
[-* AllocatedTags MUST-] conform to [-[KeyValueFormat](#key-valueformat)-]{+[KeyValueFormat](#attributes.key-valueformat)+} requirements.
* AllocatedTags {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedTags MUST be null when a *charge* is not related to a data generator-calculated split cost allocation.
  * AllocatedTags MAY be null in all other cases.
* When AllocatedTags is not null, AllocatedTags [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * AllocatedTags MUST NOT include resource tags already present in [-[Tags](#tags).-]{+[Tags](#datasets.costandusage.tags).+}
  * AllocatedTags MUST include all applicable user-defined and data generator-defined tags for the [-[AllocatedResourceId](#AllocatedResourceId).-]{+[AllocatedResourceId](#datasets.costandusage.allocatedresourceid).+}
  * Tag keys that do not support corresponding values MUST have a corresponding true (boolean) value set.
  * Data generator MUST NOT alter tag values unless applying true (boolean) to valueless tags.
* Data generator-defined tags {+MUST+} adhere to the following[-additional-] requirements:
  * Data generator-defined tag keys MUST be prefixed with a predetermined, data generator-specified tag key prefix that is unique to each corresponding provider-specified tag scheme.
  * Data generator SHOULD publish all data generator-specified tag key prefixes within their respective documentation.
* User-defined tags {+MUST+} adhere to the following[-additional-] requirements:
  * Data generator MUST prefix all user-defined tags scheme with a predetermined, data generator-specified tag key prefix that is unique to each corresponding user-defined tag scheme when the data generator has more than one user-defined tag scheme.

## Data Generator-Defined vs. User-Defined Tags
@@ -51,13 +50,14 @@ A set of tags assigned to tag sources that are applicable to *allocated charges*

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | JSON                                                 |
| Value format    | [Key-Value [-Format](#key-valueformat)-]{+Format](#attributes.key-valueformat)+}      |

## Introduced (version)

