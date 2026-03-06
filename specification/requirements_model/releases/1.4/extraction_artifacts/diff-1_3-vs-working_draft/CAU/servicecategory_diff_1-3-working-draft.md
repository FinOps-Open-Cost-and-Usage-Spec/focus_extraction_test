## Diff

diff --git a/specification/datasets/cost_and_usage/columns/servicecategory.md b/specification/datasets/cost_and_usage/columns/servicecategory.md
index c16df2a5..ad38f92f 100644
--- a/specification/datasets/cost_and_usage/columns/servicecategory.md
+++ b/specification/datasets/cost_and_usage/columns/servicecategory.md
@@ -4,9 +4,8 @@ The Service Category is the highest-level classification of a [*service*](#gloss

## Requirements

ServiceCategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* ServiceCategory MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ServiceCategory MUST be of type String.
* ServiceCategory MUST NOT be null.
* ServiceCategory MUST be one of the allowed values.
@@ -25,13 +24,14 @@ Highest-level classification of a *service* based on the core function of the *s

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | [-:--------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed Values                                       |

Allowed values:

