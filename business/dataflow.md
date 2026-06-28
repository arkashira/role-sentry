# dataflow.md

## System Dataflow Architecture
### Overview
Role-sentry's dataflow architecture is designed to handle the ingestion, processing, storage, and serving of data related to role-agents, product pipeline, and market signals.

### External Data Sources
External data sources provide the initial input for the dataflow pipeline. These sources include:

| Component | Description |
| --- | --- |
| `market-data-api` | API endpoint for retrieving market data |
| `product-pipeline-api` | API endpoint for retrieving product pipeline data |
| `role-agents-api` | API endpoint for retrieving role-agents data |
| `validated-pain-api` | API endpoint for retrieving validated pain data |

### Ingestion Layer
The ingestion layer is responsible for collecting data from external sources and preparing it for processing. This layer includes:

| Component | Description |
| --- | --- |
| `data-ingester` | Service responsible for collecting data from external sources |
| `data-validator` | Service responsible for validating data integrity |
| `data-normalizer` | Service responsible for normalizing data formats |

### Processing/Transform Layer
The processing/transform layer is responsible for transforming and processing the ingested data into a format suitable for storage and serving. This layer includes:

| Component | Description |
| --- | --- |
| `data-transformer` | Service responsible for transforming data into desired format |
| `data-aggregator` | Service responsible for aggregating data from multiple sources |
| `data-analyzer` | Service responsible for analyzing data for insights |

### Storage Tier
The storage tier is responsible for storing the processed data in a durable and scalable manner. This layer includes:

| Component | Description |
| --- | --- |
| `data-store` | Database or data warehouse for storing processed data |
| `data-indexer` | Service responsible for indexing data for fast querying |

### Query/Serving Layer
The query/serving layer is responsible for serving the stored data to users and applications. This layer includes:

| Component | Description |
| --- | --- |
| `data-query-service` | Service responsible for handling data queries |
| `data-serving-api` | API endpoint for serving data to users and applications |
| `auth-service` | Service responsible for authenticating and authorizing users |

### Egress to User
The egress to user layer is responsible for delivering the served data to the end-user. This layer includes:

| Component | Description |
| --- | --- |
| `data-delivery-service` | Service responsible for delivering data to users |
| `user-interface` | User interface for displaying data to users |

### Auth Boundaries
The following auth boundaries are implemented:

* `data-ingester` and `data-validator` require authentication and authorization to prevent unauthorized data access
* `data-transformer` and `data-aggregator` require authentication and authorization to prevent unauthorized data modification
* `data-query-service` and `data-serving-api` require authentication and authorization to prevent unauthorized data access
* `auth-service` is responsible for authenticating and authorizing users across the system

### ASCII Block Diagram
```
+---------------+
|  External    |
|  Data Sources  |
+---------------+
        |
        |
        v
+---------------+
|  Ingestion    |
|  Layer        |
+---------------+
        |
        |
        v
+---------------+
|  Processing/  |
|  Transform    |
|  Layer        |
+---------------+
        |
        |
        v
+---------------+
|  Storage Tier  |
+---------------+
        |
        |
        v
+---------------+
|  Query/Serving |
|  Layer        |
+---------------+
        |
        |
        v
+---------------+
|  Egress to    |
|  User        |
+---------------+
```
Note: This is a high-level architecture diagram and may require additional details and components based on specific requirements.