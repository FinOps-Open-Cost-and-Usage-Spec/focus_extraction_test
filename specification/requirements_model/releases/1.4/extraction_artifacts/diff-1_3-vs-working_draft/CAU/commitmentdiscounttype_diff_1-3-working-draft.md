## Diff

diff --git a/specification/datasets/cost_and_usage/columns/commitmentdiscounttype.md b/specification/datasets/cost_and_usage/columns/commitmentdiscounttype.md
index 61d2a9db..dd592f4f 100644
--- a/specification/datasets/cost_and_usage/columns/commitmentdiscounttype.md
+++ b/specification/datasets/cost_and_usage/columns/commitmentdiscounttype.md
@@ -4,13 +4,12 @@ Commitment Discount Type is a service-provider-assigned name to identify the typ

## Requirements

CommitmentDiscountType [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountType MUST be of type String.
* CommitmentDiscountType MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* CommitmentDiscountType {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountType MUST be null when [-[CommitmentDiscountId](#commitmentdiscountid)-]{+[CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid)+} is null.
  * CommitmentDiscountType MUST NOT be null when CommitmentDiscountId is not null.

## Column ID
@@ -27,13 +26,14 @@ A service-provider-assigned identifier for the type of *commitment discount* app

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

