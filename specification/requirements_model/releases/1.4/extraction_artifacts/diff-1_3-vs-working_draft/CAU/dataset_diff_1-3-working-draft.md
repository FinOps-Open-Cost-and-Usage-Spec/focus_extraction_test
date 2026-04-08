## Diff

diff --git a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_4fm2czl1_from.md b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_oqd_fqxg_to.md
index 3160f40f..1be2a490 100644
--- a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_4fm2czl1_from.md
+++ b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_oqd_fqxg_to.md
@@ -4,7 +4,7 @@ The Cost and Usage dataset is the primary dataset for FOCUS cost and usage data.

The specification for the Cost and Usage dataset defines a group of columns that provide qualitative values (such as dates, resource, and service provider information) categorized as "dimensions" and quantitative values (numeric values) categorized as "metrics" that can be used for performing various [FinOps capabilities][FODOFC]. Metrics are commonly used for aggregations (sum, multiplication, averaging etc.) and statistical operations within the dataset. Dimensions are commonly used to categorize, filter, and reveal details in your data when combined with metrics. The columns are presented in alphabetical order.

[-<div class='h4-nonindex'>Columns</div>-]{+## Columns<!--SkipTOC-->+}

| Column                                                                        | Column Type        | Feature Level | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------- | ------------------ | ------------- | ------------ | --------- |
@@ -43,19 +43,18 @@ The specification for the Cost and Usage dataset defines a group of columns that
| Contracted Unit Price                                 | Metric             | Conditional   | True         | Decimal   |
| Effective Cost                                              | Metric             | Mandatory     | False        | Decimal   |
| Host Provider Name                                       | Dimension          | Mandatory     | False        | String    |
| Invoice {+Detail+} ID                                                      | Dimension          | [-Recommended-]{+Conditional   | True         | String    |+}
{+| Invoice ID                                                      | Dimension          | Conditional+}   | True         | String    |
| Invoice Issuer Name                                     | Dimension          | Mandatory     | False        | String    |
| List Cost                                                        | Metric             | Mandatory     | False        | Decimal   |
| List Unit Price                                             | Metric             | Conditional   | True         | Decimal   |
| Pricing Category                                          | Dimension          | Conditional   | True         | String    |
| Pricing Currency                                          | Dimension          | Conditional   | [-True-]{+False+}        | String    |
| Pricing Currency Contracted Unit Price | Metric             | Conditional   | True         | Decimal   |
| Pricing Currency Effective Cost              | Metric             | Conditional   | [-True-]{+False+}        | Decimal   |
| Pricing Currency List Unit Price             | Metric             | Conditional   | True         | Decimal   |
| Pricing Quantity                                          | Metric             | Mandatory     | True         | Decimal   |
| Pricing Unit                                                  | Dimension          | Mandatory     | True         | String    |
[-| Provider - DEPRECATED                                        | Dimension          | Mandatory     | False        | String    |-]
[-| Publisher - DEPRECATED                                      | Dimension          | Mandatory     | False        | String    |-]
| Region ID                                                        | Dimension          | Conditional   | True         | String    |
| Region Name                                                    | Dimension          | Conditional   | True         | String    |
| Resource ID                                                    | Dimension          | Conditional   | True         | String    |
@@ -74,7 +73,7 @@ The specification for the Cost and Usage dataset defines a group of columns that
| Sub Account Type                                           | Dimension          | Conditional   | True         | String    |
| Tags                                                                 | Dimension          | Conditional   | True         | JSON      |

[-<div class='h4-nonindex'>Relationships</div>-]{+## Relationships<!--SkipTOC-->+}

The Cost and Usage dataset can be joined to the Contract Commitment dataset through the use of the Contract Commitment ID.

@@ -85,29 +84,97 @@ The Cost and Usage dataset can be joined to the Contract Commitment dataset thro
| ------------------- | ----------------- | ------------------- | ---------------------- |
| Cost and Usage      | Contract Applied  | Contract Commitment | Contract Commitment ID |

[-<div class='h4-nonindex'>Requirements</div>-]{+## Requirements<!--SkipTOC-->+}

CostAndUsage [-adheres-]{+MUST adhere+} to the following requirements:

* CostAndUsage MUST be present.
{+* CostAndUsage column presence MUST adhere to the following requirements:+}
{+  * CostAndUsage SHOULD include AllocatedMethodDetails when the data generator supports Data Generator-Calculated Split Cost Allocation.+}
{+  * CostAndUsage MUST include AllocatedMethodId when the data generator supports Data Generator-Calculated Split Cost Allocation.+}
{+  * CostAndUsage MUST include AllocatedResourceId when the data generator supports Data Generator-Calculated Split Cost Allocation.+}
{+  * CostAndUsage MUST include AllocatedResourceName when the data generator supports Data Generator-Calculated Split Cost Allocation.+}
{+  * CostAndUsage MUST include AllocatedTags when the service provider supports Data Generator-Calculated Split Cost Allocation.+}
{+  * CostAndUsage SHOULD include AvailabilityZone when the host provider supports deploying resources or services within an *availability zone*.+}
{+  * CostAndUsage MUST include BilledCost.+}
{+  * CostAndUsage MUST include BillingAccountId.+}
{+  * CostAndUsage MUST include BillingAccountName.+}
{+  * CostAndUsage MUST include BillingAccountType when the invoice issuer supports more than one possible BillingAccountType value.+}
{+  * CostAndUsage MUST include BillingCurrency.+}
{+  * CostAndUsage MUST include BillingPeriodEnd.+}
{+  * CostAndUsage MUST include BillingPeriodStart.+}
{+  * CostAndUsage MUST include CapacityReservationId when the service provider supports *capacity reservations*.+}
{+  * CostAndUsage MUST include CapacityReservationStatus when the service provider supports *capacity reservations*.+}
{+  * CostAndUsage MUST include ChargeCategory.+}
{+  * CostAndUsage MUST include ChargeClass.+}
{+  * CostAndUsage MUST include ChargeDescription.+}
{+  * CostAndUsage SHOULD include ChargeFrequency.+}
{+  * CostAndUsage MUST include ChargePeriodEnd.+}
{+  * CostAndUsage MUST include ChargePeriodStart.+}
{+  * CostAndUsage MUST include CommitmentDiscountCategory when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include CommitmentDiscountId when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include CommitmentDiscountName when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include CommitmentDiscountQuantity when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include CommitmentDiscountStatus when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include CommitmentDiscountType when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include CommitmentDiscountUnit when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include ConsumedQuantity when the service provider supports the measurement of usage.+}
{+  * CostAndUsage MUST include ConsumedUnit when the service provider supports the measurement of usage.+}
{+  * CostAndUsage MUST include ContractApplied when the service provider supports *contract commitments*.+}
{+  * CostAndUsage MUST include ContractedCost.+}
{+  * CostAndUsage MUST include ContractedUnitPrice when the service provider supports negotiated pricing concepts.+}
{+  * CostAndUsage MUST include EffectiveCost.+}
{+  * CostAndUsage MUST include HostProviderName.+}
{+  * CostAndUsage MUST include InvoiceDetailId when the invoice issuer supports payable invoices.+}
{+  * CostAndUsage MUST include InvoiceId when the invoice issuer supports payable invoices.+}
{+  * CostAndUsage MUST include InvoiceIssuerName.+}
{+  * CostAndUsage MUST include ListCost.+}
{+  * CostAndUsage MUST include ListUnitPrice when the service provider publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include PricingCategory when the service provider supports more than one pricing category across all *SKUs*.+}
{+  * CostAndUsage MUST include PricingCurrency when the service provider supports pricing and billing in different currencies.+}
{+  * CostAndUsage MUST include PricingCurrencyContractedUnitPrice when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include PricingCurrencyEffectiveCost when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include PricingCurrencyListUnitPrice when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include PricingQuantity.+}
{+  * CostAndUsage MUST include PricingUnit.+}
{+  * CostAndUsage MUST include RegionId when the host provider supports deploying resources or services within a region.+}
{+  * CostAndUsage MUST include RegionName when the host provider supports deploying resources or services within a region.+}
{+  * CostAndUsage MUST include ResourceId when the service provider supports billing based on provisioned *resources*.+}
{+  * CostAndUsage MUST include ResourceName when the service provider supports billing based on provisioned resources.+}
{+  * CostAndUsage MUST include ResourceType when the service provider supports billing based on provisioned *resources* and supports assigning types to *resources*.+}
{+  * CostAndUsage MUST include ServiceCategory.+}
{+  * CostAndUsage MUST include ServiceName.+}
{+  * CostAndUsage MUST include ServiceProviderName.+}
{+  * CostAndUsage SHOULD include ServiceSubcategory.+}
{+  * CostAndUsage MUST include SkuId when the service provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.+}
{+  * CostAndUsage MUST include SkuMeter when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.+}
{+  * CostAndUsage MUST include SkuPriceDetails when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.+}
{+  * CostAndUsage MUST include SkuPriceId when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.+}
{+  * CostAndUsage MUST include SubAccountId when the service provider supports a *sub account* construct.+}
{+  * CostAndUsage MUST include SubAccountName when the service provider supports a *sub account* construct.+}
{+  * CostAndUsage MUST include SubAccountType when the service provider supports more than one possible SubAccountType value.+}
{+  * CostAndUsage MUST include Tags when the data generator supports setting user or provider-defined tags.+}
* CostAndUsage MUST conform to ColumnHandling requirements.
* CostAndUsage MUST conform to [-NullHandling requirements.-]
[-* CostAndUsage MUST conform to DiscountHandling requirements.-]
[-* CostAndUsage MUST conform to InvoiceHandling-]{+CorrectionHandling+} requirements.
* CostAndUsage MUST conform to DataGeneratorCalculatedSplitCostAllocationHandling requirements.
{+* CostAndUsage MUST conform to DatasetCompleteness requirements.+}
{+* CostAndUsage MUST conform to DatasetConfiguration requirements.+}
{+* CostAndUsage MUST conform to DeliveryHandling requirements.+}
{+* CostAndUsage MUST conform to DiscountHandling requirements.+}
{+* CostAndUsage MUST conform to NullHandling requirements.+}

[-<div class='h4-nonindex'>Dataset ID</div>-]{+## Dataset ID<!--SkipTOC-->+}

CostAndUsage

[-<div class='h4-nonindex'>Display Name</div>-]{+## Display Name<!--SkipTOC-->+}

Cost and Usage

[-<div class='h4-nonindex'>Description</div>-]{+## Description<!--SkipTOC-->+}

Describes the cost and usage incurred through using or purchasing a service provider's *resources* or *services*.

[-<div class='h4-nonindex'>Introduced (version)</div>-]{+## Introduced (version)<!--SkipTOC-->+}

0.5
