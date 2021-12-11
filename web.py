from flask import Flask, request, redirect, render_template
import pymongo
client=pymongo.MongoClient()
Blood=client.New_Blood_database
blood_table=Blood.Blood_Table
blockchain = Flask(__name__)
blockchain.config["Secret_Key"] = "Block Chain"
@blockchain.route("/",methods=["GET","POST"])
def protect():
    return render_template("index.html")

@blockchain.route("/Abstract",methods=["GET","POST"])
def protect1():
    return render_template("Abstract.html")

@blockchain.route("/GroupMembers",methods=["GET","POST"])
def protect2():
    return render_template("GroupMembers.html")

@blockchain.route("/Login",methods=["GET","POST"])
def protect3():
    dictionary={"user":"","psw":"","Gender":"","blood":"","age":"","contact":"","E-Mail":"","address":""}
    if request.method=="POST":
        dictionary["user"] = request.form["user"]
        dictionary["psw"] = request.form["psw"]
        dictionary["Gender"] = request.form["Gender"]
        dictionary["blood"] = request.form["blood"]
        dictionary["age"] = request.form["Age"]
        dictionary["contact"] = request.form["contact"]
        dictionary["E-mail"] = request.form["mail"]
        dictionary["address"] = request.form["address"]
        print(dictionary)
        blood_table.insert_one(dictionary)
        return redirect("/results")
    return render_template("Login.html")

@blockchain.route("/results",methods=["GET","POST"])
def results():
    if request.method=="POST":
        if request.form["search"]=="A+ve":
            return redirect("/resultsA+ve")
        if request.form["search"]=="A-ve":
            return redirect("/resultsA-ve")
        if request.form["search"]=="B+ve":
            return redirect("/resultsB+ve")
        if request.form["search"]=="B-ve":
            return redirect("/resultsB-ve")
        if request.form["search"]=="O+ve":
            return redirect("/resultsO+ve")
        if request.form["search"]=="O-ve":
            return redirect("/resultsO-ve")
        if request.form["search"]=="AB+ve":
            return redirect("/resultsAB+ve")
        if request.form["search"]=="AB-ve":
            return redirect("/resultsAB-ve")
        return request.form
    output=[]
    for document in blood_table.find():
        output.append(document)
    return render_template("results.html",output=output)

@blockchain.route("/resultsA+ve",methods=["GET"])
def resultsApositive():
    output=[]
    for document in blood_table.find({"blood":"A+ve"}):
        output.append(document)
    return render_template("search_results.html",output=output)

@blockchain.route("/resultsA-ve",methods=["GET"])
def resultsAnegative():
    output=[]
    for document in blood_table.find({"blood":"A-ve"}):
        output.append(document)
    return render_template("search_results.html",output=output)

@blockchain.route("/resultsB+ve",methods=["GET"])
def resultsBpositive():
    output=[]
    for document in blood_table.find({"blood":"B+ve"}):
        output.append(document)
    return render_template("search_results.html",output=output)

@blockchain.route("/resultsB-ve",methods=["GET"])
def resultsBnegative():
    output=[]
    for document in blood_table.find({"blood":"B-ve"}):
        output.append(document)
    return render_template("search_results.html",output=output)

@blockchain.route("/resultsO+ve",methods=["GET"])
def resultsOpositive():
    output=[]
    for document in blood_table.find({"blood":"O+ve"}):
        output.append(document)
    return render_template("search_results.html",output=output)
    
@blockchain.route("/resultsO-ve",methods=["GET"])
def resultsOnegative():
    output=[]
    for document in blood_table.find({"blood":"O-ve"}):
        output.append(document)
    return render_template("search_results.html.html",output=output)
@blockchain.route("/resultsAB+ve",methods=["GET"])
def resultsABpositive():
    output=[]
    for document in blood_table.find({"blood":"AB+ve"}):
        output.append(document)
    return render_template("search_results.html",output=output)
@blockchain.route("/resultsAB-ve",methods=["GET"])
def resultsABnegative():
    output=[]
    for document in blood_table.find({"blood":"AB-ve"}):
        output.append(document)
    return render_template("search_results.html",output=output)
#@blockchain.route("/Login",methods=["GET","POST"])
#def protect4():
  #  dictionary={"user":"","psw":""}
    #if request.method=="POST":
        #dictionary["user1"] = request.form["user1"]
       # dictionary["psw1"] = request.form["psw1"]
      #  print(dictionary)
     #   return request.form
    #return render_template("Login.html")

if __name__ == "__main__":
    blockchain.run(port=1111,debug=True)

