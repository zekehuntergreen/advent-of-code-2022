use std::fs;

fn main() {
    let puzzle_input = fs::read_to_string("input.txt").expect("file not found!");
    let mut commands = puzzle_input.split("\n");
    let mut x = 1;
    let mut i = 1;
    let mut maybe_command: Option<&str> = commands.next();
    while maybe_command != None {
        let command = maybe_command.unwrap();
        maybe_command = commands.next();

        if command == "noop" {
            i = draw(i, x);
        } else {
            i = draw(i, x);
            i = draw(i, x);
            let mut s = command.splitn(2, " ");
            let _op = s.next().unwrap();
            let num: i32= s.next().expect("no arg").trim().parse().expect("nan");
            x += num;
        }
    }
}

fn draw(i: i32, x: i32) -> i32 {
    let position = (i - 1) % 40;
    if x - 1 <= position && position <= x + 1 {
        print!("#")
    } else {
        print!(".")
    }
    if i % 40 == 0 {
        print!("\n")
    }
    return i + 1;
}