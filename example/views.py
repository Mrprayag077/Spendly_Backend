from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Firebase service imports
from .firebase_service import (
    get_user_data,
    create_or_update_user,
    add_transaction,
    edit_transaction,
    delete_transaction,
)


def index(request):
    return HttpResponse("Hello from Django!")


def test(request):
    return JsonResponse({"message": "API is working 🚀"})


@csrf_exempt
def firebase_endpoint(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_uuid = data.get("userUUID")
            action = data.get("action")

            if not user_uuid or not action:
                return JsonResponse({"error": "Missing userUUID or action"}, status=400)

            if action == "get":
                user_data = get_user_data(user_uuid)
                return JsonResponse({"data": user_data}, status=200)

            elif action == "update_profile":
                profile_data = data.get("profileData")
                if not profile_data:
                    return JsonResponse({"error": "Missing profileData"}, status=400)

                allowed_fields = [
                    "balance",
                    "budget",
                    "email",
                    "name",
                    "totalExpenses",
                    "totalIncome",
                ]

                for key, value in profile_data.items():
                    if key not in allowed_fields:
                        return JsonResponse(
                            {"error": f"Field '{key}' is not allowed."}, status=400
                        )

                    if not isinstance(value, (int, float, str)):
                        return JsonResponse(
                            {"error": f"Field '{key}' must be a string or number."},
                            status=400,
                        )

                updated_profile = create_or_update_user(user_uuid, profile_data)
                return JsonResponse({"profile": updated_profile}, status=200)

            elif action == "add_transaction":
                transaction_id = data.get("transactionId")
                transaction_data = data.get("transactionData")

                if not transaction_id or not transaction_data:
                    return JsonResponse(
                        {"error": "Missing transactionId or transactionData"},
                        status=400,
                    )

                new_transaction = add_transaction(
                    user_uuid, transaction_id, transaction_data
                )
                return JsonResponse({"transaction": new_transaction}, status=200)

            elif action == "edit_transaction":
                transaction_id = data.get("transactionId")
                updated_data = data.get("transactionData")

                if not transaction_id or not updated_data:
                    return JsonResponse(
                        {"error": "Missing transactionId or updatedData"}, status=400
                    )

                updated_transaction = edit_transaction(
                    user_uuid, transaction_id, updated_data
                )
                return JsonResponse({"transaction": updated_transaction}, status=200)

            elif action == "delete_transaction":
                transaction_id = data.get("transactionId")

                if not transaction_id:
                    return JsonResponse({"error": "Missing transactionId"}, status=400)

                delete_transaction(user_uuid, transaction_id)
                return JsonResponse(
                    {"message": "Transaction deleted successfully"}, status=200
                )

            else:
                return JsonResponse({"error": "Invalid action specified"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)
