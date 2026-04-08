## Diff

diff --git a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_e4twn7_6_from.md b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_7ttv9qlx_to.md
index 6a9a4fb0..a56ba205 100644
--- a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_e4twn7_6_from.md
+++ b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_7ttv9qlx_to.md
@@ -6,12 +6,11 @@ A tag becomes *finalized* when a single value is selected from a set of possible

## Requirements

Tags [-adheres-]{+MUST adhere+} to the following requirements:

[-* Tags MUST be present in a Cost and Usage *FOCUS dataset* when the data generator supports setting user or provider-defined tags.-]
* Tags MUST conform to KeyValueFormat requirements.
* Tags MAY be null.
* When Tags is not null, Tags [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * Tags MUST include all user-defined and provider-defined tags.
  * Tags MUST only include finalized tags.
  * Tags SHOULD include tag keys with corresponding non-null values for a given *resource*.
@@ -19,19 +18,19 @@ Tags adheres to the following requirements:
  * Tag keys that do not support corresponding values, MUST have a corresponding true (boolean) value set.
  * Data generator SHOULD publish tag finalization methods and semantics within their respective documentation.
  * Data generator MUST NOT alter tag values unless applying true (boolean) to valueless tags.
* Provider-defined tags {+MUST+} adhere to the following[-additional-] requirements:
  * Provider-defined tag keys MUST be prefixed with a predetermined, provider-specified tag key prefix that is unique to each corresponding provider-specified [-tag scheme.-]{+*tag scheme*.+}
  * Data generator SHOULD publish all provider-specified tag key prefixes within their respective documentation.
* User-defined tags {+MUST+} adhere to the following[-additional-] requirements:
  * Data generator MUST prefix all but one user-defined [-tag scheme-]{+*tag scheme*+} with a predetermined, provider-specified tag key prefix that is unique to each corresponding user-defined [-tag scheme-]{+*tag scheme*+} when the data generator has more than one user-defined [-tag scheme.-]{+*tag scheme*.+}
  * Data generator MUST NOT prefix tag keys when the data generator has only one user-defined [-tag scheme.-]{+*tag scheme*.+}
  * Data generator MUST NOT allow reserved tag key prefixes to be used as prefixes for any user-defined tag keys within a prefixless user-defined [-tag scheme.-]{+*tag scheme*.+}

## Provider-Defined vs. User-Defined Tags

This example illustrates various tags produced from multiple user-defined and provider-defined [-tag schemes.-]{+*tag schemes*.+}  The first three tags illustrate examples from three different, user-defined [-tag schemes.-]{+*tag schemes*.+} The data generator predetermined that [-1-]{+one+} user-defined [-tag scheme-]{+*tag scheme*+} (i.e., `"foo": "bar"`) does not have a prepended prefix, but the remaining two user-defined [-tag schemes-]{+*tag schemes*+} (i.e., `"userDefinedTagScheme2/foo": "bar"`, `"userDefinedTagScheme3/foo": true`) do have provider-defined and reserved prefixes.  Additionally, the third tag is produced from a valueless, user-defined [-tag scheme,-]{+*tag scheme*,+} so the data generator also applies `true` as its default value.

The last two tags illustrate examples from two different, provider-defined [-tag schemes.-]{+*tag schemes*.+} Since all provider-defined [-tag schemes-]{+*tag schemes*+} require a prefix, the data generator has prepended predefined and reserved prefixes (`providerDefinedTagScheme1/`, `providerDefinedTagScheme2/`) to each tag.

```json
    {
@@ -79,13 +78,14 @@ The set of tags assigned to *tag sources* that account for potential provider-de

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

