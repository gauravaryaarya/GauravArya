Levenshtein Distance Assignment
Name: Gaurav Arya
Date: 27 June 2025

---------------------------------------

What is Levenshtein Distance?

It is a way to find how different two strings are. We calculate how many operations are needed to convert one string into another.

Allowed operations:
edit distance
- Insert a character
- Delete a character
- Replace/substitute a character

---------------------------------------

How the algorithm works (my understanding):

We make a 2D matrix of size (len(string1)+1) x (len(string2)+1).
Each cell dp[i][j] tells how many edits needed to convert first i letters of string1 to first j letters of string2.

We fill:
- First row with 0 to len(string2) -> means inserting all chars
- First column with 0 to len(string1) -> means deleting all chars

checking characters:
 If same -> no cost, copy previous diagonal
 If not same -> take min of (delete, insert, replace) and add 1

---------------------------------------

What I did in code:

-I created a function `levenshtein_matrix(s1, s2)` that builds the full matrix using loops.

-I also added a function `print_matrix(...)` to print it properly with labels.

-Then I gave 4 pairs as input and printed matrix for each one.

---------------------------------------

The 4 string pairs are:

1. Levenshtein & Lavenstaein
2. TryHackMe & TriHackingMe
3. Optimization & Progressive
4. This is easy & This is easy

---------------------------------------

What I learnt:

- How dynamic programming works with strings.
- How we can build logic step-by-step instead of using ready-made libraries.
- Got better understanding of insert/delete/replace operations.

---------------------------------------
Thank you.
