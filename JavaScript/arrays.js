var friends= ["Stewie", "Peter", "Lois", "Chris", "Meg", "Brian"]

for(var i= 0; i <= friends.length; i++){
    console.log(friends[i]);
}
friends.sort();
friends.pop();
for(var i= 0; i <= friends.length; i++){
    console.log(friends[i]);
}
