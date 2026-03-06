## Diff

diff --git a/specification/attributes/currency_format.md b/specification/attributes/currency_format.md
index b131b549..d0564ef6 100644
--- a/specification/attributes/currency_format.md
+++ b/specification/attributes/currency_format.md
@@ -24,7 +24,7 @@ Formatting for currency columns appearing in a [*FOCUS dataset*](#glossary:FOCUS
## Requirements

* Currency-related columns MUST be represented as a three-letter alphabetic code as dictated in the governing document [ISO 4217:2015](https://www.iso.org/standard/64758.html) when the value is presented in national currency (e.g., USD, EUR).
* Currency-related columns MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements when the value is presented in virtual currency (e.g., credits, tokens).

## Exceptions

