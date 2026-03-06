## Diff

diff --git a/specification/attributes/invoice_handling.md b/specification/attributes/invoice_handling.md
index 0c7d9a26..adc8a7b2 100644
--- a/specification/attributes/invoice_handling.md
+++ b/specification/attributes/invoice_handling.md
@@ -18,7 +18,7 @@ Indicates how invoice-level *charges*, including those not directly tied to usag

## Requirements

* All costs that appear on any invoice issued to a [-[*BillingAccountId*](#billingaccountid)-]{+[*BillingAccountId*](#datasets.costandusage.billingaccountid)+} MUST be included in the *FOCUS dataset*.
* If an invoice-level *charge* appears on a customer invoice but cannot be expressed using existing FOCUS columns, data generators MUST include provider-defined columns (e.g., x_ChargeSubType) to capture the non-FOCUS-defined details needed to support invoice *charges* reconciliation using the *FOCUS dataset*.

## Exceptions
