use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").expect("File not found!");
    let iter = input.split_whitespace();

    let mut grid: Vec<Vec<u8>> = Vec::new();

    // create grid
    for line in iter {
        grid.push(line.chars().map(|c| c.to_digit(10).unwrap() as u8).collect::<Vec<u8>>())
    }

    // println!("grid {:?}", grid);
    let grid_size = grid.len();

    let mut num_visible_trees = 0;
    for i in 0..grid_size {
        let current_row = &grid[i];
        for j in 0..grid_size {
            let current_tree_height = grid[i][j];
            let current_column: Vec<u8> = (0..grid_size).map(|x| grid[x][j]).collect();
            let look_left = tree_is_tallest(current_tree_height, current_row[0..j].to_vec());
            let look_right = tree_is_tallest(current_tree_height, current_row[j+1..grid[i].len()].to_vec());
            let look_up = tree_is_tallest(current_tree_height, current_column[0..i].to_vec());
            let look_down = tree_is_tallest(current_tree_height, current_column[i+1..grid.len()].to_vec());
            if look_left || look_right || look_up || look_down {
                num_visible_trees += 1;
            }
        }
    }
    println!("number of visible trees: {num_visible_trees}")

}

fn tree_is_tallest(height: u8, slice: Vec<u8>) -> bool {
    slice.into_iter().all(|t| t < height)
}