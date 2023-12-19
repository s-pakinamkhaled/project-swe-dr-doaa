
from flask import Flask, render_template, request, jsonify
from your_recommendation_module import RecommendationFactory

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        user_preferences = request.form.getlist('preferences[]')
        category_choices = request.form.getlist('categories[]')

        recommendations = []
        for choice in category_choices:
            if choice.strip() == "1":
                recommendations.append(RecommendationFactory.create_recommendation('food'))
            elif choice.strip() == "2":
                recommendations.append(RecommendationFactory.create_recommendation('movie'))
            elif choice.strip() == "3":
                recommendations.append(RecommendationFactory.create_recommendation('travel'))

        result = {}
        for i, recommendation in enumerate(recommendations):
            preferences = []
            if isinstance(recommendation, FoodRecommendation):
                preferences = ["Italian", "Mexican", "Japanese"]
            elif isinstance(recommendation, MovieRecommendation):
                preferences = ["Action", "Comedy", "Tragedy"]
            elif isinstance(recommendation, TravelRecommendation):
                preferences = ["Beach", "City", "Adventure"]
            else:
                return jsonify({"error": "Invalid recommendation category"})

            result[f"category_{i + 1}"] = {
                "preferences": preferences,
                "recommendations": recommendation.generate(user_preferences)
            }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if _name_ == '_main_':
    app.run(debug=True)