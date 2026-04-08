## Diff

diff --git a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_kk781cf1_from.md b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_ddlvbnl6_to.md
index 10230bac..a9f7bb07 100644
--- a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_kk781cf1_from.md
+++ b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_ddlvbnl6_to.md
@@ -1,21 +1,23 @@
# Pricing Currency Effective Cost

[-The-]Pricing Currency Effective Cost represents the [-cost-]{+Pricing Currency-denominated equivalent+} of {+Effective Cost. It reflects+} the {+cost of a+} *charge* [-after applying all reduced rates, discounts, and-]{+based on+} the [-applicable portion of relevant, prepaid purchases (one-time-]{+*resources* used, *services* used,+} or [-recurring) that covered this *charge*, as denominated-]{+*contract commitments* recognized+} in {+a given *charge period*.+}

{+Because+} Pricing [-Currency. This allows-]{+Currency Effective Cost differs from Effective Cost only in denomination, it follows+} the [-practitioner-]{+same pricing adjustments, amortizations, and exclusions. This column provides practitioners with a standardized baseline, allowing them+} to [-perform-]{+view costs in+} a [-conversion-]{+uniform currency, whether converting+} from[-either 1)-] a [-*national-]{+*virtual+} currency* to a [-*virtual-]{+*national+} currency* (e.g., tokens to [-USD),-]{+USD)+} or [-2)-]{+from+} one national currency to another (e.g., EUR to USD).

{+Pricing Currency Effective Cost is commonly used to support FinOps activities, including *accrual-based* reporting, forecasting, and cost allocation when pricing and billing use different currencies.+}

## Requirements

PricingCurrencyEffectiveCost [-adheres-]{+MUST adhere+} to the following requirements:

* PricingCurrencyEffectiveCost presence in a Cost and Usage *FOCUS dataset*[-is defined as follows:-]
[-  * PricingCurrencyEffectiveCost-] MUST [-be present in a Cost and Usage *FOCUS dataset* when-]{+adhere to+} the [-service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.-]{+following presence requirements:+}
  * PricingCurrencyEffectiveCost [-is RECOMMENDED to-]{+SHOULD+} be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
* PricingCurrencyEffectiveCost MUST be of type Decimal.
* PricingCurrencyEffectiveCost MUST conform to NumericFormat requirements.
* PricingCurrencyEffectiveCost MUST NOT be null.
[-* PricingCurrencyEffectiveCost MUST be a valid decimal value.-]
[-* PricingCurrencyEffectiveCost MUST be 0 in the event of prepaid purchases or purchases that are applicable to previous usage.-]
* PricingCurrencyEffectiveCost MUST be denominated in the PricingCurrency.
{+* PricingCurrencyEffectiveCost MUST be the PricingCurrency-denominated equivalent of EffectiveCost.+}

## Column ID

@@ -27,18 +29,19 @@ Pricing Currency Effective Cost

## Description

The [-cost-]{+PricingCurrency-denominated equivalent+} of {+Effective Cost, representing+} the {+cost of a+} *charge* [-after applying all reduced rates, discounts, and-]{+based on+} the [-applicable portion of relevant, prepaid purchases (one-time-]{+*resources* used, *services* used,+} or [-recurring) that covered this *charge*, as denominated-]{+*contract commitments* recognized+} in [-Pricing Currency.-]{+a given *charge period*.+}

## Content [-Constraints-]{+constraints+}

| Constraint      | Value                                                |
[-|:----------------|:------------------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | Cost and Usage             |+}
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | [-True-]{+False+}                                                |
| Data type       | Decimal                                              |
| Value format    | Numeric Format          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

