const express=require('express');
var mongo=require('mongodb').MongoClient
const bodyParser=require('body-parser');
const app=express();
app.use(bodyParser.urlencoded({extended:true}));
app.set('view engine','ejs');
app.set('views','views');
app.use( express.static( "static" ) );
app.get('/',(req,res)=>{
    res.render('index.ejs')
});
app.get('/Abstract',(req,res)=>{
    res.render('Abstract.ejs')
});
app.get('/GroupMembers',(req,res)=>{
    res.render('GroupMembers.ejs')
});
app.get('/Login',(req,res)=>{
    res.render('Login.ejs')
});
app.post('/Login',(req,res)=>{
    console.log(req.body)
    mongo.connect("mongodb://localhost:27017/",function(err, db) {
    if (err) throw err;
    var dbo = db.db("Blood_database");
    dbo.collection("Blood_table").insertOne(req.body)})
    res.redirect("/results")
    
});
app.get('/results',(req,res)=>{
    mongo.connect("mongodb://localhost:27017/",function(err, db) {
    if (err) throw err;
    var dbo = db.db("Blood_database");
    var entries=dbo.collection("Blood_table").find()
    let output=[]
    entries.forEach(entry=>{
        output.push({name:entry.user,password:entry.psw,Phone_no:entry.contact,Email:entry.mail})
    })
    console.log(output)
res.render('results.ejs',{data:entries})})

})
app.listen(5000,()=>{console.log("Listening")})