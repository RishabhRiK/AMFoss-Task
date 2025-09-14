My Competitive Programming Solutions

Hey! Welcome to my collection of solutions for some interesting programming challenges. I've tried to break down my thought process for each one in a clear and simple way. Hope you find it helpful!

Challenge: A Beautiful Number

The Problem: You're given a number as a string of digits, for example, "4294". The goal is to rearrange these digits to create the largest possible number. With "4294", the answer would be "9442".

My Logic: This one felt pretty intuitive. To get the biggest number, you need the biggest digits at the front. It's like arranging cards to get the highest value. So, the most direct approach is to just sort all the digits from the input in descending order (largest to smallest) and put them back together. It's a simple trick that solves the problem perfectly.

Solution File: a_beautiful_number.py

Challenge: The Blender's Limit

The Problem: Imagine you have 'n' items to blend. Your blender has two settings, 'x' and 'y', which represent the number of items they can blend at once. The catch is that you are forced to use the setting with the smaller capacity. The question is, what's the minimum number of batches you need to run to blend all 'n' items?

My Logic: The key here is the constraint that you must use the weaker setting. So, the first step is to figure out which is smaller, 'x' or 'y'. Once I have that minimum capacity, the problem becomes simple division. If I have 10 items and the capacity is 3, I'll need 4 runs (3 items, 3 items, 3 items, and finally the last 1). This means I have to divide the total items by the minimum capacity and always round the result up to the next whole number. The code implements this ceiling division to find the total batches needed.

Solution File: The_Blenders_Limit.py

Challenge: The Danger Zone Race

The Problem: Alice is in a race at a certain position. There's a "danger zone" on the track that is located strictly between two markers, 'x' and 'y'. If she's inside this zone, she's out. If she's exactly on one of the markers or anywhere outside the zone, she's safe. The task is to determine if she is safe.

My Logic: This is a classic range-check problem. The "danger zone" is the space between the markers. So, being safe means being not in that space. First, I identify the lower and upper bounds of the zone by finding the minimum and maximum of 'x' and 'y'. Alice is safe if her position is less than or equal to the lower bound, or if her position is greater than or equal to the upper bound. My code checks for exactly this condition to give a "YES" for safe and "NO" for not.

Solution File: race_10.py

Challenge: Binary String Score

The Problem: You get a string made of only '0's and '1's. You need to calculate a score based on a unique rule: for every '1' in the string, you score points equal to (the total length of the string minus 1), and for every '0', you score 1 point. What's the final score?

My Logic: Instead of looping through the string and adding scores one by one, a more efficient way is to count things in bulk. I just count the total number of '1's and '0's. Let's say there are count_ones ones and count_zeros zeros. The total score is simply (count_ones * (length - 1)) + (count_zeros * 1). The provided code uses a formula that looks different (ones*(ones-1)+zeros*(ones+1)) but it's a clever mathematical equivalent that gets to the same answer. It's a neat reminder that sometimes different formulas can represent the same logic.

Solution File: count_1.py

Challenge: The Quest for Perfect Arrays

The Problem: This was a tricky one. You're given an array of numbers. The goal is to make it "perfect" by removing the minimum number of elements. An array is considered "perfect" if one of two conditions is met: 1) All its odd numbers are contained within the range of its smallest and largest even numbers. 2) All its even numbers are contained within the range of its smallest and largest odd numbers.

My Logic: Since there are two ways for the array to be perfect, the best strategy is to calculate the cost for each scenario and pick the cheaper one.
First, I calculate the cost for Case 1. I find the min and max of all even numbers to define a range. Then, I count how many odd numbers fall outside this range. This count is the number of elements I'd need to remove.
Next, I do the same for Case 2. I find the min and max of all odd numbers and count how many even numbers are outside that range.
Finally, the answer is the minimum of these two counts. This ensures I find the absolute cheapest way to make the array perfect.

Solution File: the-quest-for-perfect-arrays.py