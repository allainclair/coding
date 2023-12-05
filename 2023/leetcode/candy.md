## Problem

https://leetcode.com/problems/candy

## Approach

### First part: left ⟶ right

1. Create a `candies` list to save the amount of candies of each child.
2. Run **left ⟶ right**:
   1. If `rate` > `left_neighbor_rate`,  increase `current_candy` by `1` and save it to `candies`
      because the rate must be greater than the rate of the left neighbor.
   2. Otherwise, just append `1` to `candies` because a minimum of `1` is necessary for all child. 
   3. Remember to update the `left_neighbor_rate` and `left_candy` to have them for the next iteration.

### Second part: right -> left

We need to update the candies according to the candies analysed from **right -> left**.

1. Create a **new** `candies` list to save the updated amount of candies.
2. Run **right ⟶ left**: and compare the `rate` with the `right_neighbor_rate`:
   1. If `rate > right_neighbor_rate and candy_ <= right_candy` increase
   `current_candy` by `1` because the rate must be greater than the rate of the right neighbor,
   and also the candy analysed must be greater than the `right_candy` updated
   (propagated from right to left). Save the `current_candy` it to the `candies`.
   2. Otherwise, update `current_candy`
3. 
  
## Examples

### Example 1

```python
ratings = [29, 51, 87, 87, 72, 12]
expected_candies = [1, 2, 3, 3, 2, 1]
expected_output = 12
```

#### First part: left ⟶ right

```python
ratings = [29, 51, 87, 87, 72, 12]
candies = [ 1,  2,  3,  1,  1,  1]
```

#### Second part: right ⟶ left

```python
ratings = [29, 51, 87, 87, 72, 12]
candies = [ 1,  2,  3,  3,  2,  1]  # indexes 4 and 3 updated.
sum(candies) == 12
```

### Example 2

```python
ratings = [1, 6, 10, 8, 7, 3, 2]
expected_candies = [1, 2, 5, 4, 3, 2, 1]
expected_output = 18
```

#### First part: left ⟶ right

```python
ratings = [1, 6, 10, 8, 7, 3, 2]
candies = [1, 2,  3, 1, 1, 1, 1]
```

#### Second part: right ⟶ left

```python
ratings = [1, 6, 10, 8, 7, 3, 2]
candies = [1, 2,  5, 4, 3, 2, 1]  # indexes 5, 3, 3, and 2 updated.
sum(candies) == 18
```