## Diff

diff --git a/specification/datasets/cost_and_usage/columns/commitmentdiscountname.md b/specification/datasets/cost_and_usage/columns/commitmentdiscountname.md
index 93baa3b1..dcb28662 100644
--- a/specification/datasets/cost_and_usage/columns/commitmentdiscountname.md
+++ b/specification/datasets/cost_and_usage/columns/commitmentdiscountname.md
@@ -4,14 +4,13 @@ A Commitment Discount Name is the display name assigned to a [*commitment discou

## Requirements

CommitmentDiscountName [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountName MUST be of type String.
* CommitmentDiscountName MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* CommitmentDiscountName {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountName MUST be null when [-[CommitmentDiscountId](#commitmentdiscountid)-]{+[CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid)+} is null.
  * When CommitmentDiscountId is not null, CommitmentDiscountName [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
    * CommitmentDiscountName MUST NOT be null when a display name can be assigned to a *commitment discount*.
    * CommitmentDiscountName MAY be null when a display name cannot be assigned to a *commitment discount*.

@@ -29,13 +28,14 @@ The display name assigned to a *commitment discount*.

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

