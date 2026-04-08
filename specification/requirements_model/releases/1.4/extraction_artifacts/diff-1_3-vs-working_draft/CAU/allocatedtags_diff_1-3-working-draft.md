## Diff

diff --git a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_3z87uzkt_from.md b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_3i17euvm_to.md
index c472126a..7bd83bfa 100644
--- a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_3z87uzkt_from.md
+++ b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_3i17euvm_to.md
@@ -4,29 +4,28 @@ The Allocated Tags column represents the set of *tags* assigned to *tag sources*

## Requirements

AllocatedTags [-adheres-]{+MUST adhere+} to the following requirements:

[-* AllocatedTags MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports Data Generator-Calculated Split Cost Allocation.-]
* AllocatedTags MUST conform to KeyValueFormat requirements.
* AllocatedTags {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedTags MUST be null when a *charge* is not related to a data generator-calculated split cost allocation.
  * AllocatedTags MAY be null in all other cases.
* When AllocatedTags is not null, AllocatedTags [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * AllocatedTags MUST NOT include resource tags already present in Tags.
  * AllocatedTags MUST include all applicable user-defined and data generator-defined tags for the AllocatedResourceId.
  * Tag keys that do not support corresponding values MUST have a corresponding true (boolean) value set.
  * Data generator MUST NOT alter tag values unless applying true (boolean) to valueless tags.
* Data generator-defined tags {+MUST+} adhere to the following[-additional-] requirements:
  * Data generator-defined tag keys MUST be prefixed with a predetermined, data generator-specified tag key prefix that is unique to each corresponding provider-specified [-tag scheme.-]{+*tag scheme*.+}
  * Data generator SHOULD publish all data generator-specified tag key prefixes within their respective documentation.
* User-defined tags {+MUST+} adhere to the following[-additional-] requirements:
  * Data generator MUST prefix all user-defined [-tags scheme-]{+*tag schemes*+} with a predetermined, data generator-specified tag key prefix that is unique to each corresponding user-defined [-tag scheme-]{+*tag scheme*+} when the data generator has more than one user-defined [-tag scheme.-]{+*tag scheme*.+}

## Data Generator-Defined vs. User-Defined Tags

This example illustrates various tags produced from multiple user-defined and data generator-defined [-tag schemes.-]{+*tag schemes*.+} The first two tags illustrate examples from two different, user-defined [-tag schemes.-]{+*tag schemes*.+} The second tag is produced from a valueless, user-defined [-tag scheme,-]{+*tag scheme*,+} so the data generator also applies `true` as its default value.

The last two tags illustrate examples from two different, data generator-defined [-tag schemes.-]{+*tag schemes*.+}

```json
    {
@@ -51,13 +50,14 @@ A set of tags assigned to tag sources that are applicable to *allocated charges*

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | Cost and Usage             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | JSON                                                 |
| Value format    | Key-Value Format      |

## Introduced (version)

