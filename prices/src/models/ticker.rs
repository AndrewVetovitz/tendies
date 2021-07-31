pub mod Ticker {
    #[derive(Serialize, Deserialize)]
    pub struct TickerStructure {
        filters: String,
        table: TickerData,
        rows: Vec<TickerData>,
        message: String,
        status: TickerResponseStatus
    }
    
    #[derive(Serialize, Deserialize)]
    pub struct TickerData {
        symbol: String,
        name: String,
        lastsale: String,
        netchange: String,
        pctchange: String,
        marketCap: String
    }
    
    #[derive(Serialize, Deserialize)]
    pub struct TickerResponseStatus {
        rCode: String,
        bCodeMessage: String,
        developerMessage: String
    }
}
