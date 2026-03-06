## Diff

diff --git a/specification/datasets/cost_and_usage/columns/pricingcurrency.md b/specification/datasets/cost_and_usage/columns/pricingcurrency.md
index 8f8aff20..7e620956 100644
--- a/specification/datasets/cost_and_usage/columns/pricingcurrency.md
+++ b/specification/datasets/cost_and_usage/columns/pricingcurrency.md
@@ -4,12 +4,11 @@

## Requirements

PricingCurrency [-adheres-]{+MUST adhere+} to the following requirements:

[-* PricingCurrency MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports pricing and billing in different currencies.-]
* PricingCurrency MUST be of type String.
* PricingCurrency MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* PricingCurrency MUST conform to [-[CurrencyFormat](#currencyformat)-]{+[CurrencyFormat](#attributes.currencyformat)+} requirements.
* PricingCurrency MUST NOT be null.

## Column ID
@@ -26,13 +25,14 @@ The national or virtual currency denomination that a *resource* or *service* was

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:------------------------------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | [Currency [-Format](#currencyformat)-]{+Format](#attributes.currencyformat)+}        |

## Introduced (version)

