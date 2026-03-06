## Diff

diff --git a/specification/datasets/cost_and_usage/columns/commitmentdiscountquantity.md b/specification/datasets/cost_and_usage/columns/commitmentdiscountquantity.md
index be115334..206a76f8 100644
--- a/specification/datasets/cost_and_usage/columns/commitmentdiscountquantity.md
+++ b/specification/datasets/cost_and_usage/columns/commitmentdiscountquantity.md
@@ -1,28 +1,27 @@
# Commitment Discount Quantity

Commitment Discount Quantity is the amount of a [*commitment discount*](#glossary:commitment-discount) purchased or accounted for in *commitment discount* related [*rows*](#glossary:row) that is denominated in [Commitment Discount [-Units](#commitmentdiscountunit).-]{+Units](#datasets.costandusage.commitmentdiscountunit).+} The aggregated Commitment Discount Quantity across purchase records, pertaining to a particular [Commitment Discount [-ID](#commitmentdiscountid)-]{+ID](#datasets.costandusage.commitmentdiscountid)+} during its commitment [*period*](#glossary:period), represents the total Commitment Discount Units acquired with that commitment discount. For committed usage, the Commitment Discount Quantity is either the number of Commitment Discount Units consumed by a *row* that is covered by a *commitment discount* or is the unused portion of a *commitment discount* over a [*charge period*](#glossary:chargeperiod). Commitment Discount Quantity is commonly used in *commitment discount* analysis and optimization use cases and only applies to *commitment discounts*, not [*negotiated discounts*](#glossary:negotiated-discount).

When [-[CommitmentDiscountCategory](#commitmentdiscountcategory)-]{+[CommitmentDiscountCategory](#datasets.costandusage.commitmentdiscountcategory)+} is "Usage" (usage-based *commitment discounts*), the Commitment Discount Quantity reflects the predefined amount of usage purchased or consumed. If [*commitment discount flexibility*](#glossary:commitment-discount-flexibility) is applicable, this value may be further transformed based on additional, service-provider-specific requirements. When CommitmentDiscountCategory is "Spend" (spend-based *commitment discounts*), the Commitment Discount Quantity reflects the predefined amount of spend purchased or consumed.  See [Appendix: Commitment Discount [-Flexibility](#commitmentdiscountflexibility)-]{+Flexibility](#appendix.examples:commitmentdiscountflexibility)+} for more details around *commitment discount flexibility*.

## Requirements

CommitmentDiscountQuantity [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountQuantity MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountQuantity MUST be of type Decimal.
* CommitmentDiscountQuantity MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* CommitmentDiscountQuantity {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountQuantity MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * When ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
    * CommitmentDiscountQuantity MUST NOT be null when [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
    * CommitmentDiscountQuantity MAY be null when ChargeClass is "Correction".
  * CommitmentDiscountQuantity MUST be null in all other cases.
* CommitmentDiscountQuantity MUST be a valid decimal value when not null.
* When CommitmentDiscountQuantity is not null and ChargeCategory is "Purchase", CommitmentDiscountQuantity [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term* when [-[ChargeFrequency](#chargefrequency)-]{+[ChargeFrequency](#datasets.costandusage.chargefrequency)+} is "One-Time".
  * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit that is eligible for consumption for each *charge period* that corresponds with the purchase when ChargeFrequency is "Recurring".
* When CommitmentDiscountQuantity is not null and ChargeCategory is "Usage", CommitmentDiscountQuantity [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnit that is consumed in a given *charge period* when [-[CommitmentDiscountStatus](#commitmentdiscountstatus)-]{+[CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus)+} is "Used".
  * CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnit in a given *charge period* when CommitmentDiscountStatus is "Unused".

## Column ID
@@ -43,14 +42,15 @@ The amount of a *commitment discount* purchased or accounted for in *commitment

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric [-Format](#numericformat)-]{+Format](#attributes.numericformat)+}          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

