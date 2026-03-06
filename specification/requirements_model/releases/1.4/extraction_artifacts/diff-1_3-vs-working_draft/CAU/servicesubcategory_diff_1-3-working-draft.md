## Diff

diff --git a/specification/datasets/cost_and_usage/columns/servicesubcategory.md b/specification/datasets/cost_and_usage/columns/servicesubcategory.md
index f851df6f..5332603d 100644
--- a/specification/datasets/cost_and_usage/columns/servicesubcategory.md
+++ b/specification/datasets/cost_and_usage/columns/servicesubcategory.md
@@ -1,12 +1,11 @@
# Service Subcategory

The Service Subcategory is a secondary classification of the [Service [-Category](#servicecategory)-]{+Category](#datasets.costandusage.servicecategory)+} for a [*service*](#glossary:service) based on its core function. The Service Subcategory (in conjunction with the Service Category) is commonly used for scenarios like analyzing spend and usage for specific workload types across service providers and tracking the migration of workloads across fundamentally different architectures.  

## Requirements

ServiceSubcategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* ServiceSubcategory is RECOMMENDED to be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ServiceSubcategory MUST be of type String.
* ServiceSubcategory MUST NOT be null.
* ServiceSubcategory MUST be one of the allowed values.
@@ -26,13 +25,14 @@ Secondary classification of the Service Category for a *service* based on its co

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | [-:--------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Recommended                                          |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed Values                                       |

Allowed values:

@@ -81,7 +81,7 @@ Allowed values:
| Internet of Things        | IoT Platforms                         | Unified solution that combines IoT data collection, processing, visualization, and device management.         |
| Internet of Things        | Other (Internet of Things)            | Internet of Things (IoT) services that do not fall into one of the defined subcategories.                     |
| Management and Governance | Architecture                          | Planning, design, and construction of software systems.                                                       |
| Management and Governance | Compliance                            | [-Adherance-]{+Adherence+} to regulatory standards and industry best practices.                                                |
| Management and Governance | Cost Management                       | Monitoring and controlling expenses of systems and services.                                                  |
| Management and Governance | Data Governance                       | Management of the availability, usability, integrity, and security of data.                                   |
| Management and Governance | Disaster Recovery                     | Plans and procedures that ensure systems and services can recover from disruptions.                           |
