## Diff

diff --git a/specification/datasets/cost_and_usage/columns/pricingcurrencyeffectivecost.md b/specification/datasets/cost_and_usage/columns/pricingcurrencyeffectivecost.md
index 603781a7..097395b2 100644
--- a/specification/datasets/cost_and_usage/columns/pricingcurrencyeffectivecost.md
+++ b/specification/datasets/cost_and_usage/columns/pricingcurrencyeffectivecost.md
@@ -1,21 +1,20 @@
# Pricing Currency Effective Cost

The Pricing Currency Effective Cost represents the cost of the [*charge*](#glossary:charge) after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this *charge*, as denominated in [Pricing [-Currency](#pricingcurrency).-]{+Currency](#datasets.costandusage.pricingcurrency).+} This allows the practitioner to perform a conversion from either 1) a [*national currency*](#glossary:nationalcurrency) to a [*virtual currency*](#glossary:virtualcurrency) (e.g., tokens to USD), or 2) one national currency to another (e.g., EUR to USD).

## Requirements

PricingCurrencyEffectiveCost [-adheres-]{+MUST adhere+} to the following requirements:

* PricingCurrencyEffectiveCost presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset)[-is defined as follows:-]
[-  * PricingCurrencyEffectiveCost-] MUST [-be present in a Cost and Usage *FOCUS dataset* when-]{+adhere to+} the [-service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.-]{+following presence requirements:+}
  * PricingCurrencyEffectiveCost [-is RECOMMENDED to-]{+SHOULD+} be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
* PricingCurrencyEffectiveCost MUST be of type Decimal.
* PricingCurrencyEffectiveCost MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* PricingCurrencyEffectiveCost MUST NOT be null.
* PricingCurrencyEffectiveCost MUST be a valid decimal value.
* PricingCurrencyEffectiveCost MUST be 0 in the event of prepaid purchases or purchases that are applicable to previous usage.
* PricingCurrencyEffectiveCost MUST be denominated in the [-[PricingCurrency](#pricingcurrency).-]{+[PricingCurrency](#datasets.costandusage.pricingcurrency).+}

## Column ID

@@ -31,14 +30,15 @@ The cost of the *charge* after applying all reduced rates, discounts, and the ap

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:------------------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric [-Format](#numericformat)-]{+Format](#attributes.numericformat)+}          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

