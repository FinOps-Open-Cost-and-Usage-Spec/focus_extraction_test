## Diff

diff --git a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff__zus8gjz_from.md b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_5hzin3w3_to.md
index 1b676a28..bf3f07ac 100644
--- a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff__zus8gjz_from.md
+++ b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_5hzin3w3_to.md
@@ -1,14 +1,12 @@
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
