## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractcommitmentperiodend.md b/specification/datasets/contract_commitment/columns/contractcommitmentperiodend.md
index 4996a4ca..bae427e5 100644
--- a/specification/datasets/contract_commitment/columns/contractcommitmentperiodend.md
+++ b/specification/datasets/contract_commitment/columns/contractcommitmentperiodend.md
@@ -1,14 +1,13 @@
# Contract Commitment Period End

Contract Commitment Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound) of a [*contract commitment period*](#glossary:contractcommitmentperiod). For example, a time period where [Contract Commitment Period [-Start](#contractperiodstart)-]{+Start](#datasets.contractcommitment.contractperiodstart)+} is '2024-01-01T00:00:00Z' and Contract Commitment Period End is '2024-01-02T00:00:00Z' includes January 1 2024 since Contract Commitment Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound), but does not include January 1 2025 since Contract Commitment Period End represents the *exclusive end bound*.

## Requirements

ContractCommitmentPeriodEnd [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentPeriodEnd MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentPeriodEnd MUST be of type Date/Time.
* ContractCommitmentPeriodEnd MUST conform to [-[DateTimeFormat](#date/timeformat)-]{+[DateTimeFormat](#attributes.date/timeformat)+} requirements.
* ContractCommitmentPeriodEnd MUST NOT be null.
* ContractCommitmentPeriodEnd MUST be the *exclusive end bound* of the effective period of the *contract commitment*.

@@ -26,13 +25,14 @@ The *exclusive end bound* of a *contract commitment period*.

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

