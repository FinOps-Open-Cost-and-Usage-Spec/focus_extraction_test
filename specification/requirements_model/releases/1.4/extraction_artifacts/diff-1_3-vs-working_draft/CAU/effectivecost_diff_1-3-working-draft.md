## Diff

diff --git a/specification/datasets/cost_and_usage/columns/effectivecost.md b/specification/datasets/cost_and_usage/columns/effectivecost.md
index fbca5282..31b8217d 100644
--- a/specification/datasets/cost_and_usage/columns/effectivecost.md
+++ b/specification/datasets/cost_and_usage/columns/effectivecost.md
@@ -1,30 +1,28 @@
# Effective Cost

Effective Cost represents the[-[*amortized*](#glossary:amortization)-] cost of [-the-]{+a+} [*charge*](#glossary:charge) [-after applying all reduced rates, discounts, and-]{+based on+} the [-applicable portion of relevant, prepaid purchases (one-time-]{+[*resources*](#glossary:resource) used, [*services*](#glossary:service) used,+} or [-recurring) that covered this *charge*. The *amortized* portion included should be proportional to the [Pricing Quantity](#pricingquantity) and the time granularity of the data. Since amortization breaks down and spreads the cost of-]{+[*contract commitments*](#glossary:contract-commitment) recognized in+} a [-prepaid purchase, to subsequent eligible *charges*, the-]{+given [*charge period*](#glossary:charge-period).+} Effective Cost [-of the original prepaid *charge* is set to 0. Effective Cost does not mix or "blend" costs across multiple-]{+differs from [Billed Cost](#datasets.costandusage.billedcost) when+} *charges* [-of the same [*service*](#glossary:service). This cost is denominated in the [Billing Currency](#billingcurrency). The Effective Cost is commonly utilized to track-]{+(both pre-paid+} and [-analyze spending trends.-]{+post-paid) are invoiced separately from usage.+}

[-This column resolves two challenges that are faced-]{+For all *charges*, Effective Cost reflects all applicable pricing adjustments (e.g., reduced pricing from [*negotiated discounts*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount)). For usage *charges*, Effective Cost includes the recognized portion of *Billed Cost* from related purchase *charges* (e.g., amortized portions of prepayments, drawdowns). For purchase *charges*, Effective Cost excludes any amounts recognized in related usage *charges* (e.g., usage covered+} by [-practitioners:-]{+*commitments*, pre-payments, or marketplace purchases which draw down based on usage), regardless of when those related *charges* are invoiced.+}

[-1. Practitioners need to *amortize* relevant purchases, such as upfront fees, throughout-]{+Effective Cost is denominated in+} the [-*commitment* and distribute them-]{+[Billing Currency](#datasets.costandusage.billingcurrency). Effective Cost is commonly used+} to [-the appropriate reporting groups (e.g., [*tags*](#glossary:tag), [*resources*](#glossary:resource)).-]
[-2. Many [*commitment discount*](#glossary:commitment-discount) constructs include a recurring expense for the *commitment* for every [*billing period*](#glossary:billing-period)-]{+support FinOps activities, including [*accrual-based*](#glossary:accrual-based-accounting) reporting, forecasting,+} and[-must distribute this-] cost [-to the *resources* using the *commitment*. This forces reconciliation between the initial *commitment* [*row*](#glossary:row) per period and the actual usage *rows*.-]{+allocation.+}

## Requirements

EffectiveCost [-adheres-]{+MUST adhere+} to the following requirements:

[-* EffectiveCost MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* EffectiveCost MUST be of type Decimal.
* EffectiveCost MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* EffectiveCost MUST NOT be null.
* EffectiveCost MUST be a valid decimal value.
* EffectiveCost MUST be 0 when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Purchase" and the purchase is intended to cover future eligible *charges*.
* EffectiveCost MUST be denominated in the BillingCurrency.
* The sum of EffectiveCost in a given *billing period* MAY differ from the sum of the invoices received for the same *billing period* for a [*billing account*](#glossary:billing-account).
* When ChargeCategory is not "Usage" or "Purchase", EffectiveCost [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * EffectiveCost of a *charge* calculated based on other *charges* (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the EffectiveCost of those related *charges*.
  * EffectiveCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [-[BilledCost](#billedcost).-]{+[BilledCost](#datasets.costandusage.billedcost).+}
* *Charges* for a given [-[CommitmentDiscountId](#commitmentdiscountid)-]{+[CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) MUST+} adhere to the following[-additional-] requirements:
  * The sum of EffectiveCost where ChargeCategory is "Usage" MUST equal the sum of BilledCost where ChargeCategory is "Purchase".
  * The sum of EffectiveCost where ChargeCategory is "Usage" MUST equal the sum of EffectiveCost where ChargeCategory is "Usage" and [-[CommitmentDiscountStatus](#commitmentdiscountstatus)-]{+[CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus)+} is "Used", plus the sum of EffectiveCost where ChargeCategory is "Usage" and CommitmentDiscountStatus is "Unused".

## Column ID

@@ -36,26 +34,19 @@ Effective Cost

## Description

[-The *amortized* cost-]{+Cost+} of [-the-]{+a+} *charge* [-after applying all reduced rates, discounts, and-]{+based on+} the [-applicable portion of relevant, prepaid purchases (one-time-]{+*resources* used, *services* used,+} or [-recurring) that covered this *charge*.-]

[-### Concerning Granularity and Distribution of Recurring Fee-]

[-Service providers should distribute the *commitment* purchase amount instead of including a *row* at the beginning of a period so practitioners do not need to manually distribute the fee themselves.-]

[-### Concerning Amortization Approaches-]

[-Eligible purchases should be *amortized* using a methodology determined by the service provider that reflects the needs of their customer base and is proportional to the Pricing Quantity and the time granularity of the *row*. Should a practitioner desire to *amortize* relevant purchases using-]{+*contract commitments* recognized in+} a [-different approach, the practitioner can do so using the [Billed Cost](#billedcost) for the line item representing the initial purchase.-]{+given *charge period*.+}

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:------------------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | [Numeric [-Format](#numericformat)-]{+Format](#attributes.numericformat)+}          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

