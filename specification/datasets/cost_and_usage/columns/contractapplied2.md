# Contract Applied

Contract Applied is a set of properties that associate a charge with one or more [*contract commitments*](#glossary:contract-commitment), denoted as key-value pairs in a JSON object.  Contract Applied allows the practitioner to track the progress of the commitments to which they have agreed with a service provider.

The FOCUS-defined properties are:

* `Contract ID`: The unique identifier representing a single contract.
* `Contract Commitment ID`: The unique identifier representing a single contract term.
* `Contract Commitment Applied Cost`: The value of the charge applied to a single contract term.
* `Contract Commitment Applied Quantity`: The usage of the charge applied to a single contract term.
* `Contract Commitment Applied Unit`: The unit of measure for the usage of the charge applied to a single contract term.

In addition to these, a data generator may include one or more custom properties, also denoted as key-value pairs.

## Requirements

### Content Requirements

The following keys are used for contract application properties to facilitate querying data across allocations and across service providers. FOCUS-defined keys will appear in the list below, and custom keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

<b>Contract ID</b>

Contract ID is a service-provider-assigned identifier for a contract describing the agreed terms between a service provider and a customer.  Contracts can include commitment to a certain amount of spend or usage over an agreed period of time.

"ContractId" property MUST adhere to the following requirements:

* "ContractId" MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *contract commitments*.
* "ContractId" MUST be of type String.
* "ContractId" MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* "ContractId" nullability is defined as follows:
  * "ContractId" MUST be null when a [*charge*](#glossary:charge) is not related to a *contract commitment*.
  * "ContractId" MUST NOT be null when a *charge* is related to a *contract commitment*.
* When "ContractId" is not null, "ContractId" MUST adhere to the following requirements:
  * "ContractId" MUST be a unique identifier within the service provider.
  * "ContractId" SHOULD be a fully-qualified identifier.

<b>Contract Commitment ID</b>

A Contract Commitment ID is a service-provider-assigned identifier describing an agreement agreed between a service provider and a customer.  Contracts can include commitment to a certain amount of spend or usage over an agreed period of time.

"ContractCommitmentID" property MUST adhere to the following requirements:

* "ContractCommitmentID" MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *contract commitments*.
* "ContractCommitmentID" MUST be of type String.
* "ContractCommitmentID" MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* "ContractCommitmentID" nullability is defined as follows:
  * "ContractCommitmentID" MUST be null when a [*charge*](#glossary:charge) is not related to a *contract commitment*.
  * "ContractCommitmentID" MUST NOT be null when a *charge* is related to a *contract commitment*.
* When "ContractCommitmentID" is not null, "ContractCommitmentID" MUST adhere to the following requirements:
  * "ContractCommitmentID" MUST be a unique identifier within the service provider.
  * "ContractCommitmentID" SHOULD be a fully-qualified identifier.
  * "ContractCommitmentID" MUST have one and only one parent "ContractID".
  * "ContractCommitmentID" MUST be equal to ResourceID when ChargeCategory is "Purchase" and the charge represents a purchase of that contract commitment.
  * "ContractCommitmentID" MUST be equal to ResourceID when ChargeCategory is "Usage" and the charge represents an unused portion of that contract commitment.
  * "ContractCommitmentID" MAY be equal to "ContractID".

<b>Contract Commitment Applied Cost</b>

Contract Commitment Applied Cost represents the cost of the charge applied to the contract line item.  Contract Commitment Applied Cost is associated with the contract line item via Contract Commitment ID.  Contract Commitment Applied Cost is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a service provider and a customer.

"ContractCommitmentAppliedCost" property MUST adhere to the following requirements:

* "ContractCommitmentAppliedCost" MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider associates the *charge's* value with one or more *contract commitments*.
* "ContractCommitmentAppliedCost" MUST be of type Decimal.
* "ContractCommitmentAppliedCost" MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* "ContractCommitmentAppliedCost" MUST adhere to the following nullability requirements:
  * "ContractCommitmentAppliedCost" MUST NOT be null when "ContractCommitmentAppliedQuantity" is null.
  * "ContractCommitmentAppliedCost" MAY be null in all other cases.
* "ContractCommitmentAppliedCost" MUST be a valid decimal value.
* "ContractCommitmentAppliedCost" MUST be denominated in the BillingCurrency.

## Column ID

ContractApplied

## Display Name

Contract Applied

## Description

A set of properties that associate a charge with one or more [*contract commitments*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :----------------------------------------------------|
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension and Metric                                 |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | JSON                                                 |
| Value format    | [JSON Object Format](#attributes.jsonobjectformat)   |

## Introduced (version)

1.3
