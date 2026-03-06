## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractperiodend.md b/specification/datasets/contract_commitment/columns/contractperiodend.md
index f12fba6c..1fd7351c 100644
--- a/specification/datasets/contract_commitment/columns/contractperiodend.md
+++ b/specification/datasets/contract_commitment/columns/contractperiodend.md
@@ -1,14 +1,13 @@
# Contract Period End

Contract Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound) of a [*contract period*](#glossary:contractperiod). For example, a time period where [Contract Period [-Start](#contractperiodstart)-]{+Start](#datasets.contractcommitment.contractperiodstart)+} is '2024-01-01T00:00:00Z' and Contract Period End is '2024-01-02T00:00:00Z' includes January 1 2024 since Contract Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound), but does not include January 1 2025 since Contract Period End represents the *exclusive end bound*.

## Requirements

ContractPeriodEnd [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractPeriodEnd MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractPeriodEnd MUST be of type Date/Time.
* ContractPeriodEnd MUST conform to [-[DateTimeFormat](#date/timeformat)-]{+[DateTimeFormat](#attributes.date/timeformat)+} requirements.
* ContractPeriodEnd MUST NOT be null.
* ContractPeriodEnd MUST be the *exclusive end bound* of the effective period of the *contract*.

@@ -26,13 +25,14 @@ The *exclusive end bound* of a *contract period*.

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

