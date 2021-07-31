use crate::request;

fn main() {
    let res =  request::rest_call::test_call();
    println!("Hello, world!");
}
