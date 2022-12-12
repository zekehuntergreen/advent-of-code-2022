use std::fs;

fn main() {
    let puzzle_input = fs::read_to_string("input.txt").expect("file not found!");
    let mut commands = puzzle_input.split("\n");
    let mut x = 1;
    let mut i = 1;
    let mut maybe_command: Option<&str> = commands.next();
    let mut total = 0;
    while maybe_command != None {
        let command = maybe_command.unwrap();
        maybe_command = commands.next();

        if command != "noop" {
            (i, total) = increment_i(i, x, total);
            let mut s = command.splitn(2, " ");
            let _op = s.next().unwrap();
            let num: i32= s.next().expect("no arg").trim().parse().expect("nan");
            x += num;
        }
        (i, total) = increment_i(i, x, total);
    }
    println!("{total}")
}

fn increment_i(mut i: i32, x: i32, mut total: i32) -> (i32, i32){
    i += 1;
    // println!("incremented i to {i}");
    if i % 40 == 20 && i <= 220  {
        let signal_strength = x * i;
        println!("register X has the value {x}, so the signal strength is {i} * {x} = {signal_strength}");
        total += signal_strength;
    }
    return (i, total)
}
