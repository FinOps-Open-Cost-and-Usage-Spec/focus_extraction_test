## Diff

diff --git a/specification/datasets/cost_and_usage/dataset.md b/specification/datasets/cost_and_usage/dataset.md
index 55c66a85..27300a18 100644
--- a/specification/datasets/cost_and_usage/dataset.md
+++ b/specification/datasets/cost_and_usage/dataset.md
@@ -4,77 +4,76 @@ The Cost and Usage dataset is the primary dataset for FOCUS cost and usage data.

The specification for the Cost and Usage dataset defines a group of columns that provide qualitative values (such as dates, resource, and service provider information) categorized as "dimensions" and quantitative values (numeric values) categorized as "metrics" that can be used for performing various [FinOps capabilities][FODOFC]. Metrics are commonly used for aggregations (sum, multiplication, averaging etc.) and statistical operations within the dataset. Dimensions are commonly used to categorize, filter, and reveal details in your data when combined with metrics. The columns are presented in alphabetical order.

[-<div class='h4-nonindex'>Columns</div>-]{+## Columns<!--SkipTOC-->+}

| Column                                                                        | Column Type        | Feature Level | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------- | ------------------ | ------------- | ------------ | --------- |
| [Allocated Method [-Details](#allocatedmethoddetails)-]{+Details](#datasets.costandusage.allocatedmethoddetails)+}                           | Dimension          | Recommended   | True         | JSON      |
| [Allocated Method [-ID](#allocatedmethodid)-]{+ID](#datasets.costandusage.allocatedmethodid)+}                                     | Dimension          | Conditional   | True         | String    |
| [Allocated Resource [-ID](#allocatedresourceid)-]{+ID](#datasets.costandusage.allocatedresourceid)+}                                 | Dimension          | Conditional   | True         | String    |
| [Allocated Resource [-Name](#allocatedresourcename)-]{+Name](#datasets.costandusage.allocatedresourcename)+}                             | Dimension          | Conditional   | True         | String    |
| [Allocated [-Tags](#allocatedtags)-]{+Tags](#datasets.costandusage.allocatedtags)+}                                              | Dimension          | Conditional   | True         | JSON      |
| [Availability [-Zone](#availabilityzone)-]{+Zone](#datasets.costandusage.availabilityzone)+}                                        | Dimension          | Recommended   | True         | String    |
| [Billed [-Cost](#billedcost)-]{+Cost](#datasets.costandusage.billedcost)+}                                                    | Metric             | Mandatory     | False        | Decimal   |
| [Billing Account [-ID](#billingaccountid)-]{+ID](#datasets.costandusage.billingaccountid)+}                                       | Dimension          | Mandatory     | False        | String    |
| [Billing Account [-Name](#billingaccountname)-]{+Name](#datasets.costandusage.billingaccountname)+}                                   | Dimension          | Mandatory     | True         | String    |
| [Billing Account [-Type](#billingaccounttype)-]{+Type](#datasets.costandusage.billingaccounttype)+}                                   | Dimension          | Conditional   | False        | String    |
| [Billing [-Currency](#billingcurrency)-]{+Currency](#datasets.costandusage.billingcurrency)+}                                          | Dimension          | Mandatory     | False        | String    |
| [Billing Period [-End](#billingperiodend)-]{+End](#datasets.costandusage.billingperiodend)+}                                       | Dimension          | Mandatory     | False        | Date/Time |
| [Billing Period [-Start](#billingperiodstart)-]{+Start](#datasets.costandusage.billingperiodstart)+}                                   | Dimension          | Mandatory     | False        | Date/Time |
| [Capacity Reservation [-ID](#capacityreservationid)-]{+ID](#datasets.costandusage.capacityreservationid)+}                             | Dimension          | Conditional   | True         | String    |
| [Capacity Reservation [-Status](#capacityreservationstatus)-]{+Status](#datasets.costandusage.capacityreservationstatus)+}                     | Dimension          | Conditional   | True         | String    |
| [Charge [-Category](#chargecategory)-]{+Category](#datasets.costandusage.chargecategory)+}                                            | Dimension          | Mandatory     | False        | String    |
| [Charge [-Class](#chargeclass)-]{+Class](#datasets.costandusage.chargeclass)+}                                                  | Dimension          | Mandatory     | True         | String    |
| [Charge [-Description](#chargedescription)-]{+Description](#datasets.costandusage.chargedescription)+}                                      | Dimension          | Mandatory     | True         | String    |
| [Charge [-Frequency](#chargefrequency)-]{+Frequency](#datasets.costandusage.chargefrequency)+}                                          | Dimension          | Recommended   | False        | String    |
| [Charge Period [-End](#chargeperiodend)-]{+End](#datasets.costandusage.chargeperiodend)+}                                         | Dimension          | Mandatory     | False        | Date/Time |
| [Charge Period [-Start](#chargeperiodstart)-]{+Start](#datasets.costandusage.chargeperiodstart)+}                                     | Dimension          | Mandatory     | False        | Date/Time |
| [Commitment Discount [-Category](#commitmentdiscountcategory)-]{+Category](#datasets.costandusage.commitmentdiscountcategory)+}                   | Dimension          | Conditional   | True         | String    |
| [Commitment Discount [-ID](#commitmentdiscountid)-]{+ID](#datasets.costandusage.commitmentdiscountid)+}                               | Dimension          | Conditional   | True         | String    |
| [Commitment Discount [-Name](#commitmentdiscountname)-]{+Name](#datasets.costandusage.commitmentdiscountname)+}                           | Dimension          | Conditional   | True         | String    |
| [Commitment Discount [-Quantity](#commitmentdiscountquantity)-]{+Quantity](#datasets.costandusage.commitmentdiscountquantity)+}                   | Metric             | Conditional   | True         | Decimal   |
| [Commitment Discount [-Status](#commitmentdiscountstatus)-]{+Status](#datasets.costandusage.commitmentdiscountstatus)+}                       | Dimension          | Conditional   | True         | String    |
| [Commitment Discount [-Type](#commitmentdiscounttype)-]{+Type](#datasets.costandusage.commitmentdiscounttype)+}                           | Dimension          | Conditional   | True         | String    |
| [Commitment Discount [-Unit](#commitmentdiscountunit)-]{+Unit](#datasets.costandusage.commitmentdiscountunit)+}                           | Dimension          | Conditional   | True         | String    |
| [Consumed [-Quantity](#consumedquantity)-]{+Quantity](#datasets.costandusage.consumedquantity)+}                                        | Metric             | Conditional   | True         | Decimal   |
| [Consumed [-Unit](#consumedunit)-]{+Unit](#datasets.costandusage.consumedunit)+}                                                | Dimension          | Conditional   | True         | String    |
| [Contract [-Applied](#contractapplied)-]{+Applied](#datasets.costandusage.contractapplied)+}                                          | Dimension / Metric | Conditional   | True         | JSON      |
| [Contracted [-Cost](#contractedcost)-]{+Cost](#datasets.costandusage.contractedcost)+}                                            | Metric             | Mandatory     | False        | Decimal   |
| [Contracted Unit [-Price](#contractedunitprice)-]{+Price](#datasets.costandusage.contractedunitprice)+}                                 | Metric             | Conditional   | True         | Decimal   |
| [Effective [-Cost](#effectivecost)-]{+Cost](#datasets.costandusage.effectivecost)+}                                              | Metric             | Mandatory     | False        | Decimal   |
| [Host Provider [-Name](#hostprovidername)-]{+Name](#datasets.costandusage.hostprovidername)+}                                       | Dimension          | Mandatory     | False        | String    |
| [Invoice [-ID](#invoiceid)-]{+Detail ID](#datasets.costandusage.invoicedetailid)                                                      | Dimension          | Recommended   | True         | String    |+}
{+| [Invoice ID](#datasets.costandusage.invoiceid)+}                                                      | Dimension          | Recommended   | True         | String    |
| [Invoice Issuer [-Name](#invoiceissuername)-]{+Name](#datasets.costandusage.invoiceissuername)+}                                     | Dimension          | Mandatory     | False        | String    |
| [List [-Cost](#listcost)-]{+Cost](#datasets.costandusage.listcost)+}                                                        | Metric             | Mandatory     | False        | Decimal   |
| [List Unit [-Price](#listunitprice)-]{+Price](#datasets.costandusage.listunitprice)+}                                             | Metric             | Conditional   | True         | Decimal   |
| [Pricing [-Category](#pricingcategory)-]{+Category](#datasets.costandusage.pricingcategory)+}                                          | Dimension          | Conditional   | True         | String    |
| [Pricing [-Currency](#pricingcurrency)-]{+Currency](#datasets.costandusage.pricingcurrency)+}                                          | Dimension          | Conditional   | [-True-]{+False+}        | String    |
| [Pricing Currency Contracted Unit [-Price](#pricingcurrencycontractedunitprice)-]{+Price](#datasets.costandusage.pricingcurrencycontractedunitprice)+} | Metric             | Conditional   | True         | Decimal   |
| [Pricing Currency Effective [-Cost](#pricingcurrencyeffectivecost)-]{+Cost](#datasets.costandusage.pricingcurrencyeffectivecost)+}              | Metric             | Conditional   | [-True-]{+False+}        | Decimal   |
| [Pricing Currency List Unit [-Price](#pricingcurrencylistunitprice)-]{+Price](#datasets.costandusage.pricingcurrencylistunitprice)+}             | Metric             | Conditional   | True         | Decimal   |
| [Pricing [-Quantity](#pricingquantity)-]{+Quantity](#datasets.costandusage.pricingquantity)+}                                          | Metric             | Mandatory     | True         | Decimal   |
| [Pricing [-Unit](#pricingunit)-]{+Unit](#datasets.costandusage.pricingunit)+}                                                  | Dimension          | Mandatory     | True         | String    |
|[-[Provider - DEPRECATED](#providername)                                        | Dimension          | Mandatory     | False        | String    |-]
[-| [Publisher - DEPRECATED](#publishername)                                      | Dimension          | Mandatory     | False        | String    |-]
[-|-] [Region [-ID](#regionid)-]{+ID](#datasets.costandusage.regionid)+}                                                        | Dimension          | Conditional   | True         | String    |
| [Region [-Name](#regionname)-]{+Name](#datasets.costandusage.regionname)+}                                                    | Dimension          | Conditional   | True         | String    |
| [Resource [-ID](#resourceid)-]{+ID](#datasets.costandusage.resourceid)+}                                                    | Dimension          | Conditional   | True         | String    |
| [Resource [-Name](#resourcename)-]{+Name](#datasets.costandusage.resourcename)+}                                                | Dimension          | Conditional   | True         | String    |
| [Resource [-Type](#resourcetype)-]{+Type](#datasets.costandusage.resourcetype)+}                                                | Dimension          | Conditional   | True         | String    |
| [Service [-Category](#servicecategory)-]{+Category](#datasets.costandusage.servicecategory)+}                                          | Dimension          | Mandatory     | False        | String    |
| [Service [-Name](#servicename)-]{+Name](#datasets.costandusage.servicename)+}                                                  | Dimension          | Mandatory     | False        | String    |
| [Service Provider [-Name](#serviceprovidername)-]{+Name](#datasets.costandusage.serviceprovidername)+}                                 | Dimension          | Mandatory     | False        | String    |
| [Service [-Subcategory](#servicesubcategory)-]{+Subcategory](#datasets.costandusage.servicesubcategory)+}                                    | Dimension          | Recommended   | False        | String    |
| [SKU [-ID](#skuid)-]{+ID](#datasets.costandusage.skuid)+}                                                              | Dimension          | Conditional   | True         | String    |
| [SKU [-Meter](#skumeter)-]{+Meter](#datasets.costandusage.skumeter)+}                                                        | Dimension          | Conditional   | True         | String    |
| [SKU Price [-Details](#skupricedetails)-]{+Details](#datasets.costandusage.skupricedetails)+}                                         | Dimension          | Conditional   | True         | JSON      |
| [SKU Price [-ID](#skupriceid)-]{+ID](#datasets.costandusage.skupriceid)+}                                                   | Dimension          | Conditional   | True         | String    |
| [Sub Account [-ID](#subaccountid)-]{+ID](#datasets.costandusage.subaccountid)+}                                               | Dimension          | Conditional   | True         | String    |
| [Sub Account [-Name](#subaccountname)-]{+Name](#datasets.costandusage.subaccountname)+}                                           | Dimension          | Conditional   | True         | String    |
| [Sub Account [-Type](#subaccounttype)-]{+Type](#datasets.costandusage.subaccounttype)+}                                           | Dimension          | Conditional   | True         | String    |
| [-[Tags](#tags)-]{+[Tags](#datasets.costandusage.tags)+}                                                                 | Dimension          | Conditional   | True         | JSON      |

[-<div class='h4-nonindex'>Relationships</div>-]{+## Relationships<!--SkipTOC-->+}

The Cost and Usage dataset can be joined to the Contract Commitment dataset through the use of the Contract Commitment ID.

@@ -85,29 +84,95 @@ The Cost and Usage dataset can be joined to the Contract Commitment dataset thro
| ------------------- | ----------------- | ------------------- | ---------------------- |
| Cost and Usage      | Contract Applied  | Contract Commitment | Contract Commitment ID |

[-<div class='h4-nonindex'>Requirements</div>-]{+## Requirements<!--SkipTOC-->+}

CostAndUsage [-adheres-]{+MUST adhere+} to the following requirements:

* CostAndUsage MUST be present.
* CostAndUsage {+column presence MUST adhere to the following requirements:+}
{+  * CostAndUsage SHOULD include [AllocatedMethodDetails](#datasets.costandusage.allocatedmethoddetails) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).+}
{+  * CostAndUsage MUST include [AllocatedMethodId](#datasets.costandusage.allocatedmethodid) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).+}
{+  * CostAndUsage MUST include [AllocatedResourceId](#datasets.costandusage.allocatedresourceid) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).+}
{+  * CostAndUsage MUST include [AllocatedResourceName](#datasets.costandusage.allocatedresourcename) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).+}
{+  * CostAndUsage MUST include [AllocatedTags](#datasets.costandusage.allocatedtags) when the service provider supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).+}
{+  * CostAndUsage SHOULD include [AvailabilityZone](#datasets.costandusage.availabilityzone) when the host provider supports deploying resources or services within an *availability zone*.+}
{+  * CostAndUsage MUST include [BilledCost](#datasets.costandusage.billedcost).+}
{+  * CostAndUsage MUST include [BillingAccountId](#datasets.costandusage.billingaccountid).+}
{+  * CostAndUsage MUST include [BillingAccountName](#datasets.costandusage.billingaccountname).+}
{+  * CostAndUsage MUST include [BillingAccountType](#datasets.costandusage.billingaccounttype) when the invoice issuer supports more than one possible BillingAccountType value.+}
{+  * CostAndUsage MUST include [BillingCurrency](#datasets.costandusage.billingcurrency).+}
{+  * CostAndUsage MUST include [BillingPeriodEnd](#datasets.costandusage.billingperiodend).+}
{+  * CostAndUsage MUST include [BillingPeriodStart](#datasets.costandusage.billingperiodstart).+}
{+  * CostAndUsage MUST include [CapacityReservationId](#datasets.costandusage.capacityreservationid) when the service provider supports *capacity reservations*.+}
{+  * CostAndUsage MUST include [CapacityReservationStatus](#datasets.costandusage.capacityreservationstatus) when the service provider supports *capacity reservations*.+}
{+  * CostAndUsage MUST include [ChargeCategory](#datasets.costandusage.chargecategory).+}
{+  * CostAndUsage MUST include [ChargeClass](#datasets.costandusage.chargeclass).+}
{+  * CostAndUsage MUST include [ChargeDescription](#datasets.costandusage.chargedescription).+}
{+  * CostAndUsage SHOULD include [ChargeFrequency](#datasets.costandusage.chargefrequency).+}
{+  * CostAndUsage MUST include [ChargePeriodEnd](#datasets.costandusage.chargeperiodend).+}
{+  * CostAndUsage MUST include [ChargePeriodStart](#datasets.costandusage.chargeperiodstart).+}
{+  * CostAndUsage MUST include [CommitmentDiscountCategory](#datasets.costandusage.commitmentdiscountcategory) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountName](#datasets.costandusage.commitmentdiscountname) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountQuantity](#datasets.costandusage.commitmentdiscountquantity) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountUnit](#datasets.costandusage.commitmentdiscountunit) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [ConsumedQuantity](#datasets.costandusage.consumedquantity) when the service provider supports the measurement of usage.+}
{+  * CostAndUsage MUST include [ConsumedUnit](#datasets.costandusage.consumedunit) when the service provider supports the measurement of usage.+}
{+  * CostAndUsage MUST include [ContractApplied](#datasets.costandusage.contractapplied) when the service provider supports *contract commitments*.+}
{+  * CostAndUsage MUST include [ContractedCost](#datasets.costandusage.contractedcost).+}
{+  * CostAndUsage MUST include [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) when the service provider supports negotiated pricing concepts.+}
{+  * CostAndUsage MUST include [EffectiveCost](#datasets.costandusage.effectivecost).+}
{+  * CostAndUsage MUST include [HostProviderName](#datasets.costandusage.hostprovidername).+}
{+  * CostAndUsage MUST include [InvoiceDetailId](#datasets.costandusage.invoicedetailid).+}
{+  * CostAndUsage MUST include [InvoiceId](#datasets.costandusage.invoiceid).+}
{+  * CostAndUsage MUST include [InvoiceIssuerName](#datasets.costandusage.invoiceissuername).+}
{+  * CostAndUsage MUST include [ListCost](#datasets.costandusage.listcost).+}
{+  * CostAndUsage MUST include [ListUnitPrice](#datasets.costandusage.listunitprice) when the service provider publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include [PricingCategory](#datasets.costandusage.pricingcategory) when the service provider supports more than one pricing category across all [*SKUs*](#glossary:sku).+}
{+  * CostAndUsage MUST include [PricingCurrency](#datasets.costandusage.pricingcurrency) when the service provider supports pricing and billing in different currencies.+}
{+  * CostAndUsage MUST include [PricingCurrencyContractedUnitPrice](#datasets.costandusage.pricingcurrencycontractedunitprice) when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include [PricingCurrencyEffectiveCost](#datasets.costandusage.pricingcurrencyeffectivecost) when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include [PricingCurrencyListUnitPrice](#datasets.costandusage.pricingcurrencylistunitprice) when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include [PricingQuantity](#datasets.costandusage.pricingquantity).+}
{+  * CostAndUsage MUST include [PricingUnit](#datasets.costandusage.pricingunit).+}
{+  * CostAndUsage MUST include [RegionId](#datasets.costandusage.regionid) when the host provider supports deploying resources or services within a region.+}
{+  * CostAndUsage MUST include [RegionName](#datasets.costandusage.regionname) when the host provider supports deploying resources or services within a region.+}
{+  * CostAndUsage MUST include [ResourceId](#datasets.costandusage.resourceid) when the service provider supports billing based on provisioned *resources*.+}
{+  * CostAndUsage MUST include [ResourceName](#datasets.costandusage.resourcename) when the service provider supports billing based on provisioned resources.+}
{+  * CostAndUsage MUST include [ResourceType](#datasets.costandusage.resourcetype) when the service provider supports billing based on provisioned *resources* and supports assigning types to *resources*.+}
{+  * CostAndUsage MUST include [ServiceCategory](#datasets.costandusage.servicecategory).+}
{+  * CostAndUsage MUST include [ServiceName](#datasets.costandusage.servicename).+}
{+  * CostAndUsage MUST include [ServiceProviderName](#datasets.costandusage.serviceprovidername).+}
{+  * CostAndUsage SHOULD include [ServiceSubcategory](#datasets.costandusage.servicesubcategory).+}
{+  * CostAndUsage MUST include [SkuId](#datasets.costandusage.skuid) when the service provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.+}
{+  * CostAndUsage MUST include [SkuMeter](#datasets.costandusage.skumeter) when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.+}
{+  * CostAndUsage MUST include [SkuPriceDetails](#datasets.costandusage.skupricedetails) when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.+}
{+  * CostAndUsage MUST include [SkuPriceId](#datasets.costandusage.skupriceid) when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.+}
{+  * CostAndUsage MUST include [SubAccountId](#datasets.costandusage.subaccountid) when the service provider supports a *sub account* construct.+}
{+  * CostAndUsage MUST include [SubAccountName](#datasets.costandusage.subaccountname) when the service provider supports a *sub account* construct.+}
{+  * CostAndUsage MUST include [SubAccountType](#datasets.costandusage.subaccounttype) when the service provider supports more than one possible SubAccountType value.+}
{+  * CostAndUsage MUST include [Tags](#datasets.costandusage.tags) when the data generator supports setting user or provider-defined tags.+}
{+* CostAndUsage MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.+}
{+* CostAndUsage+} MUST conform to [-[ColumnHandling](#columnhandling)-]{+[NullHandling](#attributes.nullhandling)+} requirements.
* CostAndUsage MUST conform to [-[NullHandling](#nullhandling)-]{+[DiscountHandling](#attributes.discounthandling)+} requirements.
* CostAndUsage MUST conform to [-[DiscountHandling](#discounthandling)-]{+[InvoiceHandling](#attributes.invoicehandling)+} requirements.
* CostAndUsage MUST conform to [-[InvoiceHandling](#invoicehandling)-]{+[DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling)+} requirements.
* CostAndUsage MUST conform to [-[DataGeneratorCalculatedSplitCostAllocationHandling](#datagenerator-calculatedsplitcostallocationhandling)-]{+[DatasetConfiguration](#attributes.datasetconfiguration)+} requirements.

[-<div class='h4-nonindex'>Dataset ID</div>-]{+## Dataset ID<!--SkipTOC-->+}

CostAndUsage

[-<div class='h4-nonindex'>Display Name</div>-]{+## Display Name<!--SkipTOC-->+}

Cost and Usage

[-<div class='h4-nonindex'>Description</div>-]{+## Description<!--SkipTOC-->+}

Describes the cost and usage incurred through using or purchasing a service provider's [*resources*](#glossary:resource) or [*services*](#glossary:service).

[-<div class='h4-nonindex'>Introduced (version)</div>-]{+## Introduced (version)<!--SkipTOC-->+}

0.5
