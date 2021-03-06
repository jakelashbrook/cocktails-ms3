import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    # recipes to be shown
    recipes = list(mongo.db.recipes.find())
    # recipes to be shown on mobile devices
    mobile_recipes = [recipes[0], recipes[1], recipes[2]]
    # Find users who love recipe
    loved = mongo.db.loved.find().sort("loved_by", 1)

    return render_template(
        "home.html",
        recipes=recipes,
        mobile_recipes=mobile_recipes,
        loved=loved)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template(
        "cocktails.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("User already Exists, Please try another username.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the newly created user into 'session' cookie
        # using the session function imported
        session["user"] = request.form.get("username").lower()
        flash("Congratulations, you have registered a new account")
        return redirect(url_for('profile', username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check to see if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # make sure the hashed password matches user inputs
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome {}".format(
                            request.form.get("username")))
                        return redirect(url_for('get_cocktails'))

            else:
                # invalid password entry
                flash("Oopsy, Incorrect username and/or password")
                return redirect(url_for('login'))

        else:
            # username doesn't exist in db
            flash("Oopsy, Incorrect username and/or password")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session users username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # grabs recipes created by a specific user
    recipes = mongo.db.recipes.find().sort("created_by", 1)

    if session["user"]:
        return render_template(
            "profile.html",
            recipes=recipes,
            username=username)

    return redirect(url_for('login'))


@app.route("/delete_account", methods=["GET", "POST"])
def delete_account():
    # grab session userfrom db
    mongo.db.users.remove({"username": session["user"]})
    # logout user from session after removing account
    session.pop("user")
    flash(
        "You have successfully removed your account!")
    return redirect(url_for('get_recipes'))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for('login'))


@app.route("/get_cocktails", methods=["GET", "POST"])
def get_cocktails():
    # get the cocktails from the db
    recipes = list(mongo.db.recipes.find())
    return render_template('cocktails.html', recipes=recipes)


@app.route("/cocktails/<category>")
def cocktails(category):
    # Show recipes of that specific category
    if category == "All":
        recipes = list(mongo.db.recipes.find())
    elif category == "Mocktails":
        recipes = list(mongo.db.recipes.find({"category_name": "mocktails"}))
    elif category == "Fruity":
        recipes = list(mongo.db.recipes.find({"category_name": "fruity"}))
    elif category == "Sour":
        recipes = list(mongo.db.recipes.find({"category_name": "sour"}))
    elif category == "Dessert":
        recipes = list(mongo.db.recipes.find({"category_name": "dessert"}))
    elif category == "Sparkling":
        recipes = list(mongo.db.recipes.find({"category_name": "sparkling"}))

    return render_template(
        "cocktails.html", category=category, recipes=recipes)


@app.route("/add_cocktail", methods=["GET", "POST"])
def add_cocktail():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "img_url": request.form.get("img_url"),
            "ingredients": request.form.getlist("ingredients"),
            "garnish": request.form.get("garnish"),
            "method_step_one": request.form.get("method_step_one"),
            "method_step_two": request.form.get("method_step_two"),
            "inspiration": request.form.get("inspiration"),
            "eat_with": request.form.get("eat_with"),
            "summary": request.form.get("summary"),
            "author": request.form.get("author"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Cocktail recipe has been successfully added")
        return redirect(url_for('get_cocktails'))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_cocktail.html", categories=categories)


@app.route("/edit_cocktail/<recipe_id>", methods=["GET", "POST"])
def edit_cocktail(recipe_id):
    if request.method == "POST":
        edit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "img_url": request.form.get("img_url"),
            "ingredients": request.form.getlist("ingredients"),
            "garnish": request.form.get("garnish"),
            "method_step_one": request.form.get("method_step_one"),
            "method_step_two": request.form.get("method_step_two"),
            "inspiration": request.form.get("inspiration"),
            "eat_with": request.form.get("eat_with"),
            "summary": request.form.get("summary"),
            "author": request.form.get("author"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Cocktail recipe has been successfully updated!")
        return redirect(url_for('get_cocktails', username=session["user"]))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_cocktail.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("The recipe has been successfully deleted")
    return redirect(url_for('get_recipes'))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # Add category to the db
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("Your category has been successfully added")
        return redirect(url_for("get_categories"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("The selected category has been successfully deleted")
    return redirect(url_for('get_categories'))


@app.route("/get_user_recipes")
def get_user_recipes():
    recipes = mongo.db.recipes.find().sort("recipe_name", 1)
    return render_template("user_recipes.html", recipes=recipes)


@app.route("/get_users")
def get_users():
    users = mongo.db.users.find().sort("username", 1)
    return render_template("users.html", users=users)


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("The User Account has been Successfully Removed")
    return redirect(url_for('get_users'))


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    # Find specific recipe in db
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if not recipe:
        flash("Recipe does not exist")
        return render_template("cocktails.html")

    return render_template("cocktail-recipe.html", recipe=recipe)


@app.route("/add_love", methods=["GET", "POST"])
def add_love():
    if request.method == "POST":
        lover = {
            "loved_by": request.form.get("loved_by"),
        }
        mongo.db.loved.insert_one(lover)
        flash("Thanks for sharing the love")
        return redirect(url_for("get_recipes"))
    return render_template("home.html", lover=lover)


@app.route("/get_promotions")
def get_promotions():
    promotions = mongo.db.promotions.find().sort("email", 1)
    return render_template("promotions.html", promotions=promotions)


@app.route("/add_promotion", methods=["GET", "POST"])
def add_promotion():
    if request.method == "POST":
        email = {
            "email_address": request.form.get("email_address"),
        }
        mongo.db.promotions.insert_one(email)
        flash("You are now signed up for our Promotions")
        return redirect(url_for('get_recipes'))
    promotions = mongo.db.promotions.find().sort("email_address", 1)
    return render_template("promotions.html", promotions=promotions)


@app.errorhandler(404)
def page_not_found(e):
    """To handle not found page"""
    return render_template(
        "error_404.html", title="Error 404"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
