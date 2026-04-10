# Commitment Program Eligibility Details

Commitment Program Eligibility Details identifies the [*commitment programs*](#glossary:commitment-program) that could potentially cover [*charges*](#glossary:charge), subject to [*service provider*](#glossary:service-provider) constraints. By distinguishing the pool of spend that was eligible to be covered, Commitment Program Eligibility Details provides the fundamental denominator for calculating precise commitment coverage metrics. This allows FinOps practitioners to accurately size the pool of uncovered spend that could realistically be covered by a future commitment. In this context, *commitment programs* include both discount-bearing programs (e.g., Flexible Spend Plans, Resource Reservations) and advance resource commitments (e.g., Advance Resource Commitments), provided the service provider treats them as [*commitments*](#glossary:commitment).

## Requirements

CommitmentProgramEligibilityDetails MUST adhere to the following requirements:

* CommitmentProgramEligibilityDetails MUST be of type String.
* CommitmentProgramEligibilityDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentProgramEligibilityDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* CommitmentProgramEligibilityDetails MUST NOT be null when a charge is eligible for a [*commitment program*](#glossary:commitment-program), regardless of whether a [*commitment*](#glossary:commitment) was actually applied to the charge.
* CommitmentProgramEligibilityDetails MUST NOT reflect restrictions (e.g., transient account configurations, quotas) that might temporarily prevent purchase or participation in a *commitment program*.
* CommitmentProgramEligibilityDetails MUST include all publicly available *commitment programs* for which the usage is eligible.
* CommitmentProgramEligibilityDetails MAY include negotiated *commitment programs* when the usage is eligible and the program is not broadly applicable across the service provider's service catalog.
* CommitmentProgramEligibilityDetails MUST NOT include data related to *commitment* [*periods*](#glossary:period) or payment options.
* CommitmentProgramEligibilityDetails MUST conform to [CommitmentProgramEligibilityDetailsObject](#datasets.costandusage.commitmentprogrameligibilitydetails.commitmentprogrameligibilitydetailsobject) requirements when CommitmentProgramEligibilityDetails is not null.

## Column ID

CommitmentProgramEligibilityDetails

## Display Name

Commitment Program Eligibility Details

## Description

The types of [*commitment programs*](#glossary:commitment-program) available for a specific usage row.

## Content Constraints

| Constraint    | Value                                                                                                                        |
|:-------------------------------------|:---------------------------------|
| Dataset       | [Cost and Usage](#datasets.costandusage)                                                                                     |
| Column type   | Dimension                                                                                                                    |
| Feature level | Conditional                                                                                                                  |
| Allows nulls  | True                                                                                                                         |
| Data type     | JSON                                                                                                                         |
| Value format  | [JsonObjectFormat](#attributes.jsonobjectformat)                                                                             |
| Object        | [CommitmentProgramEligibilityDetailsObject](#datasets.costandusage.commitmentprogrameligibilitydetails.commitmentprogrameligibilitydetailsobject) |

## Introduced (version)

1.4
