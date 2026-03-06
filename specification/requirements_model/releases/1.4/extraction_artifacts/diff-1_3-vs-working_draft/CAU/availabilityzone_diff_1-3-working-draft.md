## Diff

diff --git a/specification/datasets/cost_and_usage/columns/availabilityzone.md b/specification/datasets/cost_and_usage/columns/availabilityzone.md
index 289843a9..e24d7a8a 100644
--- a/specification/datasets/cost_and_usage/columns/availabilityzone.md
+++ b/specification/datasets/cost_and_usage/columns/availabilityzone.md
@@ -4,11 +4,10 @@ An [*availability zone*](#glossary:availability-zone) is a host-provider-assigne

## Requirements

AvailabilityZone [-adheres-]{+MUST adhere+} to the following requirements:

[-* AvailabilityZone is RECOMMENDED to be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within an *availability zone*.-]
* AvailabilityZone MUST be of type String.
* AvailabilityZone MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* AvailabilityZone MUST be null when a [*charge*](#glossary:charge) is not specific to an *availability zone*.

## Column ID
@@ -25,13 +24,14 @@ A host-provider-assigned identifier for a physically separated and isolated area

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Recommended                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

