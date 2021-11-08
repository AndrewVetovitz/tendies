use serde::Deserialize;

#[derive(Debug, Deserialize, )]
pub struct TickerStructure {
    filters: String,
    table: TickerData,
    rows: Vec<TickerData>,
    message: String,
    status: TickerResponseStatus
}

#[derive(Debug, Deserialize)]
pub struct TickerData {
    symbol: String,
    name: String,
    lastsale: String,
    netchange: String,
    pctchange: String,
    marketCap: String
}

#[derive(Debug, Deserialize)]
pub struct TickerResponseStatus {
    rCode: String,
    bCodeMessage: String,
    developerMessage: String
}
