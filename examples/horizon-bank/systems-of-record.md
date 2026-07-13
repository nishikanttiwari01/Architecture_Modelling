# Horizon Bank System-of-Record Catalogue

Authority is qualified by entity, attribute group, lifecycle, legal entity and effective time. Application IDs remain gaps until the full application catalogue is established.

| ID | Name | Definition | Type | Owner | Organisational Scope | Record Status | Relationships | Source Type | Gap |
|---|---|---|---|---|---|---|---|---|---|
| HB-SOR-01 | Party Identity Authority | Authority for verified identity attributes during active and retained relationship states | Authority decision | Customer Data Owner | Group and country | Proposed | HB-DATA-01 | Author model | Application ID and country exceptions pending |
| HB-SOR-02 | Deposit Account Authority | Authority for deposit account state, balance and holds by country entity and effective time | Authority decision | Deposit Data Owner | Country | Proposed | HB-DATA-03; HB-PRD-02; HB-PRD-03 | Author model | Processor application ID pending |
| HB-SOR-03 | Credit Exposure Authority | Authority for facility, loan, limit utilisation and exposure lifecycle state | Authority decision | Credit Data Owner | Group and country | Proposed | HB-DATA-04; HB-PRD-05; HB-PRD-06 | Author model | Attribute-level split pending |
| HB-SOR-04 | General Ledger Authority | Authority for approved legal-entity ledger balances by accounting period | Authority decision | Finance Data Owner | Group and country | Proposed | HB-DATA-05 | Author model | Ledger application ID pending |
