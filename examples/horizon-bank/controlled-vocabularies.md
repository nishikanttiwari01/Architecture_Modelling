# Horizon Bank Controlled Vocabularies

| Vocabulary | Value | Definition |
|---|---|---|
| record_status | Proposed | Awaiting governance decision |
| record_status | Assumed | Accepted fictional baseline pending author refinement |
| record_status | Current | Operates in the fictional current state |
| record_status | Active | Governed and in active use |
| record_status | Retired | No longer active |
| architecture_state | Current | Present architecture |
| architecture_state | Transition | Controlled intermediate architecture |
| architecture_state | Target | Intended architecture direction |
| architecture_state | Not applicable | Architecture state does not apply |
| organisational_scope | Group | Whole banking group |
| organisational_scope | Country | One country organisation |
| organisational_scope | Group and country | Group standard with country implementation |
| legal_entity_scope | Group | Holding or group entity scope |
| legal_entity_scope | Country Bank | Licensed country bank scope |
| legal_entity_scope | Shared Services | Shared-services legal entity scope |
| legal_entity_scope | Multiple legal entities | More than one legal entity |
| jurisdiction_scope | Unspecified | Jurisdiction awaits a governance decision |
| jurisdiction_scope | Country | One jurisdiction |
| jurisdiction_scope | Cross-border | More than one jurisdiction |
| customer_segment_scope | Retail | Retail segment |
| customer_segment_scope | SME | Small and medium-sized enterprise segment |
| customer_segment_scope | Corporate | Corporate segment |
| customer_segment_scope | SME and Corporate | SME and corporate segments |
| customer_segment_scope | Retail and SME | Retail and SME segments |
| customer_segment_scope | Retail, SME and Corporate | Retail, SME and corporate segments |
| customer_segment_scope | Private and Institutional | Private-banking and institutional segments |
| customer_segment_scope | All segments | Every governed customer segment |
| customer_segment_scope | Not applicable | Customer segment does not apply |
| source_type | Author model | Fictional teaching decision created for this book |
| source_type | Official source | Verified primary external source |
| source_type | Derived | Derived from governed records |
| confidence | High | Strong evidence and unambiguous scope |
| confidence | Medium | Useful mapping with interpretation or overlap |
| confidence | Low | Exploratory or incomplete mapping |
| confidence | Pending | Confidence awaits assessment |
| verification_status | Unverified | Not independently checked |
| verification_status | Verified | Checked against its governed source |
| verification_status | Not applicable | Verification does not apply |
| ownership_type | Accountable owner | Role accountable for definition and outcome |
| ownership_type | Steward | Role maintaining controlled information |
| ownership_type | Service owner | Role accountable for an application service |
| ownership_type | Control owner | Role accountable for a control |

## Migration rule

Generic `Scope`, `Status` and `ownership` fields are deprecated. Governed catalogues must use the applicable dimension-specific field and exact vocabulary value. Migration is incremental, and the validator checks every dimension-specific field as soon as it is present.
