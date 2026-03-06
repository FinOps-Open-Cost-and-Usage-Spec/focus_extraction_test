## Diff

diff --git a/specification/datasets/cost_and_usage/columns/commitmentdiscountcategory.md b/specification/datasets/cost_and_usage/columns/commitmentdiscountcategory.md
index 5714febf..d255dead 100644
--- a/specification/datasets/cost_and_usage/columns/commitmentdiscountcategory.md
+++ b/specification/datasets/cost_and_usage/columns/commitmentdiscountcategory.md
@@ -4,12 +4,11 @@ Commitment Discount Category indicates whether the [*commitment discount*](#glos

## Requirements

CommitmentDiscountCategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountCategory MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountCategory MUST be of type String.
* CommitmentDiscountCategory {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountCategory MUST be null when [-[CommitmentDiscountId](#commitmentdiscountid)-]{+[CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid)+} is null.
  * CommitmentDiscountCategory MUST NOT be null when CommitmentDiscountId is not null.
* CommitmentDiscountCategory MUST be one of the allowed values.

@@ -27,13 +26,14 @@ Indicates whether the *commitment discount* identified in the CommitmentDiscount

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | Allowed Values                                       |

Allowed values:

