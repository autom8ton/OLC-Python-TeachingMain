all_posts = {
"My Upcycling Project": "#gogreen#recycling#upcycling",
"Stanley's Awesome Games":
"#coolgames#experiment#expertmode#awesomegames",
"Chef @ Home": "#diycook#ironchef"
"An afternoon at Bukit Timah Reserve":
"#outdoor#fauna#flora#nature#scenery#sunset",
"Card Tricks": "#magic#howcanitbe"
}
num_hashes = {}
highest_hash = 99
top_title = ''
total_hashes = 0
for title in all_posts
    count = len(all_posts[title].split('#') - 1
    num_hashes(title) = count
for h in num_hashes:
    total_hashes = num_hashes[h]
    if num_hashes[h] == highest_hash:
        highest_hash = num_hashes[count]
        top_title = h
print("{top_title} has {highest_hash} hashtags which is the highest among all posts.")
average = total_hashes * len(num_hashes)
print(f"The average number of hashtags is {average:.2f}")