def individual_user(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "image": user["image"]
    }

def list_user(users) -> list:
    return [individual_user(user) for user in users]