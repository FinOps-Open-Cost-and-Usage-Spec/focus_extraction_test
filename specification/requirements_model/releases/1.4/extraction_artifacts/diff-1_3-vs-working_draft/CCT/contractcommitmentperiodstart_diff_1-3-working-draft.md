## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractcommitmentperiodstart.md b/specification/datasets/contract_commitment/columns/contractcommitmentperiodstart.md
index 4734caf5..00664697 100644
--- a/specification/datasets/contract_commitment/columns/contractcommitmentperiodstart.md
+++ b/specification/datasets/contract_commitment/columns/contractcommitmentperiodstart.md
@@ -1,14 +1,13 @@
# Contract Commitment Period Start

Contract Commitment Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound) of a [*contract commitment period*](#glossary:contractcommitmentperiod). For example, a time period where Contract Commitment Period Start is '2024-01-01T00:00:00Z' and [Contract Commitment [-End](#contractcommitmentperiodend)-]{+End](#datasets.contractcommitment.contractcommitmentperiodend)+} is '2025-01-01T00:00:00Z' includes January 1 2024 since Contract Commitment Period Start represents the *inclusive start bound*, but does not include *charges* for January 2 2025 since Contract Commitment Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound).

## Requirements

ContractCommitmentPeriodStart [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentPeriodStart MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentPeriodStart MUST be of type Date/Time.
* ContractCommitmentPeriodStart MUST conform to [-[DateTimeFormat](#date/timeformat)-]{+[DateTimeFormat](#attributes.date/timeformat)+} requirements.
* ContractCommitmentPeriodStart MUST NOT be null.
* ContractCommitmentPeriodStart MUST be the *inclusive start bound* of the effective period of the *contract commitment*.

@@ -26,13 +25,14 @@ The *inclusive start bound* of a *contract commitment period*.

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-------------------------------------|-]{+|:----------------|:-----------------------------------------------------|+}
{+| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |+}
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Date/Time                                            |
| Value format    | [Date/Time [-Format](#date/timeformat)-]{+Format](#attributes.date/timeformat)+}      |

## Introduced (version)

