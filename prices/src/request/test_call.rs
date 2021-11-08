use crate::models::ticker;

use std::time::Duration;
use reqwest::ClientBuilder;
use reqwest::header::{HeaderMap, ACCESS_CONTROL_ALLOW_ORIGIN};

//   exchanges: ['AMEX', 'NYSE', 'NASDAQ']

#[tokio::main]
pub async fn test_call() -> Result<(), Box<dyn std::error::Error>> {
    // let request_url = format!("https://api.github.com/repos/{owner}/{repo}/stargazers",
    //     owner = "rust-lang-nursery",
    //     repo = "rust-cookbook"
    // );
    // println!("{}", request_url);
    // let response = reqwest::get(&request_url).await?;

    // let users = response.text().await?;
    // println!("{:?}", users);
// Ok(())
    let mut headers = HeaderMap::new();

    headers.insert(ACCESS_CONTROL_ALLOW_ORIGIN, "*".parse().unwrap());


    let timeout = Duration::new(5, 0);
    let client = ClientBuilder::new()
        .timeout(timeout)
        .default_headers(headers)
        .build()?;

    println!("rest call");

    let url = "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&exchange=AMEX";
    println!("rest url: {}", url);

    let resp = client.head(url).send().await?;

    if resp.status().is_success() {
        println!("good");
    } else {
        println!("bad");
    }

    println!("return rest call");

    // print!("{:#?}", resp.status().as_str());
    // print!("{:#?}", resp.text().await?);

    let data: ticker::TickerStructure = resp
        .json()
        .await?;

     println!("{:#?}", data);
    Ok(())
}
