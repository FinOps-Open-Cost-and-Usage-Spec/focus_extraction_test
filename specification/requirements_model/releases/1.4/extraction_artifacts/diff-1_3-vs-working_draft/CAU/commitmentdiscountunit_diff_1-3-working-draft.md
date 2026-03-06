## Diff

diff --git a/specification/datasets/cost_and_usage/columns/commitmentdiscountunit.md b/specification/datasets/cost_and_usage/columns/commitmentdiscountunit.md
index f8a70036..41e82ab9 100644
--- a/specification/datasets/cost_and_usage/columns/commitmentdiscountunit.md
+++ b/specification/datasets/cost_and_usage/columns/commitmentdiscountunit.md
@@ -1,24 +1,23 @@
# Commitment Discount Unit

Commitment Discount Unit represents the service-provider-specified measurement unit indicating how a service provider measures the [Commitment Discount [-Quantity](#commitmentdiscountquantity)-]{+Quantity](#datasets.costandusage.commitmentdiscountquantity)+} of a [*commitment discount*](#glossary:commitment-discount). The CommitmentDiscountUnit column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

## Requirements

CommitmentDiscountUnit [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountUnit MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountUnit MUST be of type String.
* CommitmentDiscountUnit MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* CommitmentDiscountUnit SHOULD conform to [-[UnitFormat](#unitformat)-]{+[UnitFormat](#attributes.unitformat)+} requirements.
* CommitmentDiscountUnit {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountUnit MUST be null when CommitmentDiscountQuantity is null.
  * CommitmentDiscountUnit MUST NOT be null when CommitmentDiscountQuantity is not null.
* When CommitmentDiscountUnit is not null, CommitmentDiscountUnit [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.
  * CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
  * When accounting for [*commitment discount flexibility*](#glossary:commitment-discount-flexibility), the CommitmentDiscountUnit value SHOULD reflect this consideration.

See [Examples: Commitment Discount [-Flexibility](#commitmentdiscountflexibility)-]{+Flexibility](#appendix.examples:commitmentdiscountflexibility)+} for more details around *commitment discount flexibility*.

## Column ID

@@ -34,13 +33,14 @@ The service-provider-specified measurement unit indicating how a service provide

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | [Unit [-Format](#unitformat)|-]{+Format](#attributes.unitformat)                |+}

## Introduced (version)

