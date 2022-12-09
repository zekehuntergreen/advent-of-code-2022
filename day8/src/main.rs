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
            let current_col: Vec<u8> = (0..grid_size).map(|x| grid[x][j]).collect();
            let visible_in_row = tree_is_tallest(current_tree_height, partition(current_row, j, grid_size));
            let visible_in_col = tree_is_tallest(current_tree_height, partition(&current_col, i, grid_size));
            if visible_in_row || visible_in_col {
                num_visible_trees += 1;
            }
        }
    }
    println!("number of visible trees: {num_visible_trees}")

}

fn partition(row: &Vec<u8>, p: usize, grid_size: usize) -> Vec<Vec<u8>>{
    vec![row[0..p].to_vec(), row[p+1..grid_size].to_vec()]
}

fn tree_is_tallest(height: u8, slices: Vec<Vec<u8>>) -> bool {
    slices.iter().any(|s| s.into_iter().all(|t| t < &height))
}