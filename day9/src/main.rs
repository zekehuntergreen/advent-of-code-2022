use std::{fs, collections::HashSet};

fn main() {
    let num_knots = 10;
    let mut knots: Vec<(i32, i32)> = Vec::new();
    for _ in 0..num_knots{
        knots.push((0, 0))
    }
    let mut tail_positions: HashSet::<(i32, i32)> = HashSet::new();

    let lines = fs::read_to_string("test_input_2.txt").expect("File not found");
    let iter = lines.split("\n");
    for line in iter {
        let mut iter = line.splitn(2, " ");
        let direction = iter.next().unwrap();
        let steps_str = iter.next().unwrap();
        let steps: u8 = steps_str.parse().unwrap();

        println!("\n== {direction} {steps} ==\n");

        let increment: (i32, i32) = match direction {
            "R" => (1, 0),
            "L" => (-1, 0),
            "U" => (0, 1),
            "D" => (0, -1),
            _ => panic!("Unknown direction"),
        };

        // find H position after it has followed directions
        for _step in 0..steps{
            //  move head
            knots[0].0 += increment.0;
            knots[0].1 += increment.1;

            // move all other knots
            for i in 1..knots.len() {
                let current_knot = knots[i];
                let previous_knot = knots[i - 1];
                knots[i] = match (previous_knot.0 - current_knot.0, previous_knot.1 - current_knot.1) {
                    // If the head is ever two steps directly up, down, left, or right from the tail,
                    // the tail must also move one step in that direction so it remains
                    // close enough
                    (2, 0) => (current_knot.0 + 1, current_knot.1), // right
                    (0, 2) => (current_knot.0, current_knot.1 + 1), // up
                    (-2, 0) => (current_knot.0 - 1, current_knot.1), // left
                    (0, -2) => (current_knot.0, current_knot.1 -1), // down
                    // Otherwise, if the head and tail aren't touching 
                    (0, 0) => current_knot, // same
                    // and aren't in the same row or column, 
                    (_, 0) => current_knot,
                    (0, _) => current_knot,
                    // (and aren't diagonally adjacent)
                    (1, 1) => current_knot,
                    (-1, 1) => current_knot,
                    (1, -1) => current_knot,
                    (-1, -1) => current_knot,
                    // the tail always moves one step diagonally to keep up
                    (x, y) => (current_knot.0 + (x / x.abs()), current_knot.1 + (y / y.abs())),
                };
            }
            tail_positions.insert(*knots.last().unwrap());
        }
        print_grid(&knots);
    }
    println!("there are {:?} unique tail positions", tail_positions.len());
}

fn print_grid(knots: &Vec<(i32, i32)>) {
    print!("\n");
    for y in (-15..15).rev() {
        for x in -15..15 {
            if knots.contains(&(x, y)) {
                let p = &knots.iter().position(|&(a, b)| (x, y) == (a, b)).unwrap();
                print!("{p}")
            } else if (x, y) == (0, 0) {
                print!("s")
            } else {
                print!(".")
            }
        }
        print!("\n");
    }
}