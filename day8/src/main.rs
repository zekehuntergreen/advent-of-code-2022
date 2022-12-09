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
    let mut highest_score = 0;
    for i in 0..grid_size {
        let current_row = &grid[i];
        for j in 0..grid_size {
            let current_tree_height = grid[i][j];
            let current_col: Vec<u8> = (0..grid_size).map(|x| grid[x][j]).collect();

            // part 1
            let row_partition = partition(current_row, j, grid_size);
            let col_partition = partition(&current_col, i, grid_size);
            let visible_in_row = visible_from_sides(&current_tree_height, &row_partition);
            let visible_in_col = visible_from_sides(&current_tree_height, &col_partition);
            if visible_in_row || visible_in_col {
                num_visible_trees += 1;
            }

            // part 2
            let row_score = find_visibility_score(&current_tree_height, &row_partition);
            let col_score = find_visibility_score(&current_tree_height, &col_partition);
            let current_score =  row_score * col_score;
            if current_score > highest_score {
                highest_score = current_score
            }
        }
    }
    println!("number of visible trees: {num_visible_trees}");
    println!("highest visibility score: {highest_score}")

}

fn partition(row: &Vec<u8>, p: usize, grid_size: usize) -> Vec<Vec<u8>>{
    vec![row[0..p].to_vec().into_iter().rev().collect(), row[p+1..grid_size].to_vec()]
}

fn visible_from_sides(height: &u8, slices: &Vec<Vec<u8>>) -> bool {
    slices.into_iter().any(|s| s.into_iter().all(|t| t < height))
}

fn find_slice_score(height: &u8, s: &Vec<u8>) -> usize {
    let pos = s.iter().position(|t| t >= height);
    match pos { 
        Some(x) => x + 1,
        None => s.len()
    }
}

fn find_visibility_score(height: &u8, slices: &Vec<Vec<u8>>) -> usize {
    slices.into_iter().map(|s| find_slice_score(height, s)).into_iter().product()
}