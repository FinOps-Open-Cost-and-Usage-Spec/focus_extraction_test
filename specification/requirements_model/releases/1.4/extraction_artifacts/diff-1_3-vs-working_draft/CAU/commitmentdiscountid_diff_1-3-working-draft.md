## Diff

diff --git a/specification/datasets/cost_and_usage/columns/commitmentdiscountid.md b/specification/datasets/cost_and_usage/columns/commitmentdiscountid.md
index 1af739b5..6391e544 100644
--- a/specification/datasets/cost_and_usage/columns/commitmentdiscountid.md
+++ b/specification/datasets/cost_and_usage/columns/commitmentdiscountid.md
@@ -4,15 +4,14 @@ A Commitment Discount ID is the identifier assigned to a [*commitment discount*]

## Requirements

CommitmentDiscountId [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountId MUST be of type String.
* CommitmentDiscountId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* CommitmentDiscountId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountId MUST be null when a [*charge*](#glossary:charge) is not related to a *commitment discount*.
  * CommitmentDiscountId MUST NOT be null when a *charge* is related to a *commitment discount*.
* When CommitmentDiscountId is not null, CommitmentDiscountId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CommitmentDiscountId MUST be a unique identifier within the service provider.
  * CommitmentDiscountId SHOULD be a fully-qualified identifier.

@@ -30,13 +29,14 @@ The identifier assigned to a *commitment discount* by the service provider.

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

