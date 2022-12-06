use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt")
        .expect("Couldn't read input file");
    let num_distinct_characters = 14; // part 2
    let iter = contents.split_whitespace();
    for line in iter {
        let characters = line.chars().collect::<Vec<char>>();
        let message_length = characters.len();
        for i in num_distinct_characters..message_length {
            let last_n = &characters[i - num_distinct_characters..i];
            if !(1..num_distinct_characters).any(|i| last_n[i..].contains(&last_n[i - 1])) {
                println!("At index {:?} each element of {:?} is unique.", i, last_n);
                break;
            }
        }
    }
}
