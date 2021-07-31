use crate::models::Ticker;

//   exchanges: ['AMEX', 'NYSE', 'NASDAQ']

#[tokio::main]
pub async fn test_call() -> Result<(), Box<dyn std::error::Error>> {
    let client = reqwest::Client::builder()
        .build()?;

    // let tmp_dir = Builder::new().prefix("example").tempdir()?;

    // Ok(())

    // https://www.nasdaq.com/market-activity/stocks/screener?exchange=nyse&letter=0&render=download
    // https://www.nasdaq.com/market-activity/stocks/screener?exchange=nyse&letter=0&render=download
    // https://www.nasdaq.com/market-activity/stocks/screener?exchange=nyse&letter=0&render=download
    // https://www.nasdaq.com/market-activity/stocks/screener?exchange=nyse&letter=0&render=download
    // https://www.nasdaq.com/market-activity/stocks/screener?exchange=nyse&letter=0&render=download

     let resp = client
         .get("https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&exchange=AMEX")
         .send()
         .await?;

     print!("{:#?}", resp.status().as_str());
     print!("{:#?}", resp.text().await?);

     let data: Ticker = resp
         .json()
         .await?;

     println!("{:#?}", data);
    Ok(())
}
