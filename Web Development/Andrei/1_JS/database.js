var database = [];

function User(username, password){
    this.username = username;
    this.password = password
};

User.prototype.greet = function(){
    return `Hello my name is ${this.username} and my password is ${this.password}`
}


database.push(new User("hamza",'45865454741'));
database.push(new User("ali",'how about a sip'));
database.push(new User("mohammad",'helloMyFriends'));
database.push(new User("ismail",'enjoybc'));

module.exports = database;
