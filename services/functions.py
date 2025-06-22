from bson.objectid import ObjectId
from conections.mongo import conection_mongo
from flask import jsonify

def create_comment(user_id, data):
    try:
        id_publication = data.get("Id_publication")
        comment_text = data.get("Comment")

        if not id_publication or not comment_text:
            return {"error": "Missing data"}, 400

        db = conection_mongo()
        comments_collection = db["Comments"]

        comment_doc = {
            "Id_publication": ObjectId(id_publication),  
            "Id_user": int(user_id),               
            "Comment": comment_text,
            "status":1,
            "Likes": []  
        }

        comments_collection.insert_one(comment_doc)

        return {"message": "Comment created successfully"}, 201

    except Exception as e:
        return {"error": f"Failed to create comment: {str(e)}"}, 500
