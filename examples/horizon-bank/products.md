# Horizon Bank Product Catalogue

The hierarchy distinguishes a product family, a governed product and a sellable or contractable product variant. Level 1 records have no parent. Level 2 and 3 records must reference exactly one parent.

| ID | Name | Definition | Level | Parent ID | Product Family | Product | Product Variant | Owner | Scope | Status | Relationships | Source Type | Gap |
|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|
| HB-PRD-01 | Deposits and Accounts | Products that store customer funds and provide account services | 1 |  | Deposits and Accounts |  |  | Deposit Product Owner | All segments | Current | HB-VS-03 | Author model | Country variants open |
| HB-PRD-02 | Transaction Account | Account for payments, balances and day-to-day servicing | 2 | HB-PRD-01 | Deposits and Accounts | Transaction Account |  | Deposit Product Owner | Retail, SME and Corporate | Current | HB-VS-03; HB-VS-04 | Author model | Fee variants open |
| HB-PRD-03 | Term Deposit | Time-bound deposit with governed interest conditions | 2 | HB-PRD-01 | Deposits and Accounts | Term Deposit |  | Deposit Product Owner | All segments | Current | HB-VS-03 | Author model | Pricing variants open |
| HB-PRD-04 | Credit | Products that create and service credit exposure | 1 |  | Credit |  |  | Chief Credit Officer | All segments | Current | HB-VS-05 | Author model | Product taxonomy open |
| HB-PRD-05 | Consumer and Mortgage Credit | Consumer instalment and mortgage lending products | 2 | HB-PRD-04 | Credit | Consumer and Mortgage Credit |  | Retail Credit Product Owner | Retail | Current | HB-VS-05 | Author model | Local terms open |
| HB-PRD-06 | Business and Corporate Credit | Facilities and loans for SME and corporate customers | 2 | HB-PRD-04 | Credit | Business and Corporate Credit |  | Corporate Credit Product Owner | SME | Current | HB-VS-05 | Author model | Corporate variants open |
| HB-PRD-07 | Payment and Cash Management | Services for initiating, executing and controlling payments and liquidity | 1 |  | Payment and Cash Management |  |  | Payments Product Owner | All segments | Current | HB-VS-04 | Author model | Rail coverage open |
| HB-PRD-08 | Cards and Merchant Services | Card issuing, card processing and merchant-acquiring services | 1 |  | Cards and Merchant Services |  |  | Cards Product Owner | Retail, SME and Corporate | Current | HB-VS-04 | Author model | Scheme choices open |
| HB-PRD-09 | Trade Finance | Documentary and contingent trade products | 1 |  | Trade Finance |  |  | Trade Product Owner | Corporate | Current | HB-VS-03; HB-VS-04 | Author model | Instrument variants open |
| HB-PRD-10 | Investment, Advisory and Custody | Investment, portfolio, custody and asset-servicing products | 1 |  | Investment, Advisory and Custody |  |  | Wealth Product Owner | Private and Institutional | Current | HB-VS-06 | Author model | Suitability and market scope open |
