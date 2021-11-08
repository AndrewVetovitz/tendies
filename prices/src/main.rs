mod request;
pub mod models;

fn main() {
    let res =  request::test_call::test_call();
    println!("Hello, world!");
}
