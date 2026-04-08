## Diff

diff --git a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_i_bcxnsn_from.md b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_j4xb6ue0_to.md
index 7b1a6916..e69de29b 100644
--- a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_i_bcxnsn_from.md
+++ b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_j4xb6ue0_to.md
@@ -1,33 +0,0 @@
[-# Invoice Handling-]

[-FinOps practitioners must be able to reconcile FOCUS datasets with the corresponding invoices and usage statements they receive from *Invoice Issuers*. In practice, this means ensuring that all monetary *charges* that appear on an invoice or usage statement — including those not tied to metered usage — are represented in the *FOCUS dataset*. Without this alignment, it becomes difficult to perform accurate invoice reconciliation, financial reporting, and chargeback.-]

[-This attribute introduces requirements for how charges such as usage, taxes, credits, refunds, etc, inclusive of support, training, and marketplace transactions, and any other type of charge should be captured and categorized. It also defines expectations around the completeness and consistency of invoice-level totals within the dataset, enabling FOCUS datasets to be used in a system of record for all invoiced costs.-]

[-## Attribute ID-]

[-InvoiceHandling-]

[-## Attribute Name-]

[-Invoice Handling-]

[-## Description-]

[-Indicates how invoice-level *charges*, including those not directly tied to usage, should be represented in a FOCUS Cost and Usage dataset.-]

[-## Requirements-]

[-* All costs that appear on any invoice issued to a *BillingAccountId* MUST be included in the *FOCUS dataset*.-]
[-* If an invoice-level *charge* appears on a customer invoice but cannot be expressed using existing FOCUS columns, data generators MUST include provider-defined columns (e.g., x_ChargeSubType) to capture the non-FOCUS-defined details needed to support invoice *charges* reconciliation using the *FOCUS dataset*.-]

[-## Exceptions-]

[-* Informational line items that have zero monetary impact and are included solely for transparency MAY be excluded. Examples include:-]
[-  * Tax exemption notifications-]
[-  * SLA credit details when the credit is already applied to the charged amount-]
[-* If such informational items are excluded, data generators MUST document this in their FOCUS implementation guide and ensure the sum of included charges still equals the invoice total.-]

[-## Introduced (version)-]

[-1.3-]
