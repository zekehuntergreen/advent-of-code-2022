use std::{fs, collections::HashSet};

fn main() {
    let mut head = (0, 0);
    let mut tail = (0, 0);
    let mut tail_positions: HashSet::<(i32, i32)> = HashSet::new();

    let lines = fs::read_to_string("input.txt").expect("File not found");
    let iter = lines.split("\n");
    for line in iter {
        let mut iter = line.splitn(2, " ");
        let direction = iter.next().unwrap();
        let steps = iter.next().unwrap();
        let steps_int: u8 = steps.parse().unwrap();

        // println!("\n== {direction} {steps} ==\n");

        let increment: (i32, i32) = match direction {
            "R" => (1, 0),
            "L" => (-1, 0),
            "U" => (0, 1),
            "D" => (0, -1),
            _ => panic!("Unknown direction"),
        };
        // println!("incremenet is {:?}", increment);

        // find H position after it has followed directions
        for _step in 0..steps_int{
            //  move head
            head.0 += increment.0;
            head.1 += increment.1;

            // move tail
            tail = match (head.0 - tail.0, head.1 - tail.1) {
                // If the head is ever two steps directly up, down, left, or right from the tail,
                // the tail must also move one step in that direction so it remains
                // close enough
                (2, 0) => (tail.0 + 1, tail.1), // right
                (0, 2) => (tail.0, tail.1 + 1), // up
                (-2, 0) => (tail.0 - 1, tail.1), // left
                (0, -2) => (tail.0, tail.1 -1), // down
                // Otherwise, if the head and tail aren't touching 
                (0, 0) => tail, // same
                // and aren't in the same row or column, 
                (_, 0) => tail,
                (0, _) => tail,
                // (and aren't diagonally adjacent)
                (1, 1) => tail,
                (-1, 1) => tail,
                (1, -1) => tail,
                (-1, -1) => tail,
                // the tail always moves one step diagonally to keep up
                (x, y) => (tail.0 + (x / x.abs()), tail.1 + (y / y.abs())),
                _ => panic!("can't handle difference"),
            };
            // println!("tail is at {:?}", tail);
            tail_positions.insert(tail);

            // print_grid(head, tail);
            // println!("head position {:?}", head);
        }
    }
    // println!("{:?}\n", tail_positions);
    println!("there are {:?} unique positions", tail_positions.len());
}

fn print_grid(head: (i32, i32), tail: (i32, i32)) {
    let x = [head.0, head.1, tail.0, tail.1];
    let grid_size = x.iter().fold(0, |a, &b| a.max(b)) + 1;
    print!("\n");
    for y in (0..grid_size).rev() {
        for x in 0..grid_size {
            if (x, y) == head {
                print!("H")
            } else if (x, y) == tail {
                print!("T")
            } else if (x, y) == (0, 0) {
                print!("s")
            } else {
                print!(".")
            }
        }
        print!("\n");
    }
}