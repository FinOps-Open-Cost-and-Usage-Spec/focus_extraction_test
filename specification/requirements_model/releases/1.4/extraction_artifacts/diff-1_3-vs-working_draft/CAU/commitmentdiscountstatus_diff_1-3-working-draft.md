## Diff

diff --git a/specification/datasets/cost_and_usage/columns/commitmentdiscountstatus.md b/specification/datasets/cost_and_usage/columns/commitmentdiscountstatus.md
index debfc8f9..508cbb3d 100644
--- a/specification/datasets/cost_and_usage/columns/commitmentdiscountstatus.md
+++ b/specification/datasets/cost_and_usage/columns/commitmentdiscountstatus.md
@@ -4,13 +4,12 @@ Commitment Discount Status indicates whether the [*charge*](#glossary:charge) co

## Requirements

CommitmentDiscountStatus [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountStatus MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountStatus MUST be of type String.
* CommitmentDiscountStatus {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountStatus MUST be null when [-[CommitmentDiscountId](#commitmentdiscountid)-]{+[CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid)+} is null.
  * CommitmentDiscountStatus MUST NOT be null when CommitmentDiscountId is not null and [Charge [-Category](#chargecategory)-]{+Category](#datasets.costandusage.chargecategory)+} is "Usage".
* CommitmentDiscountStatus MUST be one of the allowed values.

## Column ID
@@ -27,13 +26,14 @@ Indicates whether the *charge* corresponds with the consumption of a *commitment

## Content constraints

| Constraint      | Value                                                |
| :-------------- | [-:--------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | Allowed Values                                       |

Allowed values:

