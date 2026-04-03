## Diff

diff --git a/specification/datasets/contract_commitment/dataset.md b/specification/datasets/contract_commitment/dataset.md
index 69e79ff2..2da59bcc 100644
--- a/specification/datasets/contract_commitment/dataset.md
+++ b/specification/datasets/contract_commitment/dataset.md
@@ -2,25 +2,42 @@

The Contract Commitment dataset is a supporting dataset that describes the terms of contracts agreed between a service provider and a customer.

[-<div class='h4-nonindex'>Columns</div>-]{+## Columns<!--SkipTOC-->+}

| Column | Column Type | Feature Level | Allows Nulls | Data Type |
| [--------------------------------------------------------------------]{+:---+} | [-------------]{+:---+} | [---------------]{+:---+} | [--------------]{+:---+} | [-----------]{+:---+} |
| [Billing [-Currency](#billingcurrency-1)-]{+Currency](#datasets.contractcommitment.billingcurrency)+} | Dimension | Mandatory | True | String |
| [Contract Commitment [-Category](#contractcommitmentcategory)-]{+Applicability](#datasets.contractcommitment.contractcommitmentapplicability) | Dimension | Mandatory | False | JSON |+}
{+| [Contract Commitment Benefit Category](#datasets.contractcommitment.contractcommitmentbenefitcategory) | Dimension | Mandatory | False | String |+}
{+| [Contract Commitment Category](#datasets.contractcommitment.contractcommitmentcategory)+} | Dimension | Mandatory | False | String |
| [Contract Commitment [-Cost](#contractcommitmentcost)-]{+Cost](#datasets.contractcommitment.contractcommitmentcost)+} | Metric | Mandatory | True | [-Numeric-]{+Decimal |+}
{+| [Contract Commitment Created](#datasets.contractcommitment.contractcommitmentcreated) | Dimension | Mandatory | False | Date/Time |+}
{+| [Contract Commitment Description](#datasets.contractcommitment.contractcommitmentdescription) | Dimension | Mandatory | True | String+} |
| [Contract Commitment [-Description](#contractcommitmentdescription)-]{+Discount Percentage](#datasets.contractcommitment.contractcommitmentdiscountpercentage)+} | Dimension | Mandatory | True | {+Decimal |+}
{+| [Contract Commitment Duration Type](#datasets.contractcommitment.contractcommitmentdurationtype) | Dimension | Mandatory | False | String |+}
{+| [Contract Commitment Fulfillment Interval](#datasets.contractcommitment.contractcommitmentfulfillmentinterval) | Dimension | Mandatory | False | String |+}
{+| [Contract Commitment ID](#datasets.contractcommitment.contractcommitmentid) | Dimension | Mandatory | False | String |+}
{+| [Contract Commitment Last Updated](#datasets.contractcommitment.contractcommitmentlastupdated) | Dimension | Mandatory | False | Date/Time |+}
{+| [Contract Commitment Lifecycle Status](#datasets.contractcommitment.contractcommitmentlifecyclestatus) | Dimension | Mandatory | False | String |+}
{+| [Contract Commitment Model](#datasets.contractcommitment.contractcommitmentmodel) | Dimension | Mandatory | False | String |+}
{+| [Contract Commitment Offer Category](#datasets.contractcommitment.contractcommitmentoffercategory) | Dimension | Mandatory | False | String |+}
{+| [Contract Commitment Payment Interval](#datasets.contractcommitment.contractcommitmentpaymentinterval) | Dimension | Mandatory | False |+} String |
| [Contract Commitment [-ID](#contractcommitmentid-1)-]{+Payment Model](#datasets.contractcommitment.contractcommitmentpaymentmodel)+} | Dimension | Mandatory | False | String |
| [Contract Commitment {+Payment Upfront Percentage](#datasets.contractcommitment.contractcommitmentpaymentupfrontpercentage) | Dimension | Conditional | False | Decimal |+}
{+| [Contract Commitment+} Period [-End](#contractcommitmentperiodend)-]{+End](#datasets.contractcommitment.contractcommitmentperiodend)+} | Dimension | Mandatory | False | Date/Time |
| [Contract Commitment Period [-Start](#contractcommitmentperiodstart)-]{+Start](#datasets.contractcommitment.contractcommitmentperiodstart)+} | Dimension | Mandatory | False | Date/Time |
| [Contract Commitment [-Quantity](#contractcommitmentquantity)-]{+Quantity](#datasets.contractcommitment.contractcommitmentquantity)+} | Metric | Mandatory | True | [-Numeric-]{+Decimal+} |
| [Contract Commitment [-Type](#contractcommitmenttype)-]{+Type](#datasets.contractcommitment.contractcommitmenttype)+} | Dimension | Mandatory | False | String |
| [Contract Commitment [-Unit](#contractcommitmentunit)-]{+Unit](#datasets.contractcommitment.contractcommitmentunit)+} | Dimension | Mandatory | True | String |
| [Contract [-ID](#contractid-1)-]{+ID](#datasets.contractcommitment.contractid)+} | Dimension | Mandatory | False | String |
| [Contract Period [-End](#contractperiodend)-]{+End](#datasets.contractcommitment.contractperiodend)+} | Dimension | Mandatory | False | Date/Time |
| [Contract Period [-Start](#contractperiodstart)-]{+Start](#datasets.contractcommitment.contractperiodstart)+} | Dimension | Mandatory | False | Date/Time |
[-<div class='h4-nonindex'>Relationships</div>-]{+| [Invoice Issuer Name](#datasets.contractcommitment.invoiceissuername) | Dimension | Mandatory | False | String |+}
{+| [Pricing Currency](#datasets.contractcommitment.pricingcurrency) | Dimension | Conditional | False | String |+}
{+| [Pricing Currency Contract Commitment Cost](#datasets.contractcommitment.pricingcurrencycontractcommitmentcost) | Metric | Conditional | True | Decimal |+}
{+| [Service Provider Name](#datasets.contractcommitment.serviceprovidername) | Dimension | Mandatory | False | String |+}

{+## Relationships<!--SkipTOC-->+}

The Contract Commitment dataset can be joined to the Cost and Usage dataset through the use of Contract Commitment ID.

@@ -31,26 +48,61 @@ The Contract Commitment dataset can be joined to the Cost and Usage dataset thro
| ------------------- | ---------------------- | -------------- | -----------------|
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Applied |

[-<div class='h4-nonindex'>Requirements</div>-]{+## Requirements<!--SkipTOC-->+}

ContractCommitment [-adheres-]{+MUST adhere+} to the following requirements:

* ContractCommitment MUST be present when the service provider supports *contract commitments*.
* ContractCommitment {+column presence MUST adhere to the following requirements:+}
{+  * ContractCommitment MUST include [BillingCurrency](#datasets.contractcommitment.billingcurrency).+}
{+  * ContractCommitment MUST include [ContractCommitmentApplicability](#datasets.contractcommitment.contractcommitmentapplicability).+}
{+  * ContractCommitment MUST include [ContractCommitmentBenefitCategory](#datasets.contractcommitment.contractcommitmentbenefitcategory).+}
{+  * ContractCommitment MUST include [ContractCommitmentCategory](#datasets.contractcommitment.contractcommitmentcategory).+}
{+  * ContractCommitment MUST include [ContractCommitmentCost](#datasets.contractcommitment.contractcommitmentcost).+}
{+  * ContractCommitment MUST include [ContractCommitmentCreated](#datasets.contractcommitment.contractcommitmentcreated).+}
{+  * ContractCommitment MUST include [ContractCommitmentDescription](#datasets.contractcommitment.contractcommitmentdescription).+}
{+  * ContractCommitment MUST include [ContractCommitmentDiscountPercentage](#datasets.contractcommitment.contractcommitmentdiscountpercentage).+}
{+  * ContractCommitment MUST include [ContractCommitmentDurationType](#datasets.contractcommitment.contractcommitmentdurationtype).+}
{+  * ContractCommitment MUST include [ContractCommitmentFulfillmentInterval](#datasets.contractcommitment.contractcommitmentfulfillmentinterval).+}
{+  * ContractCommitment MUST include [ContractCommitmentId](#datasets.contractcommitment.contractcommitmentid).+}
{+  * ContractCommitment MUST include [ContractCommitmentLastUpdated](#datasets.contractcommitment.contractcommitmentlastupdated).+}
{+  * ContractCommitment MUST include [ContractCommitmentLifecycleStatus](#datasets.contractcommitment.contractcommitmentlifecyclestatus).+}
{+  * ContractCommitment MUST include [ContractCommitmentModel](#datasets.contractcommitment.contractcommitmentmodel).+}
{+  * ContractCommitment MUST include [ContractCommitmentOfferCategory](#datasets.contractcommitment.contractcommitmentoffercategory).+}
{+  * ContractCommitment MUST include [ContractCommitmentPaymentInterval](#datasets.contractcommitment.contractcommitmentpaymentinterval).+}
{+  * ContractCommitment MUST include [ContractCommitmentPaymentModel](#datasets.contractcommitment.contractcommitmentpaymentmodel).+}
{+  * ContractCommitment MUST include [ContractCommitmentPaymentUpfrontPercentage](#datasets.contractcommitment.contractcommitmentpaymentupfrontpercentage) when the service provider offers "Partial Upfront" [payment models](#datasets.contractcommitment.contractcommitmentpaymentmodel).+}
{+  * ContractCommitment MUST include [ContractCommitmentPeriodEnd](#datasets.contractcommitment.contractcommitmentperiodend).+}
{+  * ContractCommitment MUST include [ContractCommitmentPeriodStart](#datasets.contractcommitment.contractcommitmentperiodstart).+}
{+  * ContractCommitment MUST include [ContractCommitmentQuantity](#datasets.contractcommitment.contractcommitmentquantity).+}
{+  * ContractCommitment MUST include [ContractCommitmentType](#datasets.contractcommitment.contractcommitmenttype).+}
{+  * ContractCommitment MUST include [ContractCommitmentUnit](#datasets.contractcommitment.contractcommitmentunit).+}
{+  * ContractCommitment MUST include [ContractId](#datasets.contractcommitment.contractid).+}
{+  * ContractCommitment MUST include [ContractPeriodEnd](#datasets.contractcommitment.contractperiodend).+}
{+  * ContractCommitment MUST include [ContractPeriodStart](#datasets.contractcommitment.contractperiodstart).+}
{+  * ContractCommitment MUST include [InvoiceIssuerName](#datasets.contractcommitment.invoiceissuername).+}
{+  * ContractCommitment MUST include [PricingCurrency](#datasets.contractcommitment.pricingcurrency) when the service provider supports pricing and billing in different currencies.+}
{+  * ContractCommitment MUST include [PricingCurrencyContractCommitmentCost](#datasets.contractcommitment.pricingcurrencycontractcommitmentcost) when the service provider supports pricing and billing in different currencies.+}
{+  * ContractCommitment MUST include [ServiceProviderName](#datasets.contractcommitment.serviceprovidername).+}
{+* ContractCommitment MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.+}
{+* ContractCommitment MUST conform to [CorrectionHandling](#attributes.correctionhandling) requirements.+}
{+* ContractCommitment MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.+}
{+* ContractCommitment MUST conform to [DatasetConfiguration](#attributes.datasetconfiguration) requirements.+}
{+* ContractCommitment+} MUST conform to [-[ColumnHandling](#columnhandling)-]{+[DeliveryHandling](#attributes.deliveryhandling)+} requirements.
* ContractCommitment MUST conform to [-[NullHandling](#nullhandling)-]{+[NullHandling](#attributes.nullhandling)+} requirements.

[-<div class='h4-nonindex'>Dataset ID</div>-]{+## Dataset ID<!--SkipTOC-->+}

ContractCommitment

[-<div class='h4-nonindex'>Display Name</div>-]{+## Display Name<!--SkipTOC-->+}

Contract Commitment

[-<div class='h4-nonindex'>Description</div>-]{+## Description<!--SkipTOC-->+}

Describes the terms of contracts agreed between a service provider and a customer.

[-<div class='h4-nonindex'>Introduced (version)</div>-]{+## Introduced (version)<!--SkipTOC-->+}

1.3
