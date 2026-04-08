## Diff

diff --git a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_ru5srjng_from.md b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_i3yvp5p__to.md
index 181526da..e764f164 100644
--- a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_ru5srjng_from.md
+++ b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_i3yvp5p__to.md
@@ -1,30 +1,29 @@
# Effective Cost

Effective Cost represents the[-*amortized*-] cost of [-the-]{+a+} *charge* [-after applying all reduced rates, discounts, and-]{+based on+} the [-applicable portion of relevant, prepaid purchases (one-time-]{+*resources* used, *services* used,+} or [-recurring) that covered this *charge*. The *amortized* portion included should be proportional to the Pricing Quantity and the time granularity of the data. Since amortization breaks down and spreads the cost of-]{+*contract commitments* recognized in+} a [-prepaid purchase, to subsequent eligible *charges*, the-]{+given *charge period*.+} Effective Cost [-of the original prepaid *charge* is set to 0. Effective-]{+differs from Billed+} Cost [-does not mix-]{+when *covering charges* (e.g., prepaid+} or [-"blend" costs across multiple *charges* of the same *service*. This cost is denominated in the Billing Currency. The Effective Cost is commonly utilized-]{+postpaid commitment purchases) are recorded separately from the *covered charges*+} to [-track and analyze spending trends.-]{+which they are applied.+}

[-This column resolves two challenges that are faced-]{+For all *charges*, Effective Cost reflects all applicable pricing adjustments (e.g., reduced pricing from *negotiated discounts* or *commitment discounts*). For usage *charges*, Effective Cost includes the recognized portion of *Billed Cost* from related purchase *charges* (e.g., amortized portions of prepayments, drawdowns). For purchase *charges*, Effective Cost excludes any amounts recognized in related usage *charges* (e.g., usage *covered*+} by [-practitioners:-]{+*covering charges* such as *commitments*, prepayments, or marketplace purchases which draw down based on usage), regardless of when those related *charges* are invoiced.+}

[-1. Practitioners need to *amortize* relevant purchases, such as upfront fees, throughout-]{+Effective Cost is denominated in+} the [-*commitment* and distribute them-]{+Billing Currency. Effective Cost is commonly used+} to [-the appropriate reporting groups (e.g., *tags*, *resources*).-]
[-2. Many *commitment discount* constructs include a recurring expense for the *commitment* for every *billing period*-]{+support FinOps activities, including *accrual-based* reporting, forecasting,+} and[-must distribute this-] cost [-to the *resources* using the *commitment*. This forces reconciliation between the initial *commitment* *row* per period and the actual usage *rows*.-]{+allocation.+}

## Requirements

EffectiveCost [-adheres-]{+MUST adhere+} to the following requirements:

[-* EffectiveCost MUST be present in a Cost and Usage *FOCUS dataset*.-]
* EffectiveCost MUST be of type Decimal.
* EffectiveCost MUST conform to NumericFormat requirements.
* EffectiveCost MUST NOT be null.
[-* EffectiveCost MUST be a valid decimal value.-]
[-* EffectiveCost MUST be 0 when ChargeCategory is "Purchase" and the purchase is intended to cover future eligible *charges*.-]
* EffectiveCost MUST be denominated in the BillingCurrency.
*[-The sum of-] EffectiveCost [-in a given *billing period* MAY differ from the sum of the invoices received for the same *billing period* for a *billing account*.-]{+MUST reflect all applicable pricing adjustments, including but not limited to *negotiated discounts*, *commitment discounts*, and other applicable discount programs.+}
* [-When-]{+EffectiveCost MUST equal BilledCost when+} ChargeCategory is[-not-] "Usage" [-or "Purchase", EffectiveCost adheres to-]{+and+} the [-following additional requirements:-]{+*charge* is not *covered* by other eligible *charges*.+}
* EffectiveCost [-of a-]{+MUST equal BilledCost when ChargeCategory is "Purchase" and the+} *charge* [-calculated based on-]{+is neither intended to cover+} other {+eligible+} *charges* [-(e.g.,-]{+nor *covered* by other eligible *charges*.+}
{+* EffectiveCost MUST equal BilledCost+} when[-the-] ChargeCategory is [-"Tax") MUST be calculated based on the-]{+"Tax" or "Credit".+}
{+*+} EffectiveCost [-of those related *charges*.-]{+MAY differ from BilledCost when ChargeCategory is "Adjustment".+}
* EffectiveCost {+MUST include any portion+} of[-a *charge* unrelated to other *charges* (e.g., when-] the {+BilledCost of *covering* purchase *charges* (i.e.,+} ChargeCategory is [-"Credit")-]{+"Purchase") that is applied to this *charge*.+}
{+* EffectiveCost+} MUST [-match-]{+be 0 when ChargeCategory is "Purchase" and+} the [-BilledCost.-]{+purchase is intended to cover related eligible *charges*. This requirement applies even when the *covered charges* originate from different cost and usage datasets, possibly from a different ServiceProviderName.+}
* [-*Charges*-]{+EffectiveCost MUST be 0+} for [-a given CommitmentDiscountId adhere to-]{+*charges* generated by entities that do not originate+} the [-following additional requirements:-]{+cost and usage data, to avoid double-counting when merging multiple datasets.+}
* The sum of EffectiveCost [-where ChargeCategory is "Usage"-]{+across all related *covering* and *covered charges*+} MUST equal the sum of BilledCost [-where ChargeCategory is "Purchase".-]{+across the same set of *charges*, within the *charge period* of the *covering charges*, when both the *covering* and *covered charges* are present in the dataset.+}
* The sum of EffectiveCost [-where ChargeCategory is "Usage" MUST equal-]{+for a given *billing period* MAY differ from+} the sum of [-EffectiveCost where ChargeCategory is "Usage"-]{+BilledCost when *covered*+} and [-CommitmentDiscountStatus is "Used", plus the sum-]{+*covering charges* span multiple *billing periods* or *billing accounts*, or when only one side+} of [-EffectiveCost where ChargeCategory is "Usage" and CommitmentDiscountStatus-]{+a covering relationship+} is [-"Unused".-]{+present in the dataset.+}

## Column ID

@@ -36,26 +35,19 @@ Effective Cost

## Description

[-The *amortized* cost-]{+Cost+} of [-the-]{+a+} *charge* [-after applying all reduced rates, discounts, and-]{+based on+} the [-applicable portion of relevant, prepaid purchases (one-time-]{+*resources* used, *services* used,+} or [-recurring) that covered this *charge*.-]

[-### Concerning Granularity and Distribution of Recurring Fee-]

[-Service providers should distribute the *commitment* purchase amount instead of including a *row* at the beginning of a period so practitioners do not need to manually distribute the fee themselves.-]

[-### Concerning Amortization Approaches-]

[-Eligible purchases should be *amortized* using a methodology determined by the service provider that reflects the needs of their customer base and is proportional to the Pricing Quantity and the time granularity of the *row*. Should-]{+*contract commitments* recognized in+} a [-practitioner desire to *amortize* relevant purchases using a different approach, the practitioner can do so using the Billed Cost for the line item representing the initial purchase.-]{+given *charge period*.+}

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:------------------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | Cost and Usage             |+}
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | Numeric Format          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

